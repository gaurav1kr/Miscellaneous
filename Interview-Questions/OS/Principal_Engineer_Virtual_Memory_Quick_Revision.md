# Principal Engineer --- Virtual Memory Quick Revision

> **How to use this:** For each question, memorize only the **Remember**
> line.\
> In the interview, start with **Say this** and expand using the
> diagram/example only if asked.

------------------------------------------------------------------------

## 1. Explain virtual memory from CPU instruction to DRAM access

**Say this:** A CPU load/store generates a **virtual address**. The MMU
checks the **TLB**; on a hit it gets the physical address immediately.
On a miss it walks the page table. After translation, the CPU checks
caches, and only a cache miss may finally reach DRAM.

``` text
CPU instruction
      |
      v
Virtual Address
      |
      v
    TLB lookup
    /       \
  Hit       Miss
   |          |
   |      Page-table walk
   |          |
   +----------+
        |
        v
Physical Address
        |
   L1 -> L2 -> L3
        |
      DRAM
```

**Remember:** **VA → TLB → Page Table if needed → PA → Cache → DRAM.**

------------------------------------------------------------------------

## 2. Why do we need virtual memory?

**Say this:** Virtual memory provides **process isolation, protection,
flexible address spaces, demand paging, shared memory, mmap, and
Copy-on-Write**.

``` text
Process A VA ----> Physical Page A
Process B VA ----> Physical Page B

Same-looking virtual addresses
can map to different RAM.
```

**Example:** Process A cannot normally read Process B's heap just by
knowing its virtual address.

**Remember:** **Isolation + protection + flexible mapping.**

------------------------------------------------------------------------

## 3. What is stored in a Page Table Entry (PTE)?

**Say this:** A PTE contains the **physical page-frame number** plus
permission and status bits.

``` text
PTE
+-----------------------------------+
| PFN | Present | R/W | User | NX   |
|     | Accessed | Dirty | ...      |
+-----------------------------------+
```

**Remember:** **PTE = physical frame + permissions + status.**

------------------------------------------------------------------------

## 4. What happens during a TLB miss?

**Say this:** A TLB miss means the translation is not cached. The CPU
performs a **page-table walk**. If the PTE is valid, it caches the
translation in the TLB and continues.

``` text
VA -> TLB MISS
        |
        v
   Page Table
        |
   valid PTE?
     /    \
   Yes     No
    |       |
 TLB fill  Page Fault
```

**Remember:** **TLB miss does NOT automatically mean page fault.**

------------------------------------------------------------------------

## 5. TLB miss vs Page Fault

**Say this:** A **TLB miss** means "translation isn't cached." A **page
fault** means the access needs kernel handling because the page is
absent or permissions require intervention.

``` text
TLB miss
   |
Page-table walk
   |
Present?
 /     \
Yes     No
 |       |
Continue Page Fault -> Kernel
```

**Remember:** **TLB miss = translation lookup. Page fault = OS help.**

------------------------------------------------------------------------

## 6. Explain a page fault end-to-end

**Say this:** The CPU detects that the access cannot proceed and traps
into the kernel. The kernel validates the address, obtains or creates
the page, updates the PTE, and retries the instruction. Invalid access
can become `SIGSEGV`.

``` text
CPU accesses VA
      |
   Page Fault
      |
      v
   Kernel
      |
Valid mapping?
 /          \
No          Yes
|            |
SIGSEGV   Get page
             |
          Update PTE
             |
        Retry instruction
```

**Remember:** **Fault → kernel → validate → map page → retry.**

------------------------------------------------------------------------

## 7. Minor vs Major Page Fault

**Say this:** A **minor fault** needs kernel handling but no required
page read from storage. A **major fault** requires storage I/O to bring
the needed page in.

``` text
Page Fault
   |
   +-- Page already available / demand-zero -> Minor
   |
   +-- Need disk/swap read ----------------> Major
```

**Remember:** **Minor = no required disk read. Major = disk/storage
I/O.**

------------------------------------------------------------------------

## 8. What causes segmentation faults?

**Say this:** `SIGSEGV` occurs when a process accesses an **invalid
virtual address or violates page permissions**.

``` cpp
int* p = nullptr;
*p = 10;          // invalid access -> SIGSEGV
```

Other examples: dangling pointer, stack overflow, writing read-only
memory.

**Remember:** **Invalid mapping or invalid permission → SIGSEGV.**

------------------------------------------------------------------------

# Allocation and Demand Paging

