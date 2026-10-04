# IBM Cloud Bare-Metal Provisioning on IBM Z / LinuxONE

## HLD, Provisioning Flow, Kubernetes Controller Design, Reliability and Director-Round Interview Notes

> **Interview positioning:** This project can be presented as an
> **event-driven Kubernetes control plane for automating bare-metal
> lifecycle and image provisioning on IBM Z / LinuxONE**, implemented
> using Go-based controllers.

------------------------------------------------------------------------

# 1. Problem Statement

Bare-metal provisioning is significantly different from creating a VM. A
provisioning request may involve:

-   selecting a physical IBM Z / LinuxONE server,
-   resolving the requested operating-system image,
-   preparing storage,
-   exposing the image through NFS,
-   configuring export policies,
-   selecting an eligible service node,
-   creating a provisioning workload,
-   transferring/deploying the image to the target server,
-   monitoring a long-running operation,
-   handling partial failures,
-   updating the final server state.

The goal was therefore not simply to expose a REST API that executes a
long synchronous procedure. The architecture needed a reliable control
plane capable of converging the infrastructure toward a user's **desired
state**.

The core model was:

``` text
Desired State
     |
     v
Kubernetes Resources / CRDs
     |
     v
Go Controllers
     |
     v
Reconciliation
     |
     +---- Observe current state
     |
     +---- Determine required action
     |
     +---- Execute / delegate action
     |
     +---- Update status
     |
     +---- Requeue when required
```

A useful way to summarize the architecture in an interview is:

> **Kubernetes stores the desired and observed state, Go controllers
> continuously reconcile it, and external infrastructure components
> perform the actual storage and bare-metal operations.**

------------------------------------------------------------------------

# 2. Original Project Flow Diagram

The following is the original/raw architecture and provisioning-flow
diagram used as the basis for this discussion.

![IBM Cloud Bare-Metal Provisioning
Flow](./IBM-Cloud-BareMetal-Provisioning-Flow.png)

The diagram contains both regional and zonal resources and shows the
interaction among:

-   Image
-   ZonalImage
-   StorageVolume
-   ExportPolicy
-   ExportPolicyRule
-   BareMetalSpec
-   BareMetalServer
-   `bm-server-controller`
-   ProvisionServerAction
-   `bm-server-manager`
-   Fleet Manager REST server
-   Provisioning Pod
-   service node
-   NetApp/NFS storage
-   target bare-metal server

------------------------------------------------------------------------

# 3. Simplified High-Level Architecture

For an interview whiteboard, simplify the raw implementation diagram
into this:

``` text
                         User / Cloud API
                                |
                                v
                      +--------------------+
                      | Kubernetes API     |
                      | CRDs / Resources   |
                      +---------+----------+
                                |
                         Desired State
                                |
              +-----------------+------------------+
              |                 |                  |
              v                 v                  v
     +----------------+ +----------------+ +----------------+
     | Bare Metal     | | Server Action  | | Dev/Provision |
     | Controller     | | Controller     | | Controllers    |
     |      Go        | |      Go        | |      Go        |
     +-------+--------+ +-------+--------+ +-------+--------+
             |                  |                  |
             +------------------+------------------+
                                |
                                v
                     Reconciliation / Workflow
                                |
                  +-------------+--------------+
                  |                            |
                  v                            v
          Storage Integration          Bare Metal Manager
                  |                            |
                  v                            v
          NetApp / NFS                 Fleet Manager API
                                               |
                                               v
                                         Service Node
                                               |
                                               v
                                      Provisioning Pod
                                         /         \
                                        /           \
                                       v             v
                                NFS Image       Target Server
                                                     |
                                                     v
                                            IBM Z / LinuxONE
```

------------------------------------------------------------------------

# 4. Logical Architecture Layers

The system can be explained in four layers.

``` text
+------------------------------------------------------+
| 1. API / Desired-State Layer                         |
|                                                      |
| BareMetalSpec / BareMetalServer / Image / Actions   |
+--------------------------+---------------------------+
                           |
                           v
+------------------------------------------------------+
| 2. Controller / Orchestration Layer                  |
|                                                      |
| Bare Metal Controller                               |
| Provisioning / DevProvisioning Controller           |
| Server Action Controller                            |
| Pod / Job Management                                |
+--------------------------+---------------------------+
                           |
                           v
+------------------------------------------------------+
| 3. Infrastructure Integration Layer                  |
|                                                      |
| Storage Controllers / NetApp / NFS                  |
| Bare Metal Manager                                  |
| Fleet Manager                                       |
+--------------------------+---------------------------+
                           |
                           v
+------------------------------------------------------+
| 4. Physical Execution Layer                          |
|                                                      |
| Service Nodes -> Provisioning Pods -> Target Server |
|                     IBM Z / LinuxONE                 |
+------------------------------------------------------+
```

