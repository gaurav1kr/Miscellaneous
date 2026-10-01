# Edge-to-Cloud Telemetry Ingestion Pipeline

**Interview:** Emerson AspenTech --- Senior Principal Software
Developer\
**Problem:** Design an ingestion architecture for thousands of
industrial edge devices producing high-frequency time-series data under
volatile, intermittent network conditions.

------------------------------------------------------------------------

## 1. First Understand the Requirement

Do **not** start with Kafka, MQTT, databases, or cloud services.

Start by identifying what the system must achieve.

The system has:

-   Thousands of industrial devices/sensors.
-   High-frequency time-series telemetry.
-   Unreliable/intermittent WAN connectivity.
-   A requirement to continue collecting data while offline.
-   A need to send accumulated data when connectivity returns.
-   High cloud-side ingestion throughput.
-   Downstream consumers such as dashboards, alerts, analytics, and ML.

Typical telemetry:

``` text
Device      Timestamp                Metric       Value
Pump-101    10:01:01.001             Pressure     72.4
Pump-101    10:01:01.011             Pressure     72.6
Motor-52    10:01:01.001             Vibration    12.1
```

A logical record contains:

``` text
Device ID
Sequence Number
Event Timestamp
Metric
Value
Quality
Checksum
```

------------------------------------------------------------------------

# 2. Functional Requirements

  -----------------------------------------------------------------------
  ID                      Requirement             Description
  ----------------------- ----------------------- -----------------------
  FR1                     Continuous collection   Continue collecting
                                                  telemetry even when
                                                  WAN/cloud is
                                                  unavailable.

  FR2                     Store-and-forward       Persist unsent
                                                  telemetry locally and
                                                  replay after
                                                  connectivity returns.

  FR3                     Near-real-time          When online, send
                          ingestion               telemetry with low
                                                  latency.

  FR4                     Reliable delivery       Important telemetry
                                                  must not silently
                                                  disappear during
                                                  transient failures.

  FR5                     Duplicate handling      Retries must not create
                                                  duplicate logical
                                                  measurements
                                                  downstream.

  FR6                     Ordering                Preserve required
                                                  ordering, normally per
                                                  device/asset.

  FR7                     Historical storage      Store time-series data
                                                  for queries and
                                                  analytics.

  FR8                     Multiple consumers      Support alerts,
                                                  dashboards, analytics,
                                                  ML, and archival
                                                  independently.

  FR9                     Priority                Critical alarms should
                                                  have higher priority
                                                  than bulk diagnostic
                                                  data.
  -----------------------------------------------------------------------

### Interview statement

> The primary functional requirement is to reliably collect telemetry
> from industrial devices and eventually deliver it to cloud
> processing/storage despite intermittent connectivity.

------------------------------------------------------------------------

# 3. Non-Functional Requirements

## 3.1 Scalability

Potentially:

``` text
10,000 devices
100 measurements/sec/device

= 1,000,000 events/sec
```

If each measurement is approximately 200 bytes:

``` text
1,000,000 × 200 bytes
≈ 200 MB/sec raw ingress
```

The system must scale horizontally.

------------------------------------------------------------------------

## 3.2 Reliability

Failures to consider:

``` text
WAN failure
Edge process crash
Edge reboot/power loss
Cloud ingestion failure
Message broker failure
Consumer failure
Database failure
Lost ACK
Duplicate messages
```

------------------------------------------------------------------------

## 3.3 Durability

Critical telemetry waiting for cloud transmission should survive:

``` text
Process restart
Machine reboot
Temporary network outage
```

This leads to a **persistent edge WAL**.

------------------------------------------------------------------------

## 3.4 Availability

Cloud ingestion should not depend on one server or one downstream
database.

------------------------------------------------------------------------

## 3.5 Latency

When connected:

``` text
Sensor -> Cloud
```

should normally have low latency.

Critical alarms may need a faster path than bulk telemetry.

------------------------------------------------------------------------

