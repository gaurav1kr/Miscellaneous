# SBOM, SLSA, and in-toto --- Software Supply-Chain Security

**SBOM, SLSA, and in-toto** are related to **software supply-chain
security**. They are especially relevant for AI agents that generate
code, install packages, build artifacts, or trigger CI/CD pipelines.

The easiest way to remember them is:

> **SBOM = What is inside my software?**\
> **SLSA = How trustworthy was the process that built it?**\
> **in-toto = Can I cryptographically verify the steps that produced
> it?**

## Start with the Problem

Imagine this pipeline:

``` text
Developer / AI Coding Agent
        ↓
Source Code
        ↓
Dependencies
        ↓
Build
        ↓
Tests
        ↓
Docker Image
        ↓
Deployment
        ↓
Production
```

A lot can go wrong:

``` text
Malicious dependency
Compromised build server
Modified source code
Tampered artifact
Untrusted AI-generated package
Artifact replaced after build
```

Supply-chain security tries to answer:

``` text
WHAT is inside it?
       ↓
SBOM

HOW was it built?
       ↓
SLSA

CAN I verify the build steps?
       ↓
in-toto
```

------------------------------------------------------------------------

## 1. SBOM --- Software Bill of Materials

An **SBOM** is basically an **ingredient list for software**.

Think about a food label:

``` text
Chocolate Cake

Ingredients:
- Flour
- Sugar
- Cocoa
- Butter
- Eggs
```

An SBOM does the same thing for software:

``` text
my-service v2.1

Components:
├── openssl 3.x
├── curl 8.x
├── protobuf 25.x
├── grpc 1.x
├── zlib 1.x
└── my-library 2.4
```

### Why Is This Useful?

Suppose tomorrow a serious vulnerability is announced:

``` text
CVE-XXXX

Affected:
openssl version X
```

You can query your SBOMs:

``` text
Which applications contain this version?

        ↓

Service A   ✓
Service B   ✗
Service C   ✓
Service D   ✗
```

Without an SBOM, organizations may struggle to determine **where a
vulnerable library exists**.

### Common SBOM Formats

Two common formats are:

``` text
SPDX
CycloneDX
```

### Key Takeaway

> **SBOM = inventory of components and dependencies inside a software
> artifact.**

------------------------------------------------------------------------

## 2. SLSA --- Supply-chain Levels for Software Artifacts

**SLSA** is a framework for improving and assessing **software build and
supply-chain security**.

Official website: https://slsa.dev/

SBOM tells you:

> **What's inside this artifact?**

SLSA addresses questions more like:

> **Where did this artifact come from, and can I trust how it was
> produced?**

Imagine someone gives you:

``` text
payment-service.tar.gz
```

You want to know:

``` text
Which source repository produced it?

Which commit?

Which build system built it?

Was the build environment trustworthy?

What build instructions were used?

Was provenance generated?

Could someone tamper with the artifact?
```

This is where **build provenance** becomes important.

Conceptually:

``` text
Artifact
   │
   └── Provenance
          │
          ├── Source repository
          ├── Commit SHA
          ├── Build system
          ├── Build workflow
          ├── Dependencies/materials
          └── Resulting artifact identity
```

Instead of trusting:

``` text
Here's my-service.exe.

Trust me.
```

you can have verifiable provenance tying the artifact back to its build.

SLSA has evolved over time, so the important concept is more useful than
memorizing older level descriptions:

> **SLSA provides a framework for increasing confidence in software
> artifact provenance and build integrity.**

------------------------------------------------------------------------

## 3. in-toto

**in-toto** focuses on **verifying software supply-chain steps and their
metadata/attestations**.

Official website: https://in-toto.io/

Suppose your expected pipeline is:

``` text
Source
  ↓
Build
  ↓
Test
  ↓
Security Scan
  ↓
Package
  ↓
Deploy
```

You don't merely want someone to claim:

> "Yes, we tested and scanned it."

You want evidence that the expected steps occurred and that
artifacts/materials can be tied across those steps.

Conceptually:

``` text
Source
  ↓
[Build]
  │
  └── signed/attested metadata
  ↓
[Test]
  │
  └── signed/attested metadata
  ↓
[Security Scan]
  │
  └── signed/attested metadata
  ↓
[Package]
  │
  └── signed/attested metadata
  ↓
Artifact
```

