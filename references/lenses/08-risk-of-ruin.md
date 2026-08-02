# Lens 08: Risk of Ruin — Can You Survive Losing This Bet?

## Core Question

If this opportunity goes to zero, what happens to you — and can you
survive it?

This is the question the Capital Check in Lens 06 tries to answer but
doesn't. "How much money is needed to start" is a cost question. "What
happens to this person if it goes to zero" is a survival question.
Someone with $2K in savings and someone with $200K have wildly different
affordable-loss thresholds for the same "flag capital $500" verdict.

## When to Use

- **ALWAYS** when the opportunity involves financial commitment >$100
- **ALWAYS** when the opportunity involves >10 hours/week commitment
- **ALWAYS** when the opportunity could create liability (legal, contractual, debt)
- When user has limited runway (<6 months)
- When user is considering quitting a job to pursue this
- When the opportunity involves irreversible commitments (leases, hires, inventory)

## When NOT to Use

- Zero-capital validation experiments (the 7-day test) — ruin is impossible
- Pure information-gathering activities (research, interviews)
- Reversible actions with no financial commitment

## The 4 Risk-of-Ruin Checks

### Check 1: Total Resource Exposure

```
What is the total commitment if this goes to zero?

Financial:
  - Direct capital at risk: $[X]
  - Committed ongoing costs (hosting, subscriptions, contractors): $[Y]/month
  - Liability exposure (leases, contracts, debt): $[Z]
  - Opportunity cost (foregone income during commitment): $[W]

Time:
  - Hours/week: [H]
  - Weeks until kill criteria trigger: [N]
  - Total hours at risk: [H × N]

Reputation:
  - Does this put my name/public identity at risk? [yes/no]
  - Does this affect relationships I rely on? [yes/no]
  - If this fails publicly, how visible is the failure? [low/medium/high]

TOTAL EXPOSURE:
  Financial: $[X + Y×N + Z + W×N/4]  (rough)
  Time: [H × N] hours
  Reputation: [risk level]
```

### Check 2: Survival Capacity

```
If the total exposure is lost, can I survive?

Financial survival:
  - Current liquid savings: $[S]
  - Monthly burn rate (all expenses): $[B]
  - Runway without this opportunity's income: [S / B] months
  - Runway if this opportunity loses the full exposure: [(S - Total Exposure) / B] months

  If post-loss runway < 3 months → REJECT. You cannot afford this bet.
  If post-loss runway 3-6 months → FLAG. Only proceed if user explicitly
    acknowledges risk and has backup plan.
  If post-loss runway > 6 months → PASS this check.

Time survival:
  - Does this time commitment put at risk essential income-generating work?
    YES → REJECT or reduce commitment.
    NO → PASS.

Reputation survival:
  - If this fails publicly, can I recover?
    Cannot recover (fraud, harm to others) → REJECT. Floor violation.
    Slow recovery (visible failure, industry-specific) → FLAG. Proceed with caution.
    Easy recovery (small project, no public stakes) → PASS.
```

### Check 3: Kelly Criterion (Position Sizing)

The Kelly criterion calculates the optimal fraction of your bankroll to
bet, given the probability of winning and the payoff ratio.

```
Kelly fraction = p - (1-p)/b

Where:
  p = probability of success (from your confidence level, honestly assessed)
  b = ratio of potential gain to potential loss (net win / net loss)

Example:
  p = 0.60 (60% confident)
  Potential gain: $50,000
  Potential loss: $5,000
  b = 50,000 / 5,000 = 10

  Kelly = 0.60 - (0.40 / 10) = 0.60 - 0.04 = 0.56

  Full Kelly: bet 56% of bankroll
  Half Kelly (recommended): bet 28% of bankroll
  Quarter Kelly (conservative): bet 14% of bankroll
```

