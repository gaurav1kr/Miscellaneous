# Samsung OQC (Overall Quality Coverage) Automation

## Director-Round Interview Preparation Guide

**Project themes:** C++ • Linux TV Systems • D-Bus • Client/Server
Architecture • JSON-Driven Test Automation • Physical Device Reliability
• Screenshot Validation • Inception ML • QA Automation

> **Interview positioning:** OQC was a large-scale automation initiative
> proposed to reduce the manual effort required to validate candidate
> Samsung TV software images before mass production.

> **Accuracy note:** Historical sections below are based on the supplied
> project description. Exact recovery algorithms, retry counts, D-Bus
> APIs, persistence mechanisms and ML metrics were not supplied, so they
> are not presented as historical facts. Suggested designs are
> explicitly identified.

------------------------------------------------------------------------

# 1. Business Problem

For each TV product cycle, module teams such as Wi-Fi, Menu, Graphics,
Channel, Apps and Browser began development after the product
specification was released. Code was integrated continuously,
group-level system testing was performed, QA/UAT raised defects, and
developers fixed issues until Product and QA agreed on a candidate
stable image.

The candidate image then went through another image-stability validation
stage before mass production.

``` text
Product Specification
        |
        v
Module Development
        |
        v
Continuous Integration
        |
        v
Group System Testing
        |
        v
Bug Fixing
        |
        v
QA / UAT
        |
        v
Product + QA agree on Candidate Image
        |
        v
Final Image Stability Validation
        |
        v
Mass Production
```

The final validation process involved roughly:

``` text
~1,000 test scenarios
        x
40–50 TV sets
        x
3–4 hours
        +
Screenshot capture
        +
Manual screenshot verification
```

This required substantial repetitive QA effort.

The OQC idea was:

> **Automate both TV test execution and visual verification of the
> captured results.**

------------------------------------------------------------------------

# 2. OQC High-Level Architecture

``` text
                    Developer / QA
                          |
                   Test Suite JSON
                          |
                         USB
                          |
                          v
             +-------------------------+
             |       Samsung TV        |
             | Factory Settings        |
             | Test -> Start OQC Test  |
             +------------+------------+
                          |
                       Event
                          |
                          v
             +-------------------------+
             |       OQC Client        |
             |    C++ Linux Daemon     |
             |                         |
             | Parse JSON              |
             | Identify test suites    |
             | Coordinate execution    |
             +------------+------------+
                          |
                         D-Bus
                          |
                          v
             +-------------------------+
             |       OQC Server        |
             |    C++ Linux Daemon     |
             |                         |
             | Execute TV actions      |
             | Navigate UI             |
             | Capture screenshots     |
             +------------+------------+
                          |
                          v
                Captured Screenshots
                          |
                          v
                       ZIP File
                          |
                          v
                    Upload / UI
                          |
                          v
             +-------------------------+
             | Inception ML Model      |
             | Visual Validation       |
             +------------+------------+
                          |
                +---------+---------+
                |         |         |
                v         v         v
              PASS     PARTIAL     FAIL
                        PASS
```

------------------------------------------------------------------------

# 3. Core Architectural Idea

OQC had two major automation domains:

``` text
                    OQC
                     |
          +----------+----------+
          |                     |
          v                     v
  Execution Automation     Validation Automation
          |                     |
          v                     v
 C++ Client/Server        Inception ML Model
 D-Bus IPC                Image Classification
          |                     |
          v                     v
TV Actions + Images       Pass / Partial / Fail
```

The design therefore addressed both sources of manual effort:

1.  executing the scenarios,
2.  examining the resulting screenshots.

------------------------------------------------------------------------

# 4. JSON-Driven Test Definition

Developers created test sets in JSON and placed them on a USB device
attached to the TV.

An illustrative structure might look like:

``` json
{
  "testSuites": [
    {
      "name": "AboutTVValidation",
      "steps": [
        "Open Menu",
        "Open Samsung Support",
        "Open About the TV",
        "Capture Image"
      ]
    }
  ]
}
```

This JSON is illustrative only; the exact production schema was not
supplied.

The architectural advantage was separation of:

``` text
Test Definition
      !=
Execution Engine
```

