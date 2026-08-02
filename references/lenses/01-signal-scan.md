# Lens 01: Signal Scan — Where Is Money Flowing, Stuck, or Leaking?

## Core Question
Where is capital, attention, or demand concentrating — and where is it blocked?

## When to Use
- User asks "find me an opportunity in [domain]"
- User wants to know what's trending or emerging
- User says "I have no idea what to do"

## Search Strategies

### Web Search
```
[industry] market size growth rate [year]
[industry] venture capital investment trends
[industry] funding rounds 2026
[industry] revenue growth leaders
[industry] "hiring surge" OR "expansion"
```

### GitHub Search
Use `gh_grep` or the GitHub API to find:
- Repos with rapid star growth in a domain
- Underserved tooling gaps (check issue templates, "feature request" labels)
- Niche CLI tools, internal tool patterns being open-sourced
- Trending repos that solve real operational problems

### Arxiv Search
```
site:arxiv.org [domain] survey 2025 2026
site:arxiv.org [domain] emerging technology
```
Look for papers that describe new capabilities — these create new markets.

### Social Signals
- Reddit: `site:reddit.com/r/[niche] "anyone else" OR "I wish" OR "why can't"`
- Twitter/X: trending topics, viral threads about operational pain
- Niche forums: what are the most-engaged posts about?

## What to Extract

| Signal Type | What it means | Example |
|-------------|---------------|---------|
| Rapid hiring | Company is investing in a direction | "Startup hired 3 SREs in a month" |
| Funding surge | Capital is flowing into a space | "$500M into AI dev tools this quarter" |
| Price increases | Demand exceeds supply | "AWS prices up 15% YoY" |
| Regulatory shifts | New rules create compliance needs | "EU AI Act enforcement begins" |
| Tool gaps | Friction nobody has solved | "No good open-source tool for X" |
| Skill shortages | People will pay for expertise | "Can't find engineers who know Y" |
| Reflexive narratives | Crowd narrative forming around a category | "The Stripe of X" / "This changes everything" |

## Bias Warnings
- Funding != market readiness. Many funded spaces are hype, not demand.
- GitHub stars != business opportunity. Many starred repos are fun, not needed.
- Trends change fast on social. Validate with at least two independent sources.
- Reflexive narratives are themselves signals (Lens 07 Signal 6 — Reflexivity),
  but they cut both ways. Track the narrative AND the underlying fundamentals.

## ECR Phase Discipline

### Expansion Phase Output (generate 15-20+)
List 15-20+ raw signals with source citations. No filtering. Include weak
signals — they reveal adjacencies. Each entry:
- Signal: <one-line description>
- Source: <URL or search query>
- Type: funding | hiring | price | regulatory | tool-gap | skill-shortage | narrative
- Structural or hype?: <one sentence>
- Confidence: high/medium/low (based on corroboration)

Do NOT collapse to top 5 prematurely. The 15-20+ quota is enforced by ECR
(see `references/frameworks/ecr-model.md`).

### Contraction Phase Output (reduce to 3-5)
Apply weak-link elimination. Reduce to 3-5 survivors with explicit kill
reasons for the 10-15 eliminated. The kill log is valuable — it documents
what was considered and rejected.

## Weak Link: What Kills This Signal?

A signal is only valuable if it leads somewhere real. Eliminate signals
that fail any of these checks:

```
Is there a clear path from signal to transaction?
  NO -> Eliminate. A trend with no monetization path is noise.

Is the signal corroborated by 2+ independent sources?
  NO -> Flag as low-confidence. Don't act on single-source signals.

Is the signal driven by structural change (not hype)?
  Hype -> Eliminate unless timing is explicit (e.g., regulatory deadline).
  Structural -> Keep. Regulatory shifts, demographic changes, tech inflection.

Can this signal be acted on with zero capital in <7 days?
  NO -> Flag for leverage map. Some signals require resources.
  YES -> Prioritize. Fast validation is the single greatest advantage.

Does this signal benefit incumbents OR outsiders?
  Incumbents -> The signal may not be an opportunity for newcomers.
  Outsiders -> Better. Look for displacement potential.

Does the signal indicate exponential potential (Lens 07)?
  Strong power-law indicators (network effects, permissionless leverage, reflexive loop)
    -> Flag for Lens 07 evaluation. May be Tier 1.
  Linear indicators (hiring, gradual price increases)
    -> Tier 2/3 at best. Still useful, but set expectations.
```

## Time Horizon Tagging

Each signal should be tagged with expected timeline to monetization:

| Signal Type | Typical Time-to-Monetization |
|---|---|
| Funding surge | 12-24 months (when funded companies ship) |
| Regulatory shift | 6-18 months (depends on enforcement date) |
| Tool gap | 1-6 months (if you can build the tool) |
| Skill shortage | 3-12 months (if you can sell expertise) |
| Reflexive narrative | 3-9 months (window before reflexivity reverses) |
| Price increase | 1-6 months (if you can offer alternative) |

If the user has <3 months runway, filter to signals with <6 month monetization.

## Output

### Expansion Phase
List 15-20+ signals with all fields above.

### Contraction Phase
List 3-5 surviving signals, each with:
- What the signal is
- Source (URL or search query)
- Why it matters (what it implies about opportunity)
- Confidence (high/medium/low based on corroboration)
- Time-to-monetization horizon
- Kill reason for the 10-15 eliminated signals (one sentence each)

---

## Decision Protocol

### Exact Question This Lens Answers
"Where is capital, attention, or demand concentrating right now — and is
that concentration structural or hype?"

### Data Required
- Minimum 3 independent sources (web, GitHub, social, VC)
- At least 1 quantitative signal (funding amount, growth rate, price change)
- At least 1 qualitative signal (complaint pattern, narrative formation)
- Failure-case search results (see research-protocols.md)

### Confidence Threshold
- **Deploy (act on signal)**: ≥70% confidence, corroborated by 2+ independent sources, structural driver identified
- **Flag (investigate further)**: 50-70% confidence, single-source or hype-driven
- **Discard**: <50% confidence, or single-source with no structural driver

### Conflict Resolution Rules
- When Lens 01 (Signal) disagrees with Lens 02 (Demand Gap):
  - Signal present + demand absent → **hype, not opportunity**. Demand Gap wins.
  - Signal absent + demand present → **early, hidden opportunity**. Signal Scan loses; pursue with extra caution.
- When Lens 01 disagrees with Lens 06 (Anti-Bias):
  - Anti-bias always wins. A strong signal that fails saturation/moat checks is noise.
- When Lens 01 disagrees with Lens 07 (Exponential):
  - Signal may be real but linear. Lens 01 says "money is flowing"; Lens 07 says "but it's linear flow." Both correct; set Tier 2/3 expectations.
- When multiple signals conflict:
  - Structural signals (regulation, demographic, tech inflection) override narrative signals (funding hype, social buzz).