## 3.6 Backpressure

If cloud processing becomes slower than incoming traffic, the system
must degrade gracefully rather than consume unlimited memory.

------------------------------------------------------------------------

## 3.7 Security

Consider:

``` text
Device identity
X.509 certificates
TLS / mTLS
Certificate rotation
Authorization
Encryption at rest
```

------------------------------------------------------------------------

## 3.8 Observability

Important metrics:

``` text
Edge:
    WAL size
    queue depth
    oldest unsent record
    retry count
    reconnect count
    disk utilization

Cloud:
    events/sec
    consumer lag
    duplicate rate
    rejected messages
    processing latency
    end-to-end latency
```

------------------------------------------------------------------------

# 4. Important Clarifying Questions

Before designing, ask:

1.  How many devices?
2.  Measurements/sec/device?
3.  Average event size?
4.  Maximum expected offline duration?
5.  Can any telemetry be dropped?
6.  What latency is required?
7.  Is ordering required?
8.  If ordering is required, is it per-device or global?
9.  How long should telemetry be retained?
10. How much local storage does an edge gateway have?
11. What happens when local storage becomes full?
12. Are there different telemetry priorities?

The **maximum offline duration** is especially important because it
helps determine edge storage capacity.

------------------------------------------------------------------------

# 5. Approaches

## Approach 1 --- Direct Device to Cloud

``` text
Sensors
   |
   v
Edge Device
   |
   | HTTP / MQTT
   v
Cloud API
   |
   v
Database
```

### Advantage

Simple.

### Problems

If WAN disappears:

``` text
Edge --------X--------> Cloud
```

data can be lost unless the device buffers it.

Also:

``` text
Huge traffic
    |
    v
Cloud API
    |
    v
Database
```

directly couples ingestion capacity to database capacity.

**Conclusion:** insufficient by itself.

------------------------------------------------------------------------

# 6. Approach 2 --- In-Memory Edge Queue

``` text
Sensors
   |
   v
Edge Collector
   |
   v
Memory Queue
   |
   v
Cloud
```

Network outage:

``` text
Sensors
   |
   v
Memory Queue
   |
   X
  WAN
```

This handles short network interruptions.

But:

``` text
Power failure / process crash
          |
          v
      RAM lost
          |
          v
      Data lost
```

**Conclusion:** useful for performance, but insufficient for durable
store-and-forward.

------------------------------------------------------------------------

# 7. Recommended Approach --- Durable Store-and-Forward

``` text
+---------------------- INDUSTRIAL EDGE ----------------------+
|                                                            |
|  Sensors / PLCs                                            |
|       |                                                    |
|       v                                                    |
|  Edge Collector                                            |
|       |                                                    |
|       v                                                    |
|  Persistent WAL                                            |
|       |                                                    |
|       v                                                    |
|  Batcher -> Compressor -> Network Sender                   |
|                                                            |
+-----------------------------|------------------------------+
                              |
                     MQTT / HTTPS / gRPC
                       TLS / mTLS
                              |
                       Unreliable WAN
                              |
                              v
+------------------------- CLOUD -----------------------------+
|                                                            |
|  Ingestion Gateway                                         |
|       |                                                    |
|       v                                                    |
|  Durable Event Stream                                      |
|  Kafka / Event Hubs / equivalent                           |
|       |                                                    |
|       +--------------+---------------+                     |
|       |              |               |                     |
|       v              v               v                     |
|  Processor         Alerts        Raw Archive               |
|       |                                                    |
|       v                                                    |
|  Time-Series DB                                            |
|       |                                                    |
|       v                                                    |
|  Dashboard / Analytics / ML                                |
|                                                            |
+------------------------------------------------------------+
```

There are **two separate reliability boundaries**:

``` text
Edge WAL
   |
   +--> protects against WAN/network failures

Cloud Event Stream
   |
   +--> protects against downstream/cloud processing failures
```

------------------------------------------------------------------------

# 8. Persistent WAL

