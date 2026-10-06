# Networking Interview Study Guide — Principal Software Engineer (C++ / Linux)

> Goal: Build enough networking depth to answer Principal-level interviews confidently, especially:
> TCP, UDP, DNS, HTTP/HTTPS, TLS, sockets, Linux networking, C++ networking code, debugging, and distributed-system networking decisions.

---

## 0. How to Use This Guide

Do **not** start by memorizing every field in every protocol header.

Use this order:

1. **End-to-end mental model:** What happens when I type `https://www.google.com`?
2. **IP + ports + TCP/UDP:** How two processes on two machines communicate.
3. **TCP internals:** handshake, sequence/ACK, retransmission, flow/congestion control, connection close.
4. **DNS:** name → IP.
5. **HTTP:** request/response, methods, status codes, keep-alive, HTTP/1.1 vs 2 vs 3.
6. **HTTPS/TLS:** certificates, handshake, encryption.
7. **Sockets in C/C++:** server/client lifecycle and important system calls.
8. **Linux debugging:** `ip`, `ss`, `ping`, `traceroute`, `dig`, `curl`, `nc`, `tcpdump`, Wireshark, etc.
9. **Principal-level scenarios:** timeouts, retries, load balancers, NAT, proxies, connection pools, backpressure, failures.

The most important skill is being able to connect all these layers in one coherent explanation.

---

# 1. The Mental Model: How Machines Communicate

Suppose:

```text
Client application
    |
    | HTTP
    v
TCP
    |
    v
IP
    |
    v
Ethernet / Wi-Fi
    |
    v
Network
    |
    v
Server
```

A useful simplified mapping:

| Layer | Responsibility | Examples |
|---|---|---|
| Application | What applications say | HTTP, DNS, SSH, MQTT, gRPC |
| Transport | Process-to-process delivery | TCP, UDP, QUIC |
| Network | Machine-to-machine routing | IPv4, IPv6, ICMP |
| Link | Delivery on local network | Ethernet, Wi-Fi, ARP/NDP |

### Interview line

> IP gets the packet to the correct machine; TCP/UDP plus the port gets it to the correct application/process.

---

# 2. IP Address, Port, Socket

## IP address

Identifies a network interface/host for routing purposes.

Example:

```text
142.250.x.x
```

IPv4 is 32 bits.

IPv6 is 128 bits.

## Port

A port identifies a logical endpoint/service on a host.

Examples:

```text
22   SSH
53   DNS
80   HTTP
443  HTTPS
```

TCP and UDP each have their own 16-bit port namespace: `0–65535`.

## Socket

Conceptually, a socket is an OS abstraction used by a process for network communication.

A TCP connection is commonly identified by the tuple:

```text
(source IP,
 source port,
 destination IP,
 destination port)
```

Protocol is also relevant when identifying flows in the networking stack, hence you will often hear **5-tuple**:

```text
protocol + source IP + source port + destination IP + destination port
```

Example:

```text
10.0.0.5:52341 -> 142.250.x.x:443
```

This is why thousands of clients can connect to the same server port 443.

---

# 3. TCP vs UDP

## TCP

TCP provides a reliable, ordered byte stream.

Important characteristics:

- Connection-oriented
- Reliable delivery
- Ordered delivery
- Detects loss
- Retransmits lost data
- Flow control
- Congestion control
- No message boundaries — it is a **byte stream**

Typical use:

```text
HTTP/1.1
HTTP/2
SSH
database connections
many RPC protocols
```

## UDP

UDP is datagram-oriented.

Characteristics:

- Connectionless at protocol level
- No guaranteed delivery
- No guaranteed ordering
- No automatic retransmission
- Lower protocol overhead
- Preserves datagram/message boundaries

Typical use:

```text
DNS (commonly)
real-time media
gaming
telemetry
QUIC transport substrate
```

## Interview comparison

Do not say:

> UDP is always faster.

Better:

> UDP has less transport-layer machinery and lets the application choose its own reliability and congestion behavior. Whether it is faster depends on the protocol and workload.

---

# 4. TCP Three-Way Handshake

Client wants to establish a connection.

```text
Client                                  Server

SYN, seq=x
--------------------------------------->

                      SYN + ACK
                 seq=y, ack=x+1
<---------------------------------------

ACK, ack=y+1
--------------------------------------->

Connection established
```

Why three packets?

Both sides need to establish that:

- the peer is reachable,
- each side can send and receive,
- initial sequence numbers are synchronized.

## States worth knowing

Client often transitions through:

```text
CLOSED
SYN_SENT
ESTABLISHED
```

Server:

```text
LISTEN
SYN_RECEIVED
ESTABLISHED
```

Debug with:

```bash
ss -tan
```

---

# 5. TCP Reliability

TCP assigns sequence numbers to bytes.

Simplified:

```text
Sender                       Receiver

SEQ=100, 100 bytes
---------------------------->

             ACK=200
<----------------------------
```

`ACK=200` means:

> I have received everything before byte 200; send starting from 200.

If data is lost, TCP retransmits it.

Mechanisms include:

- retransmission timeout (RTO)
- duplicate ACK based fast retransmission
- modern loss detection algorithms depending on implementation

---

# 6. TCP Flow Control

Problem:

```text
Fast sender -> Slow receiver
```

The receiver has finite buffer capacity.

TCP advertises a **receive window (rwnd)**.

```text
Receiver:
"I currently have room for N more bytes."
```

Sender limits outstanding data accordingly.

### Interview distinction

**Flow control**

```text
protects the receiver
```

**Congestion control**

```text
protects the network
```

Do not mix these up.

---

# 7. TCP Congestion Control

The sender must avoid overwhelming the network.

Conceptually TCP maintains a congestion window:

```text
cwnd
```

Effective amount of outstanding data is constrained by approximately:

```text
min(cwnd, rwnd)
```

Important concepts:

- slow start
- congestion avoidance
- packet loss / ECN as congestion signals
- retransmission
- RTT
- bandwidth-delay product

Principal-level discussion:

> Increasing socket buffers alone does not guarantee higher throughput. Throughput can be constrained by RTT, congestion window, receiver window, application behavior, and the underlying network.

---

# 8. TCP Connection Termination

Typical graceful close:

```text
Client                     Server

FIN
-------------------------->

                 ACK
<--------------------------

                 FIN
<--------------------------

ACK
-------------------------->
```

A TCP connection is full duplex, so each direction is closed independently.

## TIME_WAIT

The endpoint performing the active close commonly enters `TIME_WAIT`.

Why?

Among other reasons, it helps ensure delayed packets from an old connection cannot be confused with a later connection using the same tuple and allows retransmission of the final ACK if necessary.

Useful command:

```bash
ss -tan state time-wait
```

Large numbers of `TIME_WAIT` sockets can be relevant when investigating high connection churn.

---

# 9. What Happens When You Type `https://www.google.com`?

This is one of the highest-value interview questions.

A strong answer should move layer by layer.

## Step 1 — Browser parses the URL

```text
scheme: https
host:   www.google.com
port:   443 (default)
path:   /
```

## Step 2 — DNS resolution

Browser/OS needs an IP address.

Conceptually it checks caches and configured resolution mechanisms before querying DNS.

Possible layers include:

```text
browser/application cache
OS resolver/cache
hosts file / local configuration
configured recursive DNS resolver
```

If a recursive lookup is required, the resolver may ultimately consult:

```text
Root DNS
   ↓
TLD (.com)
   ↓
authoritative DNS for google.com
```

Result:

```text
www.google.com -> one or more IPv4/IPv6 addresses
```

## Step 3 — Determine route / next hop

The OS routing table decides where the packet should go.

Inspect:

```bash
ip route
```

For an off-subnet destination, traffic normally goes toward a gateway.

On IPv4 Ethernet networks, ARP may be used to resolve a local next-hop IPv4 address to a MAC address.

Inspect:

```bash
ip neigh
```

## Step 4 — Transport connection

For traditional HTTPS over TCP:

```text
Client -> Server: SYN
Server -> Client: SYN-ACK
Client -> Server: ACK
```

For HTTP/3, the browser may instead use QUIC over UDP, where transport security is integrated with TLS 1.3.

## Step 5 — TLS handshake

Client and server negotiate security parameters.

At a high level:

```text
ClientHello
    supported TLS versions
    cipher suites
    key share
    SNI
    ALPN

ServerHello
    selected parameters
    key share

Server provides certificate/authentication information

Client validates certificate

Both derive symmetric session keys
```

TLS 1.3 differs in important details from older TLS versions, but this is the right interview-level mental model.

## Step 6 — HTTP request

Example conceptually:

```http
GET / HTTP/1.1
Host: www.google.com
...
```

For HTTP/2 or HTTP/3 the request is encoded differently, but the semantics are still HTTP.

## Step 7 — Server-side infrastructure

The request may pass through:

```text
CDN / edge
    ↓
load balancer / reverse proxy
    ↓
frontend service
    ↓
backend services / caches / databases
```

## Step 8 — HTTP response

Server returns:

```text
status
headers
body
```

## Step 9 — Browser rendering

Browser:

```text
parses HTML
fetches CSS/JS/images/fonts
constructs DOM/CSSOM
runs JavaScript
performs layout
paints/composites
```

Additional network requests may reuse existing connections.

### Principal-level concise answer

> The browser parses the URL, resolves the hostname using DNS, the OS selects a route and resolves the local next hop when necessary, then establishes the transport connection. With TCP-based HTTPS that includes a TCP handshake followed by TLS negotiation and certificate validation. The browser then sends the HTTP request. The request may traverse edge infrastructure and load balancers before reaching the application. The response comes back over the established secure connection, and the browser parses and renders the resources. With HTTP/3, QUIC over UDP replaces the TCP transport path and integrates TLS 1.3 into the connection establishment.

---

# 10. DNS

DNS translates names to records needed to locate or describe services.

Example:

```text
www.example.com -> IP address
```

Important record types:

| Record | Meaning |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | alias |
| MX | mail exchanger |
| NS | authoritative name server |
| TXT | arbitrary text / verification / policy |
| PTR | reverse lookup |

Debug:

```bash
dig google.com
dig google.com A
dig google.com AAAA
dig +trace google.com
nslookup google.com
getent hosts google.com
```

Important distinction:

`dig` asks DNS directly according to its configuration/options.

`getent hosts` uses the system's name-service configuration and can therefore be closer to how an application resolves a name on Linux.

---

# 11. HTTP Basics

HTTP is an application-layer request/response protocol.

Example:

```http
GET /users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id":123}
```

## Methods

```text
GET     read
POST    create/action
PUT     replace/update
PATCH   partial update
DELETE  delete
HEAD    headers without response body semantics of GET
OPTIONS capabilities / CORS-related usage
```

## Important status codes

```text
200 OK
201 Created
204 No Content

301 Moved Permanently
302 Found
304 Not Modified
307 Temporary Redirect
308 Permanent Redirect

400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
408 Request Timeout
409 Conflict
429 Too Many Requests

500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

Principal-level distinction:

```text
502 -> proxy/gateway received an invalid/failed response from upstream
504 -> proxy/gateway timed out waiting for upstream
```

---

# 12. HTTP/1.1 vs HTTP/2 vs HTTP/3

## HTTP/1.1

- persistent connections supported
- textual wire format
- pipelining exists but was problematic and rarely used broadly
- browsers often open multiple connections per origin

## HTTP/2

- binary framing
- multiplexes streams over one TCP connection
- header compression (HPACK)
- stream prioritization mechanisms

Important caveat:

TCP packet loss can still delay delivery of later bytes for all HTTP/2 streams sharing that TCP connection because TCP itself guarantees ordered byte delivery.

## HTTP/3

Uses:

```text
HTTP/3
  ↓
QUIC
  ↓
