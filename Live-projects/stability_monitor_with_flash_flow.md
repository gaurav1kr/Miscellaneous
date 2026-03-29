# Stability-Monitor Daemon in TV Systems

The `stability-monitor` daemon continuously runs in TV systems to monitor CPU, Memory, and Flash usage.

---

## 🔷 Overall Architecture (Updated with Flash Flow)

```mermaid
flowchart TD
    A[Start daemon] --> B[Init Threads]

    B --> T1[MemoryMonitor]
    B --> T2[FlashMonitor]
    B --> T3[CPUMonitor]

    %% Shared data
    T3 --> L1[Read proc]
    T1 --> L1
    T2 --> L1

    L1 --> L2[Update Doubly Linked List]

    %% CPU Flow
    T3 --> C1[Traverse List]
    C1 --> C2[Compute CPU 1min 3min]
    C2 --> C3{CPU Breach}

    C3 -->|Yes| C4[Kill Process]
    C4 --> C5[Core Dump]
    C5 --> C6[Remove Node]

    %% Memory Flow
    T1 --> M1[Traverse List]
    M1 --> M2[Check Memory]
    M2 --> M3{Mem Breach}
    M3 -->|Yes| M4[Kill + Alarm]

    %% Flash Flow
    T2 --> F1[Collect Flash Usage]
    F1 --> F2[Sort Descending]
    F2 --> F3[Top 5 Processes]

    F3 --> F4[Send to KPI Server]

    F3 --> F5{Flash Threshold Breach}
    F5 -->|Yes| F6[Mark Top 5 RED]
    F6 --> F7[Trigger Power Off]
    F7 --> F8[Notify Owners]

    %% Loop
    C6 --> L1
    M4 --> L1
    F4 --> L1
```

---

## 🔷 Flash Monitoring Explanation

- Collects flash usage of all processes
- Sorts them in descending order
- Top 5 processes sent to KPI server
- Helps debug customer issues (TV stuck)

### Threshold Case
- If flash exceeds limit:
  - Top 5 marked RED in KPI
  - Power-off triggered
  - Owners notified

---

(Rest of content remains same)
