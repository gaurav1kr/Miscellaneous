# Samsung Stability Monitor --- Director Round Interview Guide

## Linux TV Systems \| C/C++ \| Multithreading \| Resource Monitoring \| Fault Recovery \| Production Observability

> **Interview positioning:** Present this as a lightweight, always-on
> **system stability and fault-detection daemon** for Samsung TV
> systems. It continuously monitored per-process CPU, memory, and flash
> behavior, took protective actions on sustained/critical threshold
> violations, generated diagnostic evidence, and exposed production
> telemetry through Samsung's KPI infrastructure.

> **Important:** Sections marked **Original Design** reflect the
> supplied project notes. Sections marked **How I Would Improve It
> Today** are architectural improvements for interview discussion and
> should not be presented as features that definitely existed in the
> original implementation.

------------------------------------------------------------------------

# 1. Problem Statement

A Smart TV runs many long-lived native daemons, applications,
web-runtime processes, and platform services. A single misbehaving
process can gradually destabilize the complete device through:

-   sustained CPU consumption,
-   abnormal memory consumption,
-   excessive flash/storage consumption,
-   hangs or degraded responsiveness,
-   repeated process crashes,
-   system-level resource exhaustion.

The Stability Monitor ran continuously and monitored these conditions
with different policies for CPU, memory, and flash.

The central design idea was:

``` text
                         Linux /proc + Driver
                                |
                                v
                    +-----------------------+
                    |  Stability Monitor    |
                    |       Daemon          |
                    +-----------+-----------+
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
      CPU Monitor          Memory Monitor       Flash Monitor
         Thread                Thread               Thread
             |                  |                  |
             +------------------+------------------+
                                |
                                v
                    Shared Process Information
                    Doubly Linked List
                                |
                   +------------+------------+
                   |                         |
                   v                         v
            Protective Actions         Observability
            Alarm / SIGABRT            KPI Server
            Core Dump / Kill           Top Consumers
                   |                         |
                   v                         v
            Process Recovery          Production RCA
```

------------------------------------------------------------------------
# 2. GitHub-Friendly Unified Architecture

``` mermaid
flowchart TD
    A[Start stability-monitor daemon] --> B[Initialize Threads]

    B --> T1[MemoryMonitor Thread]
    B --> T2[FlashMonitor Thread]
    B --> T3[CPUMonitor Thread]

    T1 --> L1[Read proc via driver]
    T2 --> L1
    T3 --> L1

    L1 --> L2[Update Shared Doubly Linked List]

    T3 --> C1[Traverse Process List]
    C1 --> C2[Compute CPU 1-min and 3-min Windows]
    C2 --> C3{CPU Threshold Breach?}
    C3 -->|Yes| C4[Raise Alarm]
    C4 --> C5[Send SIGABRT]
    C5 --> C6[Generate Core Dump]
    C6 --> C7[Remove Process Node]

    T1 --> M1[Traverse Process List]
    M1 --> M2[Check Current Memory]
    M2 --> M3{Memory Threshold Breach?}
    M3 -->|Yes| M4[Kill Process + Alarm]

    T2 --> F1[Collect Flash Usage]
    F1 --> F2[Sort Descending]
    F2 --> F3[Identify Top 5]
    F3 --> F4[Push to KPI Server]
    F3 --> F5{Global Flash Threshold Breach?}
    F5 -->|Yes| F6[Mark Top 5 RED]
    F6 --> F7[Trigger Power Off]
    F7 --> F8[Notify Owners]

    C7 --> R1[Process Restarts]
    R1 --> R2[Detect via proc]
    R2 --> R3[Create New Node]
    R3 --> R4[Insert into Shared List]
```

------------------------------------------------------------------------

# 3. Original Design --- Main Components

## 4.1 Stability Monitor Daemon

The daemon is the always-running supervisory process.

Responsibilities:

``` text
Initialize monitoring infrastructure
        |
        +--> CPU monitor thread
        +--> Memory monitor thread
        +--> Flash monitor thread
        |
        +--> maintain shared process information
        |
        +--> trigger protective actions
        |
        +--> generate diagnostics / telemetry
```

The monitoring process itself must remain lightweight because an
always-on stability component must not become a source of instability.

