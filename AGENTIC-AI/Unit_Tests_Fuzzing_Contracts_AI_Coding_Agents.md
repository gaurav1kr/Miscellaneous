# Unit Tests, Fuzzing, and Contracts for AI-Generated Code

In the context of **AI-generated code and coding agents**, unit tests,
fuzzing, and contracts are different ways to verify that generated code
is correct and robust.

A useful mental model is:

> **Unit tests = Does the code behave correctly for known cases?**\
> **Fuzzing = What happens with unexpected or weird inputs?**\
> **Contracts = What must always be true when this function/API is
> used?**

These complement runtime-policy and software supply-chain controls.

------------------------------------------------------------------------

## 1. Unit Tests --- Test Known Behavior

A **unit test** tests a small piece of code---typically a function,
class, or module---in isolation.

Suppose an AI agent generates:

``` cpp
int divide(int a, int b)
{
    return a / b;
}
```

You write unit tests:

``` cpp
TEST(DivideTest, PositiveNumbers)
{
    EXPECT_EQ(divide(10, 2), 5);
}

TEST(DivideTest, NegativeNumber)
{
    EXPECT_EQ(divide(-10, 2), -5);
}
```

Conceptually:

``` text
Known Input
    ↓
Function
    ↓
Actual Output
    ↓
Compare with
Expected Output
    ↓
PASS / FAIL
```

But what about:

``` cpp
divide(10, 0);
```

If nobody thought to write that test, all existing unit tests might pass
while the code still contains a serious bug.

That's one reason we also use **fuzzing**.

### Key Takeaway

> **Unit tests verify expected behavior for cases that developers
> explicitly define.**

------------------------------------------------------------------------

# 2. Fuzzing --- Throw Unexpected Inputs at the Code

Fuzzing automatically generates large numbers of unusual, random,
malformed, or boundary-case inputs.

Instead of manually testing only:

``` text
divide(10, 2)
divide(20, 4)
divide(-10, 2)
```

a fuzzer may eventually try:

``` text
divide(0, 0)
divide(INT_MAX, 0)
divide(INT_MIN, -1)
divide(-1, 0)
divide(1234567, -923)
...
```

Potentially millions of combinations can be explored.

Conceptually:

``` text
               Fuzzer
                  ↓
       Generate unusual inputs
                  ↓
              Function
                  ↓
       ┌──────────┼──────────┐
       ↓          ↓          ↓
     Crash      Hang      Memory Error
       ↓          ↓          ↓
              REPORT BUG
```

For C/C++, fuzzing is particularly useful for discovering issues such
as:

``` text
Buffer overflow
Out-of-bounds access
Use-after-free
Integer overflow
Null pointer dereference
Unexpected exceptions
Infinite loops
Parser bugs
```

### Example: Image Parser

Imagine an AI agent writes:

``` cpp
parseImage(data, size);
```

You might have 100 carefully designed unit tests.

A fuzzer can generate thousands or millions of malformed byte sequences:

``` text
00 FF 42 ...
FF FF FF ...
00 00 00 ...
gigantic length
truncated header
invalid dimensions
corrupted metadata
```

It may discover a crash or memory-safety problem nobody anticipated.

### Key Distinction

> **Unit tests test cases you thought about.**\
> **Fuzzing helps discover cases you didn't think about.**

------------------------------------------------------------------------

# 3. Contracts --- Define What Must Always Be True

Contracts specify **rules about how software components are allowed to
behave**.

The classic concept is known as **Design by Contract**.

A function can have:

``` text
Preconditions
Postconditions
Invariants
```

Suppose we have:

``` cpp
int withdraw(Account& account, int amount);
```

We can define a contract around the operation.

## Preconditions

Things that must be true **before** calling the function:

``` text
amount > 0
amount <= account.balance
account.status == ACTIVE
```

## Postconditions

Things that must be true **after** the function succeeds:

``` text
new_balance = old_balance - amount
new_balance >= 0
```

## Invariants

Things that should **always remain true**:

``` text
account.balance >= 0
```

Conceptually:

``` text
Caller
  ↓
Check Preconditions
  ↓
Function Executes
  ↓
Check Postconditions
  ↓
Verify Invariants
  ↓
Result
```

Suppose an AI agent generates:

``` cpp
account.balance -= amount;
```

and a bug somehow results in:

``` text
balance = -5000
```

The contract:

``` text
balance >= 0
```

has been violated.

### Key Takeaway

> **Contracts formally or explicitly describe conditions that callers
> and implementations are expected to preserve.**

------------------------------------------------------------------------

# Unit Tests vs Fuzzing vs Contracts

  -------------------------------------------------------------------------
                    Unit Tests        Fuzzing           Contracts
  ----------------- ----------------- ----------------- -------------------
  Main question     Does this known   What happens with What must always be
                    case work?        unexpected        true?
                                      inputs?           

  Inputs            Manually selected Automatically     Any input
                                      generated         satisfying
                                                        preconditions

  Finds expected    Excellent         Good              Good
  bugs                                                  

  Finds unexpected  Limited           **Excellent**     Depends on
  edge cases                                            assertions/checks

  Documents         Good              Limited           **Excellent**
  intended behavior                                     

  Useful for C/C++  Yes               **Very much**     Yes
  -------------------------------------------------------------------------

------------------------------------------------------------------------

# Why These Matter for AI Coding Agents

Consider a coding agent:

``` text
User
 ↓
Coding Agent
 ↓
Generate C++ Code
 ↓
Compile
 ↓
"Compilation successful"
```

Compilation does **not** mean the generated code is correct.

A stronger agentic coding pipeline could look like:

``` text
                 AI Coding Agent
                        ↓
                 Generate Code
                        ↓
                     Compile
                        ↓
                  Unit Tests
                        ↓
                     Fuzzing
                        ↓
               Contract Checking
                        ↓
               Static Analysis
                        ↓
               Security Scanning
                        ↓
                   Create PR
```

The agent is no longer merely asking:

> **Does my generated code compile?**

Instead, it accumulates **evidence that the generated change behaves
correctly and robustly**.

------------------------------------------------------------------------

# Putting the Security and Verification Layers Together

A production AI coding system can contain several independent layers:

``` text
                     AI CODING AGENT
                            │
                            ↓
                    RUNTIME SECURITY
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
             OPA        MCP Allow-list   Sandbox
                            │
                            ↓
                     Generate Code
                            │
                            ↓
                   CODE VERIFICATION
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
          Unit Tests      Fuzzing      Contracts
              │             │             │
              └─────────────┼─────────────┘
                            ↓
                          Build
                            ↓
                 SUPPLY-CHAIN SECURITY
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
            SBOM          SLSA         in-toto
                            │
                            ↓
                         Deploy
                            │
                            ↓
                    AI OBSERVABILITY
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
          LangSmith     Braintrust      Tracing
```

------------------------------------------------------------------------

# Four Different Questions

These layers answer different questions.

## Runtime Policy

Examples:

``` text
OPA
MCP allow-lists
Sandbox permissions
```

Question:

> **What is the agent allowed to do?**

## Code Verification

Examples:

``` text
Unit tests
Fuzzing
Contracts
Static analysis
```

Question:

> **Is the code the agent generated actually correct and robust?**

## Software Supply-Chain Security

Examples:

``` text
SBOM
SLSA
in-toto
Provenance
Attestations
```

Question:

> **Can we trust the artifact and its software supply chain?**

## AI Observability and Evaluation

Examples:

``` text
Tracing
LangSmith
Braintrust
Evaluation
Monitoring
```

Question:

> **Can we observe, debug, and evaluate the AI agent itself?**

------------------------------------------------------------------------

# Key Takeaway

Remember:

``` text
Unit Tests
    ↓
"Does the code work for known cases?"

Fuzzing
    ↓
"What happens for inputs we didn't anticipate?"

Contracts
    ↓
"What conditions must always remain true?"
```

Together:

``` text
Known Behavior
      +
Unexpected Inputs
      +
Required Invariants
      ↓
Stronger Confidence
in Generated Code
```

For production **AI coding agents**, these provide an important
code-verification layer between **agent runtime security** and
**software supply-chain security**.
