# TCP/IP & Socket Programming — Simplified Interview Guide

> **Goal:** Prepare for Senior/Principal C++ systems interviews without memorizing disconnected definitions.
>
> **Best way to study this topic:** Understand one story — **how two applications establish a connection, exchange bytes reliably, detect failures, scale to many clients, and recover over an unreliable network.**

---

# 1. The Big Picture

Suppose you open a browser and connect to a server.

```text
Client Application                              Server Application
       |                                               |
       |              TCP connection                   |
       +-----------------------------------------------+
       |                                               |
     Socket                                          Socket
       |                                               |
      TCP                                             TCP
       |                                               |
       IP  ------------ Network / Internet ---------- IP
```

A **socket** is the programming interface your application uses to communicate through the network stack.

Think of it like a **telephone endpoint**:

- IP address = building address
- Port = extension number
- Socket = telephone endpoint
- TCP connection = established phone call

### Interview question
**Q: What is a socket?**

**Answer:** A socket is an OS-managed communication endpoint used by an application to send and receive data over a network. A TCP connection is identified by source IP/port and destination IP/port.

---

# 2. TCP vs UDP — Know This First

## TCP

TCP provides a **reliable, ordered byte stream**.

```text
Sender                         Receiver

ABCDEF   --------------------> ABCDEF

Lost data?       -> retransmit
Out of order?    -> reorder
Duplicate?       -> handle duplicate
Receiver slow?   -> flow control
Network busy?    -> congestion control
```

Examples: HTTPS, SSH, file transfer, database connections.

## UDP

UDP sends independent datagrams and does not guarantee delivery or ordering.

```text
Sender                         Receiver
Packet 1 --------------------> Packet 1
Packet 2 -------- X            LOST
Packet 3 --------------------> Packet 3
```

Examples: DNS, some streaming/real-time traffic, games, telemetry protocols.

### Real-life analogy

**TCP = registered courier.** You care that the complete package arrives correctly and in order.

**UDP = announcement over a loudspeaker.** Missing one announcement may be preferable to waiting for retransmission.

### Interview question
**Q: When would you choose UDP instead of TCP?**

Use UDP when low latency and message/datagram semantics matter more than built-in reliable ordered delivery, or when the application implements the required reliability itself.

---

# 3. TCP Server and Client Lifecycle

This is the most important socket-programming flow to remember.

## Server

```text
socket()
   |
   v
bind()
   |
   v
listen()
   |
   v
accept()
   |
   v
recv() <----> send()
   |
   v
close()
```

## Client

```text
socket()
   |
   v
connect()
   |
   v
send() <----> recv()
   |
   v
close()
```

## Put both sides together

```text
CLIENT                                      SERVER
                                              |
                                           socket()
                                              |
                                           bind()
                                              |
                                           listen()
                                              |
 socket()                                     |
    |                                         |
 connect() -------- TCP handshake ----------> |
    |                                      accept()
    |                                         |
 send() ----------------------------------> recv()
 recv() <---------------------------------- send()
    |                                         |
 close()                                    close()
```

### What each server API means

| API | Simple meaning |
|---|---|
| `socket()` | Create networking endpoint |
| `bind()` | Assign local IP + port |
| `listen()` | Mark it as a listening TCP socket |
| `accept()` | Obtain a new connected socket for a client |
| `recv()` | Receive bytes |
| `send()` | Send bytes |
| `close()` | Release/close socket |

### Important `accept()` concept

The listening socket remains available for new clients.

```text
                    listening socket
                         fd = 3
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          Client A      Client B      Client C
           fd=4          fd=5          fd=6
```

`accept()` returns a **new connected socket**.

### Real-life analogy

Think of a hotel:

```text
Hotel address     = IP
Reception number  = port
Reception desk    = listening socket
Guest check-in    = accept()
Guest room        = connected socket
```

Reception stays open after assigning a room.

### Interview question
**Q: Why does the server call `bind()` while a normal client usually doesn't?**

The server must be reachable at a known IP/port. The OS can normally choose an ephemeral source port for the client automatically.

---

