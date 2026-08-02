# Decision Journal — Prediction Tracking for Calibration

A decision journal is the single highest-leverage tool for improving
analytical quality over time. It forces you to record predictions
BEFORE outcomes are known, so you can later check whether your confidence
was calibrated.

Without a decision journal, you will reconstruct your past predictions to
match what happened (hindsight bias). You'll remember the wins, forget
the losses, and conclude you're a better analyst than you are.

## Why It Matters

The skill produces PASS/FLAG/REJECT verdicts with confidence levels. The
outcomes ledger (`references/ledger.md`) tracks what happened. But
neither captures **what you predicted would happen, at what confidence,
and why** — which is the actual calibration signal.

A decision journal closes this gap. It's the raw material for the
monthly calibration review (`references/calibration-protocol.md`).

## When to Write an Entry

Write a decision journal entry:

1. **After every PASS verdict** — before any action is taken. This is mandatory.
2. **After every FLAG verdict where the user decides to proceed** — optional but recommended.
3. **Before every 2-week sprint** (see `references/execution-sprints.md`) — mandatory.
4. **After every sprint ends** (killed or completed) — mandatory.
5. **When abandoning an opportunity mid-execution** — mandatory.

## Entry Format

See `templates/decision-journal-template.md` for the fillable template.
Key fields:

### Pre-Decision Entry (written BEFORE acting)

```markdown
## Decision Journal Entry — [Date]

### Decision
[One-sentence description of the opportunity/action being considered]

### Verdict from Skill
[PASS / FLAG / REJECT — and tier if applicable]

### My Prediction
[Specific, measurable prediction of what will happen]

### Confidence Level
[X]%, where X reflects my honest probability estimate.

### Key Assumptions
1. [Assumption 1 — if false, prediction fails]
2. [Assumption 2 — if false, prediction fails]
3. [Assumption 3 — if false, prediction fails]

### Reasoning
[2-3 sentences on why I believe this. Reference specific evidence,
not gut feeling.]

### What Would Prove Me Wrong
[Specific, observable signal that would invalidate the prediction]

### Kill Criteria
[Pre-committed: if X happens or Y doesn't happen by Z date, abandon]

### Emotions at Decision Time
[Honest note: am I excited? Anxious? Bored? This catches ego-driven bets.]

### Time Horizon for Review
[When will I check if this prediction was right? e.g., "30 days", "6 months"]
```

### Post-Outcome Entry (written AFTER result is known)

```markdown
## Decision Journal Update — [Date]

### Original Entry
[Link or reference to pre-decision entry]

### What Actually Happened
[Facts only. No interpretation yet.]

### Did I Hit My Prediction?
[Yes / Partially / No — with data]

### Did I Hit Kill Criteria?
[Killed / Survived / N/A]

### What Did I Get Wrong?
[Specific assumptions that were false. Be honest.]

### What Did I Get Right?
[Specific assumptions that held up.]

### What Surprised Me?
[Things I didn't predict at all but turned out to matter.]

### Calibration Note
- Predicted confidence: [X]%
- Outcome: [success/failure]
- [If X was high (>70%) and outcome was failure: I'm overconfident.
   If X was low (<30%) and outcome was success: I'm underconfident.
   If X matched outcome frequency: well-calibrated.]

### Lessons for Similar Future Decisions
[1-2 specific, transferable lessons. Not "be more careful" — that's useless.
 Things like "enterprise sales cycles are 2x longer than I assume" or
 "Reddit complaints don't convert to willingness-to-pay."]

### Would I Make This Decision Again?
[Yes / No / With changes: [specific changes]]
```

## Storage

Decision journal entries are stored in:

```
~/.local/state/opencode/business-mindset-decisions.jsonl
```

One JSON object per line (JSONL format, same as the outcomes ledger).
Append-only. Use `jq` for analysis.

### JSON Schema

