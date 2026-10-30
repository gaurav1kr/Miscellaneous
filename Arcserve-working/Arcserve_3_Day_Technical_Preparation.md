# Arcserve — 3-Day Technical Preparation Plan

**Goal:** Prepare for strong technical ownership in enterprise backup, storage, networking, and recovery systems, beyond C++.

**Time budget:** ~6 focused hours per day (18 hours total).

**Context:** Build on existing experience in Linux/Windows, C++11/14, multithreading, distributed systems, Kubernetes, Azure, and production debugging. Focus on backup-domain concepts and storage internals rather than re-learning familiar fundamentals.

> **Note:** This is a domain-oriented preparation plan, not a claim about Arcserve's internal source code or your eventual team assignment. Confirm the component your team owns with your manager.

## 1. Mental model: enterprise backup pipeline

```text
Windows / Linux / VMware / Hyper-V / Cloud workloads
                         |
            Snapshot / consistency layer
                         |
            Backup agent / data mover
                         |
       Changed-block detection and chunking
                         |
         Hashing / compression / encryption
                         |
          Network transfer and retries
                         |
             Recovery Point Server
                         |
          Data store + metadata / index
                         |
       Local / remote / cloud backup targets
                         |
       Restore / verification / replication
```

Key terms to recognize: **Arcserve Unified Data Protection (UDP)**, **Recovery Point Server (RPS)**, backup plans, recovery points, data stores, replication, and deduplication.

## 2. Priorities

| Topic | Priority | Objective |
|---|---|---|
| Backup algorithms | P0 | Understand full/incremental/differential/synthetic backup |
| Storage I/O and file systems | P0 | Reason about block-level reads, metadata, consistency, and bottlenecks |
| Deduplication and block hashing | P0 | Understand chunk identity, indexing, collisions, and lifecycle |
| TCP networking and sockets | P0 | Refresh efficient, reliable data transfer |
| Windows VSS and Linux snapshots | P0 | Understand live-workload consistency |
| Multithreading and synchronization | P1 | Apply existing skills to backup pipelines |
| Replication and failure recovery | P1 | Design for partial failure and safe resume |
| VMware and Hyper-V | P1 | Learn virtualization backup basics |
| S3 object storage and immutability | P1 | Understand remote targets and ransomware resilience |
| Kubernetes and Azure | P2 | Refresh only as needed for team responsibilities |

## 3. Day 1 — Storage internals and backup fundamentals (6 hours)

### Block A: File systems and storage I/O (2 hours)

- [ ] Block storage vs file storage vs object storage
- [ ] File-level vs image-based vs volume-level backup
- [ ] ext4, XFS, NTFS: metadata, inodes/MFT, allocation, sparse files
- [ ] Buffered I/O vs direct I/O; `pread`, `pwrite`, `fsync`, `mmap`
- [ ] Sequential vs random I/O, throughput, IOPS, latency
- [ ] RAID, SAN, NAS, SMB, NFS, and iSCSI: what problem each solves

**Explain aloud:** What happens from `read()` to disk access? How do you distinguish disk throughput limits from filesystem overhead?

### Block B: Backup algorithms and consistency (2 hours)

- [ ] Full, incremental, differential, synthetic full, forever-incremental
- [ ] Recovery point, retention, backup chain, restore chain
- [ ] Change block tracking (CBT) concepts
- [ ] Windows Volume Shadow Copy Service (VSS)
- [ ] Linux LVM snapshots and filesystem freeze concepts
- [ ] Crash-consistent vs application-consistent backups
- [ ] RPO vs RTO; why restore testing matters

**Explain aloud:** How do you back up a 1 TB volume while applications keep writing? What consistency guarantees are required for a database?

### Block C: Arcserve product model and deduplication (2 hours)