# 4. TCP Connection Establishment — 3-Way Handshake

Before exchanging application data, TCP establishes connection state.

```text
CLIENT                                      SERVER

   SYN  ------------------------------------>

        <--------------------------- SYN + ACK

   ACK  ------------------------------------>

             CONNECTION ESTABLISHED
```

Think:

```text
Client: Can we communicate? My sequence starts at X.
Server: Yes. I received X. Mine starts at Y.
Client: I received Y too.
```

The handshake establishes bidirectional TCP state and synchronizes initial sequence numbers.

### Real-life analogy

```text
A: "Hello, can you hear me?"
B: "Yes. Can you hear me?"
A: "Yes."

Now conversation starts.
```

### Interview questions

**Q: Why three-way handshake?**

Both endpoints need to establish bidirectional communication state and acknowledge each other's initial sequence information.

**Q: What are SYN and ACK?**

SYN is used during connection establishment to synchronize sequence-number state; ACK acknowledges received TCP sequence space.

---

# 5. TCP Is a BYTE STREAM — Critical Concept

This causes many production bugs.

Suppose sender executes:

```text
send("HELLO")
send("WORLD")
```

Do NOT assume receiver gets:

```text
recv() -> HELLO
recv() -> WORLD
```

It could receive:

```text
recv() -> HEL
recv() -> LOWORLD
```

or

```text
recv() -> HELLOWORLD
```

TCP preserves **byte ordering**, not your application's message boundaries.

## How applications solve this: framing

One common protocol:

```text
+----------+--------------------+
| LENGTH   | PAYLOAD            |
+----------+--------------------+
|    5     | HELLO              |
+----------+--------------------+
```

Receiver:

```text
Read fixed-size length
        |
        v
Length = 5
        |
        v
Keep reading until 5 payload bytes received
```

### Real-life analogy

TCP is like a **continuous water pipe**, not a courier delivering separate boxes. Your application must define where one logical message ends and the next begins.

### Interview question
**Q: Does one `send()` correspond to one `recv()`?**

**No.** TCP is a byte stream and does not preserve application message boundaries.

---

# 6. Partial `send()` and `recv()`

Suppose you want to send 10,000 bytes.

```text
Application asks:

send(fd, buffer, 10000)

OS may return:

4000
```

That means only 4,000 bytes were accepted by that call.

You must continue with the remaining bytes.

```text
Total = 10,000

send() -> 4,000
remaining = 6,000

send() -> 3,000
remaining = 3,000

send() -> 3,000
remaining = 0

DONE
```

Conceptual loop:

```cpp
size_t offset = 0;

while (offset < length) {
    ssize_t n = send(fd, buffer + offset, length - offset, 0);

    if (n > 0)
        offset += static_cast<size_t>(n);
    else {
        // Handle EINTR, EAGAIN/EWOULDBLOCK, or fatal error appropriately.
    }
}
```

The same idea applies when receiving a protocol message of a known size: keep accumulating until the required bytes are available.

### Interview question
**Q: Why is calling `send()` once unsafe?**

Because socket APIs may complete only part of the requested operation. Production code tracks the offset and continues until the required bytes are processed or an error/closure occurs.

---

# 7. What Does `recv()` Returning 0 Mean?

```text
recv() > 0    -> bytes received
recv() == 0   -> peer has performed orderly shutdown of its sending side
recv() < 0    -> error / would-block depending on mode and errno
```

This is a common interview question.

```cpp
ssize_t n = recv(fd, buffer, sizeof(buffer), 0);

if (n == 0) {
    // EOF from peer / orderly shutdown of peer's send direction
}
```

---

# 8. Connection Closing — FIN vs RST

## FIN — Graceful shutdown

```text
CLIENT                                 SERVER

 FIN ---------------------------------->

     <------------------------------- ACK

     <------------------------------- FIN

 ACK ---------------------------------->
```

FIN essentially means:

> "I have no more bytes to send in this direction."

TCP supports half-close, so the opposite direction may remain usable for some time.

## RST — Abort/reset

RST means the TCP connection is being reset rather than gracefully finished.

