# Six Core Concepts of AI Evaluation & Observability

These six concepts are more important than any specific tool. Once you
understand them, platforms such as LangSmith and Braintrust become much
easier to understand.

We'll use one consistent example: an internal **RAG assistant** that
answers engineering questions from company documentation.

``` text
User Question
     ↓
Retriever → Vector DB
     ↓
Relevant Documents
     ↓
LLM
     ↓
Final Answer
```

## 1. Tracing --- "What exactly happened?"

**Tracing records the complete execution path of an AI request.**

Suppose the user asks:

> "How does OAuth token validation work?"

Your application gives a wrong answer. A trace might show:

``` text
User Question
      ↓
Retriever
      │
      ├─ Search query: "OAuth validation"
      ├─ Documents returned: 5
      └─ Time: 180 ms
      ↓
LLM
      │
      ├─ Model: GPT-X
      ├─ Input tokens: 4,200
      ├─ Output tokens: 600
      └─ Time: 1.8 sec
      ↓
Final Answer
```

You can drill into each step and inspect the **input and output**.

This becomes even more important with agents:

``` text
User
 ↓
Agent
 ├── LLM call
 ├── Search tool
 ├── LLM call
 ├── Database tool
 ├── LLM call
 └── Final answer
```

If the agent gives a bad answer, tracing helps determine **which step
went wrong**.

Think of it as:

> **Distributed tracing/debug logs for an AI system.**

------------------------------------------------------------------------

## 2. Evaluation --- "Was the answer actually good?"

Tracing tells you **what happened**.

Evaluation tells you **whether the result was good**.

Suppose the expected answer is:

``` text
OAuth access tokens are validated using
signature, issuer, audience and expiry checks.
```

Your AI responds:

``` text
OAuth validation verifies the token signature
and checks whether the token has expired.
```

An evaluation system can assess dimensions such as:

  Metric           Score
  -------------- -------
  Correctness       0.92
  Relevance         0.96
  Completeness      0.75
  Faithfulness      0.98

The response is mostly correct but incomplete because it didn't mention
**issuer and audience validation**.

Evaluations can be performed by:

``` text
Human evaluator
      OR
Rule/code
      OR
Another LLM acting as a judge
```

That last approach is commonly called an **LLM-as-a-Judge**.

------------------------------------------------------------------------

## 3. Datasets --- "What should I test against?"

You need a repeatable collection of examples for evaluation.

That's your **evaluation dataset**.

For example:

  Question                    Expected answer
  --------------------------- ----------------------------------------
  What is OAuth?              OAuth is an authorization framework...
  What is OBO?                On-Behalf-Of allows...
  How are tokens validated?   Verify signature, issuer...
  When does a token expire?   Based on the exp claim...

Perhaps you create:

``` text
OAuth Evaluation Dataset
        │
        ├── Question 1
        ├── Question 2
        ├── Question 3
        ├── ...
        └── Question 500
```

Every time you change your RAG system, run those **same 500 questions**.

This is analogous to a **regression test suite** in conventional
software.

> **Dataset ≈ AI regression test cases**

------------------------------------------------------------------------

## 4. Scorers --- "How do I measure quality?"

A **scorer is the function or mechanism that calculates an evaluation
metric**.

For example:

``` text
AI Answer
    ↓
Correctness Scorer
    ↓
0.92
```

You could have multiple scorers:

``` text
                     ┌→ Correctness scorer → 0.92
                     │
AI Response ─────────┼→ Relevance scorer   → 0.97
                     │
                     ├→ Faithfulness       → 0.88
                     │
                     └→ Safety scorer      → 1.00
```

Scorers can be very simple.

For example:

``` python
def contains_expected_term(answer):
    return "OAuth" in answer
```

Or sophisticated, where another LLM evaluates the answer:

``` text
Question
Expected Answer
Actual Answer
      ↓
Judge LLM
      ↓
"Score correctness from 0–1"
      ↓
0.91
```

So:

> **Evaluation = the overall testing process**\
> **Scorer = how an individual metric is calculated**

------------------------------------------------------------------------

## 5. Experiments --- "Is version B actually better than version A?"

Suppose your production RAG application currently uses:

``` text
Chunk size = 500
Top-K = 5
Model = Model A
Prompt = V1
```

You think changing Top-K from **5 → 10** will improve answers.

Don't just deploy it. Create an experiment:

``` text
             Evaluation Dataset
                    500 Questions
                         │
               ┌─────────┴─────────┐
               ↓                   ↓
          Experiment A        Experiment B

          Top-K = 5           Top-K = 10
               ↓                   ↓
          Run 500 tests        Run 500 tests
               ↓                   ↓
        Correctness 87%       Correctness 92%
        Latency 1.2 sec       Latency 1.8 sec
        Cost $0.30            Cost $0.47
```

Now you have an engineering decision:

**B is more accurate, but slower and more expensive. Is that trade-off
worthwhile?**

This is much better than:

> "I tried the new prompt and it seems better."

Think of experiments as:

> **A/B testing + benchmarking + regression testing for AI systems.**

------------------------------------------------------------------------

## 6. Production Monitoring --- "Is my AI still working properly?"

Everything above can happen **before deployment**.

But after deployment, real users will ask things you never anticipated.

Production monitoring watches what's happening in the live system.

``` text
                     Production AI
                          │
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
      Quality           Latency            Cost
        ↓                 ↓                 ↓
      91%               1.4 sec          $120/day
```

You might monitor:

``` text
Task success rate
Correctness
Hallucination rate
Tool failures
Retrieval failures
Latency
Token consumption
Cost
User feedback
Agent loops
```

Imagine your dashboard normally shows:

``` text
Answer quality:      93%
Tool success:        98%
Average latency:     1.3 sec
```

Suddenly:

``` text
Answer quality:      71%   ⚠️
Tool success:        97%
Average latency:     1.4 sec
```

Something changed.

Perhaps new documents were added to your knowledge base and retrieval
quality deteriorated.

Production monitoring helps detect that.

------------------------------------------------------------------------

# How the Six Concepts Connect

``` text
                    DATASET
                       │
             500 representative questions
                       │
                       ↓
                  EXPERIMENT
                       │
              Run your AI system
                       │
                       ↓
                    TRACES
                       │
             What happened internally?
                       │
                       ↓
                  EVALUATION
                       │
                Was it correct?
                       │
                       ↓
                    SCORERS
                       │
         Correctness / Relevance / Safety
                       │
                       ↓
              Compare experiments
                 V1 vs V2 vs V3
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

This forms a **continuous feedback loop**.

Bad production cases become new dataset examples → modify the agent →
run an experiment → evaluate it → deploy the improvement → monitor
again.

## Mapping to Traditional Software Engineering

  Traditional Software           AI Engineering
  ------------------------------ ---------------------------
  Logs / distributed tracing     **Tracing**
  Testing                        **Evaluation**
  Test cases                     **Datasets**
  Assertions / metrics           **Scorers**
  Benchmark / A-B testing        **Experiments**
  Production observability/APM   **Production monitoring**

## Key Takeaway

The six concepts to remember are:

1.  **Tracing** --- What happened internally?
2.  **Evaluation** --- Was the result good?
3.  **Datasets** --- What examples should we repeatedly test?
4.  **Scorers** --- How do we measure each quality dimension?
5.  **Experiments** --- Is the new version actually better?
6.  **Production Monitoring** --- Is the deployed AI system continuing
    to perform well?

Together, these concepts form a large part of **LLMOps / AI
observability and evaluation**.