------------------------------------------------------------------------

# 4. Shared Process Model --- Doubly Linked List

The supplied design uses one shared doubly linked list as the central
source of truth for process monitoring.

``` text
HEAD
 |
 v
+---------+    +---------+    +---------+
| PID 101 |<-->| PID 205 |<-->| PID 331 |
| CPU     |    | CPU     |    | CPU     |
| Memory  |    | Memory  |    | Memory  |
+---------+    +---------+    +---------+
                                |
                                v
                               TAIL
```

Each process node contains conceptually:

``` text
ProcessNode
    |
    +-- PID
    +-- CPU usage history
    |      +-- 1-minute samples
    |      +-- 3-minute samples
    |
    +-- current memory snapshot
    |
    +-- prev
    +-- next
```

### Why a doubly linked list?

The important design reason was dynamic process lifecycle management.

When a monitored process is terminated:

``` text
A <-> B <-> C

Delete B

A <------> C
```

Deletion is O(1) when the node is already known.

The structure also naturally supports process insertion when a service
restarts.

### Interview answer

> "Processes were dynamic---they could terminate and restart---so we
> needed a structure supporting frequent traversal plus efficient
> insertion and deletion. A doubly linked list gave us O(1) removal once
> the process node was identified, without shifting elements as an
> array/vector would."

------------------------------------------------------------------------

# 5. Process Lifecycle

``` text
Process appears in /proc
        |
        v
Create ProcessNode
        |
        v
Insert into shared list
        |
        v
CPU / Memory monitoring
        |
        v
Threshold breach?
      /     \
    No       Yes
    |         |
    |         v
    |    Alarm / SIGABRT / Kill
    |         |
    |         v
    |      Core Dump
    |         |
    |         v
    |    Remove Node
    |         |
    |         v
    |   Process Restarts
    |         |
    +---------+
```

The supplied project notes state that a process killed through `SIGABRT`
produces a core dump and is removed from the list; after the
system/service manager restarts it, the process is detected again and a
new node is inserted.

------------------------------------------------------------------------

# 6. CPU Monitor

CPU monitoring is **historical/stateful** rather than a single-snapshot
decision.

## Inputs

The supplied design uses:

``` text
/proc/uptime
/proc/[PID]/stat
CLK_TCK / Hertz
```

Conceptual calculation:

``` text
total_time = utime + stime
total_time += cutime + cstime       (optional)

seconds = uptime - (starttime / Hertz)

cpu_usage = 100 * ((total_time / Hertz) / seconds)
```

The project notes describe a four-core system as having an aggregate
capacity of 400%.

------------------------------------------------------------------------

# 7. Why CPU Uses Sliding Windows

A short CPU spike does not necessarily mean the process is unhealthy.

Example:

``` text
Time       CPU

10:00:00   20%
10:00:10   25%
10:00:20   98%    <-- temporary spike
10:00:30   30%
10:00:40   22%
```

Killing immediately at the 98% sample would create a false positive.

Instead, the original policy evaluates sustained CPU behavior:

``` text
>= 95% for 1 minute

        OR

>= 90% for 3 minutes
```

Conceptually:

``` text
CPU samples
    |
    v
Time Window
    |
    +--> 1-minute average
    |
    +--> 3-minute average
             |
             v
      Threshold Evaluation
             |
      +------+------+
      |             |
    Normal        Breach
                    |
                    v
                  Alarm
                    |
                    v
                 SIGABRT
                    |
                    v
                Core Dump
```

This is an excellent interview point:

> **The policy distinguishes a transient spike from sustained resource
> abuse.**

------------------------------------------------------------------------

# 8. CPU History Storage

The project notes identify a time-series/ring-buffer style
representation as an appropriate way to maintain samples.

Conceptually:

``` text
ProcessNode

CPU Samples:
+----+----+----+----+----+----+
| t1 | t2 | t3 | t4 | t5 | t6 |
+----+----+----+----+----+----+
                  ^
                  |
              newest sample
```

Once capacity is reached:

``` text
oldest sample overwritten
```

This provides bounded memory usage---important for an always-running
daemon.

------------------------------------------------------------------------