UDP
```

Benefits include:

- stream multiplexing without TCP's cross-stream transport head-of-line blocking
- integrated TLS 1.3
- faster connection establishment in common cases
- connection migration support

---

# 13. HTTPS and TLS

HTTPS is:

```text
HTTP over a secure transport using TLS
```

For HTTP/1.1 and HTTP/2 this is normally TLS over TCP.

For HTTP/3, HTTP runs over QUIC, which uses TLS 1.3 for cryptographic handshake/security.

TLS provides:

```text
Confidentiality
Integrity
Authentication of the server
```

Mutual TLS can authenticate both client and server.

---

# 14. Symmetric vs Asymmetric Cryptography

## Symmetric

Same secret key is used for encryption/decryption.

Advantages:

```text
fast
efficient for bulk traffic
```

Examples:

```text
AES
ChaCha20
```

## Asymmetric

Public/private key pair.

Used for:

```text
digital signatures
authentication
key establishment mechanisms
```

Examples/families:

```text
RSA
ECDSA
Ed25519
ECDH-related key agreement
```

Modern TLS uses public-key cryptography during authentication/key establishment and symmetric cryptography for bulk application traffic.

---

# 15. TLS Certificate Validation

Server presents a certificate chain.

Client typically validates things such as:

```text
Is the certificate currently valid?
Does the requested hostname match?
Does the chain lead to a trusted root?
Are signatures valid?
Are certificate constraints/usages acceptable?
Has policy/revocation handling rejected it?
```

Chain:

```text
Root CA
   ↓ signs
Intermediate CA
   ↓ signs
Server certificate
```

The root CA is trusted through the client's/OS's trust store.

---

# 16. TLS Interview Topics

Know these terms:

```text
TLS 1.2
TLS 1.3
certificate
CA
certificate chain
public/private key
session key
cipher suite
SNI
ALPN
mTLS
certificate expiry
certificate rotation
```

## SNI

Server Name Indication allows the client to indicate the hostname during TLS setup so one IP can serve certificates/sites for multiple hostnames.

## ALPN

Application-Layer Protocol Negotiation lets client/server select an application protocol such as:

```text
h2
http/1.1
```

---

# 17. Socket Programming in C/C++

For a TCP server:

```text
socket()
   ↓
bind()
   ↓
listen()
   ↓
accept()
   ↓
recv()/send()
   ↓
close()
```

For a TCP client:

```text
socket()
   ↓
connect()
   ↓
send()/recv()
   ↓
close()
```

---

# 18. Minimal TCP Server Lifecycle

```cpp
int server_fd = socket(AF_INET, SOCK_STREAM, 0);

bind(server_fd, ...);

listen(server_fd, backlog);

int client_fd = accept(server_fd, ...);

recv(client_fd, buffer, ...);

send(client_fd, response, ...);

close(client_fd);
close(server_fd);
```

What each call means:

### `socket()`

Creates a socket descriptor.

### `bind()`

Associates a local IP/address and port with the socket.

### `listen()`

Marks a TCP socket as a passive/listening socket.

### `accept()`

Removes/returns a completed incoming connection from the accept queue and creates a new connected socket.

Important:

```text
listening socket != connected client socket
```

The listening socket remains available for additional connections.

### `send()/recv()`

Transfer bytes.

### `close()`

Releases the file descriptor and participates in connection teardown according to socket state/options.

---

# 19. Critical C++ Networking Gotcha: TCP Has No Message Boundaries

Suppose sender does:

```cpp
send(fd, "HELLO", 5, 0);
send(fd, "WORLD", 5, 0);
```

Receiver is **not guaranteed** to observe:

```text
recv() -> HELLO
recv() -> WORLD
```

It may receive chunks such as:

```text
HELLOWORLD
```

or:

```text
HEL
LOWORLD
```

TCP provides bytes, not application messages.

Therefore your protocol needs framing.

Common approaches:

```text
fixed-size message
delimiter
length-prefix
self-describing protocol framing
```

Example:

```text
[4-byte length][payload]
```

This is a very valuable C++ interview point.

---

# 20. Partial send / partial receive

Never assume:

```cpp
send(fd, buf, 1000, 0)
```

always sends all 1000 bytes.

Likewise `recv()` can return fewer bytes than the logical application message.

Production code needs loops and proper error handling.

Pseudo-pattern:

```cpp
while (total < size) {
    ssize_t n = send(fd, data + total, size - total, 0);

    if (n > 0) {
        total += n;
    } else {
        // handle error / interruption / closure
    }
}
```

---

# 21. Blocking vs Non-Blocking I/O

## Blocking socket

A call such as:

```cpp
recv()
```

may wait until data, EOF, an error, or a configured timeout occurs.

Simple programming model, but a thread-per-connection architecture becomes expensive at very large connection counts.

## Non-blocking

Socket operations return immediately when they would otherwise block, typically indicating:

```text
EAGAIN / EWOULDBLOCK
```

Then use readiness/event mechanisms such as:

```text
select
poll
epoll     (Linux)
kqueue    (BSD/macOS)
IOCP      (Windows completion model)
```

---

# 22. select vs poll vs epoll

## select

- old and portable
- fd-set size limitations on many systems
- repeatedly scans descriptor sets
- modifies fd sets passed to it

## poll

- no `FD_SETSIZE` interface limitation
- still requires scanning the descriptor array

## epoll

Linux-specific scalable event notification facility.

Typical model:

```text
epoll_create1()
epoll_ctl()
epoll_wait()
```

Good interview statement:

> For a Linux server handling many concurrent mostly-idle connections, I would generally consider non-blocking sockets with epoll or use a mature async networking framework built on the platform's event facilities, rather than creating one blocking thread per connection.

---

# 23. Level-Triggered vs Edge-Triggered epoll

## Level-triggered

You continue receiving readiness notifications while the descriptor remains ready.

Simpler.

## Edge-triggered

Notification is associated with a state transition.

Usually requires non-blocking descriptors and draining reads/writes until:

```text
EAGAIN
```

Otherwise you risk leaving data unread without receiving the notification pattern your code expects.

Principal interviews may ask this.

---

# 24. Common Socket Options

Know the purpose of:

```text
SO_REUSEADDR
SO_REUSEPORT
SO_RCVBUF
SO_SNDBUF
SO_KEEPALIVE
TCP_NODELAY
```

## TCP_NODELAY

Disables Nagle's algorithm.

Useful for latency-sensitive applications that send small writes, but should not be applied blindly.

## SO_KEEPALIVE

Enables TCP keepalive probes according to OS-level timing/settings.

Important:

TCP keepalive is not the same thing as application-level health checks.

---

# 25. Nagle's Algorithm

Nagle's algorithm tries to reduce many tiny TCP packets by coalescing small writes when unacknowledged data is outstanding.

Can increase latency for certain interactive/request patterns.

Disable via:

```cpp
TCP_NODELAY
```

when justified by latency behavior.

Do not say "Nagle is bad." It is a bandwidth/packet-efficiency vs latency tradeoff.

---

# 26. Network Byte Order

Network protocols traditionally use **big endian** byte order.

Functions:

```cpp
htons()
htonl()
ntohs()
ntohl()
```

Meaning:

```text
host to network short
host to network long
network to host short
network to host long
```

Very common low-level C/C++ networking question.

---

# 27. IPv4 Subnet Basics

Example:

```text
192.168.1.10/24
```

`/24` means first 24 bits represent the network prefix.

Equivalent netmask:

```text
255.255.255.0
```

Typical network:

```text
192.168.1.0/24
```

Host addresses lie within that subnet subject to address semantics/configuration.

You should understand:

```text
subnet
prefix/CIDR
default gateway
routing table
private IP
public IP
```

---

# 28. Private IPv4 Ranges

Important private address ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

These are commonly used inside private networks and are not globally routed on the public Internet.

---

# 29. NAT

Network Address Translation rewrites address information, and commonly ports as well.

Typical home network:

```text
Laptop
192.168.1.10:53000
        |
        | NAT/PAT
        v