- [ ] Understand Arcserve UDP's high-level architecture
- [ ] Understand the role of a Recovery Point Server (RPS)
- [ ] Understand backup destinations, data stores, recovery points, and replication
- [ ] Fixed-size vs content-defined chunking (conceptual comparison)
- [ ] SHA-256 and content-addressed chunks; hashes are identifiers, not proof against every collision
- [ ] Hash indexes, reference tracking, garbage collection, compression
- [ ] Source-side vs target-side deduplication and tradeoffs

**Explain aloud:** If 100 machines share similar OS files, how can a backup system avoid storing identical chunks 100 times? How would it avoid deleting shared data prematurely?

**Day 1 deliverable:** Draw the end-to-end backup flow and explain full → incremental → restore without notes.

## 4. Day 2 — Networking and distributed reliability (6 hours)

### Block A: Networking and data transfer (2 hours)

- [ ] TCP handshake, retransmissions, sliding windows, flow vs congestion control
- [ ] RTT, bandwidth-delay product, packet loss, throughput
- [ ] Blocking vs nonblocking sockets, `epoll` (Linux), IOCP (Windows)
- [ ] Connection pooling, chunking, buffering, backpressure
- [ ] SMB, NFS, iSCSI at a high level
- [ ] TLS and authentication for backup traffic

**Explain aloud:** Why might backup throughput remain low even with a high-bandwidth network link?

### Block B: Replication, resumability, and correctness (2 hours)

- [ ] Idempotent writes and retries
- [ ] Chunk IDs, offsets, manifests, acknowledgments
- [ ] Resume after connection loss without duplicate or corrupt data
- [ ] Durable checkpoints and metadata commit ordering
- [ ] Replication lag, consistency, partial failures
- [ ] Checksum validation and restore verification
- [ ] Concurrency races during deduplication and deletion

**Explain aloud:** A 500 GB backup stops at 95%. Design a safe resume protocol. What state is persisted on each side?

### Block C: Practical network debugging (2 hours)

- [ ] Inspect sockets using `ss -tin` and `ss -s`
- [ ] Capture traffic with `tcpdump` on your own test setup
- [ ] Generate traffic with `iperf3` if installed
- [ ] Observe retransmissions, RTT, and bandwidth behavior
- [ ] Simulate a dropped connection in a local sender/receiver prototype

**Day 2 deliverable:** Sketch a chunk-transfer protocol with durable acknowledgment, retry, and resume behavior.

## 5. Day 3 — Performance, recovery, and ownership (6 hours)

### Block A: Performance analysis (2 hours)

- [ ] CPU vs disk vs network vs memory bottlenecks
- [ ] `iostat -xz 1`, `pidstat -dru 1`, `vmstat 1`, `top`
- [ ] `strace -tt -T` for syscall latency; `perf` for CPU hotspots
- [ ] Lock contention, bounded queues, thread pools
- [ ] Batch size, parallelism, buffering, read/write amplification
- [ ] Establish baseline metrics before tuning

**Explain aloud:** A job that previously took 30 minutes now takes 3 hours. What metrics and logs would you collect first?

### Block B: Crash recovery and restore correctness (2 hours)

- [ ] Write-ahead logging / journaling concepts
- [ ] Atomic rename and durable metadata updates
- [ ] Crash between writing chunk data and updating the manifest
- [ ] Orphaned chunks, missing references, garbage collection
- [ ] Corrupt blocks, checksum mismatches, retry strategy
- [ ] RPO, RTO, restore drills, disaster recovery testing
- [ ] Immutability, least privilege, ransomware-resilient backups

**Explain aloud:** What happens if power fails after chunk data is written but before its metadata is committed?

### Block C: Mini-project and review (2 hours)

Build a small **C++14 incremental backup prototype** on synthetic files. This is an educational project, not a production backup tool.

- [ ] Read a large file in fixed-size chunks
- [ ] Calculate SHA-256 per chunk using OpenSSL
- [ ] Store unique chunks under hash-derived identifiers
- [ ] Write a versioned manifest with ordered chunk references
- [ ] Run a second backup after modifying a few blocks
- [ ] Transfer missing chunks to a local TCP receiver
- [ ] Simulate disconnect and resume transfer
- [ ] Restore original bytes and verify whole-file checksum
- [ ] Test corrupted chunks and interrupted metadata writes
- [ ] Record throughput and bottlenecks

