# LangSmith --- Quick Overview

LangSmith is an **observability, debugging, evaluation, and monitoring
platform for applications built with LLMs and AI agents**. It is
especially useful once an AI application becomes more complex than a
single prompt/response.

It comes from **LangChain**, but **you can use LangSmith even if your
application doesn't use LangChain**.

## Simple Way to Think About It

Suppose you build a RAG/agent system:

**User → Agent → LLM → Retriever → Vector DB → LLM → Answer**

Something goes wrong and the final answer is bad.

Without observability, you may only see:

> Question → Bad answer

With **LangSmith**, you can inspect the execution trace:

``` text
User Question
   ↓
Agent
   ↓
Retriever
   ├── Query: "OAuth token validation"
   ├── Documents retrieved: 5
   └── Latency: 220 ms
   ↓
LLM
   ├── Model: GPT-5.x
   ├── Prompt
   ├── Retrieved context
   ├── Response
   ├── Token usage
   └── Latency
   ↓
Tool Call
   ↓
Final Answer
```

So it's somewhat like **distributed tracing/APM for AI applications**,
with AI-specific evaluation capabilities added.

## What LangSmith Provides

  Capability                What it helps with
  ------------------------- ------------------------------------------------------
  **Tracing**               See every LLM, agent, retrieval and tool call
  **Debugging**             Understand why an agent produced an incorrect result
  **Evaluation**            Test whether answers are correct/relevant/safe
  **Datasets**              Maintain test cases for an AI application
  **Experiments**           Compare prompts/models/agent implementations
  **Monitoring**            Track production AI behavior
  **Latency tracking**      Find slow LLM/tool/retrieval operations
  **Token/cost tracking**   Understand model usage and cost
  **Human feedback**        Review and score AI outputs

## Example: RAG Application

Imagine you've built an internal documentation assistant.

User asks:

> "How does OAuth token validation work?"

Your system retrieves documents and sends them to an LLM.

If the answer is wrong, LangSmith lets you investigate:

``` text
Did retrieval return the correct documents?
            ↓
Was the right context sent to the LLM?
            ↓
Which prompt was used?
            ↓
Which model generated the response?
            ↓
Did the agent invoke the correct tool?
            ↓
How long did each operation take?
            ↓
How many tokens did it consume?
```

This is particularly valuable because **LLM failures aren't always model
failures**. The problem might actually be retrieval, context
construction, prompt design, tool selection, or an earlier agent
decision.

## LangSmith vs LangChain

They're related but serve different purposes.

### LangChain --- Build the AI Application

``` text
LLM
Agents
Tools
RAG
Retrievers
Workflows
```

### LangSmith --- Understand and Improve the AI Application

``` text
Tracing
Debugging
Evaluation
Testing
Monitoring
Experiments
```

A useful analogy from conventional software engineering is:

> **LangChain ≈ application framework**\
> **LangSmith ≈ tracing + debugging + testing + observability for the AI
> layer**

## Key Takeaway

For engineers learning **RAG and agentic AI architecture**, LangSmith is
worth understanding because **LLM observability and evaluation** are
increasingly important production-AI concepts---not just knowing how to
call an LLM API.
