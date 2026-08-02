# Decision Journal Entry Template

Copy this template for each decision. Fill in BEFORE acting on a PASS
verdict. See `references/decision-journal.md` for full protocol.

---

## Decision Journal Entry — [DATE]

### Decision
<!-- One-sentence description of the opportunity/action -->

### Skill Verdict
<!-- PASS / FLAG / REJECT — and tier if applicable -->

### My Prediction
<!-- Specific, measurable prediction of what will happen -->
<!-- BAD: "will get traction" -->
<!-- GOOD: "100 GitHub stars + 5 Pro signups in 30 days" -->

**Prediction**: 

### Confidence Level
<!-- Honest probability estimate. If you'd bet money on it at 60% odds, write 60%. -->
<!-- Don't write 80% because it feels more committed. -->

**Confidence**: [%]

### Key Assumptions
<!-- 3-5 assumptions. If any is false, prediction fails. -->
1. 
2. 
3. 

### Reasoning
<!-- 2-3 sentences. Reference specific evidence, not gut feeling. -->

### What Would Prove Me Wrong
<!-- Specific, observable signal that would invalidate the prediction -->

**Disconfirming signal**: 

### Kill Criteria
<!-- Pre-committed. If X happens or Y doesn't happen by Z date, abandon. -->

- If [signal] does NOT happen by [date] → abandon
- If [anti-signal] DOES happen → abandon immediately

### Emotions at Decision Time
<!-- Honest note. Catches ego-driven bets. -->
<!-- Excited? Anxious? Bored? Reluct? -->

**Emotional state**: 

### Time Horizon for Review
<!-- When will you check if this prediction was right? -->

**Review date**: [date]

---

## Post-Outcome Entry (fill in AFTER result is known)

### What Actually Happened
<!-- Facts only. No interpretation yet. -->

### Did I Hit My Prediction?
<!-- Yes / Partially / No — with data -->

### Did I Hit Kill Criteria?
<!-- Killed / Survived / N/A -->

### What Did I Get Wrong?
<!-- Specific assumptions that were false. Be honest. -->

### What Did I Get Right?
<!-- Specific assumptions that held up. -->

### What Surprised Me?
<!-- Things I didn't predict at all but turned out to matter. -->

### Calibration Note
- Predicted confidence: [%]
- Outcome: [success/failure]
- [If high confidence + failure: overconfident. If low confidence + success: underconfident.]

### Lessons for Similar Future Decisions
<!-- 1-2 specific, transferable lessons. Not "be more careful" — that's useless. -->
<!-- Things like "enterprise sales cycles are 2x longer than I assume" -->

1. 
2. 

### Would I Make This Decision Again?
<!-- Yes / No / With changes: [specific changes] -->

---

## Storage

Save completed entries to:
```
~/.local/state/opencode/business-mindset-decisions.jsonl
```

As JSON (one object per line):

```json
{
  "type": "pre-decision",
  "id": "dec-001",
  "date": "YYYY-MM-DD",
  "opportunity": "[name]",
  "skill_verdict": "PASS",
  "tier": "2",
  "prediction": "[specific prediction]",
  "confidence_pct": [X],
  "assumptions": ["...", "...", "..."],
  "reasoning": "[2-3 sentences]",
  "disconfirming_evidence_signal": "[specific]",
  "kill_criteria": "[specific]",
  "emotions": "[honest note]",
  "review_date": "YYYY-MM-DD"
}
```

After outcome:
```json
{
  "type": "post-outcome",
  "id": "dec-001",
  "date": "YYYY-MM-DD",
  "actual_outcome": "[facts]",
  "prediction_hit": "yes/partially/no",
  "kill_criteria_hit": "killed/survived/n-a",
  "what_i_got_wrong": "[specific]",
  "what_i_got_right": "[specific]",
  "surprises": "[specific]",
  "calibration": "[note]",
  "lessons": ["...", "..."],
  "would_do_again": "yes/no/with-changes: [changes]"
}
```