**WAL = Write-Ahead Log.**

Telemetry is written to persistent local storage **before relying on
network delivery**.

``` text
Sensor
   |
   v
Persistent WAL
   |
   v
Network Sender
   |
   v
Cloud
```

Example WAL:

``` text
Sequence    Timestamp       Metric          Value

1001        10:00:01        temperature     72.1
1002        10:00:02        temperature     72.5
1003        10:00:03        temperature     73.0
```

If WAN goes down:

``` text
Sensor
   |
   v
WAL
   |
   X
 Network

WAL continues growing:

1001
1002
1003
1004
1005
...
```

When WAN returns:

``` text
WAL                        Cloud

1001 ---------------------->
1002 ---------------------->
1003 ---------------------->
1004 ---------------------->
             <------------- ACK
```

------------------------------------------------------------------------

# 9. WAL Segmentation

Do not use one infinitely growing file.

Example:

``` text
wal-0001.log    seq 1      - 10000
wal-0002.log    seq 10001  - 20000
wal-0003.log    seq 20001  - 30000
wal-0004.log    active
```

Suppose:

``` text
checkpoint = 25000
```

Then:

``` text
wal-0001.log -> fully ACKed -> delete
wal-0002.log -> fully ACKed -> delete
wal-0003.log -> partially ACKed -> keep
wal-0004.log -> keep
```

------------------------------------------------------------------------

# 10. Normal Runtime Flow

``` text
Sensor
   |
   v
WAL
   |
   v
Batch
   |
   v
Send
   |
   v
Cloud durable storage
   |
   v
ACK
   |
   v
Checkpoint
   |
   v
WAL cleanup
```

Important rule:

``` text
WRITE -> SEND -> ACK -> CHECKPOINT -> CLEANUP
```

------------------------------------------------------------------------

# 11. Why Sequence Numbers?

Suppose the edge sends:

``` text
Device A, Sequence 101
```

Cloud stores it successfully.

But ACK gets lost:

``` text
Edge                         Cloud

seq=101 --------------------> stored

        <------ ACK ----------X
```

Edge retries:

``` text
seq=101 --------------------> Cloud
```

Cloud has now received the same event twice.

Use:

``` text
(DeviceID, SequenceNumber)
```

as the stable event identity.

Example:

``` text
Pump-101, 1001
Pump-101, 1002
Pump-101, 1003
```

Cloud can recognize replayed records.

------------------------------------------------------------------------

# 12. Delivery Guarantee

A practical design is:

``` text
At-least-once delivery
        +
Idempotent processing
```

Rather than claiming end-to-end exactly-once delivery across an
unreliable WAN.

Interview statement:

> I would normally choose at-least-once delivery with idempotent
> consumers. The edge may retransmit when an ACK is lost, while a stable
> device ID and sequence number allow the cloud to identify duplicate
> logical events.

------------------------------------------------------------------------

# 13. Batching

Do not send every sensor measurement as an independent network
operation.

``` text
Record
Record
Record
Record
Record
   |
   v
 Batch
   |
   v
Compress
   |
   v
Network
```

Flush based on:

``` text
records >= MAX_BATCH_SIZE

        OR

elapsed_time >= MAX_BATCH_DELAY
```

Example:

``` text
500 records
OR
500 ms

whichever occurs first
```

This balances:

``` text
Throughput <------> Latency
```

------------------------------------------------------------------------

# 14. Cloud Durable Event Stream

Do not design:

``` text
Devices -> API -> Database
```

Instead:

``` text
Devices
   |
   v
Cloud Ingestion
   |
   v
Durable Event Stream
   |
   +----------+----------+
   |          |          |
   v          v          v
TSDB       Alerts      Archive
```

Why?

Suppose:

``` text
Incoming = 1,000,000 events/sec

Database temporarily handles
         = 700,000 events/sec
```

Without buffering, ingestion immediately suffers.

With a durable event stream:

``` text
Fast producers
      |
      v
+--------------------+
| Durable Event Bus  |
+--------------------+
      |
      v
Slower consumers
```

the backlog can temporarily grow while downstream systems recover.

------------------------------------------------------------------------

# 15. Partitioning and Ordering

A likely interview question:

> How would you partition Kafka?

Possible key:

``` text
partitionKey = DeviceID
```

Then:

``` text
Device A

100
101
102
103
 |
 v
Partition 17
```

This allows **per-device ordering**.

Avoid global ordering unless it is explicitly required.

``` text
Global ordering
      |
      v
Reduced parallelism
      |
      v
Poor scalability
```

Principal-level answer:

> I would first establish the ordering domain. For most telemetry
> pipelines, per-device or per-asset ordering is sufficient and allows
> horizontal partitioning.

------------------------------------------------------------------------

# 16. Event Time vs Ingestion Time

Suppose network disappears at 10:00.

Device records:

``` text
10:01 temperature 80
10:02 temperature 82
10:03 temperature 85
```

Network returns at 10:20.

Cloud receives all records around:

``` text
10:20
```

Therefore preserve both:

``` text
eventTime
    = when measurement occurred

ingestionTime
    = when cloud received it
```

Otherwise historical analytics become incorrect.

Also consider clock synchronization/drift using NTP/PTP depending on
industrial requirements.

------------------------------------------------------------------------

# 17. Reconnection Storm

Suppose:

``` text
5000 gateways
     |
     X
Plant network outage
```

Each gateway accumulates telemetry locally.

Network returns:

``` text
5000 gateways
     |
     +--------------------> Cloud
     +--------------------> Cloud
     +--------------------> Cloud
     ...
```

This can create a huge traffic spike.

Use:

``` text
Exponential backoff
        +
Random jitter
        +
Server throttling
        +
Replay rate limiting
```

Example:

``` text
delay = min(base * 2^attempt, maxDelay)
        + random_jitter
```

------------------------------------------------------------------------

# 18. Backpressure

Suppose cloud cannot keep up:

``` text
Cloud overloaded
      |
      v
Ingestion throttles
      |
      v
Edge reduces transmission rate
      |
      v
Persistent WAL grows
```

At that point telemetry priority becomes important.

``` text
Priority 1
Critical alarms
Never silently discard

Priority 2
Operational telemetry
Retain according to policy

Priority 3
High-frequency diagnostics
May aggregate/expire if explicitly allowed
```

------------------------------------------------------------------------

# 19. Edge Disk Full

A Senior Principal interviewer may ask:

> What if the WAN is down for three days and the WAL fills the disk?

This must be an explicit product policy.

Possible approach:

``` text
Critical alarms
    -> highest retention priority

Operational telemetry
    -> normal retention

Diagnostic telemetry
    -> aggregate / expire oldest if allowed
```

Monitor:

``` text
WAL disk utilization
Oldest unsent event
Number of unsent records
Dropped/aggregated record count
```

Never silently discard important telemetry.

------------------------------------------------------------------------

# 20. Failure Handling Summary

  -----------------------------------------------------------------------
  Failure                             Response
  ----------------------------------- -----------------------------------
  WAN unavailable                     Continue writing to WAL

  Edge process crashes                Recover WAL after restart

  ACK lost                            Retransmit; cloud deduplicates

  Duplicate event                     Device ID + sequence number

  Cloud unavailable                   Backoff and retain locally

  Consumer slow                       Event-stream backlog grows

  Database unavailable                Event stream retains data

  Edge disk full                      Explicit priority/retention policy

  Device clock incorrect              Event + ingestion timestamps, drift
                                      detection

  Mass reconnect                      Backoff + jitter + throttling

  Corrupt WAL/event                   Checksum + validation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 21. LLD --- Main Edge Components

