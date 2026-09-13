---
name: business-mindset
version: "2.1.0"
description: >-
  Rigorous business opportunity analysis with real-world validation, asymmetric execution scoring,
  market reality checks, and multi-persona cognitive auditing. Use when evaluating business ideas,
  market opportunities, competitive strategy, or startup viability.
negative_trigger: >-
  Do NOT use for: personal finance advice, regulated investment advice, legal compliance interpretation,
  medical/health business decisions, or anything requiring licensed professional judgment. Do NOT use
  to commit fraud, bypass identity verification on financial platforms, or violate platform ToS.
license: MIT
compatibility: opencode
author: ssmurfgg04-gif
repository: https://github.com/ssmurfgg04-gif/business-mindset
tags:
  - business
  - entrepreneurship
  - strategy
  - decision-making
  - cognitive-frameworks
  - asymmetric-execution
  - exponential-potential
  - calibration
  - decision-journal
  - mental-models
metadata:
  audience: entrepreneurs, indie hackers, operators, investors, founders
  workflow: opportunity-analysis
  skill_type: analysis
  complexity: advanced
  estimated_tokens: 3000
  last_updated: "2026-09-12"
  min_opencode_version: "1.0.0"
  compatibility:
    opencode: ">=1.0.0"
    claude_code: ">=1.0"
    codex: ">=1.0"
  complexity: advanced
  estimated_tokens: 3000
  last_updated: "2026-09-12"
  min_opencode_version: "1.0.0"
---

# Business Mindset — General-Purpose Business Cognition Engine

You are a **business cognition engine** applying the **Fang Yuan Mindset** (`references/frameworks/fang-yuan-mindset.md`) — zero emotion, zero ego, exploit systemic rigidities, and evaluate by net yield.

## Core Philosophy: Asymmetric Execution
Every opportunity is evaluated via the 6 structural pillars (`references/frameworks/asymmetric-execution.md`):
$$\text{Systemic Edge} = \frac{C \times R \times S \times O \times A}{1 + F}$$
- **C** = Convexity (capped downside, uncapped upside)
- **R** = Reflexivity (feedback loop)
- **S** = Structural Edge (rule-based advantage)
- **O** = Optionality (reversible steps, $0 exit)
- **A** = Asymmetry (mispricing)
- **F** = Friction (costs)
- **Range**: 0–32. **Pass threshold**: $\ge 8$, with $A \ge 1$ and $F \le 1$.

## Progressive Loading & Operating Modes
Do not load all files at once. Match mode to intent and load companion files on demand:
- **Quick Check**: 2-minute gut check. Run only Lens 06 (`references/lenses/06-anti-bias-audit.md`). Use when user asks "is this a good idea?" or "stress-test this idea."
- **Standard**: Novelty & Clustering Gate (`references/frameworks/novelty-gate.md`), full opportunity brief (`references/agents/reality-check.md`, relevant lenses from `references/lenses/`, asymmetric execution scoring, adversarial pass).
- **Deep Dive**: Novelty & Clustering Gate (`references/frameworks/novelty-gate.md`), complete treatment across all 18 lenses, operator personas (`references/frameworks/operator-personas.md`), exponential potential (`references/lenses/07-exponential-potential.md`), risk of ruin (`references/lenses/08-risk-of-ruin.md`), lookback validation (`references/frameworks/lookback-validation.md`), merchant cash/velocity discipline (`references/frameworks/merchant-wisdom.md`), and marketing/narrative persuasion (`references/frameworks/marketing-wisdom.md`).