## 9. Why can `malloc(1 GB)` succeed without consuming 1 GB RAM?

**Say this:** `malloc()` can reserve **virtual address space** without
immediately allocating all physical pages. RAM is typically committed as
pages are touched.

``` text
malloc(1 GB)

Virtual:
[================ 1 GB ================]

Physical RAM:
[ little/no private RAM yet ]

Write pages
    |
Page faults
    |
Physical pages allocated
```

**Remember:** **malloc reserves; touching pages consumes physical
memory.**

------------------------------------------------------------------------

## 10. What happens on first access to newly allocated memory?

**Say this:** The first access to an untouched anonymous page commonly
causes a **minor page fault**. The kernel supplies a zero-filled
physical page and maps it.

``` text
p = malloc(...)
      |
p[0] = 1
      |
Minor fault
      |
Allocate zeroed page
      |
Update PTE
```

**Remember:** **First touch creates the physical backing.**

------------------------------------------------------------------------

## 11. Explain demand paging

**Say this:** Pages are brought into physical memory **only when
accessed**, rather than eagerly allocating/loading the whole mapping.

``` text
Mapped:
[A][B][C][D]

Program touches C
       |
       v
Only C becomes resident
```

**Remember:** **Allocate/load on demand, not upfront.**

------------------------------------------------------------------------

# fork() and Copy-on-Write

## 12. Explain `fork()` using Copy-on-Write

**Say this:** After `fork()`, parent and child initially share physical
pages. Writable private pages are protected so that a write triggers a
**COW fault**, creating a private copy.

``` text
Before write:

Parent VA ---+
             +---> Physical Page A
Child VA ----+

Child writes
      |
   COW fault
      |
      +--> Parent -> Page A
      |
      +--> Child  -> Page B (copy)
```

**Remember:** **fork shares first; copies only on write.**

------------------------------------------------------------------------

## 13. Why is `fork()` relatively cheap initially?

**Say this:** Because the OS does not copy the complete process memory
immediately. It mostly creates child metadata/page tables while physical
pages remain shared via COW.

``` text
Without COW: Copy 10 GB now
With COW:    Share 10 GB now, copy changed pages later
```

**Remember:** **Pay for pages only when they are modified.**

------------------------------------------------------------------------

## 14. What if parent and child modify the same COW page simultaneously?

**Say this:** Both writes can trigger COW handling. Kernel
synchronization makes the operation race-safe, and each process
ultimately gets its **own private physical page**.

``` text
Shared Page A
   /       \
Parent     Child
write      write
 |          |
COW        COW
 |          |
Page B     Page C
```

**Remember:** **After COW writes, each process owns its private copy.**

------------------------------------------------------------------------

# Shared Memory and mmap

## 15. How does shared memory work across processes?

**Say this:** The kernel maps the **same physical frames** into multiple
process address spaces.

``` text
Process A              Process B
VA 0x1000              VA 0x9000
    |                       |
    +--------+   +----------+
             v   v
        Physical Page
        [ shared data ]
```

Synchronization is still required.

**Remember:** **Shared memory = multiple PTEs → same physical page.**

------------------------------------------------------------------------

## 16. Can two processes have the same virtual address?

**Say this:** Yes. Virtual addresses are meaningful only inside a
process's address space.

``` text
Process A: 0x1000 -> Physical X
Process B: 0x1000 -> Physical Y
```

**Remember:** **Same VA does not imply same physical memory.**

------------------------------------------------------------------------

## 17. Can two virtual addresses point to the same physical address?

**Say this:** Yes. Shared memory, shared libraries, file mappings, and
COW can create this situation.

``` text
VA 0x1000 ---+
             +---> Physical Page X
VA 0x9000 ---+
```

**Remember:** **Different VA → same PA is perfectly valid.**

------------------------------------------------------------------------

## 18. How does `mmap()` work?

**Say this:** `mmap()` creates a virtual-memory mapping backed by a
**file or anonymous memory**. Pages are normally populated lazily when
accessed.

``` text
mmap(file)
   |
Virtual range
   |
first access -> fault
   |
Page Cache / Physical Page
```

**Remember:** **mmap creates mappings; faults populate pages.**

------------------------------------------------------------------------

## 19. `mmap()` vs `malloc()`

**Say this:** `malloc()` is a **user-space allocator API**. `mmap()` is
an OS primitive for creating virtual-memory mappings. Allocators may
internally use `mmap()`.

``` text
Application
    |
 malloc()
    |
Allocator
  /    \
brk   mmap
```