``` text
+-----------------------+
|      Collector        |
+-----------+-----------+
            |
            v
+-----------------------+
|      Normalizer       |
+-----------+-----------+
            |
            v
+-----------------------+
|      WAL Writer       |
+-----------+-----------+
            |
            v
+-----------------------+
|       Batcher         |
+-----------+-----------+
            |
            v
+-----------------------+
|       Sender          |
+-----------+-----------+
            |
            v
         Cloud

Supporting components:

Retry Controller
Checkpoint Manager
Retention Manager
Metrics / Health Monitor
```

Responsibilities:

### Collector

Receives sensor samples.

### Normalizer

Adds:

``` text
Device ID
Sequence number
Timestamp
Schema version
```

### WAL Writer

``` text
Append records
Segment rotation
Checksums
Recovery
```

### Batcher

Builds batches based on:

``` text
size OR timeout
```

### Sender

Handles:

``` text
Connection
Transmission
ACK processing
Retry
```

### Checkpoint Manager

Stores:

``` text
highest durably ACKed sequence
```

### Retention Manager

Reclaims fully acknowledged WAL segments and applies disk-space policy.

------------------------------------------------------------------------

# 22. WAL Durability Detail

Calling:

``` cpp
write(fd, data, size);
```

does not always mean the data has physically reached persistent storage.

Conceptually:

``` text
Application
    |
    | write()
    v
OS Page Cache
    |
    | fsync()/fdatasync()
    v
Storage Device
```

Calling `fsync()` for every telemetry record can be expensive.

Possible compromise:

``` text
Record
Record
Record
Record
   |
   v
Group append
   |
   v
Periodic/group fsync
```

This is a trade-off between:

``` text
Durability <------> Throughput
```

------------------------------------------------------------------------

# 23. Crash Recovery

After restart:

``` text
Start Edge Agent
      |
      v
Load checkpoint
      |
      v
Scan WAL segments
      |
      v
Validate checksum/record length
      |
      v
Detect incomplete tail
      |
      v
Truncate/ignore partial tail record
      |
      v
Resume after last ACKed sequence
```

------------------------------------------------------------------------

# 24. C++11/14 Data Model

``` cpp
struct TelemetryRecord
{
    std::string deviceId;
    uint64_t sequenceNo;
    int64_t eventTimeMs;
    std::string metric;
    double value;
};
```

------------------------------------------------------------------------

# 25. C++11/14 WAL Interface

``` cpp
class Wal
{
public:
    bool append(const TelemetryRecord& record);

    std::vector<TelemetryRecord> readAfter(
        uint64_t checkpoint,
        size_t maxRecords);

    bool persistCheckpoint(uint64_t sequenceNo);

    uint64_t loadCheckpoint() const;

    void reclaim(uint64_t checkpoint);
};
```

------------------------------------------------------------------------

# 26. Cloud Client Interface

``` cpp
class CloudClient
{
public:
    struct Result
    {
        bool success;
        uint64_t highestDurablyStoredSequence;
    };

    Result send(
        const std::vector<TelemetryRecord>& batch);
};
```

------------------------------------------------------------------------

# 27. C++ Store-and-Forward Logic

``` cpp
class EdgeAgent
{
public:
    EdgeAgent(Wal& wal, CloudClient& cloud)
        : wal_(wal),
          cloud_(cloud),
          checkpoint_(wal.loadCheckpoint())
    {
    }

    bool ingest(const TelemetryRecord& record)
    {
        // Persist locally before depending on WAN delivery.
        return wal_.append(record);
    }

    void flushOnce()
    {
        const size_t kBatchSize = 500;

        std::vector<TelemetryRecord> batch =
            wal_.readAfter(checkpoint_, kBatchSize);

        if (batch.empty())
            return;

        CloudClient::Result result =
            cloud_.send(batch);

        if (!result.success)
        {
            // Keep data in WAL.
            // Retry later using backoff + jitter.
            return;
        }

        if (result.highestDurablyStoredSequence >
            checkpoint_)
        {
            checkpoint_ =
                result.highestDurablyStoredSequence;

            if (wal_.persistCheckpoint(checkpoint_))
            {
                wal_.reclaim(checkpoint_);
            }
        }
    }

private:
    Wal& wal_;
    CloudClient& cloud_;

    uint64_t checkpoint_;
};
```

