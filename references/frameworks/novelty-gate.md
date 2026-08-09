# Novelty & Clustering Gate — The "Same Old Ideas" Filter

## The Problem It Solves

The skill's research protocols scan outward, which means they surface what is
already hyped: agent economies, vertical SaaS, compliance tooling, longevity,
"personal AI sovereignty." An agent that evaluates whatever it searched for
will keep recommending the crowded categories of the year — the "same old
ideas" failure.

This gate runs **BEFORE** deep scoring, on any candidate that reached a
flattering verdict in early lenses. It separates **genuinely novel** from
**hyped-with-a-twist**.

## The Two-Filter Test

### Filter A — Category Clustering Quarantine

Ask: *Is this category already a hypothesis cluster?*

High clustering indicators (any 2 of these = quarantine):
- 5+ well-funded competitors OR 10+ active entrants in the past 12 months
- The idea is a direct instance of a category the market already names
  ("the agent economy," "AI compliance," "longevity biomarker," "AI SDR")
- Multiple "one-person unicorn" or "top emerging niches" listicles push the
  same category in the current cycle
- The candidate's headline is lay a familiar noun-verb phrase, e.g.
  "AI [domain] [does x]" with a generic vertical swapped in
- The pattern is "category + AI wrapper" rather than a new category, new
  underlying mechanism, or new unit of value

If quarantine triggers: **score novelty 0**, demote any "Tier 1" language,
and lower confidence by 15%. Do NOT proceed with novel-framing language —
the analysis still runs, but the verdict cannot be "genuinely novel."

### Filter B — Base-Rate Reality Pressure

Force a lookback base rate for the exact category (see lookback-validation):

| Base rate | Force action |
|-----------|--------------|
| < 15% empirical success in category | Cap verdict at FLAG; confidence −20 pts |
| < 8% | Force REJECT unless a specific structural edge (S≥2) is proven |
| Existing failures by well-funded operators | High alarm — REJECT unless a wedge they lacked is specified |

Hard rule: **if high-confidence hyptotypes crashed this year, the new
candidate is an echo, not a channel.** (Case study: AGENTS — independent
2026 experiments had agents work with real budgets for ~30 days: hundreds of
commits, dozens of endpoints, thousands of data points — $0 revenue. An
"agent civilization" or "agent commerce" pitch is now an echo of a proven,
tested failure of the underlying unit, not a discovery of a missing layer.)

## Verdict Consistency Law (automatic)

The final verdict must agree with the lowest pillar/z-efficient signal:

```
pillars <8                     -> no Tier 1/Moonshot language, no PASS
exponential veto failed         -> force Tier 3
base-rate < 15%                 -> cap at FLAG, never PASS
confidence > 35% without        -> discount by 15-20 pts as overconfidence
calibration evidence
```

An output that says "Tier 1 Moonshot" beside a 4/32 pillar score or a 15%
base rate is a **verdict leakage** — same implied-order the honesty of the
whole engine. Default to the lower tier when tiers disagree.

## The "Crazy but Real" Requirement

Users who ask for "something crazy / novel / exponential" usually do NOT
want a new coat of paint on a trending category — they want a genuine
novelty: a new underlying structure of value, or new unit of control that
touches a force nobody institutions the category.

- If the candidate is exciting-but-clustered → REJECT as novelty, it's the
  current hype, not a novel bet
- If the candidate is novel but unbuildable solo → still valid, mark it
  "pipedream" tier, and structure a reversible ladder of tests, don't
  reject for size alone
- If the candidate is failing base rates of exact adjacent
  failures → REJECT with the failure record shown

The gate's output is one of: **NOVEL / CLUSTERED / ECHO**. Only NOVEL can
qualify for a PASS-class verdict from this gate.

## Integration

Runs before Lens 07 and before the 6-Pillar scoring, and again before any
verdict, as a veto check. The agent MUST state the gate result in the final
brief header: `Novelty Gate: NOVEL / CLUSTERED / ECHO`.