**Remember:** **malloc = allocator; mmap = mapping primitive.**

------------------------------------------------------------------------

# Page Cache

## 20. What is the page cache?

**Say this:** The page cache is RAM used by the kernel to cache **file
contents**, avoiding repeated storage I/O.

``` text
Application read()
       |
   Page Cache
    /      \
 HIT       MISS
 |          |
RAM       Disk
```

**Remember:** **Page cache = files cached in RAM.**

------------------------------------------------------------------------

## 21. How do memory-mapped files interact with page cache?

**Say this:** File-backed `mmap()` normally maps pages from the **page
cache**. `MAP_SHARED` writes dirty the shared cached page; `MAP_PRIVATE`
writes use COW.

``` text
File on disk
     |
 Page Cache
     |
 mmap PTE
     |
 Process VA
```

**Remember:** **File mmap normally uses page-cache pages.**

------------------------------------------------------------------------

# Page Tables and Memory Metrics

## 22. Why are page tables multi-level?

**Say this:** A single flat page table would waste huge amounts of
memory for sparse address spaces. Multi-level tables allocate lower
levels only where mappings exist.

``` text
PGD
 |
 +--> PUD
       |
       +--> PMD
             |
             +--> PTE -> Page
```

**Remember:** **Multi-level paging saves page-table memory for sparse VA
spaces.**

------------------------------------------------------------------------

## 23. RSS vs VSZ

**Say this:** **VSZ** is total mapped virtual address space. **RSS** is
the resident portion currently backed by physical RAM.

``` text
VSZ:
[==========================]

RSS:
[=======]
```

**Remember:** **VSZ = mapped. RSS = resident.**

------------------------------------------------------------------------

# Memory Pressure

## 24. What happens under memory pressure?

**Say this:** Linux tries to reclaim memory: discard clean file cache,
write back dirty pages, reclaim anonymous memory through swap if
available, and shrink caches. Severe pressure can eventually lead to
OOM.

``` text
Low free memory
      |
   Reclaim
  /   |    \
cache swap writeback
      |
Still insufficient?
      |
     OOM
```

**Remember:** **Reclaim first; OOM is the last resort.**

------------------------------------------------------------------------

## 25. What is swapping?

**Say this:** Swapping moves anonymous pages from RAM to swap storage so
RAM can be reused.

``` text
RAM page
   |
swap out
   v
SSD / Swap

Later access
   |
Page fault
   |
swap in
```

**Remember:** **Swap trades RAM pressure for storage latency.**

------------------------------------------------------------------------

## 26. What is thrashing?

**Say this:** Thrashing happens when the working set does not fit in RAM
and the system spends most of its time continuously evicting and
faulting pages.

``` text
Need A -> load A
Need B -> evict A
Need A -> load A
Need B -> evict A
...
```

**Remember:** **More paging than useful work = thrashing.**

------------------------------------------------------------------------

## 27. How does OS choose pages to reclaim?

**Say this:** Linux approximates which pages are **hot and cold** using
access history and reclaim algorithms rather than implementing a perfect
LRU.

``` text
HOT pages  -> keep
WARM pages -> monitor
COLD pages -> reclaim candidates
```

Modern Linux may use Multi-Gen LRU when enabled.

**Remember:** **Prefer reclaiming cold pages; preserve the working
set.**

------------------------------------------------------------------------

## 28. What are dirty and accessed bits?

**Say this:** The **accessed bit** tells the OS a page has been
referenced. The **dirty bit** tells it the page has been modified.

``` text
Read page  -> Accessed = 1
Write page -> Accessed = 1, Dirty = 1
```

**Remember:** **Accessed = used. Dirty = modified.**

------------------------------------------------------------------------

# TLB Coherency and Multicore

## 29. What happens when a page-table entry changes?

**Say this:** The kernel updates the PTE, but CPUs may still have the
old translation cached in their TLBs. Those stale entries must be
invalidated.

``` text
PTE changed
    |
Old TLB entry still exists
    |
Invalidate TLB
```

**Remember:** **Changing PTE != automatically removing stale TLB
translations.**

------------------------------------------------------------------------

## 30. What is a TLB shootdown?

**Say this:** When another CPU may have cached a changed translation,
the kernel asks that CPU to invalidate the stale TLB entry.

``` text
CPU 0 changes PTE
       |
       | IPI
       v
CPU 1 ----> invalidate TLB
CPU 2 ----> invalidate TLB
CPU 3 ----> invalidate TLB
```

