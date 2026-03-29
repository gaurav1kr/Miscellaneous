# Stability-Monitor Daemon in TV Systems

The `stability-monitor` daemon continuously runs in TV systems to monitor **CPU, Memory, and Flash usage** of all processes and ensure system stability.

---

## 🔷 Unified Architecture (All 3 Threads)

```mermaid
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

---

## 🔷 Core Design

- Multi-threaded daemon
- Single **shared doubly linked list**
- CPU = historical monitoring
- Memory = real-time monitoring
- Flash = system-wide analysis + KPI integration

---

## 🔷 Doubly Linked List

### Node Contains
- PID
- CPU stats (history for 1min & 3min)
- Memory stats
- prev / next pointers

### Benefits
- O(1) deletion
- Efficient traversal
- Dynamic updates

---

## 🔷 CPUMonitor

### Rules
- >=95% for 1 min
- >=90% for 3 min

### Action
- Kill process
- Core dump
- Remove node

---

## 🔷 MemMonitor

### Limits
- Daemon → 40 MB
- Default → 110 MB
- WebApp → 600 MB

### Action
- Kill process
- Raise alarm

---

## 🔷 FlashMonitor

### Flow
- Collect usage
- Sort descending
- Identify top 5

### KPI Integration
- Send top 5 to Samsung KPI server
- Helps debug TV stuck issues

### Threshold Case
- If exceeded:
  - Mark top 5 RED
  - Trigger power-off
  - Notify owners

---

## 🔷 Thread Synchronization

- Shared linked list across threads
- Requires:
  - Mutex locks
  - Safe insert/delete

---

## 🔷 Key Highlights

- Single source of truth
- Fast deletion (linked list)
- Real-time + historical monitoring
- Strong observability via KPI