# 9. CPU Threshold Breach Flow

``` text
Read CPU statistics
        |
        v
Add sample
        |
        v
Calculate sliding-window values
        |
        v
+-------------------------------+
| >=95% for 1 min               |
|           OR                  |
| >=90% for 3 min               |
+---------------+---------------+
                |
             Breach
                |
                v
          Trigger Alarm
                |
                v
           Send SIGABRT
                |
                v
        Generate Core Dump
                |
                v
       Remove Process Node
```

The core dump is particularly valuable because simply restarting the
process restores service but does not explain the defect.

------------------------------------------------------------------------

# 10. Memory Monitor

Memory uses a different monitoring strategy.

The supplied thresholds are:

  Process category   Identification            Limit
  ------------------ ---------------------- --------
  Daemon             `PPID = 1`                40 MB
  DefaultApp         regular applications     110 MB
  WebApp             WebRuntime               600 MB

The supplied design uses **current memory snapshot only**, rather than
CPU-style history.

``` text
Read process memory
        |
        v
Classify process
        |
        v
Select threshold
        |
        v
Current memory > limit?
       /       \
     No         Yes
     |           |
   Continue    Alarm
                 |
                 v
           Kill Process
```

### Why different from CPU?

The original project notes describe memory monitoring as faster
snapshot-based detection, while CPU monitoring deliberately tracks
historical behavior.

This gives a good architectural discussion:

``` text
CPU
  -> historical
  -> sustained behavior
  -> sliding window

Memory
  -> current snapshot
  -> category-specific threshold

Flash
  -> aggregated/system-wide
  -> top consumers + KPI
```

------------------------------------------------------------------------

# 11. Flash Monitor

Flash monitoring has a broader system-level role.

The supplied design focuses on critical storage such as `/opt`.

Flow:

``` text
Collect per-process flash usage
             |
             v
      Sort descending
             |
             v
       Select Top 5
          /      \
         /        \
        v          v
   KPI Server   Threshold Check
                    |
                    v
             Global breach?
               /       \
             No         Yes
             |           |
          Continue    Mark Top 5 RED
                         |
                         v
                  Trigger Power Off
                         |
                         v
                    Notify Owners
```

------------------------------------------------------------------------

# 12. Why Top Five?

The system does not only need to know:

``` text
Flash is full.
```

For production debugging, engineers need to know:

``` text
WHO consumed it?
```

Therefore:

``` text
Total flash problem
        |
        v
Rank processes
        |
        v
Top 5 consumers
        |
        v
KPI telemetry
```

When a customer reports:

``` text
TV hang
performance issue
abrupt power-off
```

engineers can inspect KPI data around that timestamp and identify
abnormal consumers.

------------------------------------------------------------------------

# 13. KPI Server --- Production Observability

This part turns Stability Monitor from a purely local watchdog into a
production-debugging system.

``` text
Customer TV
    |
    v
Stability Monitor
    |
    +--> Top 5 flash consumers
    +--> resource anomaly
    +--> RED marking
    |
    v
Samsung KPI Server
    |
    v
Engineering / Process Owner
    |
    v
Root Cause Analysis
```

A good Director-round statement:

> "The local action protected the device, but telemetry solved the
> second problem: explaining why the protection was triggered in the
> field."

------------------------------------------------------------------------

# 14. Threading Architecture

The design contains three concurrent monitoring threads:

``` text
                   Shared Process List
                          / | \
                         /  |  \
                        /   |   \
                       v    v    v
                     CPU  Memory Flash
                   Thread Thread Thread
```

Because they access shared process state, synchronization is required
around operations such as:

``` text
insert node
delete node
update CPU history
update memory state
traverse shared list
```

------------------------------------------------------------------------

# 15. Important Race Condition

This is a very probable systems-interview question.

Suppose:

``` text
CPU Thread                       Memory Thread

Find PID 500
   |
Get node pointer
   |
                                   Detect breach
                                       |
                                   Delete PID 500
                                       |
                                   Free node
   |
Read node
   |
   X use-after-free
```

This can cause the **stability daemon itself to crash**.

That would be particularly serious because the component responsible for
protecting system stability becomes unstable.