```text
FIN = orderly/graceful shutdown
RST = abort/reset
```

### Real-life analogy

FIN:

> "I'm done speaking. Goodbye."

RST:

> Phone connection is abruptly terminated/reset.

### Interview question
**Q: FIN vs RST?**

FIN performs orderly shutdown. RST aborts/resets the connection and can cause pending communication to fail immediately.

---

# 9. TIME_WAIT — Why Does It Exist?

After an active close, one side commonly remains in `TIME_WAIT` for a period.

Why?

## Reason 1 — Old packets

Delayed packets belonging to the old connection should be allowed to expire rather than interfere with a later connection using the same tuple.

## Reason 2 — Final ACK may be lost

```text
CLIENT                                  SERVER

             <---------------- FIN

ACK ------------------------ X
                         ACK lost

             <---------------- FIN again

ACK -------------------------->
```

The TIME_WAIT endpoint is still around and can acknowledge a retransmitted FIN.

### Interview answer to remember

> TIME_WAIT helps prevent delayed segments from an old connection interfering with a new incarnation and allows the final ACK to be retransmitted if necessary.

---

# 10. Flow Control vs Congestion Control

This distinction is asked frequently.

## Flow Control

Protects the **receiver**.

```text
Fast Sender                     Slow Receiver
    |                                 |
    | -------- DATA ----------------> |
    |                                 |
    | <---- smaller receive window -- |
    |                                 |
    |       sender slows down         |
```

Receiver advertises available receive-window space (`rwnd`).

Think:

> Don't overwhelm the receiving machine/application path.

## Congestion Control

Protects the **network**.

```text
Sender ---- Router ---- Router ---- Receiver
                ^
                |
             congestion
```

TCP adjusts how much data it puts in flight using a congestion window (`cwnd`) and a congestion-control algorithm.

Useful concepts:

- Slow Start
- Congestion Avoidance
- Fast Retransmit
- Fast Recovery

Effective in-flight sending is constrained by both receiver and network conditions, often summarized conceptually as:

```text
usable window <= min(rwnd, cwnd)
```

### Easy memory trick

```text
FLOW control       -> protects RECEIVER
CONGESTION control -> protects NETWORK
```

### Real-life analogy

Flow control:

> Warehouse says, "I only have space for 10 more boxes."

Congestion control:

> Highway is congested, so fewer trucks should enter at once.

---

# 11. TCP Keepalive vs Application Heartbeat

Suppose a client disappears because its machine loses power or the network path breaks.

No graceful FIN may arrive.

```text
Client ---------------- Server
   X
power/network failure
```

TCP keepalive can periodically probe an otherwise idle connection according to OS/socket configuration.

But applications often implement their own heartbeat:

```text
Client                    Server

PING -------------------->

     <---------------- PONG
```

Why application heartbeat?

Because your application may want faster failure detection and may need to know whether the **application/service** is responsive, not merely whether the TCP stack/path responds.

### Interview question
**Q: TCP keepalive vs heartbeat?**

TCP keepalive is a transport-level liveness mechanism. Application heartbeat is protocol-specific and can verify service-level responsiveness with application-controlled timing and semantics.

---

# 12. Blocking vs Nonblocking I/O

## Blocking socket

```text
Thread
  |
 recv()
  |
  +------ waits because no data
  |
 data arrives
  |
 continues
```

Simple model:

```text
Client 1 -> Thread 1
Client 2 -> Thread 2
Client 3 -> Thread 3
```

Easy to program, and perfectly reasonable for many workloads.

But tens of thousands of mostly idle connections can make thread-per-connection expensive because of thread memory, scheduling, and context-switch overhead.

## Nonblocking socket

If data is unavailable, the operation returns immediately, commonly with:

```text
EAGAIN / EWOULDBLOCK
```

But this is bad:

```text
while (true)
    recv(fd, ...);   // busy polling
```

So scalable servers combine nonblocking sockets with an event mechanism.

---

# 13. `select`, `poll`, `epoll`, IOCP

You don't need to memorize every API for most interviews. Understand the architecture.

## Linux — `epoll`