Public IP:62001
        |
     Internet
```

The NAT device keeps state mapping the internal flow to the external flow.

This lets many private hosts share a public IPv4 address.

---

# 30. ARP

ARP maps an IPv4 address to a link-layer/MAC address on the local network.

Example:

```text
Who has 192.168.1.1?
Tell 192.168.1.10.
```

View neighbor table:

```bash
ip neigh
```

Important:

ARP is local-link behavior; routers do not forward ordinary ARP requests across routed networks.

IPv6 uses Neighbor Discovery rather than ARP.

---

# 31. ICMP and ping

`ping` normally uses ICMP Echo Request/Reply.

```bash
ping google.com
```

Useful for:

```text
basic reachability
latency
packet-loss clues
```

But:

> Ping failure does not necessarily mean the application/service is down.

ICMP can be filtered while TCP 443 works normally.

---

# 32. traceroute

Shows the path/hops toward a destination, subject to routing and network policy.

```bash
traceroute google.com
```

Linux traceroute implementations/modes may use UDP, ICMP, or TCP probes.

It relies on IP TTL/hop-limit expiration and ICMP responses to infer intermediate hops.

Useful for:

```text
routing problems
unexpected network path
latency location
```

---

# 33. Linux Networking Debugging Toolkit

This section is extremely important for interviews.

## 1. Check interfaces and IP addresses

```bash
ip addr
ip link
```

Older:

```bash
ifconfig
```

Prefer modern `ip`.

## 2. Check routing

```bash
ip route
ip route get 8.8.8.8
```

## 3. Check neighbors / ARP

```bash
ip neigh
```

## 4. DNS

```bash
dig google.com
nslookup google.com
getent hosts google.com
```

## 5. Basic reachability

```bash
ping <host>
```

## 6. Path

```bash
traceroute <host>
tracepath <host>
```

## 7. Listening/connected sockets

```bash
ss -lntp
ss -lunp
ss -tan
```

Older:

```bash
netstat -anp
```

## 8. Test HTTP

```bash
curl -v https://example.com
curl -I https://example.com
```

## 9. Test a TCP port

```bash
nc -vz example.com 443
```

## 10. Inspect TLS

```bash
openssl s_client -connect example.com:443 -servername example.com
```

## 11. Packet capture

```bash
sudo tcpdump -i any host <ip>
sudo tcpdump -i any port 443
sudo tcpdump -nn -i any tcp
```

Then analyze a `.pcap` with Wireshark when needed.

## 12. Process using a port

```bash
ss -lntp
lsof -i :8080
```

---

# 34. My Standard Network Debugging Workflow

Interview question:

> Service A cannot connect to Service B. How do you debug it?

Use a layered approach.

## Step 1 — Application/configuration

Check:

```text
correct hostname?
correct port?
correct protocol?
proxy configuration?
timeout?
credentials?
recent deployment/config change?
```

## Step 2 — DNS

```bash
getent hosts service-b
dig service-b
```

Question:

```text
Does the name resolve to the expected IP?
```

## Step 3 — Routing/interface

```bash
ip addr
ip route
ip route get <destination-ip>
```

Question:

```text
Does the host have a valid route to the destination?
```

## Step 4 — Reachability

```bash
ping <ip>
traceroute <ip>
```

Use cautiously because ICMP may be blocked.

## Step 5 — Transport/port

```bash
nc -vz host 443
```

or:

```bash
curl -v https://host
```

Interpretation:

```text
Connection refused
    -> host reachable but no listener, wrong port, or explicit reject

Timeout
    -> packet drop/firewall/routing/service overload possibilities

DNS failure
    -> resolver/name issue
```

These are heuristics, not absolute proofs.

## Step 6 — Server socket

On server:

```bash
ss -lntp
```

Verify:

```text
Is process listening?
Which address?
127.0.0.1 only?
0.0.0.0?
IPv6 only?
Correct port?
```

## Step 7 — TLS

```bash
openssl s_client -connect host:443 -servername host
```

Check:

```text
certificate
hostname
chain
expiry
TLS negotiation
SNI
```

## Step 8 — Packet capture

```bash
tcpdump
```

Ask:

```text
Do SYN packets leave?
Does SYN-ACK return?
Are retransmissions occurring?
Does TLS start?
Are resets being sent?
```

## Step 9 — Infrastructure

Check:

```text
firewall
security groups
network ACLs
Kubernetes NetworkPolicy
service/endpoints
load balancer
proxy
NAT
DNS configuration
```

### Principal-level answer structure

> I debug networking layer-by-layer rather than immediately capturing packets: configuration → name resolution → route → transport reachability → listener → TLS/application protocol → packet capture → network infrastructure. This quickly narrows which layer owns the failure.

---

# 35. Reading TCP Symptoms

## Connection refused

Usually:

```text
SYN ->
<- RST
```

Common causes:

```text
nothing listening on destination port
wrong port
firewall actively rejecting
```

## Connection timeout

Possibilities:

```text
firewall silently dropping
routing issue
host unavailable
SYN/SYN-ACK lost
network congestion
```

Capture packets before concluding.

## Connection reset

`RST` indicates abrupt TCP connection termination.

Possible causes:

```text
application closed/reset socket
proxy/load balancer terminated connection
protocol mismatch
server error
idle timeout
```

## DNS works but HTTPS fails

Investigate:

```text
TCP connectivity
TLS
certificate
proxy/firewall
server
```

## IP works but hostname fails

Likely area:

```text
DNS / name-service configuration
```

---

# 36. tcpdump Filters Worth Memorizing

```bash
tcpdump -i any host 10.0.0.5

