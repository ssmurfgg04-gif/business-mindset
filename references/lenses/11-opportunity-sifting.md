# Lens 11: Opportunity Sifting — Sorting 50 Raw Signals Down to 3 Worth Pursuing

<lens>
<core_question>
Given a raw pool of opportunities (from Lens 01-05, 07-10), which 3 are worth
the user's finite time and capital — and which 47 should be killed, with reasons?
</core_question>

<when_to_use>
- After running multiple lenses in expansion mode (ECR Phase 1)
- Before ECR Phase 2 contraction — this IS the contraction methodology
- When user says "I have too many ideas" or "which of these should I pursue?"
- After Lens 06 has flagged/rejected the obvious bad ones
- When deciding between 2-5 surviving opportunities
</when_to_use>

<when_not_to_use>
- Single opportunity evaluation (use Lens 06 + 07 + 08 directly)
- Pre-expansion (need 15-20+ candidates first; sifting 3 is premature contraction)
</when_not_to_use>
</lens>

## Core Philosophy

<principle>
The skill's expansion phase generates 15-20+ candidates per lens, often 50+
total across lenses. Without a structured sifting methodology, the user will
either (a) pick the most familiar one (anti-bias failure) or (b) try to pursue
3 at once (focus failure).

Sifting is not elimination — it's prioritization with explicit kill reasons.
Every killed opportunity gets a one-sentence reason. This serves two purposes:
1. The user can audit the sifting logic
2. If the top 3 all fail validation, the kill log tells you which to revisit
</principle>

## The 5-Stage Sifting Pipeline

<sifting_pipeline>

### Stage 1: Pool → Filtered (50 → 20)

Apply 5 hard vetoes. Any opportunity failing any veto is killed immediately.

<hard_vetoes>
1. **No clear path to revenue in 90 days** — Kill. If you can't see how money
   flows in 90 days, the opportunity is too speculative for a solo operator.

2. **Requires capital the user doesn't have** — Kill (or defer). Check against
   intake or autonomous default ($0). If the opportunity needs >$5K to test,
   and the user has $0, kill.

3. **No identifiable buyer** — Kill. "Everyone" is not a buyer. "Solo developers
   using AI coding tools who hit token cost issues" is a buyer.

4. **User explicitly lacks capability to execute** — Kill. If the opportunity
   requires a skill the user doesn't have and can't acquire in 30 days, kill.
   (e.g., opportunity requires FDA regulatory expertise; user has none.)

5. **Fails the Safety Floor** — Kill. Anything requiring fraud, ToS violation,
   KYC bypass, or exploitation of vulnerable parties.
</hard_vetoes>

Record kill reasons: "[Opportunity] killed: [veto #]: [specific reason]"

### Stage 2: Filtered → Ranked (20 → 8)

Score each surviving opportunity on 5 axes, 0/1/2 each (max 10):

<scoring_axes>
1. **Asymmetry** (0-2)
   - 0: Linear payoff. Effort in = value out.
   - 1: Mild asymmetry. Some leverage, but mostly linear.
   - 2: Strong asymmetry. Small fixed bet, large upside. Passes Lens 07 veto.

2. **Evidence** (0-2)
   - 0: Single-source signal. No corroboration.
   - 1: 2-3 independent sources. Medium confidence.
   - 2: 3+ diverse sources + spend evidence. High confidence.

3. **Fit** (0-2)
   - 0: User has no relevant skill/network/domain. Generic opportunity.
   - 1: User has partial fit (one relevant skill or some domain knowledge).
   - 2: User has strong fit (skills + network + domain all align).

4. **Urgency** (0-2)
   - 0: No time pressure. Will exist in 12 months unchanged.
   - 1: Moderate window (6-12 months before saturation).
   - 2: Acute window (<6 months — regulatory deadline, tech inflection, incumbent weakness).

5. **Reversibility** (0-2)
   - 0: First step is irreversible (lease, hire, inventory).
   - 1: First step has small sunk cost but mostly reversible.
   - 2: First step is fully reversible at $0. Can abandon without consequence.
</scoring_axes>

<scoring_rules>
- Opportunities scoring ≥6/10 advance to Stage 3
- Opportunities scoring 4-5/10 are flagged for "second look" (kept in reserve)
- Opportunities scoring ≤3/10 are killed

