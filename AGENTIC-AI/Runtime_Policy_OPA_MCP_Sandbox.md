# Runtime Policy for Agentic AI

Runtime policy is the set of **rules enforced while an AI agent is
executing** that determines what the agent is actually allowed to do.

A useful mental model is:

> **Runtime policy = enforced controls around an AI agent's actions,
> tools, and resource access.**

For example:

``` text
User
  ↓
AI Agent
  ↓
"I need to modify a configuration file"
  ↓
Runtime Policy
  ↓
┌─────────────────────────────────────┐
│ Is this tool allowed?               │
│ Is this operation allowed?          │
│ Is this file accessible?            │
│ Is network access permitted?        │
│ Does this require approval?         │
└─────────────────────────────────────┘
  ↓
ALLOW / DENY / REQUIRE APPROVAL
```

Three important mechanisms are:

1.  **OPA (Open Policy Agent)**
2.  **MCP allow-lists**
3.  **Sandbox permissions**

These operate at somewhat different layers and can be combined for
defense in depth.

------------------------------------------------------------------------

## 1. OPA --- Open Policy Agent

**OPA (Open Policy Agent)** is a general-purpose **policy engine**.

Instead of scattering authorization rules throughout application or
agent code, policy decisions can be externalized to a dedicated policy
layer.

Conceptually:

``` text
Agent
  ↓
Wants to perform action
  ↓
Policy Enforcement Point
  ↓
OPA
  ↓
Evaluate policy
  ↓
ALLOW / DENY
```

OPA policies are commonly expressed using its policy language, **Rego**.

### Example Policies

Conceptually, an organization might define:

``` text
Allow read operations

Allow writes only to /workspace/

Deny access to /etc/

Deny production database deletion

Require approval for production deployment
```

If an agent attempts:

``` text
action   = delete
resource = production_database
```

OPA evaluates the policy and can return:

``` text
DENY
```

### Why OPA Matters

The important architectural idea is **separating policy from agent
reasoning**.

``` text
Agent reasoning
      ↓
"I want to deploy this build."
      ↓
Policy Engine
      ↓
"You're not authorized to deploy production."
      ↓
DENY
```

The LLM does not get to override the policy.

Official project: https://www.openpolicyagent.org/

------------------------------------------------------------------------

## 2. MCP Allow-Lists

**MCP (Model Context Protocol)** provides a standardized way for AI
applications and agents to connect to tools and external systems.

For example:

``` text
                  AI Agent
                     ↓
                    MCP
                     ↓
       ┌─────────────┼──────────────┐
       ↓             ↓              ↓
    GitHub        Database      Filesystem
    Server         Server          Server
```

However, giving an agent access to an MCP server does not necessarily
mean it should be allowed to use every tool exposed by that server.

### Example

Imagine a database MCP server exposes:

``` text
read_customer()
search_orders()
update_customer()
delete_customer()
drop_table()
```

You might configure an allow-list:

``` text
Allowed:
✓ read_customer
✓ search_orders

Not allowed:
✗ update_customer
✗ delete_customer
✗ drop_table
```

This follows the security principle of:

> **Least privilege --- give the agent only the capabilities necessary
> for its task.**

### Multiple Levels of Allow-Listing

You can think about allow-listing at several levels:

``` text
MCP Server
   ↓
Allowed tools
   ↓
Allowed operations
   ↓
Allowed resources
```

For example, a coding agent connected to a GitHub MCP server might
receive:

``` text
✓ search_code
✓ read_file
✓ create_branch
✓ create_pull_request

✗ merge_pull_request
✗ delete_repository
✗ change_repository_permissions
```

This is much safer than simply putting an instruction in the system
prompt:

``` text
"Please don't delete anything."
```

A prompt is an instruction.

> **An allow-list is an enforced capability boundary.**

------------------------------------------------------------------------

## 3. Sandbox Permissions

Sandboxing operates at a lower execution/resource layer.

Suppose an AI coding agent can generate and execute code:

``` text
Agent
 ↓
Writes Python script
 ↓
Executes script
```

That generated code should generally not receive unrestricted access to
the host machine.

Instead, it can execute inside a **sandbox**.

``` text
Host Machine
│
├── Secrets
├── SSH keys
├── Production credentials
├── Personal files
│
└── Sandbox
      │
      ├── /workspace      READ/WRITE
      ├── /tmp            READ/WRITE
      ├── /system         DENY
      │
      ├── Network
      │     ├── approved-api.com   ALLOW
      │     └── everything else    DENY
      │
      └── Process limits
            ├── CPU
            ├── Memory
            └── Execution time
```

### Typical Sandbox Controls

A sandbox may restrict:

-   Filesystem access
-   Network access
-   Process execution
-   Environment variables
-   Secrets
-   CPU
-   Memory
-   Execution duration
-   System calls
-   Container or VM capabilities

### Example: Filesystem Protection

Suppose generated code attempts:

``` text
rm -rf /important-data
```

The sandbox can prevent the process from accessing that directory.

The protection does not depend on whether the LLM understands that the
operation is dangerous.

### Example: Network Protection