The original notes therefore require mutex-based critical-section
protection for safe insertion, deletion, and traversal.

------------------------------------------------------------------------

# 16. Synchronization Strategy

A straightforward safe model is:

``` text
Thread
  |
  v
Acquire mutex
  |
  v
Access / update shared list
  |
  v
Release mutex
```

However, lock scope matters.

Avoid holding the shared-list lock while doing slow external work such
as:

``` text
core-dump handling
network communication
KPI upload
power-off coordination
```

Conceptually:

``` text
LOCK
 |
 +--> find/update/copy required metadata
 |
UNLOCK
 |
 +--> expensive external action
```

This minimizes contention.

------------------------------------------------------------------------

# 17. Biggest Probable Challenge I Faced

## Building an Always-On Monitor That Must Not Become a Stability Problem Itself

This is the strongest Director-level challenge story.

> "The biggest challenge was that the stability monitor itself was an
> always-running system daemon. It was responsible for identifying
> processes that destabilized the TV, so its own CPU usage, memory
> footprint, synchronization behavior and failure handling had to be
> extremely controlled."

There are several competing requirements:

``` text
Detect problems quickly
        |
        +--> frequent sampling

BUT

Keep monitor overhead low
        |
        +--> avoid excessive /proc reads
        +--> bounded CPU history
        +--> efficient data structures

AND

Multiple monitor threads
        |
        +--> synchronization required

BUT

Avoid lock contention / deadlocks

AND

Take corrective action
        |
        +--> process termination

BUT

Avoid false positives
        |
        +--> sustained CPU windows
```

### Interview answer

> "One of the biggest challenges was designing a monitor that was itself
> lightweight and reliable. We had CPU, memory and flash monitoring
> operating concurrently over dynamic process information. Processes
> could disappear or restart while another thread was traversing the
> shared state, so synchronization had to prevent races and
> use-after-free conditions without turning the shared lock into a
> bottleneck.
>
> At the same time, we didn't want transient CPU spikes to cause
> unnecessary process kills, so CPU used sustained one-minute and
> three-minute windows rather than a single sample. Memory used a
> different snapshot-based policy, and flash monitoring aggregated the
> top consumers and sent them to the KPI system.
>
> Another important aspect was diagnosability. For CPU threshold
> violations we used SIGABRT so that a core dump was available.
> Restarting a bad process can restore service, but without diagnostic
> evidence the root cause is lost.
>
> So the real engineering balance was detection speed versus monitoring
> overhead, concurrency safety versus lock contention, and automated
> recovery versus enough evidence to debug field failures."

------------------------------------------------------------------------

# 18. Why `SIGABRT` Instead of Only `SIGKILL`?

The supplied design specifically uses `SIGABRT` for the CPU breach flow.

This is valuable because it supports:

``` text
Resource violation
      |
      v
SIGABRT
      |
      v
Core Dump
      |
      v
Process restarts
      |
      v
Service restored

AND

Core Dump
      |
      v
Offline debugging
      |
      v
Root cause
```

A hard kill may stop the process but can remove the opportunity to
capture useful crash-state evidence.

------------------------------------------------------------------------

# 19. Why Not One Generic Threshold Algorithm?

Because CPU, memory, and flash have different failure characteristics.

``` text
                 Resource Monitoring
                        |
       +----------------+----------------+
       |                |                |
       v                v                v
      CPU             Memory           Flash
       |                |                |
 Historical          Snapshot       Aggregated
       |                |                |
1m / 3m window     Type-specific      Top 5
       |             limits             |
       v                v                v
Sustained abuse    Immediate action   KPI + protection
```

A Director-level lesson:

> **Use a policy appropriate to the resource rather than forcing all
> signals through one generic mechanism.**

------------------------------------------------------------------------

# 20. Complexity Discussion

Assume `N` monitored processes.

### Full traversal

CPU or memory scanning the process list:

``` text
O(N)
```

### Known-node deletion

Doubly linked list:

``` text
O(1)
```

once the node is located.

### Flash ranking

If all `N` processes are fully sorted:

``` text
O(N log N)
```

The supplied design says the processes are sorted descending and the top
five are selected.

------------------------------------------------------------------------

# 21. Failure Scenarios to Prepare