A new or modified scenario could be represented as data rather than
requiring the entire native execution framework to be redesigned.

------------------------------------------------------------------------

# 5. Starting the OQC Test

The tester used factory settings:

``` text
Factory Settings
       |
       v
      Test
       |
       v
 Start OQC Test
       |
       v
 Trigger Event
       |
       v
 Begin OQC Workflow
```

The C++ client/server daemons participated in the workflow after OQC was
started.

------------------------------------------------------------------------

# 6. OQC Client Responsibilities

Based on the supplied project description:

``` text
OQC Client
    |
    +--> Access test definition from USB
    |
    +--> Parse JSON
    |
    +--> Identify configured test suites
    |
    +--> Execute suites one by one
    |
    +--> Coordinate with OQC Server
```

A concise interview explanation:

> **The client handled test definition and orchestration; the server
> handled actual TV-side execution.**

------------------------------------------------------------------------

# 7. OQC Server Responsibilities

For a test such as:

``` text
Open Menu
    |
    v
Samsung Support
    |
    v
About the TV
    |
    v
Check expected items
```

the server performed the actual execution and captured the resulting
image.

Conceptually:

``` text
Receive execution request
        |
        v
Perform TV action
        |
        v
Navigate to expected screen
        |
        v
Capture screenshot
        |
        v
Return execution/result information
```

The process repeated across the test suites.

------------------------------------------------------------------------

# 8. C++ Client/Server + D-Bus

The client/server architecture was implemented in C++ and used D-Bus for
local IPC.

``` text
+-------------+                       +-------------+
| OQC Client  |                       | OQC Server  |
+------+------+                       +------+------+
       |                                     |
       | Execute test/action                 |
       |------------------------------------>|
       |                                     |
       |                             TV execution
       |                             Screenshot
       |                                     |
       | Result/completion                   |
       |<------------------------------------|
```

The architectural value is the responsibility boundary:

``` text
Client:
"What should execute?"

Server:
"Perform the requested TV operation."
```

This avoids putting JSON parsing, sequencing, platform operations and
screenshot execution into one monolithic component.

------------------------------------------------------------------------

# 9. End-to-End Flow

``` text
Developer creates test JSON
            |
            v
Copy JSON to USB
            |
            v
USB attached to TV
            |
            v
Tester starts OQC from Factory Settings
            |
            v
OQC event triggered
            |
            v
Client parses JSON
            |
            v
Load test suites
            |
            v
Select next test
            |
            v
D-Bus request to server
            |
            v
Server executes TV scenario
            |
            v
Capture screenshot
            |
            v
Store artifact
            |
            v
More tests?
      +-----+-----+
      |           |
     Yes          No
      |           |
      +-----------+--> Package screenshots
                           |
                           v
                          ZIP
                           |
                           v
                       Upload UI
                           |
                           v
                  Inception ML Model
                           |
                   +-------+-------+
                   |       |       |
                 PASS   PARTIAL   FAIL
                         PASS
```

------------------------------------------------------------------------

# 10. Why Client/Server?

A Director may ask why this was not one process.

The design separated:

``` text
Orchestration
     |
     | D-Bus
     v
Execution
```

This gives cleaner ownership:

-   JSON/test-definition logic belongs to orchestration.
-   TV/platform operations belong to execution.
-   IPC defines a clear contract between them.
-   Components can be debugged/evolved independently.

------------------------------------------------------------------------

# 11. Why D-Bus?

Both sides were Linux TV daemons. D-Bus is well suited for local
inter-process communication among Linux services.

The important interview answer is not merely:

> "We used D-Bus."

Instead:

> "We used D-Bus as the IPC boundary between the orchestration daemon
> and the daemon responsible for actual device-side execution."

------------------------------------------------------------------------

# 12. Screenshot Collection

Every executed scenario produced visual evidence.

``` text
Test 001 -> Screenshot 001
Test 002 -> Screenshot 002
Test 003 -> Screenshot 003
...
Test N   -> Screenshot N
```

At completion:

``` text
Captured Images
      |
      v
Package
      |
      v
ZIP File
      |
      v
Upload for Validation
```

This transformed the result of the physical-device run into a portable
test artifact.

------------------------------------------------------------------------

# 13. ML-Based Visual Validation