Then a verifier can reason about whether the expected supply-chain
policy was followed.

### Key Takeaway

> **in-toto = framework for securing and verifying the chain of steps
> used to produce software.**

------------------------------------------------------------------------

# How SBOM + SLSA + in-toto Fit Together

This is the part worth remembering:

``` text
                     SOFTWARE ARTIFACT
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
        SBOM             SLSA            in-toto
          │                │                │
          ↓                ↓                ↓
     What's inside?   How trustworthy   Can we verify
                       was the build?    supply-chain
                                         steps/evidence?
```

They are **complementary**, not competing technologies.

------------------------------------------------------------------------

# Practical CI/CD Example

Imagine:

``` text
Git Repository
      ↓
CI Build
      ↓
Dependencies
      ↓
Compile
      ↓
Tests
      ↓
Security Scan
      ↓
Container Image
      ↓
Registry
      ↓
Kubernetes
```

You could add supply-chain security controls:

``` text
Git Repository
      ↓
CI Build
      │
      ├── Generate SBOM
      │
      ├── Generate provenance
      │
      └── Generate/sign attestations
      ↓
Container Image
      ↓
Verification
      ↓
Policy
      ↓
ALLOW / DENY DEPLOYMENT
```

For example, deployment policy might require:

``` text
✓ SBOM exists
✓ No prohibited dependency
✓ Provenance is valid
✓ Artifact came from approved repository
✓ Artifact came from approved CI builder
✓ Required security scan completed
✓ Artifact digest matches attestation

                 ↓

              DEPLOY
```

Otherwise:

``` text
DENY
```

------------------------------------------------------------------------

# Why This Matters for AI Coding Agents

Suppose an autonomous coding agent can:

``` text
Agent
 ↓
Generate code
 ↓
Add dependency
 ↓
Build
 ↓
Run tests
 ↓
Create PR
 ↓
Trigger CI/CD
```

The agent could accidentally introduce:

``` text
Unknown package
Vulnerable dependency
Wrong package version
Malicious package
Unapproved build tool
```

So runtime-policy concepts can be combined with software supply-chain
controls:

``` text
                    AI Coding Agent
                           │
                           ↓
                    MCP Allow-list
                  What tools can it use?
                           │
                           ↓
                         OPA
                  Is action permitted?
                           │
                           ↓
                       Sandbox
                  Where can code execute?
                           │
                           ↓
                       Source Code
                           │
                           ↓
                         Build
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
           SBOM          SLSA         in-toto
             │             │             │
         Components     Provenance    Attestations /
                                     supply-chain
                                       evidence
             └─────────────┬─────────────┘
                           ↓
                    Policy Verification
                           ↓
                    ALLOW / DENY DEPLOY
```

------------------------------------------------------------------------

# Runtime Security vs Supply-Chain Security

These provide two complementary security areas.

## Agent Runtime Security

``` text
MCP allow-lists
OPA
Sandbox
Permissions
```

These controls determine:

> **What can the agent do?**

## Software Supply-Chain Security

``` text
SBOM
SLSA
in-toto
Provenance
Attestations
```

These controls help establish:

> **What was produced, where did it come from, and can we trust how it
> was produced?**

------------------------------------------------------------------------

# Quick Comparison

  -----------------------------------------------------------------------
  Technology              Main Question           Primary Purpose
  ----------------------- ----------------------- -----------------------
  **SBOM**                What is inside the      Component/dependency
                          software?               inventory

  **SLSA**                How trustworthy was the Build integrity and
                          build process?          provenance

  **in-toto**             Can we verify the       Attestation and
                          supply-chain steps?     supply-chain
                                                  verification
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Key Takeaway

Remember:

``` text
SBOM
  ↓
WHAT is inside the artifact?

SLSA
  ↓
HOW trustworthy was the process
that produced the artifact?

in-toto
  ↓
CAN we verify the expected
supply-chain steps and evidence?
```

For production **AI coding agents and autonomous software-engineering
agents**, it is useful to understand both:

``` text
Runtime Security
     +
Supply-Chain Security
```

because autonomous agents increasingly have the ability not only to
**generate code**, but also to **install dependencies, execute builds,
create artifacts, trigger CI/CD, and potentially influence production
deployments**.