## Process exits while being monitored

The process may disappear between discovery and `/proc/<pid>` access.

Treat process disappearance as a normal lifecycle event rather than
necessarily a daemon failure.

## CPU thread and memory thread act on the same process

Correct synchronization/state transition is needed to prevent double
deletion or invalid memory access.

## KPI server unavailable

Local device protection should not conceptually depend on successful
telemetry delivery. The supplied notes establish KPI integration, but do
not specify the exact buffering/retry behavior; do not claim a
particular implementation unless you remember it.

## Core dump fails

The supplied notes state that a core dump is generated on the CPU breach
path, but they do not specify fallback behavior. In an interview,
distinguish the original behavior from how you would harden it.

## Monitor itself consumes excessive resources

Sampling frequency, bounded history, lock duration, and telemetry volume
should be controlled.

------------------------------------------------------------------------

# 22. Director-Level Design Trade-Offs

## Detection speed vs overhead

Higher sampling frequency:

``` text
+ faster detection
- more CPU
- more /proc access
```

Lower frequency:

``` text
+ lower monitor overhead
- slower anomaly detection
```

## Historical accuracy vs memory

More CPU samples:

``` text
+ better history
- larger per-process memory footprint
```

A fixed-size ring buffer bounds the cost.

## Mutex simplicity vs concurrency

Single mutex:

``` text
+ simple correctness model
- potential contention
```

More granular locking:

``` text
+ more concurrency
- greater complexity
- higher deadlock/race risk
```

For a small embedded process population, simple and correct can be
preferable to over-engineering.

------------------------------------------------------------------------

# 23. How I Would Improve It Today

These are **architectural improvements**, not claims about the original
implementation.

## 23.1 Read-Write Lock

If traversal/read operations dominate mutations:

``` text
Readers:
CPU / Memory / Flash
      |
      +--> concurrent read access

Writer:
insert/delete/update requiring exclusivity
```

A read-write lock could improve concurrency, although the actual benefit
should be measured.

## 23.2 Cooldown / Hysteresis

Avoid repeated actions when a process repeatedly approaches a threshold.

``` text
Normal
  |
  v
Threshold breach
  |
  v
Action
  |
  v
Cooldown
  |
  v
Eligible for next action
```

## 23.3 Critical-Process Whitelist / Policy

Some platform-critical processes may need different recovery behavior.

## 23.4 Rate-Limited Alerting

Avoid flooding telemetry/owners during cascading failures.

## 23.5 More Explicit State Machine

Per-process monitoring state could make concurrent actions easier to
reason about:

``` text
Healthy
  |
  v
Suspected
  |
  v
Violation
  |
  v
Terminating
  |
  v
Restarting
  |
  v
Healthy
```

------------------------------------------------------------------------

# 24. Observability I Would Discuss

Original notes identify centralized logging and KPI visibility.

Useful operational signals include:

``` text
CPU threshold breaches
Memory threshold breaches
Flash threshold breaches
Process kills
Core-dump generation
Process restarts
Top flash consumers
```

For a modernized version, I would additionally consider:

``` text
monitor loop latency
sampling duration
lock wait time
number of monitored processes
daemon CPU overhead
daemon memory footprint
KPI send failures
false-positive / repeated-action rate
```

Again, these additional metrics are proposed improvements unless they
were present in the actual implementation.

------------------------------------------------------------------------

# 25. Probable Director-Round Questions

## "Why did you use a doubly linked list?"

> "The monitored process set was dynamic. Processes could be terminated
> and restarted, and once we had a node, a doubly linked list gave us
> O(1) deletion without shifting other entries. It also supported
> straightforward insertion and continuous traversal."

## "Why not `std::vector`?"

> "Vector gives excellent locality and would be attractive for
> read-heavy stable data, but deleting arbitrary process entries
> requires shifting elements and invalidates iterators/references. Our
> process lifecycle involved dynamic removal and reinsertion, so the
> linked-list trade-off was useful."

## "Why do you need locks?"

> "CPU, memory and flash monitors share process information. Without
> synchronization, one thread could delete a node while another was
> traversing it, causing a use-after-free or corrupted links."

## "Would you keep the mutex while generating a core dump?"