Veto dimensions (auto-kill if score 0):
- Asymmetry = 0 → kill (no leverage, will be linear grind)
- Reversibility = 0 → kill unless explicitly approved by user (irreversible first step too risky)
</scoring_rules>

### Stage 3: Ranked → Top Candidates (8 → 3)

Apply 3 tiebreakers to the top 8:

<tiebreakers>
1. **Highest expected value (EV)**
   EV = (probability of success) × (payoff if successful) - (cost if failed)
   
   Use rough estimates:
   - Probability: from Lens 06 confidence, adjusted for calibration history
   - Payoff: from Lens 07 (Tier 1 = high, Tier 2 = medium, Tier 3 = low)
   - Cost: from Lens 08 (financial + time opportunity cost)
   
   Pick the 3-4 with highest EV.

2. **Lowest correlation with other opportunities**
   If two top opportunities are correlated (both depend on the same market,
   same buyer, same technology), pick one. Diversification reduces portfolio
   risk.

3. **Fastest path to evidence**
   Among EV-equivalent opportunities, pick the one that generates evidence
   fastest. A 7-day validation beats a 90-day validation. Speed of learning
   compounds.
</tiebreakers>

### Stage 4: Top Candidates → Finalist (3 → 1)

Run adversarial pass on each of the top 3 (see `references/adversarial-audit.md`).
The opportunity that survives the adversarial pass most cleanly is the finalist.

If multiple survive equally, the user decides. The skill presents the 2-3
finalists with their adversarial notes and lets the user pick.

### Stage 5: Finalist → Action

The finalist gets:
- Full Lens 06 audit
- Lens 07 exponential scoring
- Lens 08 risk-of-ruin check
- Lens 09 pricing analysis
- Lens 10 competitor teardown
- Pre-mortem
- Single Next Action (from execution-sprints.md)
- 2-week sprint plan
- Decision journal entry

</sifting_pipeline>

## The Sifting Decision Matrix

<decision_matrix>
```
Stage 1 (hard vetoes):     50 → 20   (kill 30, ~60%)
Stage 2 (5-axis scoring):  20 → 8    (kill 12, ~60%)
Stage 3 (tiebreakers):     8 → 3     (kill 5, ~60%)
Stage 4 (adversarial):     3 → 1     (kill 2, ~66%)
Stage 5 (full pipeline):   1 → action

Total: 50 → 1, ~98% kill rate.
```

The 98% kill rate is correct. Most opportunities are not worth pursuing. The
skill's value is in identifying the 2% that are, with explicit reasoning for
why the other 98% were rejected.
</decision_matrix>

## Anti-Pattern: "I'll pursue 3 in parallel"

<anti_pattern>
The most common sifting failure is the user (or agent) refusing to pick one.

"I have 3 great opportunities, I'll work on all 3 in parallel."

NO. This fails for 3 reasons:

1. **Focus is a multiplier.** One opportunity pursued with 100% focus beats 3
   pursued with 33% each. The 100% focus opportunity gets 10x the depth of
   validation, iteration, and learning.

2. **Parallel opportunities compete for the same scarce resources** — your time,
   your cognitive bandwidth, your decision-making capacity. They don't actually
   run in parallel; they context-switch, which is worse than serial.

3. **You can't calibrate from parallel bets.** If 1 of 3 succeeds, you don't
   know if it was skill or luck. If you'd pursued only that 1 and it succeeded,
   you'd have stronger signal about your judgment.

The skill's output is ONE opportunity, with the other 2-3 as documented backups
if the first fails validation. Not 3 in parallel.
</anti_pattern>

## Few-Shot Examples

<examples>

### Example 1: 50 opportunities → 1 finalist

<example>
<situation>
User ran Lens 01 (signal scan) + Lens 02 (demand gap) on "AI tools for solo developers." Expansion generated 47 raw candidates. User asks to sift.
</situation>

<thinking>
Let me work through the sifting pipeline.

