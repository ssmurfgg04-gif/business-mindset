# SCHEMA.md — Business Mindset Skill

## File Tree

```
business-mindset/
│
├── SKILL.md                          ← Entry point. 18 lenses, 19 intent families,
│                                        adversarial audit, MANDATORY real-world
│                                        verification, multi-persona synthesis,
│                                        operator wisdom, mental models, distribution
│                                        engineering as pre-gate, Remix nested
│                                        routing, Elite Mandate final gate.
│
├── SCHEMA.md                         ← THIS FILE.
├── README.md
├── LICENSE                           ← MIT.
├── CONTRIBUTING.md
│
    ├── references/
    │   ├── research-protocols.md         ← Search strategies + failure-case search
    │   ├── real-world-verification.md    ← MANDATORY: actual GitHub/web searches before PASS
    │   ├── subagent-prompts.md           ← 6 sub-agent dispatch templates
    │   ├── intake.md                     ← Optional user intake
    │   ├── ledger.md                     ← Generalized position tracking
    │   ├── exponential-research.md       ← Source research for Lens 07
    │   ├── asymmetry-scorecard.md
    │   ├── execution-sprints.md
    │   ├── decision-journal.md
    │   ├── calibration-protocol.md
    │   ├── adversarial-audit.md
    │   ├── business-fundamentals.md
    │   ├── growth-playbook.md
    │   ├── anti-patterns-compendium.md
    │   ├── cognitive-biases-catalog.md
    │   ├── research-opportunity-identification.md
    │   ├── research-business-operations.md
    │   ├── research-operator-wisdom.md
    │   ├── research-pricing-competitor.md
    │   ├── profit-engineering.md         ← Monetization checklist + unit economics stress test
    │   ├── pipeline-checklist.md         ← 11-phase, 60+ step mandatory execution checklist
    │   ├── skill-health-diagnostic.md    ← 7-metric self-diagnostic
    │   ├── reddit-mining-protocol.md     ← MANDATORY demand-side verification
    │   ├── customer-interview-protocol.md ← MANDATORY Mom Test verification
    │   ├── god-of-business-gap-analysis.md ← Operator composite comparison
    │   │
    │   ├── agents/
    │   │   └── reality-check.md          ← Market data validation agent
    │   │
    │   ├── validation/
    │   │   └── case-studies.md           ← Historical scored examples & base rates
    │   │
    │   ├── frameworks/
    │   │   ├── fang-yuan-mindset.md
    │   │   ├── operator-personas.md
    │   │   ├── operator-wisdom.md
    │   │   ├── mental-models.md
    │   │   ├── ecr-model.md
    │   │   ├── effectuation.md
    │   │   ├── asymmetric-execution.md
    │   │   ├── remix-cognitive-lifecycle.md
    │   │   ├── tri-persona-debate.md     ← Munger/Musk/Thiel adversarial collision
    │   │   ├── gtm-activation.md         ← 4-phase Go-To-Market activation
    │   │   ├── money-making-mastery.md   ← Money equation, 5 search paths, pricing power
    │   │   ├── sales-and-negotiation-mastery.md ← Money-capture layer: sales psychology, objection engineering, closing
    │   │   └── lookback-validation.md    ← Base-rate checking protocol
│   │
│   └── domains/
│       ├── tech-saas-playbook.md
│       ├── services-playbook.md
│       ├── physical-products-playbook.md
│       └── boring-business-playbook.md
│
├── scripts/                          ← Automated verification & simulation runners
│   ├── evaluate.py                   ← Asymmetry scorecard test runner
│   ├── simulate.py                   ← 24-month synthetic market counter-attack simulator
│   ├── brier_score.py                ← Prediction calibration & forecasting accuracy tool
│   └── judge.py                      ← LLM-as-a-Judge evaluation runner
│
├── schemas/
│   └── agent-protocol.json           ← Agent API request/response JSON schema
│
├── templates/
│   ├── decision-journal-template.md
│   ├── sprint-plan-template.md
│   ├── post-mortem-template.md
│   └── execution-artifact-template.md ← MVP JSON + unit economics + landing wireframe
│
├── examples/
│   ├── golden-output.md
│   ├── calibration-dataset.md        ← 12 opportunities tested with real searches
│   ├── calibration-simulations.md    ← 30+ domains via mental simulation
│   └── calibration-matrix.md         ← 55-niche evaluation matrix
│
└── .github/ISSUE_TEMPLATE/
    ├── bug-report.md
    └── lens-request.md
```

