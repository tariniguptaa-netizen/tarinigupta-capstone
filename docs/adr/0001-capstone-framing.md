```markdown
# ADR-0001: Capstone Framing — tarinigupta-capstone

- **Status:** Draft v1
- **Date:** 17/08/2026
- **Author:** TARINI GUPTA

## Context
To build a production-grade, context-aware AI assistant that eliminates developer search friction and LLM code hallucinations by providing version-accurate, structure-preserving retrieval of FastAPI documentation.

## Decision — Solution Framing Canvas

| Box | Your answer |
|-----|-------------|
| **Inputs** | Text queries from developers  |
| **Outputs** | a structured conscise response with valid resouces list|
| **Tools** | Openapi , vector db  |
| **Memory** | short term session conversation |
| **Autonomy level** | chatbot but uses AI for some complex queries|
| **Decision boundaries** | need human approval when modifying code/scripts |

## Consequences

- **Positive:** gives user proper response rather than hallunicating with valid citations. 
- **Negative / risks:** dependent on the FastApi documentation which should be updated.
- **Things we'll re-visit:** multiligiual support , adding memory 
```

**Reading this template:**

- **Status** — `Draft v1` for now. Later ADRs might be `Accepted`, `Superseded`, or `Deprecated`.
- **Six Canvas boxes** — these are the Solution Framing Canvas you saw on Day 2. Each box is *one* sentence; if you can't say it in one sentence, you don't understand the choice well enough yet.
- **Consequences** — positive, negative, things to revisit. Negative consequences matter as much as positive ones; we want learners to be honest about trade-offs from W1.