The ZIP was uploaded through a UI, and captured images were evaluated
using an **Inception-based ML model** trained using up-to-date expected
images for the respective scenarios.

``` text
Expected / Training Images
           |
           v
    Train Inception Model
           |
           v
       Trained Model
           ^
           |
Captured Screenshot
           |
           v
        Inference
           |
     +-----+-----+
     |     |     |
     v     v     v
   PASS PARTIAL FAIL
         PASS
```

------------------------------------------------------------------------

# 14. Why Visual Validation Is Hard

Exact pixel matching is brittle for UI testing.

Conceptually, an automated validator must distinguish:

``` text
Correct Screen
      vs
Acceptable Visual Variation
      vs
Actual UI Defect
```

The supplied project used an Inception ML model rather than relying only
on manual inspection.

Do not claim specific accuracy, augmentation methods or dataset sizes
unless you remember them.

------------------------------------------------------------------------

# 15. Major Challenge #1 --- Training the ML Model

The project was around **2020**, before today's multimodal/agentic AI
tooling.

The real challenge was not just training a neural network. It was making
the automated decision trustworthy enough for QA.

Bad classification has two forms:

``` text
False Positive
Correct image -> FAIL

False Negative
Incorrect image -> PASS
```

Too many false positives make QA stop trusting automation.

False negatives can allow actual regressions to escape.

### Director-round answer

> "One of the major challenges was visual validation. This was around
> 2020, so we didn't have today's multimodal foundation models. We used
> an Inception-based image model trained with expected scenario images.
> The difficult part was making Pass, Partial Pass and Fail
> classification reliable enough that automation actually reduced manual
> verification rather than generating another stream of false alarms."

------------------------------------------------------------------------

# 16. Major Challenge #2 --- Reliability on Physical TVs

This is the strongest systems story.

OQC was not executing against a deterministic software mock.

It was controlling real televisions.

External/device problems could include:

``` text
Remote-control problem

One test getting stuck

TV/application hang

Slow UI transition

Unexpected device state
```

With approximately 1,000 tests, the system needed to prevent one
problematic scenario from unnecessarily destroying the entire run.

``` text
Test 1 -> PASS
Test 2 -> PASS
Test 3 -> problem
            |
            v
       detect / handle
            |
            v
Test 4 -> continue where possible
```

The supplied project description says the system was improved
significantly over roughly **3--4 months** until it was running well.

------------------------------------------------------------------------

# 17. Biggest Probable Challenge I Faced

> "The biggest challenge was making a long-running automation suite
> reliable on physical TVs. Writing an individual automation step was
> relatively straightforward, but when you run around a thousand
> scenarios, even rare device-side failures become important. A
> remote-control event could fail, a test could stop, an application
> could hang, or the TV could become unresponsive.
>
> We needed to make sure one bad scenario did not unnecessarily
> invalidate the value of the complete multi-hour run. We iteratively
> improved the framework based on actual failures seen on devices, and
> over roughly three to four months the execution became much more
> stable.
>
> The second major challenge was visual validation. Around 2020 we
> didn't have today's multimodal AI capabilities. We used an
> Inception-based model trained with expected images, and the real
> difficulty was making Pass, Partial Pass and Fail classification
> trustworthy enough for QA.
>
> Architecturally, I separated test orchestration from device execution
> using C++ client/server daemons communicating through D-Bus. The
> client parsed and sequenced JSON-defined tests, while the server
> performed the TV operations and screenshot capture."

------------------------------------------------------------------------

# 18. Failure Isolation

A key design objective for a long-running suite is:

``` text
One Test Failure
       |
       X
Should NOT automatically imply
       |
       v
Entire Test Run Lost
```

A conceptual robust workflow is:

``` text
Execute Test
     |
     +--> Success -> Capture -> Next
     |
     +--> Failure
             |
             v
       Classify problem
             |
       +-----+------+
       |            |
   Recoverable   Severe
       |            |
       v            v
   Recover and   Record / stop
   continue       according to policy
```

**Historical caution:** The exact retry/recovery state machine was not
supplied. Use this as architectural reasoning unless you remember the
implementation.

------------------------------------------------------------------------

# 19. Test Independence

Physical UI automation is vulnerable to cascading failures.

