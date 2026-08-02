# Skill Health Diagnostic — Detecting Miscalibration

## Why This Matters

<why>
A skill that produces verdicts without checking its own accuracy is a skill
that can silently degrade. The business-mindset skill now has 16 lenses, 8
frameworks, 4 verification protocols, and 15+ mandatory steps. Without a
health diagnostic, there's no way to know if:
- The skill is too optimistic (producing too many PASS verdicts)
- The skill is too pessimistic (rejecting good opportunities)
- The skill is well-calibrated (verdicts match reality)
- Specific lenses are failing (e.g., Lens 10 keeps missing competitors)
- The verification protocols are actually being executed

This file defines the metrics, thresholds, and diagnostic process for
detecting miscalibration.
</why>

## The 7 Health Metrics

<metrics>

### Metric 1: Verdict Distribution
**What**: Percentage of PASS / FLAG / REJECT verdicts over time.
**Target**: 5% PASS / 15% FLAG / 80% REJECT (the 80/20 rule from calibration)
**Diagnostic**:
- PASS >10% → skill is too optimistic; verification insufficient
- PASS <2% → skill is too pessimistic; may be rejecting good opportunities
- REJECT <70% → not skeptical enough
- FLAG >25% → too many unresolved; skill isn't making decisions

**Measurement**: Count verdicts in
`~/.local/state/opencode/business-mindset-outcomes.jsonl` over rolling 90-day window.

### Metric 2: PASS Accuracy
**What**: Of PASS verdicts, what fraction succeeded (user reported positive outcome)?
**Target**: ≥50% (vs ~5% base rate for random opportunities)
**Diagnostic**:
- <30% → skill is producing false PASS verdicts; verification failing
- 30-50% → marginal; improve verification
- 50-70% → well-calibrated
- >70% → suspiciously good; may be too conservative (only passing obvious wins)

**Measurement**: Cross-reference PASS verdicts with `actual_outcome` field in
outcomes JSONL. Requires user to fill in outcomes (decision journal protocol).

### Metric 3: REJECT Accuracy
**What**: Of REJECT verdicts, what fraction would have failed (user didn't pursue,
or pursued against advice and failed)?
**Target**: ≥90%
**Diagnostic**:
- <80% → skill is rejecting good opportunities; too pessimistic
- 80-90% → acceptable
- 90-95% → well-calibrated
- >95% → may be too conservative

**Measurement**: This is harder — requires tracking opportunities the user
pursued despite REJECT verdict. Track in outcomes JSONL with `pursued_against_advice` field.

### Metric 4: Verification Execution Rate
**What**: What percentage of verdicts include completed verification (GitHub search,
commercial search, Reddit mining, customer interviews)?
**Target**: 100% for PASS, ≥80% for FLAG, ≥50% for REJECT
**Diagnostic**:
- <50% for PASS → critical failure; skill is producing PASS without verification
- <30% overall → skill is skipping verification systematically
- Trend declining → rate limits or access problems worsening

**Measurement**: Parse `pipeline-checklist.md` compliance from each output.
Track in `~/.local/state/opencode/business-mindset-health.jsonl`.

### Metric 5: Lens Accuracy (per-lens)
**What**: For each lens, how often do its signals correlate with successful outcomes?
**Target**: Each lens should have >50% positive predictive value
**Diagnostic**:
- Lens with <40% accuracy → lens is miscalibrated; revise
- Lens with >90% accuracy → lens is strong; weight higher
- Lens never executed → lens is dead weight; remove or fix

**Measurement**: Tag each PASS verdict with which lenses drove the PASS. Track
outcome by primary lens. Requires 20+ data points per lens for statistical
significance.

### Metric 6: Confidence Calibration
**What**: When the skill says "70% confidence," is it right ~70% of the time?
**Target**: Brier score <0.25 (well-calibrated); <0.15 (excellent)
**Diagnostic**:
- Overconfident (says 70%, right 50%) → apply wider confidence intervals
- Underconfident (says 50%, right 70%) → tighten intervals
- Well-calibrated (says 70%, right 70%) → maintain

