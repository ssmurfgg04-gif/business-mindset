# Calibration Protocol — Monthly, Quarterly, Annual Reviews

The decision journal (`references/decision-journal.md`) and outcomes ledger
(`references/ledger.md`) accumulate raw data. Without structured review,
that data is a graveyard. This file defines the review cadence that turns
raw data into calibration improvements.

## Why Calibration Matters

Calibration = the alignment between your confidence and your outcomes.

- **Well-calibrated**: when you say "70% confident," you're right ~70% of the time.
- **Overconfident**: when you say "70% confident," you're right ~50% of the time.
- **Underconfident**: when you say "70% confident," you're right ~90% of the time.

Most people (and most AI agents) are systematically overconfident. The only
known fix is measurement + feedback. This protocol provides the structure.

## Monthly Calibration Review (30 minutes, first of each month)

### Trigger
Run on the 1st of each month, or at the start of the first session after
the 1st. The skill should auto-prompt: "Monthly calibration review due.
30 minutes required. Proceed?"

### Inputs
- `~/.local/state/opencode/business-mindset-decisions.jsonl` (decision journal)
- `~/.local/state/opencode/business-mindset-outcomes.jsonl` (outcomes ledger)
- `~/.local/state/opencode/business-mindset-ledger.jsonl` (positions)

### Steps

1. **Pull all pre-decision entries from the last 30 days that have post-outcome entries.**
   ```bash
   jq -s 'group_by(.id) | map(select(length==2)) | map(select(.[1].date >= "2026-07-01"))' "$DECISIONS"
   ```

2. **For each entry, compare predicted confidence to actual outcome:**
   - Predicted 80%+ confidence, outcome = success → calibrated
   - Predicted 80%+ confidence, outcome = failure → overconfident
   - Predicted <40% confidence, outcome = success → underconfident
   - Predicted <40% confidence, outcome = failure → calibrated

3. **Compute aggregate calibration:**
   - Count of high-confidence (>70%) predictions
   - Count of high-confidence predictions that succeeded
   - Ratio = success rate (should be ~70-80% if calibrated)
   - If ratio < 60% → systematically overconfident
   - If ratio > 90% → systematically underconfident

4. **Identify per-lens accuracy:**
   - Group outcomes by primary lens that drove the PASS verdict
   - Compute success rate per lens
   - Flag lenses with <40% or >90% success rates (both are problems)

5. **Identify recurring error patterns:**
   - Read "what I got wrong" fields across entries
   - Cluster similar errors (e.g., "underestimated enterprise sales cycle" appears 3x)
   - These are your blind spots

6. **Write the calibration summary:**
   ```markdown
   ## Monthly Calibration Review — [Month Year]

   ### Headline Metrics
   - Decisions reviewed: [N]
   - High-confidence predictions: [N]
   - High-confidence successes: [N] ([%])
   - Calibration verdict: [overconfident / underconfident / calibrated]

   ### Per-Lens Accuracy
   | Lens | Predictions | Successes | Rate | Verdict |
   |------|-------------|-----------|------|---------|
   | 01 Signal Scan | | | | |
   | 02 Demand Gap | | | | |
   | 03 Arbitrage | | | | |
   | 04 Leverage | | | | |
   | 05 Network Path | | | | |
   | 07 Exponential | | | | |
   | 08 Risk of Ruin | | | | |

   ### Recurring Error Patterns
   1. [Pattern — frequency]
   2. [Pattern — frequency]
   3. [Pattern — frequency]

   ### Confidence Adjustment for Next Month
   - For Lens [X]: apply -[N]% confidence adjustment (overconfident)
   - For Lens [Y]: apply +[N]% confidence adjustment (underconfident)
   - Overall: [adjustment]

   ### One Specific Change
   [Pick ONE blind spot to actively counter this month. E.g., "I will
   double enterprise sales cycle estimates for all B2B opportunities."]
   ```

### Output
The calibration summary is appended to:
```
~/.local/state/opencode/business-mindset-calibration.md
```
And the confidence adjustments are cached in:
```json
{
  "calibration_date": "2026-07-31",
  "lens_adjustments": {
    "01-signal-scan": -5,
    "02-demand-gap": 0,
    "03-arbitrage": -10,
    "07-exponential": -15
  },
  "overall_adjustment": -8,
  "active_blind_spot": "enterprise sales cycle underestimation"
}
```
at `~/.local/state/opencode/business-mindset-calibration.json`.

The skill reads this cache at the start of each analysis and applies the
adjustment to confidence levels in the output.

## Quarterly Framework Audit (2 hours, end of each quarter)

### Trigger
Run at the end of March, June, September, December. The skill prompts:
"Quarterly framework audit due. 2 hours required. Review the last 3
months of decisions and outcomes. Proceed?"

### Purpose
The monthly review checks calibration. The quarterly audit checks whether
the **frameworks themselves** are working. Are the lenses surfacing real
opportunities, or just generating activity?

### Steps

1. **Pull all outcomes from the last 90 days.**
2. **Compute per-framework metrics:**
   - 6 Pillars: of opportunities that scored >8, what fraction succeeded?
   - Asymmetry Scorecard: of opportunities that scored >3.5, what fraction succeeded?
   - Lens 07: of Tier 1 opportunities, what fraction achieved Tier 1 outcomes?
   - Anti-bias gate: of PASS verdicts, what fraction should have been REJECT?