This separation is useful because the Kubernetes controller should
orchestrate infrastructure rather than directly contain every
implementation detail for storage, image transfer, hardware management,
and pod execution.

------------------------------------------------------------------------

# 5. Main Domain Resources

## 5.1 Image

Represents an imported operating-system or machine image.

``` text
Image
  |
  | projected
  v
ZonalImage
```

The image is logically available at a broader scope, while the zonal
representation connects it to infrastructure available in a particular
zone.

------------------------------------------------------------------------

## 5.2 BareMetalSpec

Represents the requested/desired bare-metal configuration.

Conceptually it may contain information such as:

``` text
BareMetalSpec
    |
    +-- image reference
    +-- hardware/server requirements
    +-- zone
    +-- networking information
    +-- provisioning configuration
```

The important design principle is that the client specifies **what it
wants**, rather than explicitly orchestrating every provisioning step.

------------------------------------------------------------------------

## 5.3 BareMetalServer

Represents the actual server instance whose lifecycle is being managed.

``` text
BareMetalSpec
       |
       v
BareMetalServer
       |
       +-- ZonalImage reference
       +-- physical server identity
       +-- provisioning state
       +-- observed status
```

The server controller watches/reconciles this resource.

------------------------------------------------------------------------

## 5.4 StorageVolume

Represents storage information associated with the image.

The controller can use it to resolve information such as:

``` text
NFS host
NFS export path
volume identity
image location
```

------------------------------------------------------------------------

## 5.5 ExportPolicy and ExportPolicyRule

These resources control which nodes are permitted to access the NFS
image.

``` text
ExportPolicy
      |
      v
ExportPolicyRule
      |
      v
Allowed service/provisioning nodes
```

This separates image storage from storage-access policy.

------------------------------------------------------------------------

## 5.6 ProvisionServerAction

Represents a long-running provisioning operation.

Instead of making the `BareMetalServer` controller perform the complete
provisioning workflow synchronously:

``` text
BareMetalServer
      |
      v
Server Controller
      |
      v
ProvisionServerAction
      |
      v
Execution / Manager Layer
```

This is an important separation between **desired server lifecycle** and
**execution of a long-running action**.

------------------------------------------------------------------------

# 6. Regional and Zonal Design

The original diagram explicitly separates regional and zonal resources.

Conceptually:

``` text
             REGIONAL
---------------------------------

Image

BareMetalSpec


          Projection /
           Reference
               |
               v

              ZONAL
---------------------------------

ZonalImage

BareMetalServer

Service Nodes

Provisioning Pod

Physical Bare Metal
```

Physical infrastructure exists in a specific location/zone. A
higher-level resource can represent user intent while zonal resources
represent the infrastructure required to realize that intent.

Advantages include:

-   locality-aware provisioning,
-   failure isolation,
-   clearer infrastructure ownership,
-   zone-specific storage and service-node selection,
-   separation between API abstraction and physical realization.

------------------------------------------------------------------------

# 7. End-to-End Provisioning Flow

The raw diagram can be explained as the following logical flow.

------------------------------------------------------------------------

## Step 1 - Import the Image

An image enters the system:

``` text
Image Import
     |
     v
   Image
     |
     v
 ZonalImage
```

Associated storage resources can represent:

``` text
Image
  |
  +--> ZonalImage
  |
  +--> StorageVolume
  |
  +--> ExportPolicy
  |
  +--> ExportPolicyRule
```

The actual image bytes reside in storage while Kubernetes resources
represent metadata and desired/observed state.

------------------------------------------------------------------------

## Step 2 - BareMetalSpec References the Image

A provisioning request identifies the desired image.

``` text
BareMetalSpec
       |
       | image reference
       v
     Image
```

Conceptually:

``` text
"I need a bare-metal server
 in zone Z
 using image X
 with configuration Y."
```

The caller should not have to manually coordinate NFS, service nodes,
pods, or image copying.

------------------------------------------------------------------------