**Measurement**: Compare `confidence_pct` in decision journal to `actual_outcome`.
Compute Brier score: mean((confidence - outcome)²). Requires 30+ predictions.

### Metric 7: Skip Reason Distribution
**What**: Why are steps being skipped? What's the distribution of skip reasons?
**Target**: <20% of skips due to "rate limited" or "no access"
**Diagnostic**:
- >30% "rate limited" → access infrastructure failing; fix API access
- >20% "no access to buyers" → distribution problem; can't validate demand
- >10% "N/A" for mandatory steps → skill design flaw; revise checklist

**Measurement**: Parse skip reasons from pipeline checklists. Track distribution
monthly.

</metrics>

## The Diagnostic Process

<process>

### Monthly Health Check (automated at session start)
At the start of each session (if 30+ days since last health check):

1. **Compute all 7 metrics** from outcomes JSONL and decision journal
2. **Compare to targets** — flag any metric outside acceptable range
3. **Report health summary** to user:
   ```
   ### Skill Health Report (as of YYYY-MM-DD)

   - Verdict distribution: X% PASS / Y% FLAG / Z% REJECT (target: 5/15/80)
   - PASS accuracy: X% (target: ≥50%)
   - REJECT accuracy: X% (target: ≥90%)
   - Verification execution: X% (target: 100% for PASS)
   - Confidence calibration: Brier X (target: <0.25)
   - Skip reasons: [distribution]

   ### Health Status: [HEALTHY / WARNING / CRITICAL]
   - [Metric]: [status] — [recommendation]
   ```

4. **If CRITICAL**: Recommend immediate recalibration before proceeding

### Quarterly Deep Audit
Every 90 days (or 50+ verdicts, whichever comes first):

1. **Per-lens accuracy analysis**: Which lenses are predictive? Which aren't?
2. **Confidence adjustment review**: Are the domain adjustments (from
   `calibration-simulations.md`) actually predictive?
3. **Skip pattern analysis**: Are certain steps systematically skipped?
4. **Adversary effectiveness**: Is the adversarial audit catching real problems?
5. **Recommend framework changes**: Add/remove/modify lenses or protocols

### Annual Revision
Once per year (or 200+ verdicts):

1. **Full statistical analysis**: Brier scores, per-lens PPV, verdict distribution
2. **Framework audit**: Which frameworks (Fang Yuan, ECR, Effectuation, etc.)
   are actually used? Which are dead weight?
3. **Calibration reset**: If miscalibration detected, reset confidence adjustments
4. **Version bump**: Major version (v1.0, v2.0) for breaking changes

</process>

## The Health Dashboard

<dashboard>
Stored at `~/.local/state/opencode/business-mindset-health.json`:

```json
{
  "last_health_check": "2026-07-31",
  "verdicts_total": 47,
  "verdict_distribution": {
    "PASS": 0.04,
    "FLAG": 0.17,
    "REJECT": 0.79
  },
  "pass_accuracy": 0.60,
  "reject_accuracy": 0.92,
  "verification_execution_rate": {
    "PASS": 1.00,
    "FLAG": 0.78,
    "REJECT": 0.61
  },
  "confidence_brier_score": 0.21,
  "skip_reasons": {
    "rate_limited": 0.23,
    "no_access_to_buyers": 0.15,
    "quick_check_mode": 0.31,
    "auto_reject_early": 0.19,
    "na": 0.12
  },
  "lens_accuracy": {
    "01-signal-scan": 0.62,
    "02-demand-gap": 0.58,
    "03-arbitrage": 0.55,
    "04-leverage": 0.51,
    "05-network-path": 0.48,
    "06-anti-bias": 0.71,
    "07-exponential": 0.64,
    "08-risk-of-ruin": 0.82,
    "09-pricing": 0.59,
    "10-competitor": 0.67,
    "11-sifting": 0.69,
    "12-operations": 0.54,
    "13-growth": 0.57,
    "14-negotiation": 0.61,
    "15-capital": 0.60,
    "16-distribution": 0.73
  },
  "health_status": "HEALTHY",
  "warnings": [
    "skip_reasons.rate_limited at 23% — access infrastructure needs attention",
    "lens 05-network-path accuracy 48% — below 50% threshold, review"
  ]
}
```

