# Diagnose False Sharing in a Multithreaded Workload (C++11/Linux)

## 60-second interview answer
False sharing occurs when independent variables modified by different threads occupy the same CPU cache line. Coherence operates at cache-line granularity, so writes by one core invalidate another core's copy, creating cache-line bouncing and poor scaling even when there is no data race. I would benchmark single-thread versus multithread throughput, inspect memory layout, use `perf c2c` on supported hardware to locate contended cache lines, pad or align per-thread hot counters, and benchmark again under identical conditions.

## Simple layout

```text
BEFORE (illustrative 64-byte cache line)
+-----------------------------------------------------------+
| atomic counter A | atomic counter B | remaining bytes ... |
+-----------------------------------------------------------+
     Thread 1 writes     Thread 2 writes
     -> cache-line ownership bounces between cores

AFTER
+------------------ 64-byte cache line --------------------+
| aligned counter A + padding                              |
+-----------------------------------------------------------+
+------------------ 64-byte cache line --------------------+
| aligned counter B + padding                              |
+-----------------------------------------------------------+
```

## Complete C++11 example

```cpp
#include <atomic>
#include <chrono>
#include <iostream>
#include <thread>

struct BadCounters {
    std::atomic<long> a{0};
    std::atomic<long> b{0};
};

struct alignas(64) PaddedCounter {
    std::atomic<long> value{0};
};

struct GoodCounters {
    PaddedCounter a;
    PaddedCounter b;
};

const long N = 10000000;

template <typename Counter>
void run(const char* name, Counter& a, Counter& b) {
    auto start = std::chrono::steady_clock::now();
    std::thread t1([&] {
        for (long i = 0; i < N; ++i)
            a.fetch_add(1, std::memory_order_relaxed);
    });
    std::thread t2([&] {
        for (long i = 0; i < N; ++i)
            b.fetch_add(1, std::memory_order_relaxed);
    });
    t1.join();
    t2.join();
    auto end = std::chrono::steady_clock::now();
    std::cout << name << ": "
              << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count()
              << " ms, values=" << a.load() << "," << b.load() << "\n";
}

int main() {
    BadCounters bad;
    GoodCounters good;
    run("Adjacent atomics", bad.a, bad.b);
    run("Padded atomics", good.a.value, good.b.value);
    std::cout << "sizeof(BadCounters)=" << sizeof(BadCounters)
              << ", sizeof(GoodCounters)=" << sizeof(GoodCounters) << "\n";
}
```

Compile and run:

```bash
g++ -std=c++11 -O2 -pthread -Wall -Wextra false_sharing.cpp -o false_sharing
./false_sharing
```

Results depend on core placement, CPU architecture, scheduling, and system load. Repeat runs; do not assume padding always improves performance.

## Diagnose on Linux

```bash
perf stat -e cycles,instructions,cache-misses ./false_sharing
perf c2c record -- ./false_sharing
perf c2c report
```

`perf c2c` and HITM reporting depend on CPU and kernel support. Generic cache misses alone do not prove false sharing. Inspect field offsets with `offsetof`, use a representative workload, and verify whether the hot variables share a cache line.

## Why relaxed atomics?

Each thread updates a separate counter. `memory_order_relaxed` avoids stronger ordering constraints that are not needed for this counting benchmark, while preserving atomicity. False sharing can still occur because hardware cache coherence remains necessary.

## Interview questions

1. **Is false sharing a data race?** No. Separate atomics can still share a cache line.
2. **Why does it hurt?** Cache-line invalidations and ownership transfers between cores.
3. **How do you identify it?** Scaling tests, address/layout inspection, and `perf c2c` where supported.
4. **How do you fix it?** Align/pad per-thread hot state or aggregate locally and merge later.
5. **Does padding always help?** No; larger working sets can increase cache pressure.
6. **What is true sharing?** Threads access the same memory location, not just the same cache line.

## Whiteboard recall

**Independent writes + same cache line → coherence bouncing → poor scaling.**

**Measure → inspect layout → pad or use thread-local accumulation → remeasure.**