## Step 3 - Create / Project BareMetalServer

The desired specification results in a server resource.

``` text
BareMetalSpec
       |
       v
BareMetalServer
       |
       v
ZonalImage
```

The `BareMetalServer` now represents the desired and observed lifecycle
of the target machine.

------------------------------------------------------------------------

## Step 4 - Bare-Metal Server Controller Reconciles

The Go controller follows the Kubernetes reconciliation model.

``` text
Resource event
     |
     v
Work Queue
     |
     v
Reconcile()
     |
     v
Read Desired State
     |
     v
Read Observed State
     |
     v
Desired == Observed?
    /            \
  Yes             No
   |               |
Return       Determine action
                   |
                   v
             Execute/delegate
                   |
                   v
              Update Status
                   |
                   v
                 Requeue
```

A useful mental model is:

``` text
Desired State - Observed State = Reconciliation Work
```

The controller is not just an event handler. Events cause
reconciliation, but the resource state determines what should happen.

------------------------------------------------------------------------

## Step 5 - Resolve NFS / Storage Information

From the original design:

``` text
bm-server-controller
        |
        | Read NFS information
        v
   StorageVolume
```

The provisioning workflow needs enough information to locate the
requested image:

``` text
NFS hostname
export path
volume
image path
access policy
```

------------------------------------------------------------------------

## Step 6 - Determine Eligible Service Nodes

Provisioning is performed through suitable service infrastructure.

``` text
Service Nodes
      |
      v
Filter Eligible Nodes
      |
      v
Selected Service Node
```

Eligibility can be based on architecture and deployment-specific
properties such as:

``` text
zone
health
labels
capacity
role
availability
```

The raw design shows a service-node label similar to:

``` text
genctl.role.service = "true"
```

This allows provisioning workloads to be scheduled onto appropriate
service nodes rather than arbitrary Kubernetes workers.

------------------------------------------------------------------------

## Step 7 - Create ProvisionServerAction

The controller creates an explicit action representing the long-running
provisioning operation.

``` text
BareMetalServer
       |
       v
bm-server-controller
       |
       v
ProvisionServerAction
```

This separation provides a clean responsibility boundary:

``` text
Server Controller:
"What lifecycle transition is required?"

Action / Manager Layer:
"How is that operation executed?"
```

------------------------------------------------------------------------

## Step 8 - Bare-Metal Manager Processes the Action

Conceptually:

``` text
ProvisionServerAction
         |
         v
  bm-server-manager
         |
         | POST /provision
         v
 fleetman-rest-server
```

The request can include the information needed by the provisioning
infrastructure, such as:

``` text
target server
NFS hostname
NFS image path
image metadata
provisioning parameters
```

------------------------------------------------------------------------

## Step 9 - Create Provisioning Pod

Fleet/provisioning infrastructure creates a workload on an eligible
service node.

``` text
Fleet Manager
      |
      v
Create Provisioning Job / Pod
      |
      v
+--------------------------------+
| Service Node                   |
|                                |
|     Provisioning Pod           |
|                                |
|     NFS volume mounted         |
+---------------+----------------+
                |
                v
          Image accessible
```

This is an important architectural decision.

The controller remains a lightweight control-plane component, while the
actual image-transfer operation executes as an isolated Kubernetes
workload.

------------------------------------------------------------------------

## Step 10 - Provision the Target IBM Z / LinuxONE Server

The provisioning pod accesses the image through NFS and deploys/copies
it to the target bare-metal server.

``` text
       NetApp / NFS
            |
            | mounted image
            v
     Provisioning Pod
            |
            | deploy / copy image
            v
 Target Bare-Metal Server
            |
            v
     IBM Z / LinuxONE
```

After completion, the result is reflected back into resource status.

Conceptually:

``` text
Requested
    |
    v
Preparing
    |
    v
StorageReady
    |
    v
Provisioning
    |
    v
ImageDeployment
    |
    v
Verification
    |
    v
Ready
```

Failures can transition to retryable or terminal states.

------------------------------------------------------------------------

# 8. Why Kubernetes Controllers Were a Good Fit

## Declarative Desired State

Instead of requiring a caller to issue:

``` text
Create volume
Configure NFS
Create export rule
Find service node
Create pod
Copy image
Check physical server
Update database
```

the caller declares:

``` text
I want Server A
using Image B
in Zone C.
```

Controllers determine how to reach that state.