> "No. I would keep critical sections as small as possible. I would
> safely capture/update the state under the lock, release it, and then
> perform slow external work."

## "Why are CPU and memory policies different?"

> "A short CPU spike can be legitimate, so CPU uses sustained windows.
> The supplied memory design uses category-specific current thresholds
> and takes immediate action. Different resources have different failure
> characteristics."

## "How do you avoid false CPU positives?"

> "By evaluating sustained one-minute and three-minute windows rather
> than reacting to one sample."

## "Why generate a core dump?"

> "Recovery and diagnosis are separate requirements. Restarting the
> process restores functionality, while the core dump preserves evidence
> needed to understand the defect."

## "What happens after the process is killed?"

> "Its node is removed. When the process is restarted by the
> system/service manager and appears again, a new node is created and
> inserted."

## "How would you reduce monitor overhead?"

> "Bound CPU history, tune sampling intervals, minimize `/proc` reads,
> keep lock scope small, avoid expensive work while holding shared
> locks, and measure the daemon's own CPU/memory overhead."

## "What would you redesign today?"

> "I would evaluate read-write locking, explicit per-process state,
> cooldown/hysteresis, rate-limited alerts, and stronger
> self-observability---but I would introduce them only if measurements
> justify the added complexity."

------------------------------------------------------------------------

# 26. 90-Second Director-Round Answer

> "At Samsung I worked on a C/C++ stability-monitor daemon running
> continuously on Linux-based TV systems. Its job was to detect
> processes that could destabilize the device through abnormal CPU,
> memory or flash consumption.
>
> We had separate CPU, memory and flash monitoring threads sharing a
> central process model implemented using a doubly linked list. The list
> suited the dynamic process lifecycle because when a process was
> terminated we could remove its node efficiently, and when the service
> restarted we inserted it again.
>
> The monitoring policy depended on the resource. CPU was stateful: we
> maintained historical samples and looked for sustained high
> utilization over one-minute and three-minute windows so that a
> temporary spike did not immediately kill a process. Memory used
> category-specific current thresholds. Flash monitoring ranked
> consumers, continuously reported the top five to Samsung's KPI system,
> and used that telemetry for field root-cause analysis.
>
> For sustained CPU violations, we raised an alarm and used SIGABRT so
> that we obtained a core dump before the process restarted. That was
> important because recovery alone isn't enough---you also need evidence
> to diagnose why the process became unhealthy.
>
> The biggest engineering challenge was ensuring that an always-on
> stability daemon did not itself become a stability problem. Multiple
> threads accessed dynamic process state, so we had to protect
> insertion, deletion and traversal from races while keeping critical
> sections and monitoring overhead low. The broader design trade-off was
> fast detection versus overhead, concurrency versus synchronization
> complexity, and automatic recovery versus avoiding false positives."

------------------------------------------------------------------------

# 27. Whiteboard Diagram to Memorize

``` text
                      Linux /proc
                          |
                          v
                 Stability Monitor
                       Daemon
                          |
         +----------------+----------------+
         |                |                |
         v                v                v
       CPU              Memory           Flash
      Thread            Thread           Thread
         |                |                |
         +----------------+----------------+
                          |
                          v
                 Shared Process DLL
                          |
           +--------------+--------------+
           |                             |
           v                             v
      Threshold Engine               KPI Server
           |                             |
           v                             v
  Alarm / SIGABRT / Kill           Field Telemetry
           |
           v
       Core Dump
           |
           v
    Process Restart
```

Then explain:

``` text
CPU    -> historical 1m / 3m windows
Memory -> current category-specific snapshot
Flash  -> aggregate -> sort -> top 5 -> KPI
```

------------------------------------------------------------------------

# 28. Five Lines to Remember

1.  **"The stability monitor was an always-on protection daemon, so its
    own overhead and reliability were part of the design requirement."**
2.  **"CPU used sustained sliding windows to distinguish a real runaway
    process from a temporary spike."**
3.  **"The shared doubly linked list supported dynamic process insertion
    and O(1) deletion once a process node was identified."**
4.  **"SIGABRT gave us both recovery through restart and diagnostic
    evidence through a core dump."**
