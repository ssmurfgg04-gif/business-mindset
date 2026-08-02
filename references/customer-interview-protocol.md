# Customer Interview Protocol — The Mom Test and Beyond

## Why This Matters

<why>
Most founder customer interviews are worthless. The founder asks "would you
use this?" The customer says "yes" (to be polite). The founder builds. Nobody
buys. The founder is confused.

**The Mom Test** (Rob Fitzpatrick, 2013) is the canonical fix: ask about
the past, not the future. Ask about specific behaviors, not opinions. The
customer's mom would say your idea is great — that's the test. If your
questions would make your mom lie to you, they're bad questions.

This protocol integrates the Mom Test with YC user research, Sean Ellis
PMF testing, and practitioner wisdom into a structured interview methodology
the skill can execute.
</why>

## The 5 Principles

<principles>

### 1. Ask about the past, not the future
**Bad**: "Would you use this?" (Future — polite lie)
**Good**: "When did you last have this problem?" (Past — concrete recall)

People can't predict their future behavior. They can recall past behavior
accurately. Always anchor to specific past events.

### 2. Ask about specific behaviors, not opinions
**Bad**: "Do you think this is a good idea?" (Opinion — meaningless)
**Good**: "What did you do the last time this happened?" (Behavior — real)

Opinions are free. Behaviors cost time/money. Behaviors reveal true priorities.