``` text
Agent-generated code
      ↓
tries network request
      ↓
Network Policy
      ↓
api.company.com → ALLOW

unknown-site.com → DENY
```

This can reduce risks such as unintended data exfiltration.

------------------------------------------------------------------------

# How OPA, MCP Allow-Lists, and Sandboxes Fit Together

These mechanisms are complementary rather than alternatives.

``` text
                       AI AGENT
                           │
                           ↓
                  MCP TOOL ALLOW-LIST
                           │
                  "Can I use this tool?"
                           ↓
                     OPA POLICY
                           │
             "Is this action permitted
              for this user/context?"
                           ↓
                        TOOL
                           │
                           ↓
                       SANDBOX
                           │
              "What can the executed code
                actually access?"
                           ↓
                  Operating System /
                  Network / Resources
```

## Example: Production Deployment

Imagine an AI coding agent wants to deploy code to production.

### MCP Allow-List

Question:

> Is `deploy()` even an available tool for this agent?

If not, the agent cannot invoke it.

### OPA

If the tool is available, the next question might be:

> Is this particular user or agent authorized to deploy this repository
> to production?

OPA can evaluate contextual information and return:

``` text
ALLOW
DENY
REQUIRE APPROVAL
```

### Sandbox

If scripts or generated code are executed during the workflow:

> What files, network destinations, processes, and system resources can
> that code actually access?

The sandbox provides the lower-level execution boundary.

------------------------------------------------------------------------

# Defense in Depth

Using these controls together creates **defense in depth**.

  -----------------------------------------------------------------------
  Mechanism                           Main Question
  ----------------------------------- -----------------------------------
  **OPA**                             Is this action allowed according to
                                      organizational policy?

  **MCP allow-list**                  Which tools and capabilities can
                                      the agent use?

  **Sandbox permissions**             What resources can executed code
                                      actually access?
  -----------------------------------------------------------------------

The architecture might look like:

``` text
User
 ↓
Agent
 ↓
MCP Capability Restriction
 ↓
OPA Authorization
 ↓
Human Approval (when required)
 ↓
Tool
 ↓
Sandbox
 ↓
Infrastructure Permissions
 ↓
Operating System / Network / Cloud
```

Each layer reduces the amount of damage that a failure at another layer
can cause.

------------------------------------------------------------------------

# The LLM Should Not Be the Security Boundary

This is one of the most important principles.

## Weak Approach

``` text
System Prompt:

"Never delete production data."

        ↓
       LLM
        ↓
Agent decides whether to comply
```

This depends too heavily on model behavior.

Prompt injection, hallucination, incorrect reasoning, or an unexpected
tool sequence could cause problems.

## Stronger Approach

``` text
Agent
 ↓
MCP capability restriction
 ↓
OPA authorization
 ↓
Sandbox/resource restrictions
 ↓
Infrastructure permissions
```

Even if the model makes a poor decision, external controls can limit
what it is capable of doing.

------------------------------------------------------------------------

# Example: Coding Agent

Consider a coding agent with repository and shell access.

``` text
Developer
    ↓
Coding Agent
    ↓
Planner
    ↓
LLM
    ↓
GitHub MCP
    ↓
Shell / Code Execution
```

A secure runtime architecture could be:

``` text
Developer
    ↓
Agent
    ↓
MCP Allow-List
    │
    ├── read_repository       ✓
    ├── create_branch         ✓
    ├── create_pull_request   ✓
    ├── merge_to_main         ✗
    └── delete_repository     ✗
    ↓
OPA
    │
    ├── Is user authorized?
    ├── Is repository allowed?
    ├── Is environment production?
    └── Does this require approval?
    ↓
Sandbox
    │
    ├── /workspace       RW
    ├── SSH keys         DENY
    ├── secrets          LIMITED
    ├── network          RESTRICTED
    └── execution        LIMITED
    ↓
Actual Operation
```

------------------------------------------------------------------------

# Runtime Policy in Agentic AI Architecture

As AI applications evolve:

``` text
Simple AI

Prompt
  ↓
LLM
  ↓
Answer
```

into:

``` text
Agentic AI

User
 ↓
Agent
 ↓
LLM
 ↓
Tools
 ↓
MCP Servers
 ↓
APIs
 ↓
Databases
 ↓
Shell
 ↓
Cloud Infrastructure
```

security requirements change significantly.

The system must control not only:

> **What can the AI say?**

but increasingly:

> **What can the AI actually do?**

That is why runtime policy becomes a major component of production
Agentic AI architecture.

------------------------------------------------------------------------

# Key Takeaway

Remember the three layers this way:

``` text
MCP Allow-List
      ↓
"What tools can the agent use?"

OPA
      ↓
"Is this particular action allowed?"

Sandbox
      ↓
"What can executed code actually access?"
```

Together:

``` text
Agent
 ↓
CAPABILITY CONTROL
MCP Allow-List
 ↓
POLICY CONTROL
OPA
 ↓
EXECUTION CONTROL
Sandbox
 ↓
RESOURCE CONTROL
OS / Network / Cloud IAM
```

The central security principle is:

> **Do not rely on the LLM itself to enforce security. Enforce security
> outside the model using deterministic runtime controls.**