5.  **"KPI telemetry converted a local protection mechanism into a
    production root-cause-analysis capability."**

------------------------------------------------------------------------

# 29. Project Positioning Alongside the IBM Projects

``` text
Samsung Stability Monitor
-------------------------
C / C++
Linux internals
/proc
Multithreading
Mutex / race conditions
Resource monitoring
Sliding windows
Data structures
Core dumps
Embedded-system reliability
Production telemetry



------------------------------------------------------------------------

# Appendix A --- Original Detailed Project Notes

The following preserves the supplied Stability Monitor notes for
reference.

# Stability-Monitor Daemon in TV Systems

The `stability-monitor` daemon continuously runs in TV systems to
monitor **CPU, Memory, and Flash usage** of all processes and ensure
system stability.

------------------------------------------------------------------------

## 🔷 Unified Architecture (All 3 Threads)

``` mermaid
flowchart TD
    A[Start stability-monitor daemon] --> B[Initialize Threads]

    B --> T1[MemoryMonitor Thread]
    B --> T2[FlashMonitor Thread]
    B --> T3[CPUMonitor Thread]

    %% Shared Data
    T1 --> L1[Read proc via driver]
    T2 --> L1
    T3 --> L1

    L1 --> L2[Update Doubly Linked List]

    %% CPU Flow
    T3 --> C1[Traverse List]
    C1 --> C2[Compute CPU usage 1min 3min]
    C2 --> C3{CPU Threshold Breach}

    C3 -->|>=95% 1min OR >=90% 3min| C4[Trigger Alarm]
    C4 --> C5[Send SIGABRT]
    C5 --> C6[Generate Core Dump]
    C6 --> C7[Remove Node]

    %% Memory Flow
    T1 --> M1[Traverse List]
    M1 --> M2[Check Current Memory]
    M2 --> M3{Memory Breach}
    M3 -->|Yes| M4[Kill Process + Alarm]

    %% Flash Flow
    T2 --> F1[Collect Flash Usage]
    F1 --> F2[Sort Descending]
    F2 --> F3[Top 5 Processes]

    F3 --> F4[Send to KPI Server]

    F3 --> F5{Flash Threshold Breach}
    F5 -->|Yes| F6[Mark Top 5 RED]
    F6 --> F7[Trigger Power Off]
    F7 --> F8[Notify Owners]

    %% Process Restart Flow
    C7 --> R1[Process Restarts]
    R1 --> R2[Read proc again]
    R2 --> R3[Create Node]
    R3 --> R4[Insert into List]

    %% Loop
    R4 --> L1
    M4 --> L1
    F4 --> L1