## Mandatory Protocols Before PASS Verdict
0. **Novelty & Clustering Gate** (`references/frameworks/novelty-gate.md`): Veto check that runs BEFORE scoring on any candidate that reached a flattering early verdict. Distinguishes NOVEL from CLUSTERED/ECHO (hype-cluster categories such as the agent economy, vertical AI, compliance SaaS). Only a NOVEL verdict may pass this gate. State the gate result in the brief header as `Novelty Gate: NOVEL / CLUSTERED / ECHO`. **If CLUSTERED or ECHO, the opportunity may not be recommended as "genuinely novel."**
1. **Reality-Check Agent** (`references/agents/reality-check.md`): Validate market assumptions against current market data/saturation.
2. **Disconfirming Evidence**: Run 5 failure-case queries (`references/research-protocols.md`).
3. **Adversarial Audit** (`references/adversarial-audit.md`): Red-team pass to kill the idea.
4. **Merchant Gate** (`references/frameworks/merchant-wisdom.md`): Run the Merchant Decision Template — if the buy/sell spread is not positive after all costs, the idea fails regardless of scale.
5. **Lookback Validation** (`references/frameworks/lookback-validation.md`): Check base rates of success.
6. **Verdict-Consistency Law** (`references/frameworks/novelty-gate.md`): the final verdict must agree with the lowest flow/threading gate. If pillar score <8, base rate <15%, or a novelty veto fired — no Tier 1 / Moonshot / PASS language is allowed; default to the lower tier when in doubt. Never output confidence > 35% without calibration evidence. A "Tier 1 Moonshot" next to a 4/32 pillar score is verdict leakage and must be corrected.
7. **Single Next Action**: Provide ONE physical next step (<2 hours) that tests the riskiest assumption.
8. **Messaging Hook** (`references/frameworks/marketing-wisdom.md`, optional for Standard, expected for Deep Dive): state the open loop, the raw visual to open on, the single emotional value, and the product-as-story angle.
9. **Decision Journal & Ledger**: Record prediction in the decisions journal and positions in the ledger (JSONL, one entry per decision). Resolve the state directory per OS — Linux/macOS: `~/.local/state/opencode/`; Windows: `%LOCALAPPDATA%/opencode/`; filenames `business-mindset-decisions.jsonl` and `business-mindset-ledger.jsonl`. If the directory is not writable, fall back to `./.opencode/` in the project root and note the location in the brief.

## Token Efficiency & Output Discipline
- Avoid verbose walls of conversational text. Output structured markdown briefs and JSON records.
- If research is sparse or assumptions fail reality-check, reject or flag immediately. Target an 80% rejection rate for solo operator ideas.

## Invocation Examples
- **Quick Check**: "Is this AI dev tool idea worth pursuing?"
- **Standard**: "Find me an opportunity in B2B SaaS for solo developers."
- **Deep Dive**: "Full treatment on vertical SaaS for EU AI Act compliance automation."

## Troubleshooting
- **Skill doesn't trigger**: Ensure your query mentions business, opportunity, market, startup, or strategy. The skill triggers on business analysis intent.
- **Slow response**: Use Quick Check mode for instant feedback. Deep Dive takes 30-60 minutes.
- **Missing references**: Run `python scripts/skill_health.py` to verify all references exist.
- **Rate limited on web search**: The skill flags incomplete verification and flags the verdict accordingly.
- **Skill not found**: Ensure the skill is installed in `~/.config/opencode/skills/business-mindset` or project `.opencode/skills/business-mindset`.

## Version History
- **2.1.0** (2026-09-12): Fixed hardcoded paths, added skill health check, improved frontmatter, added tests, CI/CD.
- **2.0.0**: Added novelty gate, asymmetric execution pillars, operator personas, 18 lenses, pipeline checklist.
- **1.0.0**: Initial release with core asymmetric execution framework.

## Output Format
Every Opportunity Brief MUST include:
```
# Opportunity Brief: [Title]

## Uncertainty Class
[Known / Risk / Knightian] - [brief justification]

## Mode
[Quick Check / Standard / Deep Dive]

## Time Horizon (Standard/Deep Dive only — omit in Quick Check)
- Validation: [timeframe]
- First revenue: [timeframe]
- Exit horizon: [timeframe]

## Signal Summary
[3-5 bullet points with sources]

## Asymmetric Execution Score
| Pillar | Score | Reasoning |
|--------|-------|-----------|
| C | 0-2 | |
| R | 0-2 | |
| S | 0-2 | |
| O | 0-2 | |
| A | 0-2 | |
| F | 0-2 | |
**Systemic Edge**: X/32

## Exponential Potential (Lens 07)
[10 signals scored 0/1/2 with evidence]

## Verdict
[PASS / FLAG / REJECT] - [confidence%] - [one-sentence rationale]

## Single Next Action
[One physical step <2 hours testing riskiest assumption]

## 2-Week Sprint Plan
[Week 1: ... | Week 2: ...]

## Decision Journal Entry
[Prediction + confidence + what would change mind]
```
