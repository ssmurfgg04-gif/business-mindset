# Post-Mortem Template

Complete within 48 hours of sprint end. Mandatory for both completed
and killed sprints. See `references/execution-sprints.md` for full protocol.

---

## Post-Mortem — [OPPORTUNITY NAME]

### Sprint Summary
- **Sprint dates**: [start] to [end]
- **Sprint outcome**: completed / killed (Day [N]) / extended (warning)
- **Hypothesis**: [verbatim from sprint plan]
- **Kill criteria**: [verbatim from sprint plan]

### What Actually Happened
<!-- Facts only. No interpretation yet. -->
<!-- Example: "Got 47 GitHub stars, 1 Pro signup, 3 support emails" -->
<!-- NOT: "Decent traction, users seemed interested" -->

### Did We Hit Kill Criteria?
<!-- Yes/no, with data -->

- Success signal hit?: yes/no — [data]
- Kill signal hit?: yes/no — [data]

### What Did We Learn That We Didn't Expect?
<!-- Surprises = signal. The most valuable part of the post-mortem. -->

1. 
2. 
3. 

### What Would We Do Differently?
<!-- Specific, not "be better" -->
<!-- Example: "Skip HN launch; focus Discord outreach instead" -->
<!-- NOT: "Market more effectively" -->

1. 
2. 
3. 

### Decision
<!-- continue / pivot / abandon -->

**Decision**: 

**Reasoning**: [2-3 sentences. Reference specific data, not feelings.]

### If Continuing: Next Sprint Hypothesis
<!-- One sentence. What will you test next? -->

### If Abandoning: What Was the Fatal Flaw?
<!-- The single thing that killed this. Be specific. -->

**Fatal flaw**: 

**Could it have been predicted?**: yes/no — [reasoning]

**Should the skill have caught this?**: yes/no — [which lens should have flagged it]

### Calibration Check
<!-- Compare predictions to outcomes -->

- **Predicted**: [from decision journal pre-sprint entry]
- **Actual**: [what really happened]
- **Confidence was**: too high / about right / too low
- **Pattern I should remember**: [one specific lesson for similar future decisions]

### Cost Accounting
- **Time invested**: [hours]
- **Money invested**: $[amount]
- **Cost per signal learned**: $[amount / number of surprises]
- **Was it worth it?**: yes/no — [reasoning]

### Skill Feedback
<!-- What should the business-mindset skill do differently? -->

- **Which lens was most useful?**: 
- **Which lens was least useful?**: 
- **What did the skill miss?**: 
- **What should be added/changed?**: 

---

## Storage

Save completed post-mortems to:
```
~/.local/state/opencode/business-mindset-postmortems.jsonl
```

As JSON (one object per line):

```json
{
  "type": "post-mortem",
  "id": "pm-001",
  "opportunity": "[name]",
  "sprint_start": "YYYY-MM-DD",
  "sprint_end": "YYYY-MM-DD",
  "outcome": "completed/killed/extended",
  "hypothesis": "[verbatim]",
  "success_signal_hit": true/false,
  "kill_signal_hit": true/false,
  "surprises": ["...", "...", "..."],
  "would_do_differently": ["...", "...", "..."],
  "decision": "continue/pivot/abandon",
  "fatal_flaw": "[if abandoned]",
  "predicted_vs_actual": "[calibration note]",
  "time_invested_hours": [N],
  "money_invested": [N],
  "most_useful_lens": "[lens name]",
  "least_useful_lens": "[lens name]",
  "skill_missed": "[what the skill should have caught]"
}
```

These entries feed the monthly calibration review
(`references/calibration-protocol.md`).