------------------------------------------------------------------------

## Self-Healing Control Plane

If a controller process dies:

``` text
Controller crashes
      |
      v
Kubernetes restarts controller
      |
      v
Controller reads persisted resources
      |
      v
Reconcile()
      |
      v
Continue from observed state
```

Correctness should therefore not depend on an in-memory workflow
variable surviving for hours.

------------------------------------------------------------------------

## Eventual Consistency

External systems do not change atomically.

For example:

``` text
Storage ready        = yes
Provisioning action  = yes
Pod running          = yes
Physical server      = still provisioning
```

The controller repeatedly observes the system and converges it toward
the desired state.

------------------------------------------------------------------------

# 9. Critical Design Requirement - Idempotency

Reconciliation can execute multiple times for the same logical request.

Consider:

``` text
Controller
     |
     | Create provisioning job
     v
Kubernetes API
     |
     +---- creation succeeds

Controller crashes before recording next step.
```

After restart:

``` text
Reconcile()
```

A naive implementation could create a second provisioning job.

The safer pattern is:

``` text
Does deterministic provisioning action/job exist?
              |
          +---+---+
          |       |
         Yes      No
          |       |
          v       v
      Observe    Create
      existing   exactly once logically
      resource
```

The key principle:

> **Observe before acting. Repeated reconciliation should converge
> toward the same desired result rather than duplicate side effects.**

For external APIs, use stable request/action identity where possible so
retries can also be correlated or deduplicated.

------------------------------------------------------------------------

# 10. Biggest Probable Challenge

## Reliable Orchestration of a Long-Running Distributed Bare-Metal Workflow

A strong Director-round challenge is:

> **The biggest challenge was making a long-running provisioning
> workflow reliable when it crossed Kubernetes, storage/NFS, service
> nodes, provisioning pods, external management APIs, and finally
> physical hardware.**

The operation is not transactional across all these systems.

Any component can fail independently:

``` text
Kubernetes API unavailable

Controller restart

NFS temporarily unavailable

Export policy not yet applied

Fleet Manager timeout

No eligible service node

Provisioning pod failure

Network interruption

Target server unavailable

Physical provisioning failure
```

Therefore the operation cannot safely be implemented as:

``` text
function provisionServer() {
    step1();
    step2();
    step3();
    step4();
    step5();
}
```

with progress stored only in memory.

Instead, model it as a persisted state-driven workflow.

``` text
Requested
    |
    v
StorageResolved
    |
    v
ActionCreated
    |
    v
ProvisioningStarted
    |
    v
ImageInstalled
    |
    v
Ready
```

With failure handling:

``` text
                     +--> Retryable Failure
                     |        |
                     |        v
Provisioning --------+     Backoff
                     |        |
                     |        v
                     |     Reconcile
                     |
                     +--> Terminal Failure
                     |
                     +--> Ready
```

### Interview answer

> "One of the biggest challenges was reliable orchestration because
> bare-metal provisioning was a long-running distributed workflow rather
> than one atomic operation. It crossed Kubernetes resources, storage
> and NFS, service nodes, provisioning pods, management services and
> physical LinuxONE hardware. Any component could fail or the controller
> itself could restart midway.
>
> We therefore relied on reconciliation and persisted resource state
> instead of keeping the workflow only in controller memory. Operations
> had to be idempotent. After restart, the controller could determine
> whether storage was ready, whether an action or provisioning pod
> already existed, and whether the target was still provisioning, and
> then continue from the observed state rather than starting again.
>
> We also needed to distinguish transient errors from terminal failures
> and apply controlled retries. That made the system eventually
> consistent and resilient to partial failures."

------------------------------------------------------------------------

# 11. Retry and Failure Classification

Not all failures should be treated equally.

``` text
Failure
   |
   +--> Transient
   |       |
   |       +--> API timeout
   |       +--> NFS temporary failure
   |       +--> temporary service-node shortage
   |       |
   |       v
   |    Retry / Backoff
   |
   +--> Terminal
           |
           +--> invalid image
           +--> invalid server configuration
           +--> unsupported operation
           |
           v
        Mark Failed
```

For retryable failures:

``` text
retry
  |
  +--> wait
  |
  +--> reconcile again
```

Exponential backoff with limits/jitter avoids aggressive retry storms.

Most importantly:

> **Retries must be idempotent.**

------------------------------------------------------------------------

# 12. Controller Responsibility Separation