## Version Log

| Date | Version | Change |
|------|---------|--------|
| 2026-07-30 | v0.1.x | Initial skill: 6 lenses, anti-bias gate, 4 frameworks |
| 2026-07-31 | v0.2.0 | Added Lens 07 (Exponential Potential), Safety Floor, ECR enforcement, generalized ledger |
| 2026-07-31 | v0.3.0 | Added Lens 08 (Risk of Ruin), adversarial audit, multi-persona, execution sprints, calibration, 3 domain playbooks |
| 2026-07-31 | v0.4.0 | Added Lens 09-15 (pricing, competitor, sifting, operations, growth, sales, capital allocation), operator-wisdom, mental-models, cognitive-biases-catalog, 4 deep research files |
| 2026-07-31 | v0.5.0 | **CRITICAL FIX.** Added Lens 16 (Distribution Engineering) as pre-gate. Added real-world-verification.md protocol — MANDATORY actual GitHub/web searches before any PASS. Added calibration-dataset.md (12 opportunities tested with real searches, exposing the skill's prior failure mode). Added AI dev tool bias counter-measure. The skill's #1 failure was producing confident PASS verdicts for saturated opportunities without actually searching — this version fixes that. |
| 2026-07-31 | v0.5.1 | **Calibration expansion.** Strengthened commercial verification (Search 5b: direct competitor web search added to real-world-verification.md — closes the MCP registry gap where GitHub showed low saturation but commercial competitors existed). Added examples/calibration-simulations.md — 30+ domains tested via mental simulation, identifying 10 cross-domain patterns. Added domain confidence adjustment matrix to SKILL.md (named tech -20%, regulated -25%, capital-intensive auto-REJECT, audience-dependent -30%, boring +10%, emerging -15%, platform-dependent -25%, etc.). Established 80/20 rejection rule: target 80% REJECT, 15% FLAG, <5% PASS for solo operators. The skill's success metric is now honestly skeptical — bad opportunities rejected fast, not opportunities found. |
| 2026-07-31 | v0.5.2 | **Demand validation infrastructure.** Added reddit-mining-protocol.md — structured 7-query Reddit mining with 10 demand clusters, access requirements (OAuth/PRAW), scoring system, anti-patterns. Added customer-interview-protocol.md — Mom Test 7-question framework, 3-tier commitment hierarchy, push-back move, scoring rubric, Sean Ellis PMF test integration. Added domains/boring-business-playbook.md — the +10% confidence domain that kept surfacing in calibration but had no playbook; covers HVAC/plumbing/electrical with 5 specific opportunities. Added 6 Reddit-mined opportunities to calibration-simulations.md. Reddit mining and customer interviews now MANDATORY in SKILL.md constraints. The skill now has both supply-side (GitHub, commercial) and demand-side (Reddit, interviews) verification before any PASS. |
| 2026-07-31 | v0.5.3 | **Execution enforcement + self-diagnostic.** Added pipeline-checklist.md — 11-phase, 60+ step mandatory execution checklist with reasoning trace. Every verdict must include completed checklist; every skipped step needs documented reason; no silent skips. Closes the v0.5.0 execution gap permanently — frameworks don't help if steps aren't executed. Added skill-health-diagnostic.md — 7 metrics (verdict distribution, PASS/REJECT accuracy, verification execution rate, per-lens accuracy, Brier score, skip reasons) with HEALTHY/WARNING/CRITICAL thresholds. The skill can now measure its own accuracy and detect miscalibration. Final end-to-end test run on HVAC dispatch opportunity: GitHub verified (4 repos, max 11 stars — early open-source), commercial verified (5+ funded competitors — saturated commercial), verdict FLAG (wedge: solo operators underserved, but commercial saturated). The pipeline produced the correct nuanced verdict, not a false PASS. |
| 2026-07-31 | v0.6.0 | **Intuition + contrarian + god-of-business gap closure.** Added Lens 17 (Intuition & Pattern Recognition) — distinguishes expert intuition (calibrated, 10,000+ hours, articulable) from amateur intuition (bias). 5 intuition signals, gut-analysis integration framework, calibration tracking. Closes the hyper-rationality flaw — the skill now blends analysis with intuition like Jobs/Musk/Buffett. Added Lens 18 (Market Consensus & Contrarian Positioning) — 3-layer consensus mapping (public/professional/capital), "Am I Right?" stress test, contrarian classification (insight/ignorance/ego/timing), Thiel secrets framework. Added god-of-business-gap-analysis.md — compared skill to composite of 12 greatest operators, identified 12 gaps, closed 6 (intuition, contrarian, obsession axis, second-order thinking, capital allocation as final gate, narrative check). 6 remaining gaps (product taste, people judgment, political navigation, Day 1 culture, time horizon flexibility, asymmetric conviction) acknowledged as requiring human operator. The skill is now 80% of the god of business; the human provides the remaining 20% (taste, people, politics, conviction). |
| 2026-08-01 | v0.7.0 | **Top 1% psychology & money-making mastery.** Added references/mindsets/top-1-percent-psychology.md (identity axis, fear/scarcity neutralization, ego discipline, anti-fragile feedback, mental energy, long-game/short-game, ruthless empathy) and references/frameworks/money-making-mastery.md (money equation, 5 money search paths, pricing power, money velocity, capital allocation, solo operator toolkit, anti-fragile money strategy). Added Elite Mandate final gate to SKILL.md (Identity Alignment, Money Equation, Anti-Fragility) — only opportunities passing all three move forward. |
| 2026-08-02 | v0.7.1 | **Elite cognitive weapons + compounding discipline + sales mastery.** Added references/mindsets/elite-cognitive-weapons.md (probabilistic thinking & EV, Bayesian updating, second-order thinking, inversion, negotiation psychology, ego kill switch, calm under ambiguity), references/mindsets/compounding-discipline.md (boring consistency, systems over goals, deep work, delayed gratification, sunk-cost immunity, energy management), references/frameworks/sales-and-negotiation-mastery.md (Cialdini stack, outcome-based selling, negotiation ladder, objection engineering, closing frames, elite cadence). Added Psychology/Execution routing row + Sales routing upgrade to SKILL.md, new Elite Cognitive Layer output section, 3 new constraint bullets. Regenerated SCHEMA.md file tree. |

## The v0.5.0 Lesson

The skill had all the right frameworks — anti-bias, adversarial, disconfirming
evidence — but still produced a wrong PASS verdict on the first real test. The
"AI context management CLI" opportunity was rated PASS, Tier 2, with a Single
Next Action to build it. When actual GitHub searches were run, the opportunity
had 533+ competing repos including 3 with >1,000 stars (largest: 19,514 stars).

**The problem wasn't the frameworks. The problem was that frameworks don't
search the web. The agent does. And the agent is biased toward confirming its
own analysis.**

The fix: mandatory real-world verification protocol that requires the agent to
actually execute GitHub API searches, Product Hunt searches, Google searches,
and Crunchbase searches — and report results — before any PASS verdict. The
data wins over the analysis.

This is the meta-lesson for AI cognition engines: the gap between "having the
right framework" and "doing the right thing" is execution. The skill must
enforce execution of verification, not just awareness of the need for it.

## Remix-Inspired Request / Response Data Contracts

Every cognitive interaction follows a strict typed data contract (modeled on standard web Request/Response schemas):

1. **Intake Request Schema (`Intake`):**
   - `mode`: `Quick Check` | `Standard` | `Deep Dive`
   - `intent_family`: `Discovery` | `Mispricing` | `Scaling` | `Validation` | ...
   - `capital_constraints`: Dollar or time availability
   - `risk_tolerance`: Low | Medium | High
   - `target_domain`: String description of industry/idea

2. **Cognitive Response Schema (`Response`):**
   - `verdict`: `PASS` | `FLAG` | `REJECT`
   - `asymmetry_score`: Calculated via `C × R × S × O × A / (1 + F)` (Range 0-32)
   - `adversarial_verdict`: `KILLED` | `SURVIVED` | `COULDN'T BREAK IT` (via Tri-Persona Collision)
   - `single_next_action`: Exact physical action to take today
   - `execution_artifacts`: Linked MVP JSON schema and unit economics skeleton

---

## Extension Points

New lenses → `references/lenses/`, listed in SKILL.md routing.
New frameworks → `references/frameworks/`.
New domain playbooks → `references/domains/`.
New references → `references/`.
New templates → `templates/`.
New examples → `examples/`.

See CONTRIBUTING.md for design principles and PR process.
