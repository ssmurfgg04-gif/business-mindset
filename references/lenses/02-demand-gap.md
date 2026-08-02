# Lens 02: Demand Gap — What Do People Want That Nobody Provides?

## Core Question
Where is there clear, validated desire for a solution that doesn't adequately exist?

## When to Use
- User asks "what's missing in [market]"
- User says "what do people need"
- User wants to find underserved niches

## Search Strategies

### Customer Complaint Mining
```
site:reddit.com/r/[industry] "I wish" OR "why can't" OR "nobody offers"
site:reddit.com/r/[industry] "worst part" OR "frustrating" OR "hate"
site:trustpilot.com [competitor] negative review
site:g2.com [competitor] cons complaints
[industry] complaints [year]
[product] "wish it had" OR "missing feature"
```

### Workaround Detection
```
[task] how to do without [tool/software]
[problem] manual workaround
[goal] alternative to [expensive solution]
```
If people are using hacks, duct tape, or manual processes, that's demand.

### "Already Paying" Signals
```
[industry] [niche] freelancer hiring
[industry] [niche] consultant rates
[industry] [niche] "how much does it cost"
```
People paying for a service = validated demand. If the service is manual, there's
an opportunity to automate or systematize.

### Forum/Tool Analysis
Look for:
- GitHub issues requesting features that don't exist
- Stack Overflow questions with no good answers
- Product Hunt launches with high upvotes but no real solution
- Niche subreddits where the same question gets asked weekly

## The Demand Clarity Spectrum

```
Clear demand (spend money)       Fuzzy demand (wish, interesting)
        |                                  |
        v                                  v
  Already paying for            "Someone should build..."
  a solution that's             "Why doesn't X exist?"
  expensive/slow/bad            "I would use..."
        |                                  |
        +------------------+------------------+
                           v
              Prioritize clear over fuzzy.
              Fuzzy needs validation before build.
```

## What to Extract

| Gap Type | Evidence | Priority |
|----------|----------|----------|
| Paid workaround, no good tool | "I pay $500/mo for X but it's terrible" | Highest |
| Repeated complaint, no solution | "Every week someone asks for Y" | High |
| One-off complaint | "This one person wants Z" | Investigate |
| "I wish" without action | "Someone should build..." | Low |

## Bias Warnings
- Reddit complaints are amplified. Distinguish between "annoying" and "will pay."
- "I'd use that" means nothing. "I'd pay for that" means slightly more.
- The loudest complaints often belong to the smallest markets.
- If the market gap has been open for 5+ years, there's probably a structural
  reason it hasn't been filled. Ask why before assuming you can.

## ECR Phase Discipline

### Expansion Phase Output (generate 15-20+)
List 15-20+ raw demand gaps. No filtering. Each entry:
- Gap description: <one-line>
- Evidence: <quote, source, frequency>
- Demand clarity: clear / fuzzy
- Why existing solutions miss it: <one sentence>

### Contraction Phase Output (reduce to 3-5)
Apply weak-link elimination. Reduce to 3-5 survivors with explicit kill
reasons for the 10-15 eliminated.

## Weak Link: What Kills This Demand Gap?

```
Is someone already paying for a solution (even a bad one)?
  NO -> Eliminate. Complaints without payment aren't demand.

Is the gap structural (hard to solve) or merely unattended?
  Unattended -> Why hasn't anyone fixed this? Check for hidden barriers.
  Structural -> Hard to solve = opportunity if you have a novel approach.
               Hard to solve = trap if you don't.

Does solving this require behavior change?
  YES -> Eliminate unless the pain is acute (regulatory, compliance).
  NO  -> Better. People want to keep doing what they do, just better/cheaper.

Is the market large enough to matter?
  If the gap serves < 1000 people who'd pay $100/yr -> likely too small.

Is there a clear willingness-to-pay signal?
  "I wish" -> Low confidence. Investigate further.
  "I pay $X for..." -> High confidence. This is real demand.
  Evidence of manual workaround costing time/money -> Highest confidence.

What would prevent you from building this?
  Patent? Regulation? Incumbent with 90% market share?
  Any of these -> Flag for anti-bias audit.

Does this gap indicate exponential potential (Lens 07)?
  YES if: gap is structural (regulatory, tech inflection), serves a growing
          audience, can be solved with permissionless leverage, and creates
          a reflexive loop (each new user benefits existing users).
  NO if: gap is one-off, requires labor leverage, no network effect.
```

## Time Horizon Tagging

Each demand gap should be tagged:

| Gap Type | Typical Time-to-Validation |
|---|---|
| Paid workaround (manual today) | <7 days (pre-sell automation) |
| Recurring complaint, no solution | 14-30 days (interview + mockup) |
| Fuzzy "I wish" | 30-90 days (needs audience validation) |
| Behavior-change-required | 90+ days (high friction) |

If the user has <14 days, filter to gaps with manual-workaround evidence.

## Output

### Expansion Phase
List 15-20+ demand gaps with all fields above.

### Contraction Phase
List 3-5 surviving gaps, each with:
- Gap description
- Evidence (quote, source, frequency)
- Demand clarity (clear/fuzzy)
- Why existing solutions miss it
- Ballpark willingness to pay
- Time-to-validation horizon
- Kill reason for the 10-15 eliminated gaps (one sentence each)

---

## Decision Protocol

### Exact Question This Lens Answers
"Is there validated desire for a solution that doesn't adequately exist —
and will people pay for it?"

### Data Required
- Minimum 3 complaint sources (Reddit, G2, Trustpilot, niche forums)
- At least 1 willingness-to-pay signal ("I pay $X for..." or freelancer/consultant rates in the space)
- At least 1 workaround evidence (manual process, duct-tape solution)
- Failure-case search: have others tried to fill this gap and failed?

### Confidence Threshold
- **Deploy (build/proceed)**: ≥75% confidence, clear WTP signal, workaround evidence present
- **Flag (validate further)**: 50-75% confidence, fuzzy demand, no WTP signal
- **Discard**: <50% confidence, or complaints without payment evidence

### Conflict Resolution Rules
- When Lens 02 (Demand) disagrees with Lens 01 (Signal):
  - Demand present + signal absent → **early, hidden opportunity**. Pursue.
  - Demand absent + signal present → **hype, not opportunity**. Discard.
- When Lens 02 disagrees with Lens 04 (Leverage):
  - Demand present + no viable leverage → **service business**. Accept Tier 3, or wait.
  - Demand present + code leverage viable → **strong opportunity**. Both lenses agree.
- When Lens 02 disagrees with Lens 06 (Anti-Bias):
  - Anti-bias wins. Demand doesn't override saturation/moat problems.
- When demand clarity is fuzzy but signal is strong:
  - Run Lens 02 expansion again with different search strategies. If still fuzzy, defer.