Stage 1 — Hard vetoes (47 → ~20):
Kill candidates failing any of 5 vetoes. Sample kills:
- "Build a Cursor competitor" → Killed: requires >$5M capital (Veto #2)
- "AI dev tools newsletter" → Killed: no path to revenue in 90 days without 6+ months audience build (Veto #1)
- "AI dev tools for enterprise teams" → Killed: user lacks enterprise sales capability (Veto #4)
- "Crypto-based dev bounties platform" → Killed: fails Safety Floor (crypto + unregulated) (Veto #5)
- "General AI coding assistant" → Killed: no identifiable buyer specificity (Veto #3) — "everyone" is not a buyer

After 5 vetoes: 47 → 19 survivors.

Stage 2 — 5-axis scoring (19 → ~8):
Score each survivor on Asymmetry, Evidence, Fit, Urgency, Reversibility.

Sample scoring for top candidates:
- "Open-source CLI for AI context management" → Asymmetry 2, Evidence 2, Fit 2, Urgency 1, Reversibility 2 = 9/10 ✓
- "Token cost dashboard extension" → Asymmetry 0 (VETO - linear), killed
- "Vertical SaaS for solo dev compliance" → Asymmetry 2, Evidence 1, Fit 1, Urgency 2, Reversibility 1 = 7/10 ✓
- "Solo dev AI pair-programming tool" → Asymmetry 2, Evidence 1, Fit 2, Urgency 1, Reversibility 2 = 8/10 ✓
- ... (continue for all 19)

After scoring: 19 → 8 survivors (scoring ≥6).

Stage 3 — Tiebreakers (8 → 3):
Compute EV for each, eliminate correlations, pick fastest-to-evidence.

Top 3 after tiebreakers:
1. Open-source CLI for AI context management (EV: high, evidence: 14 days)
2. Vertical SaaS for solo dev compliance (EV: high, evidence: 30 days)
3. Solo dev AI pair-programming tool (EV: medium, evidence: 21 days)

#2 and #3 are correlated (both AI dev tools for solos). Pick one — keep #1 and #3 (different value props).

After correlation tiebreaker: 3 → 3 (1 and 3 kept, #2 set as backup).

Wait, that's still 3. Let me apply the EV tiebreaker more carefully:
- #1: EV = 0.5 × $1M (acquisition target) - $200 cost = ~$500K EV
- #2: EV = 0.3 × $3M (SaaS exit) - $5K cost = ~$900K EV (but higher risk)
- #3: EV = 0.4 × $500K (small SaaS) - $0 cost = ~$200K EV

By EV: #2 > #1 > #3. But #2 has higher capital requirement and lower fit.

Reorder: #1 (best EV/risk ratio) > #2 (backup) > #3 (third choice).

Stage 4 — Adversarial pass on top 3:
Run adversary on each. #1 survives (incumbent slow, wedge clear). #2 gets killed (compliance SaaS requires regulatory expertise user lacks). #3 survives (smaller but real).

Finalist: #1 — Open-source CLI for AI context management.

Stage 5 — Full pipeline on finalist:
Runs Lens 06, 07, 08, 09, 10, pre-mortem, single next action.
</thinking>

<answer>
Sifting complete. From 47 candidates:

**Finalist**: Open-source CLI for AI context management
- EV: ~$500K (50% probability × $1M acquisition outcome - $200 cost)
- Survives Lens 06 anti-bias gate (wedge: solo-dev niche underserved)
- Lens 07 Tier: 2 (Scalable Linear — code leverage, no network effects)
- Lens 08 risk-of-ruin: PASS ($200 cost, fully reversible)
- Lens 09 pricing: $29/mo Pro tier (vs $9 default — charge more)
- Lens 10 competitor: Cursor/Pilot can't go simple without cannibalizing enterprise

**Backups (if finalist fails validation)**:
1. Solo dev AI pair-programming tool (Tier 2, $0 cost)
2. Vertical SaaS for solo dev compliance (Tier 2, requires $5K + regulatory expertise)

**Kill log** (47 killed, top reasons):
- 12 killed: no path to revenue in 90 days (Veto #1)
- 8 killed: require capital user doesn't have (Veto #2)
- 7 killed: no specific buyer (Veto #3)
- 9 killed: user lacks capability (Veto #4)
- 3 killed: Safety Floor violation (Veto #5)
- 8 killed: scoring ≤3/10 (linear payoff, no leverage)

**Single Next Action**: Ship minimal CLI to GitHub. Post on HN Show HN + r/LocalLLaMA. Measure stars and inbound Pro inquiries in 14 days.

Kill criteria: <30 stars by Day 14 → kill. <100 stars + <5 Pro signups by Day 60 → kill.
</answer>
</example>

### Example 2: Refusing to pick one (negative)

<example>
<situation>
User has 3 opportunities scoring 8-9/10. Says "they're all great, I'll pursue all 3 in parallel."
</situation>

<thinking>
This is the anti-pattern. Let me push back with the reasoning.

The user is conflating "all 3 are good" with "all 3 should be pursued." These are different. A ranked list of 3 good opportunities ≠ 3 things to do.

The math: if each opportunity has 20% chance of success, pursuing 3 in parallel gives:
- Probability at least 1 succeeds: 1 - 0.8^3 = 49%
- But: focus is divided 3 ways, so each is less likely to succeed. Effective probability per opportunity drops to ~10%.
- Probability at least 1 succeeds at 10%: 1 - 0.9^3 = 27%

So parallel pursuit HALVES the probability of any success.

Serial pursuit (one at a time, 100% focus, then next if first fails):
- First opportunity at 100% focus: 25% success (focus boost)
- If first fails (75% chance), second at 100% focus: 25% success
- If second fails (56% chance), third at 100% focus: 25% success
- Probability at least 1 succeeds: 1 - 0.75 × 0.75 × 0.75 = 58%

Serial beats parallel: 58% vs 27%.

Plus serial enables calibration — you learn from #1's failure to inform #2's execution.

The user should pick one. The skill's job is to make them pick.
</thinking>

<answer>
Strong recommendation: pick ONE, not three.

The intuition that "3 good opportunities = 3 things to do" is wrong. Parallel pursuit halves your success probability (27%) vs serial pursuit (58%), because focus is a multiplier and context-switching is a tax.

**Recommended approach**:
1. Pick the highest-EV opportunity (Lens 11 Stage 3 ranking)
2. Pursue with 100% focus for 2-week sprint
3. If killed by kill criteria, move to #2 (you've already done the analysis)
4. If survived, commit fully

The other 2 opportunities don't disappear. They're documented, scored, and waiting. If #1 fails, you start #2 immediately — no analysis lost.

If you insist on parallel, the skill will run but flag the output: "User pursuing 3 in parallel against recommendation. Expected success probability reduced from 58% to 27%. Each opportunity pursued at 33% focus."

Don't pursue 3 in parallel. Pick one. The other two are insurance, not workload.
</answer>
</example>
</examples>

## Edge Cases

<edge_cases>
### Edge 1: All opportunities score ≤3/10
This means either (a) the expansion phase failed (re-run with broader search)
or (b) the user's constraints are too tight (revisit intake — maybe capital or
skill assumptions are wrong). Don't force a winner from a weak pool.

### Edge 2: One opportunity scores 10/10, everything else ≤5
Take the 10/10. Don't sifting for "balance" — if one is clearly best, commit.
But verify the 10/10 isn't scoring high because of overconfidence (run
adversarial pass before committing).

### Edge 3: User has 50+ opportunities and wants to see all of them
Show the kill log. The user seeing WHY 47 were killed is more valuable than
seeing the 47 themselves. The kill log is the audit trail.

### Edge 4: Two opportunities are equally ranked and user can't decide
Flip a coin. Seriously. If they're truly equal, the decision doesn't matter —
the execution matters. The skill's job is to confirm they're equal; the user's
job is to commit.

### Edge 5: User has run multiple sprints and all failed
This is a calibration signal. After 3+ failed sprints, run the monthly
calibration review early (see calibration-protocol.md). The pattern of failures
indicates either a systematic bias (overconfidence on certain opportunity types)
or a constraint mismatch (opportunities don't fit user's actual situation).
</edge_cases>

## Weak Link: What Kills This Sifting?

<weak_link>
```
Did expansion generate 50+ raw opportunities?
  NO → Premature sifting. Re-run expansion with broader search.
  YES → continue

Did you apply all 5 hard vetoes?
  NO → Weak candidates polluting the pool. Re-apply.
  YES → continue

Did you score on all 5 axes (not just "gut feel")?
  NO → Scoring is theater. Re-score with explicit 0/1/2.
  YES → continue

Did you compute EV (not just ranking)?
  NO → Ranking without EV misses risk-adjusted value.
  YES → continue

Did you check correlation between top opportunities?
  NO → Two correlated "opportunities" are really one.
  YES → continue

Did the finalist survive adversarial pass?
  NO → Revert to Stage 3, pick next.
  YES → Sifting complete. Proceed to action.
```
</weak_link>

## Decision Protocol

<decision_protocol>
### Exact Question This Lens Answers
"Of N raw opportunities, which 1 should the user pursue — with explicit kill
reasons for the other N-1?"

### Data Required
- 50+ raw opportunities from expansion (Lens 01-05, 07-10)
- User context (intake or autonomous defaults)
- Calibration history (if available, to adjust confidence)

### Confidence Threshold
- **Deploy (commit to finalist)**: ≥75% confidence, finalist survived adversarial pass, EV computed, backups identified
- **Flag (pursue with caution)**: 50-75% confidence, finalist survived adversarial but EV unclear
- **Discard (re-expand)**: <50% confidence, OR all finalists killed by adversarial pass

### Conflict Resolution Rules
- When Lens 11 (Sifting) disagrees with user preference:
  - Present the kill log and scoring transparently. The user can override, but the skill's recommendation stands.
  - If user overrides, document the override and the reasoning. This feeds calibration.
- When Lens 11 disagrees with Lens 06 (Anti-Bias):
  - Anti-bias wins on individual opportunities. Sifting wins on portfolio selection.
  - If anti-bias says REJECT for the finalist, revert to Stage 3 and pick next.
- When Lens 11 disagrees with Lens 07 (Exponential):
  - Sifting considers Tier 1 > Tier 2 > Tier 3, but EV matters more than tier.
  - A Tier 3 opportunity with high EV (low risk, high probability, moderate payoff) can beat a Tier 1 opportunity with low EV (high risk, low probability, high payoff).
- When user insists on parallel pursuit:
  - Flag the output: "Parallel pursuit reduces success probability from X% to Y%. Recommended: serial."
  - Document the decision. This feeds calibration.
</decision_protocol>

## Output

<output>
```
### Opportunity Sifting Results

#### Pool Summary
- Total candidates from expansion: [N]
- After Stage 1 (hard vetoes): [N] → [N]
- After Stage 2 (5-axis scoring): [N] → [N]
- After Stage 3 (tiebreakers): [N] → [N]
- After Stage 4 (adversarial): [N] → [N] finalist

#### Finalist
- Opportunity: [name]
- Stage 2 score: [X]/10 (Asymmetry [a], Evidence [e], Fit [f], Urgency [u], Reversibility [r])
- EV: $[X] (probability [p]% × payoff $[Y] - cost $[Z])
- Adversarial verdict: SURVIVED / COULDN'T BREAK IT

#### Backups (if finalist fails validation)
1. [Opportunity 2] — score [X]/10, EV $[Y]
2. [Opportunity 3] — score [X]/10, EV $[Y]

#### Kill Log (top reasons)
| Veto/Score | Count | Example |
|---|---|---|
| Hard veto #1 (no revenue path) | [N] | "[example]" |
| Hard veto #2 (capital mismatch) | [N] | "[example]" |
| Hard veto #3 (no buyer) | [N] | "[example]" |
| Hard veto #4 (no capability) | [N] | "[example]" |
| Hard veto #5 (Safety Floor) | [N] | "[example]" |
| Score ≤3/10 | [N] | "[example]" |
| Adversarial killed | [N] | "[example]" |

#### Parallel Pursuit Warning (if user requests)
- Recommended: serial (probability of success: [X]%)
- User requested: parallel (probability of success: [Y]%)
- Reduction: [-Z%]
- This decision is documented for calibration.

#### Next Step
Proceed to finalist full pipeline (Lens 06, 07, 08, 09, 10, pre-mortem, single next action).
```
</output>

## Source

Synthesized from `/references/research-opportunity-identification.md` (Part 4:
"Opportunity Sifting Framework") which contains the 4-stage pipeline, 5 hard
vetoes, 5-axis scoring rubric, and 2-week validation sprint protocol.