Important sequence:

``` text
append WAL
    |
    v
send batch
    |
    v
receive durable ACK
    |
    v
persist checkpoint
    |
    v
reclaim WAL
```

------------------------------------------------------------------------

# 28. C++ Retry --- Exponential Backoff + Jitter

``` cpp
#include <algorithm>
#include <chrono>
#include <random>
#include <thread>

void retryDelay(unsigned attempt)
{
    const unsigned kBaseMs = 200;
    const unsigned kMaxMs = 30000;

    unsigned shift =
        std::min(attempt, 10u);

    unsigned delay =
        std::min(
            kBaseMs * (1u << shift),
            kMaxMs);

    static std::mt19937 rng(
        static_cast<unsigned>(
            std::chrono::steady_clock::now()
                .time_since_epoch()
                .count()));

    std::uniform_int_distribution<unsigned>
        jitter(0, 250);

    std::this_thread::sleep_for(
        std::chrono::milliseconds(
            delay + jitter(rng)));
}
```

### Why jitter?

Without jitter:

``` text
Gateway 1 retry -> 1s -> 2s -> 4s -> 8s
Gateway 2 retry -> 1s -> 2s -> 4s -> 8s
Gateway 3 retry -> 1s -> 2s -> 4s -> 8s
```

Thousands of devices can repeatedly hit the cloud together.

With jitter:

``` text
Gateway 1 -> 4.13 sec
Gateway 2 -> 4.21 sec
Gateway 3 -> 4.07 sec
```

Retries spread out.

------------------------------------------------------------------------

# 29. Edge Threading Model

A simple conceptual model:

``` text
Sensor threads
     |
     v
Bounded memory queue
     |
     v
WAL Writer
     |
     v
Persistent WAL
     |
     v
Batch Reader
     |
     v
Sender Thread
     |
     v
Cloud
```

Important:

> The memory queue improves throughput. The WAL provides durability.

Do not confuse the two.

------------------------------------------------------------------------

# 30. Security Design

``` text
Edge Device
     |
     | Device certificate
     |
     | mTLS
     v
Cloud Gateway
     |
     v
Authenticate device
     |
     v
Authorize:
tenant / plant / device
```

Consider:

``` text
Certificate provisioning
Certificate rotation
Certificate revocation
TLS
Encryption at rest
Least privilege
Device identity
Audit logs
```

------------------------------------------------------------------------

# 31. Observability

## Edge metrics

``` text
wal_bytes
wal_records
oldest_unsent_event_age
send_rate
retry_rate
reconnect_count
disk_usage
batch_size
compression_ratio
```

## Cloud metrics

``` text
ingestion_events_per_sec
ingestion_bytes_per_sec
broker_partition_lag
consumer_lag
duplicate_rate
invalid_event_rate
processing_latency
end_to_end_latency
```

Useful signal:

``` text
current_time - event_time
```

A sudden increase may indicate that devices are replaying an offline
backlog.

------------------------------------------------------------------------

# 32. HLD in One Diagram

``` text
                         INDUSTRIAL SITE

 Sensors / PLCs
      |
      v
+----------------+
| Edge Collector |
+-------+--------+
        |
        v
+----------------+
| Persistent WAL |
+-------+--------+
        |
        v
+----------------+
| Batch/Compress |
+-------+--------+
        |
        v
+----------------+
| Network Sender |
+-------+--------+
        |
        | MQTT / HTTPS / gRPC
        | TLS / mTLS
        |
========|============ UNRELIABLE WAN =========================
        |
        v
+-------------------+
| Cloud Ingestion   |
+---------+---------+
          |
          v
+-------------------+
| Durable Event Bus |
+---------+---------+
          |
     +----+---------+-------------+
     |              |             |
     v              v             v
+----------+    +--------+    +---------+
| Processor|    | Alerts |    | Archive |
+----+-----+    +--------+    +---------+
     |
     v
+----------------+
| Time-Series DB |
+-------+--------+
        |
        v
 Dashboard / Analytics / ML
```