Example:

``` text
Test A expects Home
      |
      v
opens Settings
      |
      X fails before cleanup

Test B starts
      |
      v
TV is still in Settings
      |
      v
False failure
```

Therefore a robust automation framework should reason about:

``` text
Precondition
    |
    v
Execute
    |
    v
Validate
    |
    v
Postcondition / Reset
```

Do not claim a particular reset mechanism unless it existed in the
original system.

------------------------------------------------------------------------

# 20. State-Machine View

For an architecture interview, represent the workflow as states:

``` text
NotStarted
    |
    v
LoadingTests
    |
    v
Ready
    |
    v
Executing
    |
    v
Capturing
    |
    v
TestCompleted
    |
    +--> Next Test
    |
    v
SuiteCompleted
    |
    v
Packaging
    |
    v
Completed
```

Failure path:

``` text
Executing
    |
    v
Failure / Timeout
    |
    v
Recovery Decision
   /              \
Recoverable    Unrecoverable
    |              |
    v              v
Continue       Record / Stop
```

This is an interview design model, not a claim that these exact state
names existed.

------------------------------------------------------------------------

# 21. Scale of the Problem

Two dimensions matter:

``` text
~1,000 test scenarios
        |
        +----------------+
                         |
                  ~40–50 TVs
```

The challenge was therefore larger than:

> "Can I automate one UI test?"

The real question was:

> **Can the automation be reliable and repeatable enough to support
> production-quality validation across many scenarios and physical
> devices?**

------------------------------------------------------------------------

# 22. Sequential Execution

The supplied description says test suites executed one by one.

That is reasonable on an individual TV because UI actions share the same
device state.

``` text
Test 1
   |
   v
Test 2
   |
   v
Test 3
```

Attempting unrelated UI navigation concurrently on the same device would
create conflicting actions.

Scale can instead come from the fleet of TVs.

------------------------------------------------------------------------

# 23. Reliability Engineering Discussion

The exact historical implementation was not specified. If asked how you
would harden the architecture, discuss:

## Timeout

``` text
Start test
   |
   v
Execute
   |
   +--> completes -> next stage
   |
   +--> exceeds timeout -> recovery
```

## Retry Classification

``` text
Failure
   |
   +--> transient -> bounded retry
   |
   +--> test failure -> record + continue
   |
   +--> device-wide failure -> device recovery / safe stop
```

## Checkpointing

Track conceptually:

``` text
run ID
suite ID
current test
execution status
screenshot status
result
```

## Watchdog

Detect tests or daemons that stop making progress.

These are proposed hardening techniques unless you remember them from
the original system.

------------------------------------------------------------------------

# 24. Automation Speed vs Reliability

Fast action timing:

``` text
+ shorter total test duration
- UI may not be ready
- higher flakiness
```

Long fixed waits:

``` text
+ simpler
+ potentially more stable
- wastes execution time
```

A better modern approach is condition/readiness-based synchronization
where the platform exposes a reliable signal.

------------------------------------------------------------------------

# 25. Observability

A long-running automation framework should make it possible to answer:

``` text
Which test was executing?

Which step failed?

How long had it been running?

Did D-Bus communication succeed?

Was the screenshot generated?

Did the TV stop responding?

How many tests completed?

Why was the run interrupted?
```

The exact original logging schema was not provided, so treat these as
architecture expectations rather than historical implementation claims.

------------------------------------------------------------------------

# 26. How I Would Improve It Today

These are **modern design suggestions**, not claims about the original
2020 implementation.

### Explicit Per-Test State

``` text
QUEUED
   |
RUNNING
   |
   +--> PASSED
   +--> FAILED
   +--> TIMED_OUT
   +--> RECOVERING
```

### Durable Checkpoints

Allow execution to resume after recoverable daemon/device failures.

### Structured Correlation

``` text
run_id
tv_id
suite_id
test_id
step_id
timestamp
result
failure_reason
```

### Confidence-Aware Visual Validation

``` text
High-confidence PASS -> auto accept

High-confidence FAIL -> auto flag

Ambiguous -> human review
```

### Modern Vision Models

Modern vision/multimodal models could be benchmarked against the
Inception pipeline, especially for legitimate UI variations. Whether
they are better should be established experimentally rather than
assumed.