Instead of dedicating one blocked thread to every socket:

```text
                 epoll_wait()
                     |
          "which sockets are ready?"
                     |
          +----------+----------+
          |                     |
        fd=10                 fd=100
       readable              writable
```

Application handles the sockets reported as ready.

This enables a relatively small number of event-loop/worker threads to manage many connections.

## Windows — IOCP

IOCP = I/O Completion Ports.

Simplified mental model:

```text
epoll -> readiness model
         "socket is ready"

IOCP  -> completion model
         "asynchronous operation completed"
```

This is especially relevant for C++ engineers working across Linux and Windows.

### Interview question
**Q: How would you handle 100,000 TCP connections?**

Good direction:

> I would avoid a naive thread-per-connection architecture. On Linux I would typically use nonblocking sockets with epoll; on Windows, an asynchronous completion model such as IOCP. I would also use bounded queues, backpressure, connection limits/timeouts, and a controlled worker pool for CPU or blocking work.

---

# 14. Level-Triggered vs Edge-Triggered `epoll`

## Level-triggered

As long as unread data remains, the descriptor continues to be considered ready.

```text
Data available
     |
epoll reports fd
     |
read only some data
     |
data still available
     |
epoll can report fd again
```

## Edge-triggered

Notification is tied to readiness transitions. The usual pattern with nonblocking sockets is to drain the socket until it would block.

```text
event received
     |
recv()
     |
recv()
     |
recv()
     |
EAGAIN
     |
STOP
```

### Interview question
**Q: What is a common edge-triggered epoll bug?**

Failing to drain available data until `EAGAIN/EWOULDBLOCK`, potentially leaving data unread without receiving the notification pattern the code expected.

---

# 15. TCP Reliability — What TCP Gives You and What It Doesn't

TCP gives you:

```text
Ordered bytes
Retransmission of lost data
Duplicate handling
Flow control
Congestion control
Error detection at transport level
```

But TCP does NOT tell you:

```text
"The application processed my request."

"The database committed my request."

"The remote file is safely persisted."
```

This distinction is extremely important in distributed systems.

### Example

```text
CLIENT                              SERVER

send(payment request) -------------> TCP receives bytes
                                      |
                                      v
                                  process request
                                      |
                                      v
                                 commit database
                                      |
                     <------------- APP ACK
```

TCP delivery and application success are different concepts.

---

# 16. Principal-Level Design: Large File Transfer Over an Unreliable WAN

Suppose you must transfer a **100 GB backup** between data centers and the network can disconnect.

A weak design:

```text
send entire 100 GB

failure at 99 GB

restart from zero
```

A better design uses chunks.

```text
                 100 GB FILE
                      |
                      v
                Chunk Manager
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
      Chunk 0       Chunk 1       Chunk 2
       4 MB          4 MB          4 MB
        |             |             |
        +-------------+-------------+
                      |
                      v
                   Network
```

Each chunk can contain metadata such as:

```text
Transfer ID : backup-123
Chunk ID    : 1057
Offset      : ...
Length      : 4 MB
Checksum    : ...
```

---

# 17. Why Chunk IDs?

Suppose chunks arrive/retry like this:

```text
Chunk 10 -> received
Chunk 11 -> lost
Chunk 12 -> received
```

The receiver knows exactly what is missing:

```text
Missing = Chunk 11
```

It can request/retry only that portion, depending on protocol design.

---

# 18. Why Checksums?

Receiver verifies each chunk before accepting it.

```text
Sender
  |
calculate checksum
  |
Chunk + checksum
  |
  v
Network
  |
  v
Receiver
  |
calculate checksum again
  |
compare
  |
OK -> accept
BAD -> reject/retry
```

For security, use established cryptographic protection (typically TLS) and choose hashes/MACs according to the actual integrity/threat requirements rather than inventing a custom crypto scheme.

---

# 19. Durable Checkpoints and Resume

Suppose connection fails after 65 GB.

```text
100 GB transfer

[=========================---------]
0 GB                      65      100
                           X
                        failure
```

Don't restart from zero.

Persist progress:

```text
Transfer ID = backup-123
Committed chunks = ...
```

Reconnect:

```text
Sender                               Receiver

"backup-123 status?" -------------->

                  <------ committed chunk state

Resume missing chunks -------------->
```

### Key word: durable

If the receiver says:

```text
"Chunk 100 committed"
```

then its protocol should define what "committed" means. If it promises crash-safe completion, the chunk/data and corresponding checkpoint state must be persisted accordingly before sending that ACK.

---

# 20. Why Application-Level ACK When TCP Already ACKs?

Very important Principal-level question.

TCP ACK means roughly:

```text
TCP receiver has acknowledged sequence bytes
```

It does NOT mean:

```text
Application validated chunk
Disk write completed
Database transaction committed
```

So application protocol might send:

```text
ACK {
    transfer_id = backup-123
    chunk_id = 100
    status = COMMITTED
}
```

### Real-life analogy

Courier tracking says:

> "Parcel reached company reception."

Application ACK says:

> "Finance department opened it, validated it, and recorded the invoice."

Different guarantees.

---

# 21. Idempotency — Handling Duplicate Retries

Scenario:

```text
Sender                             Receiver

Chunk 100 ------------------------>
                                  save successfully

       <----------- ACK Chunk 100
                    X ACK lost

Sender thinks operation failed.

Chunk 100 ------------------------> RETRY
```

Receiver should not corrupt or duplicate the logical operation.

Use:

```text
Transfer ID + Chunk ID
```

Receiver can detect:

```text
backup-123 / chunk-100 already committed
```

and safely return success/current status.

### Simple definition

> An idempotent operation can be retried without changing the intended final result after the first successful application.

---

# 22. Retry — Don't Create a Retry Storm

Bad:

```text
fail -> retry immediately
fail -> retry immediately
fail -> retry immediately
```

Imagine 10,000 clients doing this simultaneously.

Better:

```text
Failure
  |
 wait ~1 sec
  |
 retry
  |
 wait ~2 sec
  |
 retry
  |
 wait ~4 sec
```

Usually add **jitter** so clients do not retry at exactly the same instant.

```text
Exponential backoff + jitter
```

---

# 23. Bounded Buffering and Backpressure

Suppose disk can read:

```text
2 GB/sec
```

but network sends only:

```text
100 MB/sec
```

Without limits:

```text
Disk Reader ---> Memory Queue ---> Network
    FAST             grows           SLOW
                      grows
                      grows
                      |
                     OOM
```

Use bounded buffering:

```text
Disk Reader
    |
    v
+------------------+
| Bounded Queue    |
| max N chunks     |
+------------------+
    |
    v
Network Sender
```

When queue becomes full:

```text
Producer slows/stops
```

This is **backpressure**.

### Real-life analogy

Restaurant kitchen produces 100 meals/minute but waiters can deliver only 20.

Don't keep cooking until the building fills with food. Limit the queue and slow production.

---

# 24. Throttling

Sometimes the application deliberately limits throughput.

Example:

```text
Backup transfer maximum = 100 MB/s
```

Why?

Because backup traffic should not consume all:

- network bandwidth
- disk bandwidth
- CPU
- memory

Possible mechanisms include rate limiting/token buckets and concurrency limits.

---

# 25. Compression

Possible pipeline:

```text
File
 |
Read chunk
 |
Compress
 |
Encrypt/TLS
 |
Send
```

Compression helps when:

```text
CPU is available
+
data compresses well
+
network is the bottleneck
```

It may not help much for already-compressed content such as JPEG, MP4, ZIP, etc.

---

# 26. Encryption

For data in transit, normally use a proven protocol such as TLS rather than custom encryption.

```text
Application
    |
    v
   TLS
    |
    v
   TCP
    |
    v
Network
```

TLS can provide confidentiality, integrity protection, and peer authentication depending on configuration.

---

# 27. Complete WAN Transfer Flow — Remember This Diagram