3. **Identify framework failures:**
   - Lenses that produced many PASS verdicts but few successes → lens is too permissive
   - Lenses that produced few PASS verdicts but those that passed succeeded → lens is well-tuned
   - Lenses that produced many REJECT verdicts that would have succeeded → lens is too strict (rare but possible)
4. **Review kill criteria effectiveness:**
   - Of sprints killed by kill criteria, would they have succeeded if extended?
   - Of sprints that survived kill criteria, did they actually succeed?
   - Kill criteria that never trigger are useless. Kill criteria that always trigger are too strict.
5. **Review the Safety Floor:**
   - Did any output violate the Floor? (Should be never, but check.)
   - Did the Floor prevent legitimate opportunities? (Possible over-correction.)
6. **Write the framework audit:**
   ```markdown
   ## Quarterly Framework Audit — Q[Number] [Year]

   ### Framework Performance
   | Framework | Predictions | Successes | Rate | Tuning Verdict |
   |-----------|-------------|-----------|------|----------------|
   | 6 Pillars (>8) | | | | tighten / loosen / OK |
   | Asymmetry (>3.5) | | | | |
   | Lens 07 Tier 1 | | | | |
   | Anti-bias PASS | | | | |

   ### Lens-Level Findings
   [Which lenses produced the best predictions? The worst?]

   ### Kill Criteria Effectiveness
   - Sprints killed: [N]
   - Killed sprints that would have succeeded: [N] (ideally 0)
   - Sprints that survived kill criteria and succeeded: [N]
   - Sprints that survived kill criteria and failed: [N] (indicates criteria too loose)

   ### Safety Floor Review
   - Floor violations: [N] (must be 0)
   - Near-misses: [N]
   - Over-corrections (legitimate opportunities blocked): [N]

   ### Recommended Framework Changes
   1. [Specific change — e.g., "Raise Asymmetry threshold from 3.5 to 3.7"]
   2. [Specific change]
   3. [Specific change]

   ### Lenses to Add/Remove/Modify
   [If any lenses consistently underperform, flag for revision or removal.
   If gaps are identified, flag for new lens.]
   ```

### Output
The framework audit is appended to:
```
~/.local/state/opencode/business-mindset-calibration.md
```
Recommended framework changes are flagged for the annual revision.

## Annual Framework Revision (4-8 hours, end of year)

### Trigger
Run in late December or early January. The skill prompts: "Annual
framework revision due. 4-8 hours required. Review the full year of data
and decide on structural changes. Proceed?"

### Purpose
The annual revision is the only time to make structural changes to the
skill itself — adding/removing lenses, changing thresholds, rewriting
frameworks. Quarterly audits identify problems; annual revisions fix them.

### Steps

1. **Pull all data from the last 12 months.**
2. **Compute annual metrics:**
   - Total opportunities analyzed
   - Total PASS verdicts
   - Total sprints run
   - Total successes / failures / abandoned
   - Overall calibration (annual)
3. **Review all quarterly audits:**
   - What framework changes were recommended?
   - Which were implemented?
   - Which are still pending?
4. **Review the skill files themselves:**
   - Which lenses have been most/least useful?
   - Which frameworks need rewriting?
   - What new lenses are needed?
5. **Make structural decisions:**
   - Add Lens [N]: [name and rationale]
   - Remove Lens [N]: [rationale]
   - Modify Lens [N]: [specific change]
   - Change thresholds: [specific changes]
   - Update Safety Floor if needed
6. **Write the annual revision document:**
   ```markdown
   ## Annual Framework Revision — [Year]

   ### Year in Review
   - Opportunities analyzed: [N]
   - PASS verdicts: [N]
   - Sprints run: [N]
   - Successes: [N] ([%])
   - Failures: [N] ([%])
   - Abandoned: [N] ([%])
   - Overall calibration: [overconfident/underconfident/calibrated]

   ### Structural Changes for Next Year
   1. [Lens additions]
   2. [Lens removals]
   3. [Threshold changes]
   4. [Framework rewrites]
   5. [Safety Floor updates]

   ### Implementation Plan
   - [Specific files to update]
   - [Specific commits to make]
   - [Specific tests to run]
   ```

### Output
The annual revision document is committed to the repo as:
```
docs/annual-revisions/[year]-revision.md
```

Structural changes are implemented as a new version (e.g., v0.3.0 → v1.0.0)
with a detailed commit message.

## Enforcement

The skill enforces review cadence by checking the calibration cache at
session start:

- If `calibration_date` in cache is >35 days old → prompt monthly review
- If last quarterly audit is >95 days old → prompt quarterly audit
- If last annual revision is >380 days old → prompt annual revision

Reviews can be deferred (user says "later") but not indefinitely. After
3 deferrals, the skill flags all output with: "Calibration stale.
Confidence levels may be misaligned. Run review to restore."

## The Point

The skill without calibration is a journal. The skill with calibration
is a learning system. The difference is whether you actually look at the
data you're collecting.