Avoid one monolithic controller.

A cleaner decomposition is:

``` text
Image / Storage Controllers
       |
       +--> image and storage lifecycle

BareMetal Server Controller
       |
       +--> desired server lifecycle

Server Action Controller
       |
       +--> provision / deprovision / server operations

DevProvisioning Controller
       |
       +--> specialized provisioning workflow

Pod / Job Management
       |
       +--> execution workload lifecycle
```

Benefits:

-   clear ownership,
-   smaller reconciliation loops,
-   independent testing,
-   easier failure isolation,
-   easier evolution,
-   fewer unrelated side effects in one controller.

------------------------------------------------------------------------

# 13. Control Plane vs Data Plane

This is useful in a Principal/Director discussion.

``` text
CONTROL PLANE
------------------------------------------------

Kubernetes Resources
Go Controllers
Bare Metal Manager
Fleet Manager orchestration

Determines:
"What should happen?"


DATA / EXECUTION PLANE
------------------------------------------------

NFS / NetApp
Service Node
Provisioning Pod
Physical Server

Performs:
"The actual image provisioning operation"
```

The controller should not copy a huge image itself. It should
orchestrate a workload designed for that task.

------------------------------------------------------------------------

# 14. Why Go Was a Good Choice

Go is a natural language for Kubernetes controller development because:

-   Kubernetes and much of its ecosystem are written in Go.
-   Client libraries are mature.
-   Controller/reconciliation patterns integrate naturally with Go.
-   Goroutines provide lightweight concurrency.
-   Deployment is simple because applications compile to standalone
    binaries.
-   Go's relatively simple concurrency and memory model works well for
    cloud control-plane services.

The architectural point is more important than arguing that Go is
universally better than another language.

------------------------------------------------------------------------

# 15. Concurrency Model

Multiple resources may require reconciliation concurrently.

Conceptually:

``` text
Kubernetes Events
       |
       v
    Work Queue
       |
 +-----+-----+------+
 |           |      |
 v           v      v
Worker 1  Worker 2 Worker 3
 |           |      |
 v           v      v
Reconcile  Reconcile Reconcile
Server A   Server B  Server C
```

Important considerations:

-   avoid global mutable state,
-   isolate reconciliation by resource,
-   use stable resource identity,
-   control worker concurrency,
-   rate-limit retries,
-   protect external dependencies from request storms.

------------------------------------------------------------------------

# 16. What if the Controller Crashes?

A likely interview question.

``` text
Before crash:

BareMetalServer
status = Provisioning

ProvisionServerAction = exists

Provisioning Pod = running


              X
       Controller crashes


After restart:

Controller
    |
    v
Read BareMetalServer
    |
    v
Observe action
    |
    v
Observe provisioning pod
    |
    v
Continue reconciliation
```

It should **not** blindly create another provisioning action.

Interview answer:

> "The controller process was not the durable source of truth.
> Kubernetes resources persisted the desired and observed state. After
> restart, reconciliation reconstructed what needed to happen from those
> resources."

------------------------------------------------------------------------

# 17. What if Two Controller Replicas Are Running?

High availability can require multiple controller replicas.

``` text
Controller Replica A
Controller Replica B
Controller Replica C
         |
         v
    Leader Election
         |
         v
    Active Leader
```

Also design resource operations assuming repeated events and optimistic
concurrency.

The deeper point:

> Distributed correctness should not rely only on an in-process mutex.
> Resource state, deterministic identity, idempotent actions, and
> Kubernetes concurrency semantics are more important.

------------------------------------------------------------------------

# 18. Pod Management

Provisioning pods are useful because the expensive/long-running work is
isolated from the controller.

``` text
Controller / Manager
        |
        v
Provisioning Job
        |
        v
Provisioning Pod
        |
        +--> Mount NFS
        |
        +--> Access image
        |
        +--> Connect to target
        |
        +--> Transfer/deploy image
        |
        +--> Report completion/failure
```

Benefits:

-   execution isolation,
-   Kubernetes scheduling,
-   resource limits,
-   restart/failure visibility,
-   logs per provisioning operation,
-   controller remains lightweight.

------------------------------------------------------------------------

# 19. Storage and NFS Flow

The image path can be viewed as:

``` text
          Image Metadata
                |
                v
           ZonalImage
                |
                v
         StorageVolume
                |
                v
        NetApp / NFS Export
                |
       ExportPolicy / Rule
                |
                v
          Service Node
                |
                v
       Provisioning Pod
                |
                v
        Target Bare Metal
```

