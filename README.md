# business-mindset

> General-purpose business cognition engine — 7 cognitive lenses + anti-bias gate + asymmetric execution frameworks + exponential potential scoring. Domain-agnostic. No saturated-market defaults.

A skill for AI coding agents (opencode, Cursor, etc.) that turns the agent into a business cognition engine. It doesn't generate business ideas directly — it applies structured cognitive lenses to systematically deconstruct markets and surface asymmetric, capital-efficient, exponential-potential opportunities.

## What it does

When a user asks "find me an opportunity in X", "analyze this market", "stress-test my idea", or "is this venture-scale?", the skill:

1. Loads the Fang Yuan meta-OS (cold rationality, zero ego) + Operator Personas framework
2. Selects the right cognitive lens(es) based on intent (8 lenses, 12 intent families)
3. Loads domain playbook if applicable (tech-saas / services / physical-products)
4. Dispatches parallel research sub-agents (web, GitHub, arxiv, VC, social) + runs mandatory failure-case searches
5. Runs ECR pipeline: expansion (15-20+ candidates) -> contraction (weak-link elimination) -> realism (match to user)
6. Applies 6-pillar asymmetric execution scoring + asymmetry scorecard
7. Applies 10-signal exponential potential scoring with tier rating (Moonshot / Scalable / Linear)
8. Runs anti-bias gate: 5 hard checks + 5-minute bias checklist + disconfirming evidence search + adversarial audit (red team)
9. Runs risk-of-ruin check (Kelly criterion, hard veto — survival trumps opportunity)
10. Runs multi-persona synthesis (Operator + Steward + Adversary)
11. Runs pre-mortem with explicit kill thresholds
12. Outputs a structured Opportunity Brief with: Single Next Action (today) + 2-week sprint plan + decision journal prompt
13. Tracks outcomes for calibration (monthly/quarterly/annual reviews adjust future confidence)

## The 16 Lenses

