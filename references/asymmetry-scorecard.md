# Asymmetry Scorecard — Weighted Opportunity Evaluation

A complementary scoring tool to the 6 Pillars (`asymmetric-execution.md`)
and Lens 07 Exponential Potential. Where the 6 Pillars evaluate structural
quality and Lens 07 evaluates exponential ceiling, this scorecard evaluates
**the asymmetry of the bet itself** — is the payoff structure stacked in
your favor?

Use this **after** Lens 06 (anti-bias) and **before** Lens 07 (exponential
potential). It's the gate between "this is a real opportunity" and "this
is a venture-scale opportunity."

## The 5 Dimensions

| Dimension | Weight | Question | What Scores 5 | What Scores 1 |
|---|---|---|---|---|
| **Downside Capped** | 25% | If this fails completely, what do I lose? | Fixed, small, pre-committed cost. $0 exit. | Unlimited liability, debt, or reputation damage. |
| **Upside Uncapped** | 25% | If this works, is there a ceiling? | No structural ceiling; 100x+ possible. | Linear ceiling tied to my hours or capital. |
| **Information Asymmetry** | 20% | What do I know that the market hasn't priced? | Structural, durable info edge (regulatory, technical, network). | Nothing — I'm trading on public info everyone has. |
| **Speed Advantage** | 15% | Can I act faster than incumbents can react? | Days-to-weeks cycle; incumbents need quarters. | Same cycle time as everyone else. |
| **Resource Efficiency** | 15% | Output per dollar of resources invested? | Permissionless leverage; ~0 marginal cost. | Heavy capital/labor per unit output. |

## Scoring Rules

Score each dimension 1-5 (no zeros, no half-points). Multiply by weight.
Sum for total. Range: 1.0 - 5.0.

```
Total = (Downside × 0.25) + (Upside × 0.25) + (InfoAsym × 0.20)
        + (Speed × 0.15) + (Resource × 0.15)
```

### Decision Thresholds

| Score | Verdict | Action |
|---|---|---|
| **> 4.0** | STRONG ASYMMETRY | Pursue. Likely Tier 1 in Lens 07. |
| **3.5 - 4.0** | GOOD ASYMMETRY | Pursue. Likely Tier 2. Confirm with Lens 07. |
| **3.0 - 3.5** | MARGINAL | Flag. Only pursue if one dimension is exceptional AND user has specific edge. |
| **< 3.0** | WEAK ASYMMETRY | Reject or redesign. The bet isn't stacked in your favor. |

**Hard rule:** Only pursue if weighted score > 3.5/5. Below that, you're
gambling, not investing.

### Veto Dimensions

Two dimensions are quasi-veto. If either scores 1, the opportunity is
capped at MARGINAL regardless of total:

- **Downside Capped = 1** → unlimited liability. No score above 3.0.
  (You can lose more than you invested. This is how people go bankrupt.)
- **Upside Uncapped = 1** → linear ceiling. No score above 3.5.
  (Even a perfect linear business isn't asymmetric.)

## Worked Example

Opportunity: "Build an open-source CLI tool for solo developers, monetize
via hosted Pro tier at $9/mo."

| Dimension | Score | Weighted | Reasoning |
|---|---|---|---|
| Downside Capped | 5 | 1.25 | $200 + weekends. Fully reversible. Can abandon anytime. |
| Upside Uncapped | 4 | 1.00 | No structural ceiling, but realistic exit is $1-5M (acquisition). Not 100x. |
| Information Asymmetry | 3 | 0.60 | Solo-dev pain is real but not uniquely known to me. Others see it too. |
| Speed Advantage | 4 | 0.60 | I can ship in a weekend. Cursor/Continue need quarters to ship features. |
| Resource Efficiency | 5 | 0.75 | Pure code leverage. ~0 marginal cost per user. |
| **Total** | | **4.20** | STRONG ASYMMETRY |

**Verdict**: 4.20 > 4.0 → STRONG ASYMMETRY. Pursue. (Consistent with the
golden-output example in `examples/golden-output.md`.)

## Relationship to Other Frameworks

| Framework | Question Answered | When to Use |
|---|---|---|
| **6 Pillars** (asymmetric-execution.md) | Is the structural quality sound? | Evaluate any opportunity |
| **Asymmetry Scorecard** (this file) | Is the bet itself stacked in my favor? | After anti-bias passes, before exponential scoring |
| **Lens 07** (exponential-potential.md) | Is this 10x+ or linear-with-optimism? | After asymmetry scorecard passes 3.5 |

All three are complementary. An opportunity can pass 6 Pillars but fail the
Asymmetry Scorecard (good structure, bad bet shape). Or pass Asymmetry
Scorecard but fail Lens 07 (good bet shape, low exponential ceiling).

## Output Format

```
### Asymmetry Scorecard

| Dimension | Score (1-5) | Weighted | Reasoning |
|---|---|---|---|
| Downside Capped (25%) | | | |
| Upside Uncapped (25%) | | | |
| Information Asymmetry (20%) | | | |
| Speed Advantage (15%) | | | |
| Resource Efficiency (15%) | | | |
| **Total** | | **/5.00** | |

### Veto Check
- Downside Capped ≥ 2: PASS / FAIL
- Upside Uncapped ≥ 2: PASS / FAIL

### Verdict
STRONG / GOOD / MARGINAL / WEAK — [action]
```