### 3. Ask about money, not interest
**Bad**: "Are you interested in this?" (Interest — everyone's interested)
**Good**: "How much did you pay to solve this last time?" (Money — validated)

Interest ≠ demand. Money = demand. Always probe willingness to pay through
past behavior.

### 4. Listen for problems, not solutions
**Bad**: Pitch your solution, ask if they like it
**Good**: Listen to their problem, ignore your solution

If you pitch your solution, the customer will react to your pitch (polite or
critical). If you listen to their problem, you learn whether your solution
fits.

### 5. Watch for the "compliment smoke bomb"
**Bad**: Customer says "that sounds great!" (Compliment — ends conversation)
**Good**: Redirect — "Thanks. But what did you do last time this happened?"

Compliments feel good but provide no information. When a customer compliments
your idea, redirect to behavior. The compliment is the conversation-ender;
the behavior question is the conversation-continuer.
</principles>

## The 7-Question Framework

<framework>
Based on YC's canonical 5 questions + Mom Test + Sean Ellis. Use these 7
questions in order. Don't add. Don't skip.

### Question 1: "Tell me about the last time you [had this problem]."
**Why**: Forces specific recall. Past behavior, not future opinion.
**Listen for**: When, where, what happened, who was involved.
**Red flag**: "I haven't really had that problem." (No demand — kill or pivot)

### Question 2: "What did you do to solve it?"
**Why**: Reveals current workaround and willingness to act.
**Listen for**:
- "I used [tool]" — current solution (your competitor)
- "I did it manually" — automation opportunity
- "I ignored it" — pain not severe enough (kill)
- "I hired someone" — high WTP signal

### Question 3: "How much did that cost you?"
**Why**: Validates willingness to pay. Past spend = future WTP.
**Listen for**:
- Specific dollar amount ("$500/month") — strong WTP
- "A lot of time" — time cost, calculable
- "Nothing, I just dealt with it" — weak demand
- Avoids the question — embarrassed about spend (premium solution possible)

### Question 4: "What was hard about solving it?"
**Why**: Surfaces the specific pain your solution should address.
**Listen for**: Specific friction ("the integration broke," "took 3 hours,"
"didn't match our workflow"). Generic complaints ("it was annoying") are weak.
**Red flag**: "It was fine, no problems." (Pain not severe — kill)

### Question 5: "Why was that hard?"
**Why**: Gets to the root cause, not the symptom.
**Listen for**: Structural reasons (workflow, integration, regulation) vs
implementation reasons (bug, UI). Structural = opportunity. Implementation =
incumbent weakness.

### Question 6: "What solutions have you tried or evaluated?"
**Why**: Reveals competitive landscape from the buyer's perspective.
**Listen for**:
- Tools they tried and abandoned — why? (your wedge)
- Tools they considered but didn't try — why? (positioning insight)
- "Nothing" — early market or low pain

### Question 7: "Who else should I talk to?"
**Why**: Network effects for interviews. 1 interview → 3 referrals → 9 → 27.
**Listen for**: Specific names (warm intros) vs "I don't know anyone" (cold).
**Bonus**: "Would you be willing to pre-pay for a solution?" (If yes → validated
demand. If no → keep interviewing.)
</framework>

## The Sean Ellis PMF Test

<sean_ellis>
After 20-30 customer interviews, run the Sean Ellis test:

**Question**: "How would you feel if you could no longer use [product]?"
- Very disappointed
- Somewhat disappointed
- Not disappointed
- N/A (I no longer use it)

**Scoring**:
- ≥40% "very disappointed" → Product-Market Fit achieved
- 25-40% → On the path, iterate
- <25% → No PMF, pivot or kill

**Critical**: Ask this only of ACTIVE users (used in past 2 weeks), not all
signups. Inactive users will say "not disappointed" because they don't use it.

**Use in Lens 13 (Growth)**: Don't scale acquisition until Sean Ellis ≥40%.
Scaling pre-PMF = premature scaling = 74% of failures.
</sean_ellis>

## The 3-Tier Commitment Hierarchy

<commitment_hierarchy>
When evaluating demand signals from interviews, rank by commitment level:

### Tier 1: Money (highest signal)
- "I'd pre-pay $X for this"
- "I already pay $Y for [bad solution]"
- Customer writes a check before product exists

**Action**: Build. Validated demand.

### Tier 2: Reputation (medium signal)
- "I'll introduce you to 5 peers with the same problem"
- "I'll be a reference customer"
- Customer puts their reputation on the line

**Action**: Build with their input. Strong signal.

### Tier 3: Time (lowest meaningful signal)
- "I'll do a 30-min call to give feedback"
- "I'll be a beta tester"
- Customer invests time but no money/reputation

**Action**: Validate further. Not enough to build.

### Tier 0: Words (no signal)
- "That sounds great!"
- "I'd definitely use that"
- "Interesting idea"

**Action**: Ignore. These are polite lies. Build nothing on words alone.
</commitment_hierarchy>

## The Push-Back Move

<push_back>
When a customer says "I'd use that" or "That sounds great," DON'T accept it.
Push back:

**Customer**: "That sounds great, I'd definitely use it!"
**You**: "I appreciate that, but I'm trying to understand if this is a real
problem. When was the last time you had this specific issue?"

**Customer**: "Well, I haven't actually had it recently, but if I did, I'd
use your tool."
**You**: "Got it. So this isn't a current pain point for you. Thanks for
the feedback — that's actually helpful."

**The insight**: Customers are polite. Your job is to find the IMPOLITE truth.
Push back on compliments. Probe for specific behaviors. Walk away if there's
no real pain.

**Anti-pattern**: Founders love compliments and avoid conflict. They accept
"that sounds great" as validation and skip the push-back. This is how bad
products get built.
</push_back>

## The Post-Interview Scoring Rubric

<scoring>
After each interview, score 0/1/2 on 5 dimensions:

| Dimension | 0 (no signal) | 1 (weak) | 2 (strong) |
|-----------|---------------|----------|------------|
| **Problem severity** | "Haven't had this" | "Sometimes annoying" | "Cost me $X / Y hours" |
| **Current solution** | "Nothing" | "Manual workaround" | "Pay for bad solution" |
| **WTP signal** | "Wouldn't pay" | "Maybe $X" | "Already pay $Y" |
| **Specificity** | Vague complaints | Some detail | Specific workflow, tools, costs |
| **Referral** | "Don't know anyone" | "Maybe I can think of someone" | Names 2+ peers, offers intro |

**Scoring**:
- 8-10: Strong opportunity — advance to validation sprint
- 5-7: Moderate — interview 5 more, re-evaluate
- 0-4: Weak — kill or pivot

**After 10 interviews**: If average score ≥7, proceed. If <5, kill. If 5-7,
interview 10 more (the answer is in more interviews, not more analysis).
</scoring>

## Few-Shot Examples

<examples>

### Example 1: Good interview (HVAC dispatch)

<example>
<interview>
**Founder**: "Tell me about the last time you had a scheduling conflict with
your technicians."

**HVAC owner**: "Last Tuesday. Had two AC emergency calls come in at the same
time. I had to call my lead tech, pull him off a maintenance job, and the
maintenance customer was pissed."

**Founder**: "What did you do to solve it?"

**HVAC owner**: "Manually called around, ended up sending my son (who's
learning) to the maintenance job to apologize and reschedule. Lost the
maintenance revenue."

**Founder**: "How much did that cost you?"

**HVAC owner**: "The maintenance was $300. Plus the customer might not come
back, so lifetime value maybe $2000."

**Founder**: "What was hard about solving it?"

**HVAC owner**: "I didn't know where my techs were. I'm using a whiteboard and
text messages. Couldn't see who was closest to the second call."

**Founder**: "Why was that hard?"

**HVAC owner**: "Because I don't have software. ServiceTitan is $400/month per
user, I have 3 techs, that's $1200/month. Can't justify it for a 3-truck
operation."

**Founder**: "What solutions have you tried?"

**HVAC owner**: "Looked at Jobber, but it's not HVAC-specific. ServiceTitan is
the industry standard but too expensive. I just use paper and texts."

**Founder**: "Who else should I talk to?"

**HVAC owner**: "Two other owners in my ACCA chapter have the same issue. Let
me introduce you."
</interview>