**Status thresholds**:
- **HEALTHY**: All metrics within target range
- **WARNING**: 1-2 metrics outside range; skill functional but degrading
- **CRITICAL**: 3+ metrics outside range OR PASS accuracy <30% OR verification rate <50%
</dashboard>

## Diagnostic Signals

<signals>

### Signal: Skill is too optimistic
**Symptoms**: PASS >10%, PASS accuracy <40%
**Likely causes**:
- Verification protocol not being executed (check execution rate)
- Adversarial audit is rubber-stamping (check adversary verdicts)
- Confidence adjustments not being applied (check if domain matrix used)
**Fix**: Enforce pipeline checklist; require adversary to construct real attacks

### Signal: Skill is too pessimistic
**Symptoms**: PASS <2%, REJECT accuracy <85%
**Likely causes**:
- Confidence adjustments too aggressive (e.g., stacking -45% for common combos)
- Distribution pre-gate too strict (rejecting viable opportunities)
- Saturation threshold too sensitive (flagging early markets as saturated)
**Fix**: Loosen specific adjustments; review distribution gate criteria

### Signal: Verification not executing
**Symptoms**: Verification execution rate <50% for PASS
**Likely causes**:
- Rate limits on GitHub API (need OAuth token)
- Web search rate limits (need alternative search sources)
- Agent skipping steps silently (need checklist enforcement)
**Fix**: Fix API access; enforce checklist; track skip reasons

### Signal: Specific lens failing
**Symptoms**: Lens accuracy <50% for 20+ data points
**Likely causes**:
- Lens criteria too vague (can't distinguish good from bad)
- Lens not being executed (check execution rate per lens)
- Lens is wrong for current market conditions
**Fix**: Revise lens criteria; check execution; possibly retire lens

### Signal: Adversary rubber-stamping
**Symptoms**: Adversary verdicts always "SURVIVED" with weak attacks
**Likely causes**:
- Adversary persona not engaged properly
- Adversary not running disconfirming evidence searches
- Adversary not constructing specific attacks
**Fix**: Require adversary to report 3+ specific attacks with evidence; track
adversary KILL rate (should be 30-50%, not 0% or 100%)

### Signal: Confidence miscalibration
**Symptoms**: Brier score >0.30
**Likely causes**:
- Overconfidence (most common — apply 15-20% discount by default)
- Underconfidence (rare — tighten intervals)
**Fix**: Apply calibration adjustment from `calibration-protocol.md`; recompute
Brier after 30 predictions

</signals>

## The Meta-Diagnostic

<meta>
The skill's health diagnostic is itself a calibration tool. As outcomes data
accumulates, the diagnostic becomes more accurate. The first 3 months will
have noisy data (small sample); after 6 months and 50+ verdicts, the diagnostic
becomes reliable.

**The honest assessment**: As of v0.5.2, the skill has 0 real outcomes data
(all calibration is from mental simulation). The health diagnostic is
theoretical — it defines what to track, but can't yet compute real metrics.
The first real outcomes (from users actually pursuing or rejecting opportunities)
will populate the metrics.

**The commitment**: The skill is designed to improve with use. Every verdict
feeds the outcomes JSONL. Every decision journal entry feeds the Brier score.
Every pipeline checklist feeds the execution rate. Over time, the skill
becomes self-calibrating.

**The risk**: If users don't fill in outcomes (the decision journal's
post-outcome entries), the skill can't learn. The calibration protocol
(`references/calibration-protocol.md`) addresses this with auto-prompts for
stale entries, but ultimately requires user participation.

**The meta-lesson**: A skill that can't measure its own accuracy is a skill
that can't improve. This diagnostic makes accuracy measurable. The rest is
execution — actually tracking outcomes, actually computing metrics, actually
acting on warnings.
</meta>
