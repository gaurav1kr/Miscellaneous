
# Stability-Monitor Daemon in TV Systems

The `stability-monitor` daemon runs consistently in TV systems, monitoring memory usage, CPU usage, and flash usage. It includes three distinct threads:

- `MemoryMonitor`
- `FlashMonitor`
- `CPUMonitor`

## Threads Overview

### 1. CPUMonitor

`CPUMonitor` checks the CPU usage of all processes running within the TV system. The TV has 4 CPU cores: core1, core2, core3, and core4. Each core can consume a maximum of 100% CPU. If any process consumes 95% or more of the overall CPU usage (400% total) for 1 minute, a memory alarm is generated, and the process is gracefully terminated with signal 6. A coredump is also created so the process owner can investigate what exactly the process was doing by analyzing the backtrace. Similarly, if a process consumes 90% of the total CPU for 3 minutes, a memory alarm is also triggered.

**Process Details**:  
`CPUMonitor` reads the `/proc` filesystem using a driver and creates a text file that contains process entries and their CPU usage for the last 3 minutes.

**CPU Usage Calculation**:

#### Preparation
To calculate CPU usage for a specific process, you'll need the following information:
- `/proc/uptime`: The system's uptime in seconds.
- `/proc/[PID]/stat`:  
    - `#14 utime`: CPU time spent in user code (clock ticks).
    - `#15 stime`: CPU time spent in kernel code (clock ticks).
    - `#16 cutime`: CPU time spent in user code by the process's children (clock ticks).
    - `#17 cstime`: CPU time spent in kernel code by the process's children (clock ticks).
    - `#22 starttime`: Time when the process started (clock ticks).
- The system's Hertz value, which can be retrieved using `getconf CLK_TCK` or `sysconf(_SC_CLK_TCK)`.

#### Calculation
First, calculate the total time spent by the process:
```
total_time = utime + stime
```
Optionally, add the time from children processes:
```
total_time = total_time + cutime + cstime
```
Next, calculate the total elapsed time since the process started:
```
seconds = uptime - (starttime / Hertz)
```
Finally, calculate the CPU usage percentage:
```
cpu_usage = 100 * ((total_time / Hertz) / seconds)
```

### 2. MemMonitor

`MemMonitor` tracks RAM usage for processes and generates memory alarms. Processes are categorized into three types:

- **Daemon**: Processes with a parent ID of 1 are classified as daemons. They are allowed a maximum of 40 MB of RAM (e.g., monitoring and backend processes).
- **DefaultApp**: Any app that is not a daemon falls under this category and has a memory limit of 110 MB (e.g., menu, channel apps).
- **WebApp**: Web applications (e.g., **WebRuntime**, which runs web apps like Netflix, browsers, Prime Video) have a memory limit of 600 MB.

If any process exceeds its memory allocation, it is terminated, and a memory alarm is triggered.

`MemMonitor` effectively uses `/proc/stat` to monitor RAM usage.

### 3. FlashMonitoring

`FlashMonitoring` computes the flash usage of processes, focusing on the `/opt` partition. If the flash storage becomes full, it may disrupt TV operations. Flash usage is calculated, and a threshold is set. If a certain percentage of flash is used, the top 5 flash-consuming processes are identified, and a flash alarm is triggered. The TV is then rebooted, and the alarm is sent to the process owners.

The top 5 flash-consuming processes are stored in a SQLite database, which is regularly updated.

## Thread Synchronization and Logging

All three threads run concurrently, using extensive thread synchronization. Logs are stored in a shared logging system.