<analysis>
**Scoring**:
- Problem severity: 2 (cost $300 + $2000 LTV)
- Current solution: 2 (manual — whiteboard + texts)
- WTP signal: 2 (already considered $1200/mo, just can't justify)
- Specificity: 2 (specific workflow, tools, costs)
- Referral: 2 (named 2 peers, offered intro)

**Total: 10/10 — STRONG opportunity.**

**Insights for product**:
- Wedge: dispatch + scheduling, not full FSM
- Pricing: $50-150/mo (vs $400 ServiceTitan) — they've considered $1200/mo, so WTP is high
- Distribution: ACCA chapter referrals (warm intros)
- Feature priority: real-time tech location, smart dispatch
</analysis>
</example>

### Example 2: Bad interview (polite lies)

<example>
<interview>
**Founder**: "Tell me about the last time you struggled with project management."

**Marketing manager**: "Oh, all the time! Project management is always a
struggle."

**Founder**: "What did you do to solve it?"

**Marketing manager**: "We use Asana. It works fine."

**Founder**: "How much did that cost you?"

**Marketing manager**: "I think it's $25/user/month. Not bad."

**Founder**: "What was hard about it?"

**Marketing manager**: "Nothing really. Asana is pretty good."

**Founder**: "Why was that hard?"

**Marketing manager**: "It wasn't really hard. We're happy with Asana."

**Founder**: "What solutions have you tried?"

**Marketing manager**: "We looked at Monday and ClickUp, but Asana works fine."

**Founder**: "Who else should I talk to?"

**Marketing manager**: "I don't really know anyone who struggles with this."
</interview>

<analysis>
**Scoring**:
- Problem severity: 0 (no specific problem mentioned)
- Current solution: 1 (uses Asana, satisfied)
- WTP signal: 0 (already pays for Asana, no pain)
- Specificity: 0 (vague, no details)
- Referral: 0 (doesn't know anyone with the problem)

**Total: 1/10 — WEAK opportunity. Kill.**

**Insight**: The customer was being polite. There's no real pain here. Asana
serves them fine. Don't build a PM tool for marketing managers.

**The Mom Test worked**: By asking about specific past behavior, we discovered
there's no real problem — despite the initial "all the time!" enthusiasm.
</analysis>
</example>
</examples>

## Integration with the Skill

<integration>
The Customer Interview Protocol runs as part of Lens 02 (Demand Gap) and
Lens 13 (Growth, Stage 0):

```
Lens 02 expansion:
1. Run Reddit Mining Protocol (reddit-mining-protocol.md)
2. Run G2/Capterra review mining
3. Run GitHub issue mining
4. Run Customer Interview Protocol (this file) — interview 10+ potential customers
5. Synthesize demand gaps with interview-validated signals weighted highest

Lens 13 Stage 0 (pre-PMF):
1. Talk to 10-20 customers/month using Customer Interview Protocol
2. Run Sean Ellis test after 20+ active users
3. Don't scale until Sean Ellis ≥40%
```

**If customer interviews cannot be conducted** (no access to buyers):
FLAG the analysis as "customer validation incomplete." Do not produce PASS
verdict without interview validation.

## Anti-Patterns

<anti_patterns>
1. **Pitching instead of listening**: Founder spends 20 minutes pitching,
   5 minutes "listening" to compliments. Bad interview.

2. **Asking about the future**: "Would you use this?" gets polite lies.
   Always ask about the past.

3. **Accepting compliments**: "That sounds great!" is not validation. Push
   back to behavior.

4. **Interviewing friends/family**: They'll lie to protect your feelings.
   Interview strangers.

5. **Interviewing one segment**: Talk to 10 different buyer types. Don't
   over-index on one segment's feedback.

6. **Not recording**: Take verbatim notes. Don't summarize — you'll lose
   the exact language (which is your marketing copy).

7. **Stopping at 5**: 5 interviews isn't enough. Interview 10-20 minimum.
   Patterns emerge at scale.

8. **Asking leading questions**: "Don't you hate when X happens?" leads
   the witness. Ask open-ended: "Tell me about the last time..."
</anti_patterns>

## The Meta-Lesson

<meta_lesson>
Customer interviews are the #1 validation tool, but most founders do them
wrong. The Mom Test's insight: ask about the past, not the future. Ask about
behaviors, not opinions. Ask about money, not interest.

The skill's Lens 02 mentioned customer interviews but didn't have a structured
protocol. This file provides that protocol — 7 questions, 3-tier commitment
hierarchy, push-back move, scoring rubric, and integration with the broader
pipeline.

**The execution gap**: Like the real-world verification protocol, the Customer
Interview Protocol only works if actually executed. The skill must enforce
execution — no PASS verdict without interview validation.

**The calibration insight**: Across 30+ mental simulations, opportunities
that would fail customer interviews (saturated markets with no real pain)
were sometimes given PASS verdicts. Interview validation catches what
frameworks miss.
</meta_lesson>