------------------------------------------------------------------------

# 27. Director-Level Trade-Offs

## Why JSON?

Separates test intent from native implementation.

``` text
Test Definition
      |
      v
Generic Execution Engine
```

## Why client/server?

Separates orchestration from TV-specific execution.

## Why C++?

Fits the native Linux TV environment and system-level integration.

## Why D-Bus?

Provides a suitable IPC boundary between Linux daemons.

## Why ML?

Automates visual interpretation rather than requiring every captured
image to be inspected manually.

## Why iterative hardening?

Physical-device automation exposes timing and environmental failures
that are difficult to discover completely during initial design.

------------------------------------------------------------------------

# 28. Probable Director-Round Questions

### What problem were you solving?

> "The final stability stage before mass production required roughly a
> thousand scenarios to run for three to four hours across around forty
> to fifty TVs, followed by manual screenshot verification. OQC
> automated both execution and visual validation."

### What did you personally propose?

> "The automation approach: JSON-driven test definitions, C++
> client/server daemons using D-Bus for execution and screenshot
> capture, followed by ML-assisted image validation."

### Why client/server?

> "To separate test orchestration from the component performing actual
> TV-side operations and provide a clean IPC contract."

### Why D-Bus?

> "The components were native Linux daemons on the TV, and D-Bus was a
> suitable local IPC mechanism."

### What was the biggest challenge?

> "Reliable execution of a long suite on physical TVs. One
> remote-control issue, stuck scenario or TV hang should not
> unnecessarily destroy the complete run."

### What was difficult about ML?

> "Building trustworthy classification using representative expected
> images and avoiding excessive false passes or false failures."

### Why not pixel-by-pixel comparison?

> "UI screenshots can have legitimate visual differences. A learned
> visual model provides a way to classify the expected scenario rather
> than requiring exact pixel identity."

### What if test 500 hangs?

> "The system needs to detect the stuck scenario, isolate the failure
> and recover/continue where possible. I would describe the exact
> historical recovery only to the extent I remember it rather than
> inventing details."

### How did you improve reliability?

> "We iteratively hardened the framework based on failures observed on
> real TVs. The supplied project history is roughly three to four months
> of improvement before it was running well."

------------------------------------------------------------------------

# 29. 90-Second Director-Round Answer

> "At Samsung, final TV image validation before mass production involved
> significant manual effort. After development, system testing and UAT,
> a candidate stable image went through another QA stage where roughly a
> thousand scenarios were run for three to four hours across around
> forty to fifty TVs. Screenshots were captured and manually inspected
> to determine whether the image was stable.
>
> I proposed automating this OQC workflow. Developers defined test
> suites in JSON and placed them on USB. From factory settings, a tester
> could start OQC. A C++ client daemon parsed the JSON and coordinated
> the tests, while a C++ server daemon performed the actual TV
> operations through a client/server architecture using D-Bus. For
> example, it could navigate Menu to Samsung Support to About the TV and
> capture the resulting screen. After the suite completed, the
> screenshots were packaged into a ZIP and uploaded through a UI.
>
> For visual validation, we used an Inception-based ML model trained
> with expected images for the scenarios, and classified results as
> Pass, Partial Pass or Fail.
>
> The hardest part was reliability at scale on physical TVs. A
> remote-control issue, a slow application, one stuck scenario or a TV
> hang could interrupt a long test run. We spent roughly three to four
> months iteratively hardening the framework so execution became stable.
> The other major challenge was making the ML classification trustworthy
> because this was around 2020, before today's multimodal AI
> capabilities.
>
> The project combined systems programming, Linux IPC, automation
> architecture, physical-device reliability and practical computer
> vision applied to a real manufacturing-quality problem."

------------------------------------------------------------------------

# 30. Whiteboard Diagram to Memorize

``` text
              Developer / QA
                    |
              JSON Tests / USB
                    |
                    v
           +------------------+
           |    Samsung TV    |
           | Start OQC Test   |
           +--------+---------+
                    |
                    v
           +------------------+
           | OQC Client C++   |
           | Parse/Orchestrate|
           +--------+---------+
                    |
                   D-Bus
                    |
                    v
           +------------------+
           | OQC Server C++   |
           | Execute/Capture  |
           +--------+---------+
                    |
                    v
               Screenshots
                    |
                    v
                   ZIP
                    |
                    v
                Upload UI
                    |
                    v
             Inception Model
                    |
            +-------+-------+
            |       |       |
          PASS   PARTIAL   FAIL
                  PASS
```