```text
                     LARGE FILE
                         |
                         v
                    Split chunks
                         |
                         v
             +-----------------------+
             | Transfer ID / Chunk ID|
             | Offset / Length       |
             | Checksum              |
             +-----------------------+
                         |
                         v
                  Bounded Queue
                         |
                         v
                  Compression?
                         |
                         v
                      TLS/TCP
                         |
                  Unreliable WAN
                         |
                         v
                      Receiver
                         |
                  Verify checksum
                         |
                         v
                    Write chunk
                         |
                         v
                Durable checkpoint
                         |
                         v
                 Application ACK
                         |
                         v
                      Sender

Failure?
   |
Reconnect
   |
Read checkpoint/status
   |
Resume missing chunks
```

If you can explain this diagram clearly, you can answer a large number of Principal-level networking design questions.

---

# 28. Common Failure Scenarios

## Scenario 1 — Server crashes

```text
Client -------- Server
                 X crash
```

Depending on timing/network state, the client may eventually observe a reset, timeout, failed read/write, or connection closure.

Design considerations:

```text
Reconnect
Retry safely
Use idempotency
Resume from durable state
```

## Scenario 2 — Network cable/path disappears

No FIN necessarily arrives.

Detection can involve:

```text
I/O timeout
TCP retransmission failure
TCP keepalive
Application heartbeat
```

## Scenario 3 — ACK lost after operation succeeded

```text
Request -> server commits
ACK     -> lost
```

Client cannot safely assume the operation failed.

Use:

```text
Request/operation ID
Idempotency
Status query / safe retry
```

This concept is fundamental to distributed systems.

---

# 29. Debugging TCP Problems

Useful tools/concepts for a systems engineer:

```text
ss / netstat     -> inspect sockets/connections
lsof             -> process/socket/file descriptors
Wireshark        -> packet inspection GUI
tcpdump          -> packet capture CLI
strace           -> socket-related system calls on Linux
```

Useful states to recognize:

```text
LISTEN
SYN_SENT
SYN_RECV
ESTABLISHED
FIN_WAIT_1
FIN_WAIT_2
CLOSE_WAIT
LAST_ACK
TIME_WAIT
```

### Important debugging question

**Many sockets stuck in `CLOSE_WAIT`. What does it suggest?**

The peer has sent FIN and the local TCP stack has received it, but the local application has not yet closed its side of those sockets. Investigate application connection cleanup/resource leaks.

**Many sockets in `TIME_WAIT`?**

Often indicates many connections are being actively closed. TIME_WAIT itself is normal; investigate connection churn/architecture and resource pressure before trying to "remove" it.

---

# 30. Principal Engineer Interview Questions

## Fundamentals

### Q1. TCP vs UDP?
Explain reliability, ordering, stream vs datagram semantics, latency/use cases.

### Q2. What is a socket?
OS-managed communication endpoint exposed to applications.

### Q3. What identifies a TCP connection?

```text
Source IP + Source Port + Destination IP + Destination Port
```

---

## Connection Lifecycle

### Q4. Explain TCP server lifecycle.

```text
socket -> bind -> listen -> accept -> recv/send -> close
```

### Q5. Explain client lifecycle.

```text
socket -> connect -> send/recv -> close
```

### Q6. What does `accept()` return?
A new connected socket; the listening socket remains available for new connections.

### Q7. Explain three-way handshake.

```text
SYN -> SYN/ACK -> ACK
```

---

## Data Transfer

### Q8. Does one `send()` equal one `recv()`?
No. TCP is a byte stream.

### Q9. Can `send()` be partial?
Yes. Track offset and continue appropriately.

### Q10. How do you define message boundaries over TCP?
Length prefix, delimiter, fixed-size records, or another framing protocol.

### Q11. What does `recv() == 0` mean?
Orderly EOF from the peer's sending direction.

---

## Connection Termination

### Q12. FIN vs RST?

```text
FIN -> orderly shutdown
RST -> abort/reset
```

### Q13. Why TIME_WAIT?
Protect against delayed old segments and allow retransmission of the final ACK.

### Q14. What is CLOSE_WAIT?
Peer has closed its send side; local application still needs to close its socket when appropriate.

---

## Reliability

### Q15. Flow control vs congestion control?