**Suggested minimal layout:**

```text
mini-backup/
  src/
    chunker.cpp
    chunk_store.cpp
    manifest.cpp
    sender.cpp
    receiver.cpp
    restore.cpp
  tests/
  README.md
```

**Correctness first:** A hash match alone is not sufficient for a security-sensitive collision policy. For a prototype, document assumptions and verify restored output with a full-file checksum. Use atomic manifest publication and only acknowledge data after it is safely committed.

**Day 3 deliverable:** Demonstrate backup → modify → incremental backup → interrupted transfer → resume → verified restore.

## 6. Technical ownership questions to rehearse

1. How do you take an application-consistent backup while writes continue?
2. What is the difference between full, incremental, differential, and synthetic full backups?
3. How does changed-block tracking improve incremental backup performance?
4. How would you implement deduplication without losing shared chunks?
5. How would you manage hash collisions and index corruption?
6. How do you resume a failed 500 GB transfer safely?
7. How do you identify disk, network, CPU, and lock bottlenecks?
8. How do you ensure backup metadata and data are crash-consistent?
9. How would you validate that a backup is restorable?
10. What metrics, alerts, logs, and tracing would you add to a backup engine?
11. How would you protect backup data against ransomware or accidental deletion?
12. How would you design a concurrency-safe chunk store and retention cleanup?

## 7. Questions for your manager / team

- Which product and component will I own: agent, backup engine, RPS, deduplication, replication, restore, or management services?
- Is the main development platform Windows, Linux, or both?
- Which storage targets and protocols matter most in our component?
- What are the team's most frequent production issues or performance bottlenecks?
- What does success look like in the first 30–60 days?
- Which architecture documents, test environments, and debugging tools should I study first?

## 8. Reference material

### Arcserve official documentation

- [Arcserve UDP documentation bookshelf](https://documentation.arcserve.com/Arcserve-UDP/Available/9.0/ENU/Bookshelf_Files/HTML/SolG/UDPSolnGuide/udp_how_udp_works.htm) — product flow and architecture.
- [Arcserve: How Deduplication Works](https://documentation.arcserve.com/Arcserve-UDP/Available/V6/ENU/Bookshelf_Files/HTML/Solutions%20Guide/udp_dedup_works.htm) — source-side deduplication concepts (older version; verify applicability).
- [Arcserve: Configure Deduplication Data Stores](https://documentation.arcserve.com/Arcserve-UDP/Available/9.0/ENU/Bookshelf_Files/HTML/SolG/UDPSolnGuide/udp_dedup_configure.htm) — data/index/hash storage configuration.

### General engineering references

- [Linux `io_uring` documentation](https://docs.kernel.org/io_uring/index.html) — optional advanced Linux I/O reading.
- [Linux `fsync(2)`](https://man7.org/linux/man-pages/man2/fsync.2.html) — durability semantics.
- [Linux `epoll(7)`](https://man7.org/linux/man-pages/man7/epoll.7.html) — scalable socket readiness.
- [Microsoft VSS overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service) — Windows snapshot fundamentals.
- [AWS S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) — immutability concepts.

## 9. Final preparation checklist

- [ ] I can explain a backup and restore end to end.
- [ ] I understand snapshots and consistency guarantees.
- [ ] I can reason about deduplication indexes and safe cleanup.
- [ ] I can diagnose network vs disk bottlenecks.
- [ ] I can design retry/resume behavior without data loss.
- [ ] I can explain durable metadata and crash recovery.
- [ ] I know what to ask to identify my team's ownership boundaries.

**Recommended emphasis:** Storage architecture, snapshot consistency, deduplication, and restore correctness are the highest-value additions to an already strong C++/systems background.