```

------------------------------------------------------------------------

## 🔷 Doubly Linked List Design (Detailed)

A **single shared doubly linked list** is used across all monitoring
threads and acts as the **central source of truth**.

### Node Structure

Each node represents a process and contains:

-   **Process ID (PID)**
-   **CPU usage history**
    -   Maintains samples for:
        -   Last 1 minute window
        -   Last 3 minute window
-   **Memory usage (current snapshot)**
-   **Pointers**
    -   `prev` → Previous node
    -   `next` → Next node

### Internal Design Insight

-   CPU history is typically stored as a **time-series buffer (ring
    buffer)** per node
-   Each sample is timestamped to support sliding window calculations
-   Memory is stored as **latest snapshot only**

------------------------------------------------------------------------

### Why Doubly Linked List?

-   ✅ **O(1) deletion** when a process is killed (no shifting like
    arrays)
-   ✅ Efficient forward/backward traversal
-   ✅ Supports dynamic insertion when processes restart
-   ✅ Works well with continuous monitoring loops

------------------------------------------------------------------------

## 🔷 Process Lifecycle Flow

1.  Process detected via `/proc`
2.  Node created and inserted into linked list
3.  CPU & Memory continuously monitored
4.  Threshold breach detected
5.  Process killed using `SIGABRT (6)`
6.  Core dump generated for debugging
7.  Node removed from linked list (O(1))
8.  Process restarts (by system/service manager)
9.  New node created and inserted again

------------------------------------------------------------------------

## 🔷 CPUMonitor (Detailed)

### System CPU Capacity

-   4 cores → Total = **400% CPU**

------------------------------------------------------------------------

### Threshold Rules

-   **\>=95% CPU for 1 minute**
-   **\>=90% CPU for 3 minutes**

------------------------------------------------------------------------

### Behavior

-   Periodically reads `/proc`
-   Tracks CPU usage per process
-   Maintains **historical data**
-   Applies **sliding window logic**

------------------------------------------------------------------------

### CPU Calculation

#### Required Inputs

-   `/proc/uptime`
-   `/proc/[PID]/stat`
-   Hertz (`CLK_TCK`)

#### Formula

    total_time = utime + stime
    total_time += cutime + cstime (optional)

    seconds = uptime - (starttime / Hertz)

    cpu_usage = 100 * ((total_time / Hertz) / seconds)

------------------------------------------------------------------------

### Sliding Window Logic (Important)

-   CPU samples collected periodically
-   Stored in node buffer
-   Compute:
    -   Avg CPU over last 1 min
    -   Avg CPU over last 3 min

------------------------------------------------------------------------

### Action on Threshold Breach

-   Raise alarm
-   Send `SIGABRT`
-   Generate core dump
-   Remove node from linked list

------------------------------------------------------------------------

## 🔷 MemMonitor (Detailed)

### Categories

  Type         Condition      Limit
  ------------ -------------- --------
  Daemon       PPID = 1       40 MB
  DefaultApp   Regular apps   110 MB
  WebApp       WebRuntime     600 MB

------------------------------------------------------------------------

### Behavior

-   Reads memory usage from `/proc`
-   Uses **current snapshot only**
-   No historical tracking
-   Faster detection compared to CPU

------------------------------------------------------------------------

### Action

-   Kill process immediately
-   Trigger memory alarm

------------------------------------------------------------------------

## 🔷 FlashMonitoring (Enhanced - Production Level)

### Scope

-   Monitors flash usage across all processes
-   Focus on critical partitions like `/opt`

------------------------------------------------------------------------

### Core Logic

1.  Collect flash usage of all running processes
2.  Sort processes in **descending order**
3.  Identify **top 5 flash consumers**

------------------------------------------------------------------------

### KPI Integration (Very Important)

-   Top 5 processes are continuously pushed to **Samsung KPI server**
-   Acts as a **telemetry and observability system**

------------------------------------------------------------------------

### Customer Issue Debug Flow

When a customer reports:

-   TV stuck / hang
-   Performance issue

👉 Engineers:

1.  Fetch KPI logs
2.  Check top 5 processes at that timestamp
3.  Identify abnormal flash consumers

------------------------------------------------------------------------

### Threshold-Based Protection

-   Global flash usage threshold is defined

-   If exceeded:

    -   Trigger **power-off signal**
    -   Mark **top 5 processes in RED** in KPI server

------------------------------------------------------------------------

### Alerting Mechanism

If customer reports **abrupt power-off**:

-   KPI already has **RED flagged processes**
-   System:
    -   Notifies process owners
    -   Helps immediate root cause analysis

------------------------------------------------------------------------

## 🔷 Thread Synchronization

Since all threads share the same linked list:

### Required Mechanisms

-   Mutex locks (critical section protection)
-   Safe insertion and deletion
-   Prevent race conditions during traversal

------------------------------------------------------------------------

## 🔷 Key Design Characteristics

### Single Source of Truth

-   One shared linked list across all monitors

### Hybrid Monitoring Model

-   CPU → Historical (stateful)
-   Memory → Real-time (stateless)
-   Flash → Aggregated + system-wide

### Fault Handling

-   Automatic process restart handling
-   Core dump enables debugging

------------------------------------------------------------------------

## 🔷 Possible Enhancements (Architect Level)

-   Use **Read-Write locks** instead of mutex
-   Introduce **cooldown period** to avoid repeated kills
-   Maintain **whitelist of critical processes**
-   Use **ring buffer for CPU samples**
-   Add **rate-limited alerting**

------------------------------------------------------------------------

## 🔷 Logging & Observability

-   Centralized logging system
-   Tracks:
    -   CPU spikes
    -   Memory breaches
    -   Flash anomalies
    -   Process kills
-   KPI server adds **production visibility**