```text
Flow       -> receiver protection
Congestion -> network protection
```

### Q16. TCP keepalive vs application heartbeat?
Transport-level liveness vs application-level health/liveness semantics.

### Q17. TCP is reliable. Why application ACK?
TCP confirms transport of bytes, not successful application processing or durable commit.

---

## Scalability

### Q18. Blocking vs nonblocking sockets?
Blocking waits; nonblocking returns when the operation cannot proceed immediately.

### Q19. How do you support 100K connections?
Event-driven/asynchronous architecture such as nonblocking + epoll on Linux or IOCP on Windows, plus controlled workers and bounded resources.

### Q20. epoll vs IOCP?
Readiness-oriented vs completion-oriented mental model.

### Q21. Level-triggered vs edge-triggered epoll?
Level continues reporting readiness while condition exists; edge requires careful draining until would-block in the common nonblocking pattern.

---

## System Design

### Q22. Design reliable 100 GB WAN transfer.
Mention:

```text
Chunk IDs
Checksums
Sequencing/offsets
Durable checkpoints
Application ACKs
Idempotency
Retry + exponential backoff + jitter
Resume
Bounded buffering/backpressure
Throttling
Compression
TLS
```

### Q23. Connection dies at 95 GB. What happens?
Reconnect, identify transfer, obtain durable committed state, and resume missing/uncommitted chunks rather than restart everything.

### Q24. ACK lost after server committed a chunk?
Retry using transfer/chunk identity; server treats operation idempotently and returns the committed status.

### Q25. Producer faster than network?
Bounded queue + backpressure + optional throttling.

---

# 31. Ten Lines to Remember Before the Interview

```text
1. TCP = reliable, ordered BYTE STREAM; it does not preserve app message boundaries.

2. Server = socket -> bind -> listen -> accept -> recv/send -> close.

3. Client = socket -> connect -> send/recv -> close.

4. Handshake = SYN -> SYN/ACK -> ACK.

5. send()/recv() may be partial; loop and track offsets/protocol state.

6. recv() == 0 means orderly EOF from the peer's send direction.

7. FIN = graceful/orderly shutdown; RST = abort/reset; TIME_WAIT protects connection teardown/reuse.

8. Flow control protects receiver; congestion control protects network.

9. Linux scalability: nonblocking + epoll. Windows: IOCP is a completion-oriented model.

10. Reliable WAN transfer = chunks + IDs + checksum + durable checkpoint + app ACK
    + idempotency + retry/resume + bounded buffering/backpressure + TLS.
```

---

# 32. One Story That Connects Everything

Imagine a backup agent transferring a **100 GB database backup** to a remote data center.

```text
Backup Client
     |
 socket()
     |
 connect()
     |
 SYN -> SYN/ACK -> ACK
     |
 connection established
     |
 split backup into chunks
     |
 send chunk 1
 send chunk 2
 send chunk 3
     |
 WAN becomes slow
     |
 TCP congestion control reduces pressure on network
     |
 receiver becomes slow
     |
 TCP flow control + app backpressure reduce production
     |
 connection breaks at 65 GB
     |
 reconnect
     |
 ask receiver for durable checkpoint
     |
 resume missing chunks
     |
 duplicate chunk appears because previous ACK was lost
     |
 Transfer ID + Chunk ID makes retry idempotent
     |
 complete remaining chunks
     |
 verify final file integrity
     |
 FIN / graceful close
```

That single scenario connects almost every networking concept an interviewer is likely to explore.

---

## Recommended Study Order

```text
1. TCP vs UDP
       |
2. Socket server/client lifecycle
       |
3. 3-way handshake
       |
4. TCP byte-stream + framing
       |
5. Partial send/recv
       |
6. FIN / RST / TIME_WAIT / CLOSE_WAIT
       |
7. Flow vs congestion control
       |
8. Keepalive / heartbeat / failures
       |
9. Blocking vs nonblocking
       |
10. epoll / IOCP
       |
11. Reliable WAN transfer design
```

Don't start by memorizing all TCP states or kernel internals. First be able to explain the above flow clearly and reason through failures.