**Rules:**
- Never bet full Kelly. Use half-Kelly or quarter-Kelly.
- If Kelly fraction is negative → the bet is bad. Don't make it.
- If Kelly fraction > 50% even at half-Kelly → your confidence is probably
  too high. Re-examine.
- If the required position exceeds Kelly → reduce commitment. Bet smaller.

**For non-financial bets** (time, reputation), apply the same logic:
- What fraction of your available time can you afford to lose?
- What fraction of your reputation capital can you afford to stake?

### Check 4: Correlated Risk

```
Is this bet correlated with other risks I'm already carrying?

Examples of correlation:
  - Another startup I'm involved in (time correlation)
  - A job in the same industry (income correlation)
  - Crypto holdings if this is a crypto play (asset correlation)
  - Real estate in the same market (geographic correlation)
  - Relationships with the same people (social correlation)

If correlated:
  - Treat the combined exposure as one bet, not two.
  - REJECT if combined exposure exceeds survival capacity.
  - FLAG if combined exposure is 50%+ of survival capacity.

The 2008 financial crisis killed people who had: job in finance + house
in finance-heavy market + 401k in financial stocks. Three "independent"
bets that were actually one correlated bet.
```

## Decision Matrix

```
Check 1 (Exposure) | Check 2 (Survival) | Check 3 (Kelly) | Check 4 (Correlation) | Verdict
-------------------|---------------------|------------------|-----------------------|--------
  Manageable       |  PASS               |  Positive        |  Uncorrelated         | PASS
  Manageable       |  PASS               |  Positive        |  Correlated           | FLAG (reduce size)
  Manageable       |  FLAG               |  Positive        |  Uncorrelated         | FLAG
  Large            |  PASS               |  Positive        |  Uncorrelated         | FLAG (reduce size)
  Large            |  FLAG               |  Positive        |  Any                  | REJECT
  Any              |  REJECT             |  Any             |  Any                  | REJECT
  Any              |  Any                |  Negative        |  Any                  | REJECT (bad bet math)
  Any              |  Any                |  Any             |  Highly correlated    | REJECT
```

## Position Sizing Recommendation

If the opportunity passes all 4 checks, the skill outputs a recommended
position size:

```
## Position Size Recommendation

Based on:
  - Confidence: [X]%
  - Payoff ratio: [b]
  - Kelly fraction: [K]
  - Survival capacity: [Y] months post-loss

Recommended commitment:
  Financial: $[min(Half-Kelly × bankroll, Survival-cap-based limit)]
  Time: [max hours/week that preserves essential income work]
  Reputation: [stake level: low/medium/high]

Hard ceiling:
  Do not commit more than $[Z] or [H] hours/week, regardless of confidence.

Rationale:
  [Why this size, not larger or smaller]
```

## Integration with Effectuation

This lens operationalizes Effectuation's **Affordable Loss** principle
(Sarasvathy, 2001). The question is never "how much could I make?" but
"what's the most I can lose, and can I absorb it?"

From `references/frameworks/effectuation.md`:
> Invest only what you're willing to lose. Never project returns — calculate
> maximum downside instead.

Lens 08 makes this concrete: it computes the maximum downside, checks
whether you can absorb it, and recommends a position size that keeps you
in the game even if the bet fails.

## Bias Warnings

- **Overconfidence in probability**: Most people (and AI agents) overestimate
  p. Use the calibration-adjusted confidence from
  `references/calibration-protocol.md` if available. If not, discount
  raw confidence by 15-20%.
- **Underestimating correlation**: Almost everything is more correlated
  than it looks. When in doubt, assume correlation.
- **Ignoring time as a resource**: Time at risk is a real cost. A 6-month
  commitment to a failing opportunity isn't "free" just because it costs
  $0 — it's 6 months of foregone other opportunities.
- **Reputation is non-renewable**: Financial losses can be earned back.
  Reputation losses, in some domains, cannot. Weight reputation risk
  higher than financial risk for high-visibility bets.