**Remember:** **TLB shootdown = cross-core translation invalidation.**

------------------------------------------------------------------------

## 31. Why can TLB shootdowns hurt multicore scalability?

**Say this:** They require cross-core interrupts and synchronization.
Frequent mapping changes can therefore interrupt many cores and create
global overhead.

``` text
1 mapping change
      |
      +--> CPU1 interrupt
      +--> CPU2 interrupt
      +--> CPU3 interrupt
      +--> CPU4 interrupt
```

**Remember:** **More cores + frequent mapping changes = expensive
coordination.**

------------------------------------------------------------------------

# Huge Pages

## 32. Why do huge pages improve performance?

**Say this:** A huge page lets one TLB entry cover much more memory,
increasing **TLB reach** and reducing page-table walks.

``` text
4 KB:
[ ][ ][ ][ ][ ][ ][ ]...
many translations

2 MB:
[====================]
one translation covers much more
```

**Remember:** **Huge page = greater TLB coverage.**

------------------------------------------------------------------------

## 33. Disadvantages of huge pages

**Say this:** Huge pages can waste memory through internal fragmentation
and make allocation, compaction, migration and COW more expensive.

``` text
2 MB page allocated

[used][................unused..............]
       ^ wasted memory
```

**Remember:** **Better translation efficiency, worse allocation
granularity.**

------------------------------------------------------------------------

## 34. Internal vs External Fragmentation

**Say this:** Internal fragmentation is wasted space **inside allocated
blocks**. External fragmentation is free memory split into pieces that
cannot satisfy a large contiguous request.

``` text
Internal:
[ USED | wasted ]

External:
[free][used][free][used][free]
```

**Remember:** **Internal = waste inside. External = holes outside.**

------------------------------------------------------------------------

# NUMA and Context Switching

## 35. What is NUMA?

**Say this:** In NUMA systems, memory is divided among nodes/sockets.
Local memory is generally faster than accessing RAM attached to another
socket.

``` text
CPU 0 ---- Local RAM 0   FAST
  |
  +------ Remote RAM 1   SLOWER
             |
           CPU 1
```

**Remember:** **Keep threads close to their memory.**

------------------------------------------------------------------------

## 36. Why can a program be slow despite available memory?

**Say this:** Because the bottleneck may be **NUMA remote access, TLB
misses, page faults, reclaim, swap, cgroup limits, allocator contention,
or storage I/O**, not total free RAM.

``` text
"20 GB available"
       !=
"my requests have fast memory access"
```

**Remember:** **Available RAM is only one memory-performance metric.**

------------------------------------------------------------------------

## 37. What happens to page tables during a context switch?

**Say this:** When switching to another process address space, the
kernel changes the CPU's **page-table root**. It does not copy the
entire page table.

``` text
Running A -> Page Table A

Context switch

Running B -> Page Table B
```

**Remember:** **Switch page-table root, not copy page tables.**

------------------------------------------------------------------------

## 38. Does every context switch flush the TLB?

**Say this:** No. Threads in the same address space can reuse
translations, and modern CPUs use **ASIDs/PCIDs** so translations from
multiple processes can remain tagged in the TLB.

**Remember:** **Modern CPUs avoid full TLB flushes whenever possible.**

------------------------------------------------------------------------

## 39. What are ASIDs/PCIDs?

**Say this:** They tag TLB entries with an address-space identifier,
allowing translations belonging to different processes to coexist
safely.

``` text
TLB

ASID 10 | VA X -> PA A
ASID 20 | VA X -> PA B
```

**Remember:** **ASID/PCID = process tag for TLB entries.**

------------------------------------------------------------------------

## 40. How are memory permissions enforced?

**Say this:** Page-table entries contain permissions such as read/write,
user/kernel and executable/non-executable. The MMU checks these
permissions during access.

``` text
PTE: Read=1 Write=0

CPU attempts write
       |
Protection fault
       |
Kernel
       |
SIGSEGV / special handling
```

**Remember:** **OS sets permissions; MMU enforces them.**

------------------------------------------------------------------------

# Principal Engineer --- Production Questions

## 41. How would you diagnose excessive page faults?

**Say this:** First determine whether they are **minor or major**, then
correlate them with application latency and memory pressure.

``` text
High page faults
      |
Minor or Major?
   /       \
Minor      Major
 |           |
COW /      Disk / swap /
first-touch page-cache miss
```

Useful tools:

``` bash
pidstat -r -p <pid> 1
vmstat 1
cat /proc/<pid>/smaps_rollup
cat /proc/pressure/memory
cat /proc/vmstat
perf stat -p <pid> -e page-faults,minor-faults,major-faults
iostat -xz 1
```

**Remember:** **Classify the fault before trying to fix it.**

------------------------------------------------------------------------

## 42. How would you diagnose increasing RSS?

**Say this:** Break RSS down into **anonymous/file-backed,
private/shared, clean/dirty** mappings before assuming a memory leak.

``` text
RSS growing
   |
   +--> Heap?
   +--> mmap?
   +--> Thread stacks?
   +--> Shared mappings?
   +--> Allocator retained memory?
```

Start with:

``` bash
cat /proc/<pid>/smaps_rollup
pmap -x <pid>
```

**Remember:** **RSS growth is a symptom, not automatically a leak.**

------------------------------------------------------------------------

## 43. Memory leak vs page cache vs allocator fragmentation

**Say this:** Compare three layers: **application live allocations**,
**allocator retained/resident memory**, and **kernel file cache**.

``` text
Application objects
       |
Allocator
       |
Process RSS

Separate from:

Kernel Page Cache
```

-   Live allocations keep growing → likely application leak.
-   Live allocations fall but allocator RSS stays high →
    fragmentation/retention.
-   File-backed/cache memory grows and is reclaimable → page cache.

**Remember:** **Live bytes vs allocator bytes vs page-cache bytes.**

------------------------------------------------------------------------

## 44. Low CPU but extremely high latency under memory pressure

**Say this:** Low CPU suggests threads may be **waiting rather than
computing**. Investigate reclaim, major faults, swap, storage I/O,
dirty-page writeback, cgroup limits, NUMA and memory PSI.

``` text
Low CPU + High latency
          |
          v
       WAITING?
      /   |    \
reclaim  I/O   swap
   |
memory stalls
```

Check:

``` bash
vmstat 1
cat /proc/pressure/memory
iostat -xz 1
pidstat -r -p <pid> 1
```

**Remember:** **Low CPU + high latency → look for waiting/stalls.**

------------------------------------------------------------------------

## 45. 100-GB database slows after switching huge pages → 4-KB pages

**Say this:** The same working set now needs vastly more page
translations, reducing TLB reach and causing more TLB misses and
page-table walks.

``` text
100 GB with 2 MB pages
≈ 51,200 pages

100 GB with 4 KB pages
≈ 26,214,400 pages
```

One 2-MB page covers **512×** as much memory as one 4-KB page.

``` text
Huge pages
    |
larger TLB reach
    |
fewer page walks
    |
better large-working-set performance
```

Validate using hardware counters for TLB misses/page walks, plus NUMA
and database latency metrics.

**Remember:** **Large DB + small pages → TLB pressure can explode.**

------------------------------------------------------------------------

# Final Mental Model --- Memorize This Page

``` text
                 VIRTUAL MEMORY
                       |
        +--------------+--------------+
        |                             |
    Translation                    Protection
        |                             |
   VA -> TLB                     R / W / X
        |                             |
      Miss                         violation
        |                             |
  Page-table walk                 Page Fault
        |
   Present?
    /    \
  Yes     No
   |       |
  PA    Page Fault
           |
         Kernel
```

### Five lines to remember

1.  **TLB miss = translation isn't cached. Page fault = kernel help is
    required.**
2.  **malloc reserves virtual memory; first touch usually creates
    physical backing.**
3.  **fork shares pages first and copies them only on write.**
4.  **Shared memory means different virtual mappings can point to the
    same physical pages.**
5.  **Under memory pressure, diagnose reclaim, faults, swap, I/O, NUMA
    and TLB behavior---not just "free RAM."**

------------------------------------------------------------------------

# 30-Second Principal Engineer Answer

If the interviewer says **"Explain virtual memory"**, you can say:

> Virtual memory gives each process an isolated virtual address space.
> When the CPU accesses memory, the MMU first looks in the TLB for the
> virtual-to-physical translation. On a TLB miss, it walks the process
> page tables. If a valid mapping exists, execution continues; otherwise
> the CPU raises a page fault and the kernel may allocate a page, load
> it from storage, perform Copy-on-Write, or reject the access. This
> abstraction enables isolation, demand paging, mmap, shared memory and
> COW. At scale, I would also care about TLB reach, huge pages, NUMA
> placement, page reclaim and TLB shootdowns because those can directly
> affect production latency.