------------------------------------------------------------------------

# 33. How to Present This in the Interview

## Step 1 --- Clarify

Say:

> Before choosing technologies, I would establish device count, event
> rate, average record size, maximum offline duration, latency target,
> loss tolerance, ordering requirement, and edge storage constraints.

## Step 2 --- Identify the hardest constraint

> The intermittent WAN is the defining constraint, so I would first make
> the edge independently durable.

## Step 3 --- Draw the edge path

``` text
Sensor -> Collector -> WAL -> Batch -> Sender
```

## Step 4 --- Draw the cloud path

``` text
Ingestion -> Durable Event Stream -> Consumers -> Storage
```

## Step 5 --- Explain delivery

``` text
At-least-once
+
stable event identity
+
idempotent processing
```

## Step 6 --- Explain scale

``` text
Partition by Device ID
+
horizontal ingestion
+
multiple consumers
```

## Step 7 --- Attack your own architecture

Discuss:

``` text
WAN down
Edge crash
ACK lost
Duplicate
Cloud down
Database down
Disk full
Reconnect storm
Consumer lag
Clock drift
```

------------------------------------------------------------------------

# 34. Principal-Level Follow-Up Questions

Be prepared for:

### Why WAL instead of an in-memory queue?

Because WAL survives process restart/reboot and enables durable
store-and-forward.

### Why not send directly to the database?

It couples ingestion availability and throughput to database
availability and throughput.

### What happens if ACK is lost?

Edge retransmits; cloud detects the duplicate using stable event
identity.

### How do you guarantee ordering?

Define the ordering scope first. Partition by Device ID for per-device
ordering.

### Why not exactly-once?

End-to-end exactly-once across edge, WAN, broker, processors and storage
is expensive and easy to misstate. At-least-once + idempotency is often
simpler and robust.

### What happens when the WAN returns?

Replay backlog gradually with throttling rather than flooding the cloud.

### What happens when the disk becomes full?

Apply an explicit priority/retention policy and raise health alerts.
Never silently discard critical data.

### What if Kafka is down?

Cloud ingestion should fail/backpressure rather than falsely ACK data
that has not been durably accepted. Edge retains unacknowledged
telemetry and retries.

### What if the time-series database is down?

The durable cloud stream retains the backlog while consumers/storage
recover.

------------------------------------------------------------------------

# 35. Final Memory Map

``` text
Requirement / Failure       Solution
-------------------------------------------------

Intermittent WAN        ->  Persistent WAL
Edge crash              ->  WAL recovery
Lost ACK                ->  Retry
Retry                    ->  Dedup / idempotency
High-frequency data     ->  Batching + compression
High cloud traffic      ->  Durable event stream
Per-device ordering     ->  Partition by Device ID
Cloud slowdown          ->  Backpressure
Mass reconnect          ->  Backoff + jitter + throttling
Disk full               ->  Priority + retention policy
Delayed telemetry       ->  Event time + ingestion time
Device security         ->  X.509 + mTLS
Operations              ->  Metrics + health monitoring
```

------------------------------------------------------------------------

# 36. One Answer to Remember

> I would design this as a durable store-and-forward pipeline. At the
> edge, telemetry is first persisted to a segmented WAL, then batched
> and transmitted to the cloud. The cloud only acknowledges data after
> durable acceptance. Because ACKs can be lost, delivery is
> at-least-once and records carry a stable device ID and sequence number
> for idempotent processing. On the cloud side, a durable event stream
> decouples high-rate ingestion from time-series storage, alerting and
> analytics. Per-device partitioning preserves the required local
> ordering while allowing horizontal scale. The design explicitly
> handles WAN outages, edge crashes, backpressure, disk exhaustion and
> reconnection storms.