```json
{
  "type": "pre-decision",
  "id": "dec-001",
  "date": "2026-07-31",
  "opportunity": "Solo-dev AI context CLI",
  "skill_verdict": "PASS",
  "tier": "2",
  "prediction": "100 GitHub stars + 5 Pro signups in 30 days",
  "confidence_pct": 60,
  "assumptions": [
    "solo devs search GitHub for context tools",
    "$9/mo is acceptable price point",
    "HN/Reddit launch drives 500+ visitors"
  ],
  "reasoning": "Underserved niche, permissionless leverage, 230+ GitHub issues validate demand",
  "disconfirming_evidence_signal": "<20 stars in week 1 = signal not reaching audience",
  "kill_criteria": "<100 stars by day 60 AND <5 Pro signups by day 90",
  "emotions": "excited but cautious",
  "review_date": "2026-08-30"
}
```

```json
{
  "type": "post-outcome",
  "id": "dec-001",
  "date": "2026-08-30",
  "original_prediction": "100 GitHub stars + 5 Pro signups in 30 days",
  "actual_outcome": "47 stars, 1 Pro signup",
  "prediction_hit": "partially",
  "kill_criteria_hit": "survived (stars <100 but trending up; 1 signup is weak)",
  "what_i_got_wrong": "HN launch drove 80 visitors not 500; algorithm didn't pick it up",
  "what_i_got_right": "solo-dev niche is real; 47 organic stars validates demand",
  "surprises": "Most signups came from a niche Discord I didn't plan for",
  "calibration": "Predicted 60% confidence, outcome was partial success. Roughly calibrated.",
  "lessons": "HN algorithm is less reliable than expected for dev tools. Niche communities (Discord) convert better.",
  "would_do_again": "yes, with changes: skip HN, focus Discord outreach"
}
```

## Analysis Commands

```bash
DECISIONS="$HOME/.local/state/opencode/business-mindset-decisions.jsonl"

# Count decisions by verdict
jq -s 'group_by(.skill_verdict) | map({verdict: .[0].skill_verdict, count: length})' "$DECISIONS"

# Show all pre-decision entries without post-outcome (pending review)
jq -s '[.[] | select(.type=="pre-decision")] | map(.id) as $pre | [.[] | select(.type=="post-outcome")] | map(.id) as $post | $pre - $post' "$DECISIONS"

# Average confidence for PASS verdicts
jq -s '[.[] | select(.type=="pre-decision" and .skill_verdict=="PASS")] | map(.confidence_pct) | add / length' "$DECISIONS"

# Calibration: for entries with both pre and post, compare confidence to outcome
jq -s 'group_by(.id) | map(select(length==2)) | map({
  id: .[0].id,
  confidence: .[0].confidence_pct,
  outcome: .[1].prediction_hit
})' "$DECISIONS"
```

## Integration with Skill

The skill prompts for decision journal entries at these points:

1. **After PASS verdict** — skill outputs the pre-decision template,
   pre-filled with the opportunity name, verdict, and kill criteria.
   User edits predictions and confidence, saves to JSONL.
2. **At sprint end** — skill prompts: "Sprint for [opportunity] ended.
   Fill in post-outcome entry. Original prediction was: [X]. What happened?"
3. **At calibration review** — skill reads the JSONL file, computes
   calibration metrics, and reports (see `references/calibration-protocol.md`).

## The Discipline

The decision journal only works if:

1. **Pre-decision entries are written BEFORE action.** Writing them after
   is hindsight theater. The skill enforces this by requiring the entry
   ID before proceeding to execution.
2. **Confidence is honest, not optimistic.** If you'd bet money on it at
   60% odds, write 60%. Don't write 80% because it feels more committed.
3. **Post-outcome entries are honest about errors.** The point is to find
   your blind spots, not to prove you were right.
4. **Entries are actually reviewed.** A journal no one reads is a diary.
   The monthly calibration review exists to force reading.

## Anti-Pattern: The Optimism Journal

Most people's first 10 decision journal entries are useless because they:

- Write 80% confidence on everything (overconfidence)
- Frame predictions vaguely ("will get traction")
- Skip the "what would prove me wrong" field
- Never write post-outcome entries because the opportunity is "still ongoing"

Force specificity. Force honesty. Force review. That's where the value is.