Under it, write:

``` text
Challenge 1:
Reliable ~1000-test execution on real TVs

Challenge 2:
Trustworthy ML visual validation in 2020
```

------------------------------------------------------------------------

# 31. Five Lines to Remember

1.  **"I proposed OQC to automate a highly manual final image-stability
    validation process before TV mass production."**
2.  **"Tests were data-driven through JSON, while C++ client/server
    daemons used D-Bus to separate orchestration from TV-side
    execution."**
3.  **"The framework executed scenarios and captured screenshots; an
    Inception-based model classified results as Pass, Partial Pass or
    Fail."**
4.  **"The hardest systems problem was ensuring that one bad scenario or
    physical-TV issue did not unnecessarily invalidate an entire
    long-running suite."**
5.  **"We iteratively hardened the system for roughly three to four
    months based on real execution failures until it was running
    well."**

------------------------------------------------------------------------

# 32. Leadership Story

Do not present OQC merely as:

> "I wrote a C++ automation tool."

Present the progression:

``` text
Observed expensive manual QA process
              |
              v
Identified automation opportunity
              |
              v
Proposed architecture
              |
              v
JSON-driven test definitions
              |
              v
C++ / D-Bus execution framework
              |
              v
Automated screenshot collection
              |
              v
ML-based visual validation
              |
              v
Observed real-device failures
              |
              v
Iteratively hardened framework
              |
              v
Practical OQC automation
```

This lets you demonstrate:

-   problem identification,
-   architectural ownership,
-   C++ systems development,
-   Linux IPC,
-   physical-device automation,
-   practical ML adoption,
-   reliability engineering,
-   iterative improvement,
-   engineering impact.

------------------------------------------------------------------------

# 33. Claims to Avoid Unless You Remember Them

Do not invent:

-   exact percentage reduction in manual effort,
-   exact engineer-hours saved,
-   exact ML accuracy,
-   exact false-positive rate,
-   exact training dataset size,
-   exact retry count,
-   exact D-Bus method names,
-   exact checkpoint implementation,
-   exact watchdog implementation,
-   exact device-reset mechanism,
-   a claim that every test always continued after every type of TV
    hang.

A safe response for an old implementation detail is:

> "I don't want to invent the exact production value because this was an
> older project, but the architectural problem we were solving was..."

Then explain the design principle.

------------------------------------------------------------------------

# 34. Positioning Against the Stability Monitor Project

``` text
Samsung Stability Monitor
-------------------------
C / C++
Linux internals
CPU / Memory / Flash
Multithreading
Shared data structures
Fault detection
Core dumps
Runtime device reliability


Samsung OQC
-----------
Large-scale QA automation
C++ client/server
D-Bus IPC
JSON-driven tests
Physical device automation
Screenshot capture
Inception ML
Long-running test reliability
Manufacturing-quality validation
```

The Stability Monitor demonstrates **low-level runtime reliability**.

OQC demonstrates **large-scale automation architecture, initiative, and
early practical ML adoption**.

------------------------------------------------------------------------

# 35. Final Director-Level Summary

OQC is best presented as an end-to-end engineering initiative:

``` text
Manual QA Bottleneck
       |
       v
Automation Proposal
       |
       +--> JSON Test Definition
       |
       +--> C++ Client
       |
       +--> D-Bus
       |
       +--> C++ Server
       |
       +--> TV Action Automation
       |
       +--> Screenshot Capture
       |
       +--> ZIP / UI
       |
       +--> Inception ML
       |
       v
Pass / Partial Pass / Fail
       |
       v
Iterative Reliability Hardening
```

A strong closing statement:

> **"What made OQC interesting was that it connected systems
> programming, physical-device automation and machine learning to solve
> a real production-quality bottleneck. The difficult part was not
> automating one happy-path test---it was making roughly a thousand
> scenarios dependable enough on real TVs that QA could actually trust
> and use the automation."**
