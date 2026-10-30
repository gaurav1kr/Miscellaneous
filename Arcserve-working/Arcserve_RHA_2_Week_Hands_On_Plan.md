# Arcserve RHA — 14-Day Hands-On C++11/14 Plan

**Objective:** Develop practical understanding of replication, cross-platform systems programming, reliability and high availability by implementing a Mini-RHA prototype. This is a learning POC, not Arcserve's proprietary design.

**Time:** 2–3 hours per day for 14 days. **Allocation:** ~70% implementation, ~30% reading/design. **Platforms:** Linux and Windows; build on one platform first, validate on the other.

## Daily plan

| Day | Topic | Deliverable | Acceptance check |
|---|---|---|---|
| 1 | RHA conceptual architecture; master/replica; initial vs incremental sync | One-page architecture and event-flow diagram | Explain write → transport → replica apply, and RPO/RTO |
| 2 | Portable C++11/14, RAII, filesystem APIs | File metadata scanner | Traverse files; capture relative path, size, mtime; handle errors |
| 3 | TCP sockets and protocol framing | Client/server skeleton | Length-prefixed messages survive partial send/recv |
| 4 | Streaming, checksums, acknowledgments | Reliable file transfer | Verify bytes and integrity; handle truncated transfers |
| 5 | Initial synchronization | Master/replica directory sync | Copy missing/changed files with temporary-file + rename apply |
| 6 | Incremental sync using periodic rescans | Create/update/delete reconciliation | Replicate edits/deletes; avoid unsafe path traversal |
| 7 | Integration milestone | **POC 1: Basic replication** | Reconcile a directory after multiple changes; log errors |
| 8 | std::thread, mutex, condition_variable | Producer-consumer work pipeline | No data races; deterministic shutdown |
| 9 | Bounded queues and backpressure | Controlled concurrent transfers | Queue capacity respected; memory stays bounded |
| 10 | Network outages and reconnection | Reconnect/retry state machine | Resume reconciliation after interruption |
| 11 | Durable checkpoints, idempotent apply | Recovery journal/checkpoint | Restart after crash without corrupting replica; atomic checkpoint writes |
| 12 | Heartbeats and HA fundamentals | Simulated HA controller | Detect missed heartbeats; **do not auto-promote** without fencing/quorum |
| 13 | Debugging and fault injection | Tests + metrics | Test disk full, process crash, network cut, duplicate messages |
| 14 | Cross-platform validation and documentation | **POC 2: Mini-RHA v1** | Build on Linux and Windows; write design, limits, test report |

## Proposed project layout

```text
mini-rha/
  CMakeLists.txt
  include/
    platform/
    protocol/
    replication/
  src/
    common/
    linux/
    windows/
    master/
    replica/
    ha_simulator/
  tests/
  docs/
    architecture.md
    failure-matrix.md
    results.md
```

## Design constraints

- Use C++11/14 only; avoid `std::filesystem` (C++17). Wrap OS-specific file enumeration and socket APIs behind narrow interfaces.
- Start with periodic scans rather than assuming filesystem notifications are a durable, complete change journal.
- Use a length-prefixed network protocol with message type, transfer ID, sequence/version and payload length. Validate lengths and paths.
- Stage incoming files in temporary files, flush as appropriate, verify integrity, then atomically rename when supported by the target filesystem.
- Define delete behavior carefully: never allow the replica to delete arbitrary paths outside its configured root.
- Treat retries as at-least-once delivery; design replica operations to be idempotent.
- A two-node heartbeat alone cannot safely determine whether a peer has failed or is partitioned. Use only simulated/manual failover unless fencing/quorum is implemented.

## Core experiments

1. Copy 1,000 small files and one large file; verify checksums.
2. Modify and delete files during a transfer; confirm a subsequent reconciliation converges.
3. Drop the TCP connection halfway through a transfer; reconnect and finish safely.
4. Kill the replica during a staged write; restart and check for corruption.
5. Limit queue capacity and network bandwidth; measure backlog and memory.
6. Simulate master isolation; verify the HA controller does not promote an unsafe second writer.

## Key metrics

- Initial sync duration and effective throughput
- Bytes sent and number of retries
- Backlog size and queue high-water mark
- Recovery time after reconnect
- File verification failures and consistency mismatches
- Memory footprint and CPU utilization

## First-week questions for the actual RHA team

- Which subsystem owns the new feature: engine, transport, storage, control service or failover?
- Which Windows and Linux versions are supported?
- How are changes detected, ordered, persisted and replayed?
- What are the process/thread boundaries and ownership rules?
- Which existing integration/failure tests must remain green?
- What compatibility requirements apply to mixed product versions?

## Definition of done

A Linux/Windows C++11/14 prototype that performs initial sync and periodic reconciliation, handles reconnects and restarts without corrupting replicated files, exposes useful logs/metrics, includes automated fault tests, and documents its limitations. It is not a production HA solution.
