# Execution Sprints — 2-Week Experiment Protocol

The skill produces opportunity briefs. Briefs without action are
intellectual entertainment. This file defines the protocol for converting
a PASS verdict into a time-boxed, kill-criteria-bound experiment.

## Why Sprints

Analysis-paralysis is the actual failure mode of most business-thinking
frameworks — more than bad ideas are. The skill can run 6 lenses + 4
frameworks per query and generate exhaustive-feeling output that still
ends in "here's a hypothesis to test" with no forcing function to act.

The sprint protocol forces action: after a PASS verdict, the deliverable
isn't "opportunities" — it's **one single next physical action the user
can take today**, followed by a 2-week sprint with pre-defined kill
criteria.

## Sprint Structure

```
Day 0: PASS verdict received.
       Define ONE next physical action (today).
       Define sprint hypothesis + kill criteria.
       Write decision journal entry (predictions).

Days 1-3: Execute first action. Observe.
          Daily 5-min check: am I learning what I expected?

Days 4-10: Iterate based on observations.
           Mid-sprint review (Day 7): kill or continue?

Days 11-14: Final push if continuing.
            Collect evidence for/against hypothesis.

Day 14 (or earlier if killed): Post-mortem within 48 hours.
                                Decision journal update (outcomes).
                                Next sprint or abandon.
```

## The ONE Next Physical Action

After a PASS verdict, the skill MUST output a single next action — not
three steps, not a roadmap. **One thing the user can do today, in under
2 hours, with what they have right now.**

Rules for the next action:
- **Physical and concrete** — not "think about" or "research." A specific
  email to send, file to create, person to call, page to publish.
- **Completable today** — under 2 hours. If it takes longer, it's not the
  next action, it's a project.
- **Generates evidence** — the action should produce a learnable signal
  (a reply, a signup, a download, a reaction).
- **Reversible** — first action should not be irreversible (no leases,
  hires, or inventory purchases as step 1).
- **Tests the riskiest assumption** — the action should test the thing
  most likely to kill the opportunity, not the thing most likely to succeed.

### Examples of Good Next Actions

- "Email 5 potential buyers with a one-paragraph description and ask
  'would you pay $X for this?'"
- "Publish a landing page with an email signup form. Drive 50 visitors
  via a niche subreddit post."
- "Ship a minimal CLI to GitHub. Post on HN Show HN."
- "Call 3 people in your network who fit the buyer profile. Ask about
  their current workaround."

### Examples of Bad Next Actions

- "Research the market further." (Vague, no signal generated.)
- "Build the MVP." (Too big for one action. What's the smallest slice?)
- "Think about pricing." (Not physical. No evidence.)
- "Set up an LLC." (Premature. Tests nothing about the opportunity.)

## Sprint Hypothesis Template

Every sprint has exactly one hypothesis. Not three. One.

```
Sprint Hypothesis:
  We believe that [specific buyer segment] will [specific behavior]
  when we [specific action/proposal].

  We will test this by [specific experiment].

  We will know we're right if [specific measurable signal] by [Day N].

Kill criteria:
  If [specific signal] does NOT happen by [Day N], we abandon.
  If [specific anti-signal] DOES happen, we abandon immediately.

Cost of sprint:
  Time: [hours]
  Money: $[amount]
  Reversible?: yes/no

Riskiest assumption being tested:
  [The one thing most likely to kill the opportunity if false.]
```

### Kill Criteria Rules

- **Specific and measurable** — "10 signups" not "traction."
- **Time-bound** — "by Day 10" not "eventually."
- **Pre-committed** — written BEFORE the sprint starts, not adjusted mid-sprint.
- **Two-sided** — define both what success looks like AND what failure looks like.
- **Honest** — don't set criteria so loose they always pass, or so tight they always fail.

## Post-Mortem Protocol (within 48 hours of sprint end)

Use the template in `templates/post-mortem-template.md`. Key sections:

1. **What was the hypothesis?** (verbatim from sprint plan)
2. **What actually happened?** (facts, not interpretation)
3. **Did we hit kill criteria?** (yes/no, with data)
4. **What did we learn that we didn't expect?** (surprises = signal)
5. **What would we do differently?** (specific, not "be better")
6. **Decision: continue / pivot / abandon** (with reasoning)
7. **Next sprint hypothesis** (if continuing or pivoting)

The post-mortem is mandatory even (especially) for killed sprints. Killed
sprints that produce no learning are double failures.

## Decision Journal Integration

Every sprint generates one decision journal entry (see
`references/decision-journal.md` and `templates/decision-journal-template.md`):

- **Pre-sprint entry** (Day 0): predictions, confidence level, reasoning
- **Post-sprint entry** (Day 14): outcomes, what was wrong, calibration note

The decision journal is the raw material for the monthly calibration review
(see `references/calibration-protocol.md`).

## Sprint Cadence

- **Solo operator, part-time**: 1 sprint at a time, 2 weeks each.
  Maximum 2 sprints in flight if they test different hypotheses.
- **Solo operator, full-time**: 1-2 sprints in parallel, 2 weeks each.
- **Team**: 1 sprint per team member, 2 weeks each. Coordinate to avoid
  testing the same hypothesis twice.

**Do not run more than 2 sprints in parallel.** Parallel sprints split
attention and degrade learning quality. If you have 3+ hypotheses to
test, queue them — don't run them simultaneously.

## When to Break Sprint Discipline

Sprints are the default. Break them only when:

1. **A black swan hits mid-sprint** — external event invalidates the
   hypothesis. Kill immediately, don't wait for Day 14.
2. **You find evidence that kills the hypothesis on Day 2** — don't
   pretend to keep learning. Kill, post-mortem, move on.
3. **A clearly better opportunity appears** — abandon current sprint
   (with post-mortem), start new one. Don't run both.
4. **You hit the kill criteria on Day 10** — kill on Day 10, don't
   extend to Day 14 hoping for a turnaround. That's sunk cost.

## Anti-Pattern: The Never-Ending Sprint

If a sprint reaches Day 14 with ambiguous results, the temptation is to
"extend by one more week to be sure." This is almost always wrong.

If Day 14 is ambiguous:
- The hypothesis was poorly defined (kill criteria weren't specific enough).
- OR the experiment didn't generate enough signal.
- OR you're rationalizing to avoid abandoning.

**Rule**: Ambiguous Day 14 = kill. Redefine hypothesis. Run a new sprint.
Don't extend. Extending is how sprints become projects, and projects
become sunk-cost traps.

## Output

After every PASS verdict, the skill outputs:

```
## Single Next Action (Today)

**ONE action**: [specific, physical, <2 hours, generates evidence]

Why this action: [tests the riskiest assumption]
Time required: [X hours]
Cost: $[Y]
Reversible: yes/no

## 2-Week Sprint Plan

**Sprint hypothesis**: [one sentence]

**Test**: [specific experiment]

**Success signal**: [measurable, by Day N]

**Kill criteria**:
- If [signal A] doesn't happen by Day [N] → abandon
- If [anti-signal B] happens → abandon immediately

**Riskiest assumption**: [the one thing most likely to kill this]

**Cost**: [time + money]
**Reversible**: yes/no

## Decision Journal Entry (Pre-Sprint)
[See templates/decision-journal-template.md — fill predictions BEFORE acting]
```