| # | Lens | Question |
|---|---|---|
| 01 | Signal Scan | Where is money flowing, stuck, or leaking? |
| 02 | Demand Gap | What do people want that nobody provides? |
| 03 | Arbitrage Pattern | Where is value systematically mispriced? (7 types) |
| 04 | Leverage Map | What force multiplier fits? (code/media/network/labor/capital) |
| 05 | Network Path | Who owns distribution? |
| 06 | Anti-Bias Audit | Is this actually good or just familiar? (hard gate + bias checklist + adversarial pass + **MANDATORY real-world verification**) |
| 07 | Exponential Potential | Is this 10x+ or just linear with optimism? (10 signals + veto) |
| 08 | Risk of Ruin | Can you survive losing this bet? (Kelly criterion, HARD VETO) |
| 09 | Pricing Power | Can I raise prices without losing customers? (6 archetypes, tier design, increase protocol) |
| 10 | Competitor Teardown | Where is the incumbent weak? (5-stage protocol, Helmer 7 Powers, counter-positioning) |
| 11 | Opportunity Sifting | Which 1 of 50 opportunities should I pursue? (5-stage pipeline with adversarial pass) |
| 12 | Business Operations | What's needed to run this? (legal, financial, team, compliance stack) |
| 13 | Growth & Scaling | How do I grow effectively? (4-stage framework, what NOT to do yet) |
| 14 | Negotiation & Sales | How do I close deals and win terms? (Voss, Ury, SPIN, Challenger, MEDDIC, Cialdini) |
| 15 | Capital Allocation | How do I fund and allocate capital? (funding strategy, Buffett-style allocation, term sheets) |
| 16 | Distribution Engineering | How do I engineer distribution BEFORE building? (#1 determinant for solo operators, PRE-GATE) |

## The 8 Frameworks

- **Fang Yuan Mindset** — meta-OS. Zero emotion, zero ego. Non-negotiable Safety Floor.
- **Operator Personas** — Operator (cold) + Steward (relational) + Adversary (red team).
- **Operator Wisdom** — 20 principles distilled from 27 greatest operators (Musk, Jobs, Bezos, Buffett, Munger, Rockefeller, Walton, Morita, Honda, etc.)
- **Mental Models** — 40 models across 5 disciplines (decision-making, systems thinking, cognitive biases, strategy, cross-disciplinary)
- **ECR Model** (Ramoglou et al., 2026, *JMS*) — Expansion-Contraction-Realism. Enforces 15-20+ expansion quota.
- **Effectuation** (Sarasvathy, 2001, *AMR*) — Means-driven entrepreneurial logic.
- **Asymmetric Execution** — 6 pillars with computable Systemic Edge formula.

## The 3 Domain Playbooks

- **Tech/SaaS** — zero-marginal-cost environments, code leverage default, GitHub/SEO distribution
- **Services** — labor leverage, productization path, burnout check, reputation as moat
- **Physical Products** — capital leverage, inventory risk, brand as moat, multi-channel distribution

## Execution Infrastructure

- **Adversarial Audit** — red team pass mandatory after Lens 06 PASS. Runs 5 disconfirming evidence searches, constructs attacks, tries to kill the idea.
- **Execution Sprints** — converts PASS into ONE single next action + 2-week experiment with pre-committed kill criteria. Anti-analysis-paralysis.
- **Decision Journal** — pre-decision predictions + post-outcome tracking. Raw material for calibration.
- **Calibration Protocol** — monthly (30 min), quarterly (2 hr), annual (4-8 hr) reviews. Computes per-lens accuracy, applies confidence adjustments.
- **Asymmetry Scorecard** — weighted 5-dimension scorecard (downside, upside, info asymmetry, speed, resource efficiency). Threshold >3.5/5.

## Installation

This skill follows the standard opencode skill structure. To install:

1. Clone this repo into your skills directory:
   ```bash
   git clone https://github.com/ssmurfgg04-gif/business-mindset.git ~/.config/opencode/skills/business-mindset
   ```

2. (If using opencode) Restart opencode or reload skills.

3. Test by asking your agent: "Find me an opportunity in [your domain of interest]."

## Repository Structure

```
business-mindset/
├── SKILL.md                          ← Entry point. Routed first on trigger.
├── SCHEMA.md                         ← Tree structure + file map + version log.
├── README.md                         ← This file.
├── LICENSE                           ← MIT.
├── CONTRIBUTING.md                   ← How to extend the skill.
├── references/
│   ├── research-protocols.md         ← How to search each source.
│   ├── subagent-prompts.md           ← Copy-pasteable sub-agent dispatch templates.
│   ├── intake.md                     ← Optional user intake protocol.
│   ├── ledger.md                     ← Generalized position & P&L tracking schema.
│   ├── exponential-research.md       ← Source research for Lens 07 (70 sources).
│   ├── lenses/
│   │   ├── 01-signal-scan.md
│   │   ├── 02-demand-gap.md
│   │   ├── 03-arbitrage-pattern.md
│   │   ├── 04-leverage-map.md
│   │   ├── 05-network-path.md
│   │   ├── 06-anti-bias-audit.md
│   │   └── 07-exponential-potential.md
│   └── frameworks/
│       ├── fang-yuan-mindset.md
│       ├── ecr-model.md
│       ├── effectuation.md
│       └── asymmetric-execution.md
├── examples/
│   └── golden-output.md              ← Worked opportunity brief example.
└── .github/
    └── ISSUE_TEMPLATE/
        ├── bug-report.md
        └── lens-request.md
```

## Key Features

- **Anti-bias gate**: Hard checks against AI's default patterns (SaaS defaults, newsletter defaults, marketplace defaults). Won't let the agent suggest saturated plays.
- **Exponential potential scoring**: 10-signal rubric (MTP, permissionless leverage, power-law tail, convexity, reflexivity, network effects, pre-chasm, MTP, asymmetric bet, etc.) with 3 veto signals and 4-tier rating.
- **Anti-pattern library**: 10 "fake exponential" patterns (WeWork, Quibi, Theranos, MoviePass, Blue Apron, etc.) with why each failed.
- **Pre-mortem mandatory**: Every PASS verdict must articulate 3 failure modes with observable leading indicators and kill thresholds.
- **Outcomes feedback loop**: Tracks historical analysis accuracy per lens; calibrates future confidence based on track record.
- **Generalized ledger**: Supports trades, SaaS, services, content, partnerships, products — not just crypto positions.
- **ECR enforcement**: 15-20+ candidates per lens in expansion before any contraction. Kill log documents what was considered and rejected.

## Operating Modes

- **Quick Check** ("is X worth pursuing?") — Lens 06 only, 5-min response
- **Standard** ("find me an opportunity in X") — 2-3 lenses + 06 + 07, 15-min response
- **Deep Dive** ("full treatment on X") — All 7 lenses + 4 frameworks + sub-agents, 30-60 min

## Autonomous Mode

The skill operates autonomously by default. It does not require user intake
to produce actionable analysis. If the user explicitly wants personalized
analysis, an optional intake protocol is available (see `references/intake.md`).

## Safety Floor

The Fang Yuan Mindset's cold rationality is a cognitive tool for analysis,
**not** a license for predation. Hard limits (see `references/frameworks/fang-yuan-mindset.md`):

1. No fraud, deception, or ToS violation.
2. No exploiting identifiable vulnerable parties.
3. Flag harm to third parties explicitly.
4. Do not bypass KYC on financial platforms.

## License

MIT — see [LICENSE](LICENSE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New lenses, frameworks, anti-patterns,
and worked examples are all welcome.

## Topics

`skill`, `business`, `opencode`, `ai-prompt`, `entrepreneurship`, `cognitive-lenses`, `anti-bias`, `exponential-potential`