## Weak Link: What Kills This Survival Check?

```
Is the user's financial situation accurately known?
  NO (no intake, no autonomous default that fits) → Flag. Use conservative defaults.

Is the confidence level honestly assessed (not overconfident)?
  NO → Discount confidence by 20% before computing Kelly.

Are there hidden commitments not captured in direct capital?
  YES (contracts, ongoing obligations, opportunity cost) → Add to exposure.

Is the bet actually uncorrelated with user's other risks?
  UNCERTAIN → Assume correlation. Treat conservatively.

Does the user have a backup plan if this fails?
  NO → Flag. Survival capacity should assume no external rescue.
```

## Output

```
### Risk of Ruin Analysis

#### Total Resource Exposure
- Financial at risk: $[X]
- Time at risk: [H hours over N weeks]
- Reputation at risk: [level]

#### Survival Capacity
- Post-loss runway: [months]
- Verdict: PASS / FLAG / REJECT

#### Kelly Position Sizing
- Confidence (adjusted): [X]%
- Payoff ratio: [b]
- Kelly fraction: [K]
- Recommended position: [half-Kelly × bankroll]

#### Correlation Check
- Other risks: [list]
- Correlation: low / medium / high
- Verdict: PASS / FLAG / REJECT

#### Overall Risk-of-Ruin Verdict
PASS / FLAG / REJECT — [reasoning]

#### Position Size Recommendation
- Financial: $[Z] (ceiling: $[ceiling])
- Time: [H] hrs/week (ceiling: [H_max])
- Reputation: [level]

#### Hard Kill
If user cannot survive losing this bet, the opportunity is rejected
regardless of any other PASS verdict. Survival trumps opportunity.
```

---

## Decision Protocol

### Exact Question This Lens Answers
"If this opportunity goes to zero, what happens to me — and can I
survive it?"

### Data Required
- Total resource exposure (financial, time, reputation)
- User's survival capacity (runway, burn rate, backup plan)
- Kelly fraction computation (confidence × payoff ratio)
- Correlation analysis with user's other risks
- User's financial situation (from intake or conservative autonomous defaults)

### Confidence Threshold
- **PASS (proceed)**: Post-loss runway >6 months, Kelly fraction positive, low correlation, survival capacity intact
- **FLAG (proceed with reduced position)**: Post-loss runway 3-6 months, OR moderate correlation, OR Kelly fraction small
- **REJECT (do not proceed)**: Post-loss runway <3 months, OR Kelly fraction negative, OR high correlation, OR survival capacity compromised

### Conflict Resolution Rules
- **Lens 08 is a hard veto.** If Lens 08 says REJECT, the opportunity is rejected regardless of what any other lens says. Survival trumps opportunity. No exceptions.
- When Lens 08 disagrees with Lens 07 (Exponential):
  - Tier 1 moonshot + risk of ruin REJECT → **reject**. You cannot afford this bet.
  - Tier 1 moonshot + risk of ruin PASS → **proceed with small position**. Reduce commitment to half-Kelly or quarter-Kelly.
- When Lens 08 disagrees with Lens 06 (Anti-Bias):
  - Anti-bias PASS + risk of ruin REJECT → **reject**. Survival wins.
  - Anti-bias FLAG + risk of ruin PASS → **consider upgrade to PASS**. The flag may have been capital-related; risk of ruin clears it.
- When Lens 08 disagrees with user's stated desire to proceed:
  - Lens 08 wins. The user can override, but the skill must explicitly warn: "This bet can ruin you. Proceed only if you accept that outcome."
- When user's financial situation is unknown (autonomous mode, no intake):
  - Use conservative defaults ($0 capital, 0-3 month runway). This will reject most capital-intensive opportunities. That's correct — don't recommend bets you can't verify the user can survive.
- When correlation is uncertain:
  - Assume correlation. Treat conservatively. Almost everything is more correlated than it looks.