tcpdump -i any port 443

tcpdump -i any tcp port 443

tcpdump -i any src host 10.0.0.5

tcpdump -i any dst host 10.0.0.5

tcpdump -nn -i any 'tcp port 443'

tcpdump -i any -w capture.pcap
```

Why `-nn`?

```text
Do not resolve hostnames or service names.
```

This makes troubleshooting faster and avoids DNS/service-name translation noise.

---

# 37. curl Debugging

```bash
curl -v https://example.com
```

Can reveal:

```text
DNS-selected address
connection attempt
TLS negotiation
certificate information
HTTP request
HTTP response headers
redirects
```

Useful:

```bash
curl -I URL
curl -L URL
curl --connect-timeout 5 URL
curl --resolve example.com:443:1.2.3.4 https://example.com/
```

`--resolve` is particularly useful for testing a hostname against a specific IP while preserving Host/SNI behavior.

---

# 38. Load Balancer

A load balancer distributes traffic across backend servers.

```text
Clients
   |
   v
Load Balancer
 /    |     \
S1    S2    S3
```

## Layer 4

Routes using transport/network information such as:

```text
IP
TCP/UDP port
connection
```

## Layer 7

Understands application protocols such as HTTP.

Can route based on:

```text
host
path
headers
cookies
```

Example:

```text
/api/*    -> API servers
/images/* -> image service
```

---

# 39. Reverse Proxy vs Forward Proxy

## Forward proxy

Acts on behalf of clients.

```text
Client -> Forward Proxy -> Internet
```

Uses:

```text
enterprise egress
filtering
privacy/policy
```

## Reverse proxy

Acts in front of servers.

```text
Client -> Reverse Proxy -> Backend
```

Uses:

```text
TLS termination
routing
load balancing
caching
authentication
rate limiting
```

---

# 40. Connection Pooling

Creating a new connection for every request costs:

```text
TCP/QUIC setup
TLS setup
kernel/network resources
latency
```

Connection pools reuse established connections.

Used by:

```text
HTTP clients
database clients
RPC clients
```

Principal-level concerns:

```text
pool size
idle timeout
stale connections
max connection lifetime
server limits
backpressure
load distribution
```

---

# 41. Timeouts

Never design a distributed network call with an accidental infinite wait.

Know:

```text
DNS timeout
connect timeout
TLS handshake timeout
request/read timeout
write timeout
idle timeout
overall deadline
```

Principal principle:

> Prefer propagating an overall request deadline across downstream calls rather than giving every dependency an independent large timeout.

Example:

```text
API total budget = 2 sec

Service A       300 ms
Service B       500 ms
DB              400 ms
retry budget    bounded
```

---

# 42. Retries

Retries help with transient failures.

But retries can make overload dramatically worse.

Bad:

```text
1000 clients
 × 3 retries
 = potentially 3000 additional attempts
```

Use:

```text
bounded retries
exponential backoff
jitter
deadline awareness
idempotency
retry only appropriate errors
```

Principal-level phrase:

> Retries are a load amplifier, so they need a retry budget and backoff.

---

# 43. Idempotency and Networking

A timeout does **not** mean the server did not execute the request.

Example:

```text
Client -> POST payment
Server executes payment
Response gets lost
Client times out
```

Blind retry could execute the operation twice.

Solutions include:

```text
idempotency key
request ID
deduplication
idempotent operation semantics
```

This is a key distributed-systems/network boundary question.

---

# 44. Keep-Alive

Two different ideas are often called keep-alive.

## HTTP persistent connection

Reuse a transport connection for multiple HTTP requests.

## TCP keepalive

Kernel probes an otherwise idle TCP connection to detect dead peers under configured conditions.

Do not confuse them.

---

# 45. Backpressure

If consumers are slower than producers:

```text
Producer >>> Consumer
```

Buffers eventually fill.

Without backpressure:

```text
memory growth
queue growth
latency explosion
timeouts
OOM
cascading failures
```

Solutions:

```text
bounded queues
flow control
rate limiting
load shedding
consumer-driven demand
concurrency limits
```

---

# 46. Latency vs Throughput

## Latency

Time for an operation.

```text
Request = 20 ms
```

## Throughput

Amount of work per unit time.

```text
10,000 requests/sec
1 Gbit/sec
```

A system can have:

```text
high throughput + poor latency
```

or:

```text
low latency + limited throughput
```

For networked services, discuss p50/p95/p99 rather than only average latency.

---

# 47. Bandwidth vs Latency

Bandwidth:

```text
how much data per second can be transferred
```

Latency:

```text
how long data/request takes to travel/complete
```

A high-bandwidth network can still have high latency.

Example:

```text
1 Gbps connection
100 ms RTT
```

For long-distance high-throughput TCP flows, the bandwidth-delay product becomes important.

---

# 48. MTU

MTU = Maximum Transmission Unit.

Common Ethernet MTU:

```text
1500 bytes
```

If packets exceed what a path can carry, fragmentation or packet-too-big/path-MTU behavior becomes relevant depending on IP version/configuration.

Problems can appear as:

```text
small requests work
large transfers stall/fail
VPN/tunnel-specific failures
```

Useful:

```bash
ip link
tracepath host
```

---

# 49. TCP MSS

MSS = Maximum Segment Size.

It represents the maximum TCP payload a peer says it can receive in a segment.

For common IPv4 Ethernet without options:

```text
MTU 1500
- IPv4 header 20
- TCP header 20
≈ MSS 1460
```

Actual values vary with IPv6, TCP options, tunnels, etc.

---

# 50. SYN Backlog / Accept Queue

A busy TCP server has kernel-managed connection queues.

Conceptually:

```text
incoming SYNs
   ↓
handshake/incomplete connection state
   ↓
completed connections waiting for accept()
   ↓
application accept()
```

If the application cannot accept quickly enough or queue limits are reached, new connection establishment can suffer.

Useful investigation:

```bash
ss -lnt
netstat -s
```

Exact queue behavior and limits are OS/version dependent, so avoid oversimplifying it as one single "backlog queue."

---

# 51. Ephemeral Port Exhaustion

A client initiating many outbound connections needs local ephemeral ports.

Example:

```text
10.0.0.5:40001 -> server:443
10.0.0.5:40002 -> server:443
...
```

Very high connection churn can contribute to port exhaustion, especially with NAT/proxies and many connections to the same destination.

Mitigations:

```text
connection reuse/pooling
HTTP/2 multiplexing
reasonable connection lifetime
capacity planning
```

Diagnose:

```bash
ss -s
cat /proc/sys/net/ipv4/ip_local_port_range
```

---

# 52. DNS Caching and TTL

DNS records have TTLs.

Caching improves:

```text
latency
DNS scalability
availability during short resolver issues
```

But creates deployment/failover considerations.

If an IP changes:

```text
some clients may continue using cached records until TTL expiry
```

Principal topics:

```text
TTL strategy
DNS failover
client caching behavior
JVM/application caches
load balancing via DNS
```

---

# 53. Kubernetes Networking — Interview Basics

Since Principal infrastructure roles often touch Kubernetes, know this flow:

```text
Client
  ↓
Load Balancer / Ingress
  ↓
Service
  ↓
Pod
```

Concepts:

```text
Pod IP
Service ClusterIP
Ingress/Gateway
DNS
NetworkPolicy
CNI
kube-proxy / dataplane implementation
```

Debugging examples:

```bash
kubectl get pods -o wide
kubectl get svc
kubectl get endpoints
kubectl describe svc <name>
kubectl exec -it <pod> -- curl ...
kubectl exec -it <pod> -- nslookup ...
```

Ask:

```text
Does DNS resolve?
Does Service have endpoints?
Can source Pod connect directly to target Pod IP?
Can it connect through Service?
Is NetworkPolicy blocking it?
Is ingress/load balancer healthy?
```

---

# 54. C++ Networking Design Questions

At Principal level, expect more than API syntax.

## Question: Design a high-performance TCP server.

Discuss:

```text
non-blocking sockets
epoll/event loop
worker/thread model
connection ownership
buffer management
protocol framing
partial reads/writes
timeouts
backpressure
bounded queues
connection limits
TLS
observability
graceful shutdown
load shedding
```

## Question: One thread per connection or event-driven?

Answer:

Thread-per-connection:

```text
simple
easy blocking code
can be reasonable for modest concurrency
```

Event-driven:

```text
handles many connections efficiently
less thread/context-switch overhead
more complex state management
```

Modern architecture can combine:

```text
small number of event loops
+
worker pool for CPU/blocking work
```

---

# 55. Buffer Management in C++ Network Servers

Avoid blindly allocating huge buffers per connection.

For 1 million connections:

```text
1 MB/connection
= ~1 TB theoretical buffer memory
```

Consider:

```text
bounded buffers
buffer pools
ring buffers
zero/minimal-copy techniques where justified
scatter/gather I/O
readv/writev
sendfile for suitable file transfer paths
```

Principal-level tradeoff:

> Optimize copying only after profiling. Correct ownership, bounded memory, and backpressure usually matter before exotic zero-copy techniques.

---

# 56. SIGPIPE in Linux Socket Programming

Writing to a closed socket may cause `SIGPIPE` on Unix-like systems.

Possible handling patterns include:

```text
ignore SIGPIPE
MSG_NOSIGNAL on send() where available
platform-specific socket options
```

Otherwise the process may be terminated by the signal depending on configuration.

This is a useful low-level C++/Linux detail.

---

# 57. Graceful Server Shutdown

Do not just kill a production server immediately.

Typical strategy:

```text
stop accepting new traffic
mark instance unhealthy / drain load balancer
allow in-flight requests to finish
enforce maximum drain deadline
close connections/resources
exit
```

For long-lived connections, define explicit draining behavior.

---

# 58. Observability for Networked Services

Metrics:

```text
request rate
error rate
latency p50/p95/p99
active connections
connection establishment failures
timeouts
retries
resets
bytes sent/received
queue depth
DNS latency/failures
TLS failures
```

Logs:

```text
request ID / trace ID
source/destination
error category
latency
upstream
retry count
```

Tracing:

```text
Client
  -> API
      -> Service A
          -> DB
```

Distributed tracing helps identify which network/service hop consumed latency.

---

# 59. Principal-Level Failure Scenario

Question:

> p99 latency suddenly increases but CPU is only 30%. What do you investigate?

Do not assume CPU bottleneck.

Check:

```text
network RTT
packet loss/retransmissions
DNS latency
connection pool saturation
TCP connection churn
TLS handshake rate
upstream latency
thread pool saturation
queueing
lock contention
disk/database
load balancer behavior
GC where relevant
timeouts/retries
```

Key point:

> Low CPU does not mean the system has spare capacity; it may be blocked on network I/O or another constrained dependency.

---

# 60. Packet Loss

Packet loss can cause:

```text
TCP retransmissions
increased latency
reduced congestion window
throughput degradation
timeouts
```

Investigate with:

```bash
ping
ss -ti
netstat -s
tcpdump
Wireshark
ethtool -S <interface>
ip -s link
```

`ss -ti` can expose useful TCP internal information depending on the platform/kernel.

---

# 61. DNS Failure Scenario

Question:

> Application cannot connect using hostname but IP works.

Approach:

```text
1. getent hosts hostname
2. dig hostname
3. inspect /etc/resolv.conf or resolver configuration
4. check DNS server reachability
5. compare application/container resolver environment
6. inspect search domains / ndots if Kubernetes
7. check cached/stale records
```

Likely layer:

```text
name resolution
```

not TCP itself.

---

# 62. TLS Failure Scenario

Symptoms:

```text
TCP connection succeeds
HTTPS fails
```

Check:

```bash
openssl s_client -connect host:443 -servername host
curl -v https://host
```

Possible causes:

```text
expired certificate
hostname mismatch
missing intermediate
untrusted CA
unsupported TLS/cipher configuration
SNI issue
mTLS client certificate missing
clock incorrect
```

---

# 63. HTTP 503 vs Network Failure

`503 Service Unavailable` means:

```text
you successfully communicated far enough to receive an HTTP response
```

Therefore DNS/TCP/TLS likely worked to at least the responding HTTP endpoint.

Now investigate:

```text
server overload
maintenance
load balancer has no healthy backend
dependency unavailable
rate/concurrency controls
```

This distinction is excellent in troubleshooting interviews.

---

# 64. Networking Commands — Interview Cheat Sheet

```bash
# Interface / IP
ip addr
ip link

# Route
ip route
ip route get <IP>

# Neighbor/ARP
ip neigh

# DNS
dig <host>
nslookup <host>
getent hosts <host>

# Reachability
ping <host>

# Path
traceroute <host>
tracepath <host>

# Sockets
ss -lntp
ss -lunp
ss -tan
ss -s

# Port connectivity
nc -vz <host> <port>

# HTTP/HTTPS
curl -v https://<host>
curl -I https://<host>

# TLS
openssl s_client -connect <host>:443 -servername <host>

# Packet capture
tcpdump -nn -i any host <IP>
tcpdump -nn -i any port 443

# Process using port
lsof -i :<port>

# Interface statistics
ip -s link
ethtool <interface>
ethtool -S <interface>
```

---

# 65. Commands: What Each One Proves

This is more important than memorizing command names.

| Command | Helps answer |
|---|---|
| `ip addr` | What IP/interface configuration do I have? |
| `ip route` | Where will packets be routed? |
| `ip neigh` | Can I resolve local next-hop neighbor info? |
| `dig` | What does DNS return? |
| `getent hosts` | What does the OS/application-style resolver return? |
| `ping` | Is ICMP reachability available and what is RTT/loss? |
| `traceroute` | What path/hops are visible? |
| `ss` | What sockets/listeners/connections exist? |
| `nc` | Can I establish basic TCP connectivity to this port? |
| `curl -v` | Does DNS + connection + TLS + HTTP work? |
| `openssl s_client` | What is happening in TLS/certificate negotiation? |
| `tcpdump` | What packets actually crossed the interface? |

---

# 66. Interview: "Have You Worked on Networking in C++?"

Do not undersell yourself just because you have not built a TCP/IP stack.

A strong framing is:

> My primary C++ work has been systems software rather than implementing network protocols themselves. I have worked extensively on Linux systems, service communication, cloud infrastructure, authentication, distributed components and production debugging, so I am comfortable reasoning across DNS, TCP/TLS, HTTP and service connectivity. At the C++ level, I understand the socket programming model—socket/bind/listen/accept/connect, partial I/O, framing, blocking versus non-blocking I/O, and Linux mechanisms such as epoll. I would distinguish that from claiming that I spent years developing a networking stack or high-performance network library.

This is accurate and still Principal-level.

---

# 67. Questions You Should Be Able to Answer

## Fundamentals

1. What is an IP address?
2. What is a port?
3. What is a socket?
4. TCP vs UDP?
5. What is a TCP 3-way handshake?
6. Why is it 3-way?
7. What is a sequence number?
8. What is an ACK?
9. What happens when a packet is lost?
10. Flow control vs congestion control?
11. What is RTT?
12. What is MTU?
13. What is MSS?
14. What is NAT?
15. What is ARP?
16. What is ICMP?

## Web

17. What happens when you type a URL?
18. How does DNS work?
19. What happens during TLS handshake?
20. How is a certificate validated?
21. HTTP vs HTTPS?
22. HTTP/1.1 vs HTTP/2 vs HTTP/3?
23. What is keep-alive?
24. What is SNI?
25. What is ALPN?
26. 502 vs 503 vs 504?

## C++ / Linux

27. Explain socket → bind → listen → accept.
28. What does `accept()` return?
29. Does one `send()` correspond to one `recv()`?
30. How do you frame TCP messages?
31. What are partial writes?
32. Blocking vs non-blocking sockets?
33. select vs poll vs epoll?
34. Edge-triggered vs level-triggered?
35. What is `TCP_NODELAY`?
36. What is `SO_KEEPALIVE`?
37. What is network byte order?
38. How would you design a server for 100K connections?

## Debugging

39. How do you debug "server unreachable"?
40. `ping` works but application doesn't. Why?
41. DNS works but TCP connect times out. What next?
42. IP works but hostname does not.
43. TCP works but HTTPS fails.
44. What does connection refused mean?
45. Timeout vs reset?
46. How do you check whether a port is listening?
47. How do you capture packets?
48. How do you inspect TLS?
49. How do you find the route to a destination?
50. How do you debug packet loss?

## Principal / System Design

51. Why use connection pooling?
52. How should retries be designed?
53. Why is exponential backoff not enough without jitter?
54. Why are deadlines important?
55. What is backpressure?
56. How can retries cause cascading failure?
57. L4 vs L7 load balancer?
58. Forward vs reverse proxy?
59. What causes p99 network latency?
60. How do you gracefully drain a server?
61. How do you monitor a network service?
62. What happens during ephemeral-port exhaustion?
63. How would you troubleshoot a Kubernetes service that is unreachable?
64. How do DNS TTLs affect failover?

---

# 68. Seven-Day Interview Preparation Plan

## Day 1 — End-to-End Fundamentals

Study:

```text
OSI/TCP-IP mental model
IP
port
socket
MAC
ARP
gateway
routing
NAT
```

Target:

> Explain how a packet gets from process A to process B.

Practice:

```bash
ip addr
ip route
ip neigh
ping
```

---

## Day 2 — TCP Deep Dive

Study:

```text
3-way handshake
sequence/ACK
retransmission
flow control
congestion control
FIN/RST
TIME_WAIT
keepalive
MSS/MTU
```

Practice:

```bash
ss -tan
ss -ti
tcpdump
```

Target:

> Draw TCP connection setup and teardown on a whiteboard.

---

## Day 3 — DNS + HTTP

Study:

```text
DNS resolution
A/AAAA/CNAME
TTL
HTTP methods
status codes
HTTP keep-alive
HTTP/1.1
HTTP/2
HTTP/3
```

Practice:

```bash
dig
getent hosts
curl -v
```

Target:

> Explain what happens after typing google.com.

---

## Day 4 — HTTPS/TLS

Study:

```text
TLS handshake
certificate
CA
chain
public/private keys
symmetric encryption
SNI
ALPN
mTLS
```

Practice:

```bash
openssl s_client
curl -v
```

Target:

> Explain how HTTPS establishes trust and encryption.

---

## Day 5 — C++ Socket Programming

Study:

```text
socket
bind
listen
accept
connect
send
recv
close
partial I/O
framing
blocking/non-blocking
select/poll/epoll
```

Write:

```text
TCP echo server
TCP client
length-prefixed protocol
```

Target:

> Explain how you would build a scalable C++ TCP server.

---

## Day 6 — Debugging

Memorize workflow:

```text
application
↓
DNS
↓
route
↓
TCP
↓
TLS
↓
HTTP
↓
backend
```

Practice intentionally breaking:

```text
wrong hostname
wrong port
server stopped
bad certificate
firewall rule if safe in a lab
```

Then diagnose with:

```text
dig
ss
nc
curl
openssl
tcpdump
```

---

## Day 7 — Principal-Level Scenarios

Study:

```text
load balancers
proxies
connection pools
timeouts
deadlines
retries
backoff+jitter
idempotency
backpressure
rate limiting
observability
Kubernetes networking
failure isolation
```

Practice 10 whiteboard scenarios.

---

# 69. Best Answering Framework for Principal Interviews

When asked a networking question, structure the answer in layers.

Example:

> "Service cannot connect. What will you do?"

Say:

```text
1. Clarify symptom and scope.
2. Verify destination/configuration.
3. Verify DNS.
4. Verify routing/interface.
5. Verify TCP connectivity.
6. Verify server listener.
7. Verify TLS.
8. Verify application protocol.
9. Capture packets if still ambiguous.
10. Check firewall/LB/Kubernetes/network policy.
11. Correlate metrics/logs/traces and recent changes.
```

Then explain what each observation would prove.

That sounds much stronger than listing random Linux commands.

---

# 70. Whiteboard Diagram to Memorize

```text
Browser / Client
      |
      | DNS query
      v
DNS Resolver
      |
      | IP
      v
Client
      |
      | route / gateway
      v
Network
      |
      | TCP handshake (HTTP/1.1 or HTTP/2)
      v
Server :443
      |
      | TLS handshake
      v
Encrypted connection
      |
      | HTTP request
      v
LB / Reverse Proxy
      |
      v
Application
      |
      v
Dependencies
```

For HTTP/3:

```text
HTTP/3 -> QUIC -> UDP
```

---

# 71. What NOT to Spend Too Much Time On Initially

For most Principal C++/systems interviews, initially deprioritize:

```text
memorizing every TCP header bit
BGP implementation internals
OSPF algorithms in depth
switch ASIC internals
advanced SDN protocols
writing a TCP stack
deep cryptographic mathematics
```

Unless the role is specifically:

```text
networking infrastructure
router/switch software
kernel networking
DPDK
NIC drivers
telecom
network security
```

Your priority is strong systems-level networking reasoning.

---

# 72. Recommended Depth for Your Profile

Given a senior C++/Linux/cloud/distributed-systems background, aim for:

```text
TCP/IP fundamentals          ██████████
TCP troubleshooting          ██████████
HTTP/HTTPS/TLS               ██████████
Linux network commands       ██████████
C++ sockets                  █████████
epoll/non-blocking I/O       ████████
DNS                          ████████
Load balancing/proxies       ████████
Kubernetes networking        ███████
UDP/QUIC                     ██████
Routing/subnetting           ██████
BGP/OSPF internals           ███
```

You do not need to pretend to be a network engineer. You need to be a Principal systems engineer who can reason about the network as part of an end-to-end system.

---

# 73. The 10 Topics to Learn First

If time is limited, master these in this exact order:

1. **What happens when you type a URL**
2. **TCP vs UDP**
3. **TCP handshake + teardown**
4. **TCP reliability, flow control, congestion control**
5. **DNS**
6. **HTTP vs HTTPS + TLS**
7. **C++ sockets: socket/bind/listen/accept/connect/send/recv**
8. **Blocking/non-blocking + epoll**
9. **Linux debugging commands and a layered debugging workflow**
10. **Timeouts, retries, load balancers, proxies, connection pooling, backpressure**

Once these are comfortable, move to MTU/MSS, NAT, Kubernetes networking, QUIC, and performance tuning.

---

# 74. One-Minute Revision Sheet

```text
IP       -> routes packets between hosts/networks
Port     -> identifies transport endpoint/service
Socket   -> OS abstraction for communication

TCP      -> reliable ordered byte stream
UDP      -> datagrams, no transport delivery/order guarantee

TCP open -> SYN, SYN-ACK, ACK
TCP close-> FIN/ACK in each direction; RST = abrupt reset

DNS      -> hostname to records/IP
ARP      -> IPv4 address to MAC on local link
NAT      -> rewrites addresses/ports
ICMP     -> control/error messages; ping uses echo

HTTP     -> application request/response semantics
HTTPS    -> HTTP protected by TLS
TLS      -> confidentiality + integrity + authentication

Server:
socket -> bind -> listen -> accept -> recv/send -> close

Client:
socket -> connect -> send/recv -> close

TCP is a byte stream:
send boundaries != recv boundaries

Linux:
ip addr
ip route
ip neigh
dig/getent
ping
traceroute
ss
nc
curl
openssl
tcpdump

Debug:
config -> DNS -> route -> TCP -> TLS -> HTTP -> backend

Principal:
timeouts
deadlines
retries + backoff + jitter
idempotency
pooling
backpressure
load balancing
observability
```

---

# 75. Final Interview Principle

For a Principal Engineer, the interviewer is rarely testing whether you memorized `tcpdump` syntax.

They are testing whether you can answer:

```text
Where can this fail?
How will you isolate the failing layer?
What evidence will you collect?
What happens under load?
What happens during partial failure?
How will the system recover?
How will you prevent recurrence?
How will you observe it in production?
```

Build every networking answer around those questions.
