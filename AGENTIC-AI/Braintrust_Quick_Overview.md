# Braintrust --- Quick Overview

Braintrust is an **AI evaluation, observability, and experimentation
platform** for LLM and agent applications.

Conceptually, it overlaps with platforms such as LangSmith, with a
strong emphasis on answering:

> **"How do I know whether my AI application is actually getting
> better?"**

Official website: https://www.braintrust.dev/

## Simple Example

Suppose you have a RAG application:

``` text
User Question
      ↓
Retriever
      ↓
Vector DB
      ↓
Retrieved Context
      ↓
LLM
      ↓
Final Answer
```

You change your system from **Model A → Model B**, change the prompt, or
modify the retrieval strategy.

The new answer may *look* better---but how do you prove it?

Braintrust lets you run the same evaluation dataset against both
versions:

``` text
                Test Dataset
                     │
             ┌───────┴───────┐
             ↓               ↓
         Version A        Version B
         Model A          Model B
             ↓               ↓
          Answers           Answers
             │               │
             └───────┬───────┘
                     ↓
                 Evaluation
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    Accuracy     Relevance    Latency
        ↓            ↓            ↓
       82%           88%         1.4s

                  vs.

       91%           94%         1.1s
```

Now you have measurable evidence about which version performs better.

## What Braintrust Provides

  Capability                   Purpose
  ---------------------------- -------------------------------------------------
  **Evals**                    Systematically evaluate AI output
  **Datasets**                 Maintain representative test cases
  **Experiments**              Compare prompts, models, and architectures
  **Scorers**                  Automatically score AI responses
  **Tracing**                  Trace LLM, agent, retrieval, and tool execution
  **Logging**                  Capture production AI interactions
  **Monitoring**               Detect quality problems in production
  **Prompt experimentation**   Experiment with prompts and models
  **Human review**             Allow humans to evaluate outputs

## Evaluation Metrics

For example, you could evaluate a RAG application using metrics such as:

``` text
Correctness        0.94
Relevance          0.91
Faithfulness       0.89
Retrieval quality  0.93
Latency            1.2 sec
Cost               $0.0031
```

You can then make a code, prompt, model, or retrieval change and rerun
the experiment.

This helps answer:

> **Did the change actually improve the AI system?**

## Braintrust vs LangSmith

Braintrust and LangSmith overlap in several areas.

  Capability              LangSmith   Braintrust
  ----------------------- ----------- -------------
  Tracing                 ✅          ✅
  LLM observability       ✅          ✅
  Evaluation              ✅          ✅
  Experiments             ✅          ✅
  Datasets                ✅          ✅
  Production monitoring   ✅          ✅
  Agent debugging         Strong      Strong
  Evaluation workflows    Strong      Major focus
  LangChain integration   Excellent   Supported
  Framework independent   Yes         Yes

The distinction is becoming less sharp as both platforms continue to add
capabilities.

A useful mental model is:

``` text
LangSmith
   ↓
"Why did my agent behave this way?"
   ↓
Tracing + Debugging + Evaluation


Braintrust
   ↓
"Did my AI system actually get better?"
   ↓
Evaluation + Experiments + Observability
```

This is a conceptual simplification rather than a strict product
boundary.

## Why Braintrust Matters for Agentic AI

Consider a production agent:

``` text
User
 ↓
Planner Agent
 ↓
Search Agent ─────→ Search Tool
 ↓
Reasoning Agent
 ↓
Code Agent ───────→ Code Repository
 ↓
Reviewer Agent
 ↓
Final Result
```

Simply checking whether the final answer *looks good* isn't sufficient.

You may want to measure:

-   Task success rate
-   Correctness
-   Tool-call accuracy
-   Hallucination rate
-   Retrieval quality
-   Number of agent steps
-   Agent loops
-   Latency
-   Token consumption
-   Cost
-   Regression rate
-   Human feedback

Braintrust helps make these characteristics **measurable and
comparable**.

## Six Important Concepts to Learn

When learning Braintrust or other AI observability/evaluation platforms,
understand these concepts:

### 1. Tracing

Records what happened during execution.

``` text
User
 ↓
Agent
 ↓
LLM
 ↓
Retriever
 ↓
Tool
 ↓
LLM
 ↓
Answer
```

Useful for answering:

> **Why did the AI behave this way?**

### 2. Evaluation

Determines whether an AI response or behavior is good.

Examples:

``` text
Correctness
Relevance
Faithfulness
Safety
Task success
```

### 3. Datasets

A reusable collection of test cases.

Think of it as:

> **AI regression test cases**

### 4. Scorers

Functions or evaluators that calculate quality metrics.

For example:

``` text
AI Response
      ↓
Correctness Scorer
      ↓
0.92
```

A scorer may use deterministic code, rules, human judgment, or another
LLM.

### 5. Experiments

Run different versions of your AI system against the same dataset.

For example:

``` text
Dataset
   │
   ├── Prompt V1 + Model A
   │
   └── Prompt V2 + Model B
             ↓
         Compare
             ↓
Quality / Cost / Latency
```

This allows data-driven decisions instead of relying on whether a few
responses *seem* better.

### 6. Production Monitoring

Tracks how the deployed AI system behaves with real users.

Typical signals include:

``` text
Quality
Task success
Latency
Cost
Token usage
Tool failures
Retrieval failures
User feedback
```

## Complete AI Evaluation Lifecycle

``` text
                    DATASET
                       │
                       ↓
                  EXPERIMENT
                       │
                       ↓
                    TRACES
                       │
                       ↓
                  EVALUATION
                       │
                       ↓
                    SCORERS
                       │
                       ↓
              Compare V1 vs V2
                       │
                       ↓
                    DEPLOY
                       │
                       ↓
             PRODUCTION MONITORING
                       │
                       ↓
             Find new bad examples
                       │
                       └──────────────→ DATASET
```

This creates a **continuous improvement loop**.

## Traditional Software Engineering Analogy

  Traditional Software           AI Engineering
  ------------------------------ -----------------------
  Logs / distributed tracing     Tracing
  Testing                        Evaluation
  Test cases                     Datasets
  Assertions / metrics           Scorers
  Benchmark / A-B testing        Experiments
  Production observability/APM   Production monitoring

## Key Takeaway

Braintrust helps engineering teams move from:

> **"The new prompt/model seems better."**

to:

> **"The new version performs measurably better across our evaluation
> dataset, while meeting our latency and cost requirements."**

That transition---from subjective inspection to **repeatable evaluation
and measurement**---is one of the most important ideas in production AI
engineering.