This separates:

``` text
image identity
      !=
image storage
      !=
storage access policy
      !=
provisioning execution
```

which is a useful separation of concerns.

------------------------------------------------------------------------

# 20. Observability

For a production provisioning system, monitor both controller health and
customer-visible provisioning performance.

Useful metrics:

``` text
Provisioning request count

Provisioning success rate

Provisioning failure rate

Requested -> Ready latency

Provisioning duration:
    p50
    p95
    p99

Reconciliation latency

Reconciliation failures

Retry count

Work-queue depth

Provisioning pod failures

NFS mount failures

Fleet Manager API errors

Fleet Manager API latency

Servers stuck in Provisioning

Time spent in each state
```

The most customer-relevant SLI is often:

``` text
Provisioning Request
        |
        | elapsed time
        v
Server Ready
```

------------------------------------------------------------------------

# 21. Logging and Correlation

Every provisioning request should have a stable identity that can be
correlated across components.

Conceptually:

``` text
BareMetalServer ID
        |
        +--> Controller logs
        |
        +--> ProvisionServerAction
        |
        +--> Manager request
        |
        +--> Provisioning Pod
        |
        +--> Fleet Manager logs
```

This is essential when debugging a workflow spanning multiple services.

------------------------------------------------------------------------

# 22. Security Considerations

Important areas include:

-   restrict NFS access through export policies,
-   ensure only authorized service nodes mount provisioning images,
-   use least-privilege Kubernetes RBAC,
-   protect credentials/secrets used by controllers,
-   validate user-supplied image/server parameters,
-   secure controller-to-manager APIs,
-   avoid logging secrets,
-   restrict provisioning pods to required privileges,
-   audit server lifecycle operations.

Bare-metal operations are particularly sensitive because provisioning
actions can modify an entire physical server.

------------------------------------------------------------------------

# 23. Deprovisioning / Delete Flow

Provisioning is only half of the lifecycle.

A delete/deprovision operation can use the same reconciliation
principles.

``` text
Delete requested
      |
      v
Mark desired state
      |
      v
Controller reconciles
      |
      +--> stop/cleanup provisioning operation
      |
      +--> clean temporary pod/job
      |
      +--> release storage/export policy references
      |
      +--> perform server cleanup as required
      |
      v
Remove finalizer
      |
      v
Resource deleted
```

Kubernetes finalizers can be useful when external cleanup must complete
before an API object disappears.

------------------------------------------------------------------------

# 24. Director-Level Trade-Off Discussion

A Director may care less about the exact Go classes and more about
architectural decisions.

Be ready to discuss:

## Why asynchronous rather than synchronous?

Provisioning can take minutes and depends on multiple external systems.
A synchronous HTTP call would be fragile and difficult to recover.

## Why Kubernetes as the control plane?

It provides persisted desired state, reconciliation, watches,
scheduling, resource lifecycle, leader election patterns, and an
ecosystem suitable for infrastructure controllers.

## Why separate provisioning pods?

Long-running image transfer should not consume or block controller
workers.

## Why multiple controllers?

Clear responsibility boundaries improve maintainability and failure
isolation.

## How do you prevent duplicate provisioning?

Idempotent reconciliation, deterministic action identity,
observe-before-create behavior, and external idempotency/correlation
where available.

## How do you recover after restart?

Reconstruct progress from persisted resources and observed external
state.

## How do you handle dependency failure?

Classify transient versus terminal failures, update status/conditions,
retry transient errors with controlled backoff, and expose actionable
diagnostics.

------------------------------------------------------------------------

# 25. Probable Director-Round Questions

### "What exactly did your controller reconcile?"

Answer in terms of desired vs observed server state rather than merely
"it watched events."

### "What happens if provisioning takes 30 minutes?"

The controller does not block for 30 minutes. It creates/delegates the
long-running action, records/observes state, and returns. Later
events/requeues continue reconciliation.

### "What if the same event arrives twice?"

Events are triggers, not commands. Reconciliation examines current
state, and operations are designed to be idempotent.

### "What happens if the controller crashes after creating the pod?"

After restart it observes that the provisioning action/pod already
exists and continues monitoring it instead of creating another.

### "What if NFS is down?"

Treat it as a retryable infrastructure failure if appropriate, expose
status, and retry using controlled backoff rather than spinning.

