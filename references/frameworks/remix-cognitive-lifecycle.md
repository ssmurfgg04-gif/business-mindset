# Remix-Inspired Cognitive Lifecycle Architecture

To elevate `business-mindset` from a static prompt collection into a robust, state-aware cognitive framework, we adapt core architectural primitives from Remix (`remix-run/remix`).

---

## 1. Cognitive Loaders vs. Cognitive Actions

Remix strictly separates data reading (`loader`) from data mutation (`action`). In business cognition:

- **Cognitive Loaders (Read Queries):**
  - **Purpose:** Pure analysis, signal scanning, demand gap identification, competitor teardowns, and asymmetry scoring.
  - **Behavior:** Side-effect free. They read references, execute search protocols, and return evaluated scores without altering persistent project state or generating deployment artifacts.

- **Cognitive Actions (State Mutations):**
  - **Purpose:** Execution planning, sprint allocation, decision journal logging, and MVP artifact generation.
  - **Behavior:** State-changing. They take winning loader verdicts and commit them to structured artifacts (JSON schemas, CSV unit economics skeletons, sprint timelines).

---

## 2. Error Boundaries (Graceful Cognitive Fallbacks)

In Remix, route errors are caught locally rather than crashing the entire tree. 

- **Cognitive Error Boundary Protocol:**
  - If a research protocol encounters high Knightian uncertainty, conflicting search results, or zero empirical validation, the engine **must not hallucinate a PASS**.
  - Instead, it catches the failure, surfaces a structured `Cognitive Error State` (e.g., *"Insufficient empirical verification; automatic safety fallback triggered: REJECT"*), and prevents confirmation bias.

---

## 3. Revalidation & Optimistic Calibration

- **Automatic Revalidation:**
  - Whenever a Cognitive Action executes (e.g., updating project assumptions), the engine automatically re-runs the asymmetry scorecard evaluation (`evaluate.py`) to re-check convexity, asymmetry, and friction against the new parameters.

---

## 4. Resource Routes (Machine-Readable JSON Endpoints)

- **Purpose:** 
  - Just as Remix routes can output raw JSON for API clients, `business-mindset` can output machine-parseable JSON schemas of briefs and scorecards for multi-agent swarms (e.g., OpenClaw or Moltask automation bots) without human markdown translation overhead.