### "How do you identify a stuck server?"

Track state-transition timestamps and alert when a server exceeds the
expected duration for a particular phase.

### "How would you scale this?"

Increase controller worker concurrency carefully, partition work by
resource, minimize shared mutable state, rate-limit external APIs, and
ensure storage/Fleet Manager are not overwhelmed.

### "Why not perform provisioning directly from the controller?"

It couples control-plane availability to a long-running data-transfer
operation. Provisioning pods provide isolation, scheduling, logs,
resource controls, and better lifecycle management.

### "What was the hardest problem?"

Reliable, idempotent orchestration across multiple independently failing
distributed components.

------------------------------------------------------------------------

# 26. 90-Second Interview Answer

> "At IBM I worked on a Go-based Kubernetes control plane for automated
> bare-metal provisioning on IBM Z/LinuxONE. We modeled desired
> infrastructure state through Kubernetes resources and used multiple
> controllers with clear responsibilities for server lifecycle,
> provisioning actions, storage-related state and execution workflows.
>
> A server request referenced an image. The system resolved the zonal
> image and NFS/storage information, determined the appropriate service
> infrastructure, and created a provisioning action. The bare-metal
> manager coordinated with Fleet Manager, which created a provisioning
> pod on an eligible service node. That pod mounted the NFS image and
> performed the image deployment to the target physical server.
>
> The most important architectural point was that we did not model
> provisioning as one long synchronous function. It crossed Kubernetes,
> storage, networking, service nodes, provisioning pods, management
> services and physical hardware, so partial failures were expected. We
> used reconciliation and persisted resource state so that operations
> were idempotent and recoverable. If a controller restarted, it could
> observe whether the action or provisioning pod already existed and
> continue instead of duplicating the operation.
>
> At Principal level, the key design concerns were controller
> responsibility boundaries, idempotency, retry and failure
> classification, regional versus zonal resource modeling, NFS access
> control, observability and eventually consistent convergence of the
> server toward the requested state."

------------------------------------------------------------------------

# 27. Whiteboard Version to Remember

Draw this first:

``` text
                 User / API
                     |
                     v
             BareMetalSpec / CR
                     |
                     v
          +----------------------+
          | Go Bare-Metal       |
          | Controller          |
          +----------+-----------+
                     |
                 Reconcile
                     |
          +----------+----------+
          |                     |
          v                     v
     Image / Storage       Server Action
          |                     |
          v                     v
      NFS / NetApp       Bare Metal Manager
                                |
                                v
                          Fleet Manager
                                |
                                v
                          Service Node
                                |
                                v
                        Provisioning Pod
                           /          \
                          v            v
                     NFS Image     Target Server
                                        |
                                        v
                                 IBM Z / LinuxONE
```

Then add the controller loop:

``` text
Desired State
     |
     v
   Observe
     |
     v
Desired == Actual?
   /          \
 Yes           No
  |             |
Return       Take Action
                |
                v
           Update Status
                |
                v
             Requeue
```

------------------------------------------------------------------------

# 28. Five Lines to Remember

1.  **"We modeled bare-metal provisioning as a Kubernetes reconciliation
    problem, not as one synchronous API workflow."**
2.  **"The Kubernetes resources persisted desired and observed state;
    the controller process itself was not the source of truth."**
3.  **"Long-running image provisioning was delegated to provisioning
    pods on service nodes rather than performed inside the
    controller."**
4.  **"The biggest engineering challenge was idempotent recovery from
    partial failures across storage, Kubernetes, management services and
    physical hardware."**
5.  **"Repeated reconciliation had to converge toward the same desired
    state without duplicating destructive operations."**

------------------------------------------------------------------------

# 29. How to Position This Project Alongside the COBOL Modernization Project

These two IBM projects demonstrate different Principal-level strengths.

``` text
COBOL -> Java Modernization
---------------------------
Advanced C++
Compiler architecture
AST / IR
Semantic preservation
Legacy modernization
Differential testing


IBM Z / LinuxONE Bare-Metal Provisioning
-----------------------------------------
Go
Kubernetes controllers
Cloud infrastructure
Distributed systems
Reconciliation
Idempotency
Failure recovery
Storage / NFS
Long-running workflows
```

Together they provide strong examples for an interview that moves
between **software architecture, systems programming, distributed
systems, cloud infrastructure, reliability, and technical leadership**.
