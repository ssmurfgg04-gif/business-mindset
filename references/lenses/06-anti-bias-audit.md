# Lens 06: Anti-Bias Audit — Is This Actually Good or Just Familiar?

## Core Question

Does this opportunity survive hard scrutiny, or is it the AI defaulting to
familiar patterns?

## When to Use

- **ALWAYS** on every output. This is the gate that prevents saturation drift.
- Also when user says "is this a good idea" or "stress-test this."

## Pre-gate: Knightian Uncertainty Classification

Before running the 5 checks, classify the opportunity on the uncertainty
spectrum. This determines how much trust to place in the analysis:

```
Known (clear market, clear model, comparable exist)
  → Standard audit. Apply all 5 checks normally.
  → Example: "Open a coffee shop in this neighborhood"

Risk (probabilities calculable, some data available)
  → Standard audit + flag all assumptions explicitly.
  → Example: "Launch a SaaS in a known category"

Knightian Uncertainty (unknown unknowns, no comparable)
  → Heavy burden of proof. Default: REJECT unless:
     a) The user has specific structural advantage
     b) The asymmetry is clearly identified
     c) It can be validated for $0 in under 7 days
  → Example: "Build a new category of AI agent"
```

**If Knightian Uncertainty**: The AI has the lowest confidence here. Present
every conclusion as a hypothesis to be tested, not a recommendation.

## The 5 Hard Checks

### 1. Saturation Check
```
Is the market accessible to everyone via public internet?
  YES → Anyone can compete. What's the barrier?
         No barrier? → FLAG (require specific wedge)

Does success depend on winning on an open marketplace?
  (Etsy, Fiverr, Upwork, Gumroad, App Store with no distribution)
  YES → FLAG (require owned-channel backup plan)

Does the core mechanic involve being cheaper/faster than others?
  YES → FLAG (require structural cost advantage: IP, regulatory, relationship)
```

### 2. Moat Check
```
After 1 year of competition, what prevents someone from copying this?
  Nothing?   → REJECT. Zero-moat.
  Brand?     → Valid but takes years.
  Data?      → Strong if proprietary/accumulated.
  Network?   → Strong if users create value for each other.
  Tech?      → Weak unless truly novel (most tech isn't).
  Switching costs? → Strong if built into workflow.

If the moat is "I'll just be better" → REJECT.
```

### 3. Capital Check
```
How much money is needed to start?
  $0          → Ideal. Proceed.
  $1-$500     → Manageable. Flag it.
  $500-$5000  → Needs validation first.
  $5000+      → REJECT unless user has capital and explicitly says so.

Is the business model cash-flow positive from day one?
  Service paid upfront → Good.
  Freemium → Needs 3-6 months runway.
  Subscription with 30-day trial → Needs reserve.
```

### 4. Novelty Check
```
Is this idea in the top 10 Google results for "[idea] business"?
  YES → Too obvious. What's the twist?
  YES + no twist → REJECT. Commodity.

Has this been done before in a different context?
  YES → That's OK. Can you adapt it to an underserved niche?
  YES + 10 competitors already → REJECT. Too late.

Is the idea genuinely non-obvious?
  The user should react with "huh, I hadn't thought of that"
  not "yeah, I've seen that before."
```

### 5. Asymmetry Check
```
What specific advantage does THIS user have?
  Domain knowledge?  → Strong
  Existing access?   → Strong (a list, a community, a relationship)
  Technical skill?   → Medium (many have this)
  Location?          → Depends on the opportunity
  Timing?            → Strong if first-mover in a window
  No advantage?      → REJECT. Competition will eat you.

If autonomous mode (no intake provided), use defaults:
  Domain knowledge?  → Assume none unless user stated context
  Existing access?   → Assume none
  Technical skill?   → Assume average
  Then: only Structural Edge (rule-based) or Timing advantage qualifies.
  Flag this clearly: "Running in autonomous mode; user-specific asymmetry not assessed."

Is the advantage structural (can't be easily replicated) or just personal?
  Structural → Good (e.g., "I have a list of 500 potential buyers")
  Personal → Weak (e.g., "I'm a fast learner")
```

## Audit Decision Matrix

```
Saturation  |  Moat  |  Capital  |  Novelty  |  Asymmetry  |  Verdict
────────────┼────────┼───────────┼───────────┼─────────────┼───────────
  ✅/⚠️     |   ✅   |    ✅     |    ✅     |     ✅      |  PASS
  ✅/⚠️     |   ✅   |    ✅     |    ⚠️     |     ✅      |  PASS (flag novelty)
  ❌        |   —    |    —      |    —      |     —       |  REJECT (saturated)
  ✅/⚠️     |   ❌   |    —      |    —      |     —       |  REJECT (zero moat)
  ✅        |   ✅   |    ❌     |    ✅     |     ✅      |  FLAG capital
  ✅        |   ⚠️   |    ✅     |    ✅     |     ✅      |  PASS (watch moat)
  ✅/⚠️     |   ✅   |    ✅     |    ✅     |     ❌      |  FLAG (autonomous mode) or REJECT (with intake)
```

### 6. Sunk Cost Reflection (Fang Yuan Axiom 1)

```
Has the user (or you) already invested time/money/effort in this direction?
  YES → Would you start this today if you hadn't already started?
  NO  → Why not? What has changed? Be honest.

Are you avoiding an idea because it's "boring" or "too small"?
  YES → That's ego. Boring + profitable beats exciting + competitive.
  
Are you attracted to an idea because it's "cool" or "impressive"?
  YES → That's ego. Cool doesn't pay rent.

Would you advise a stranger to do this?
  If the answer changes when the subject changes from yourself to a stranger,
  you're emotionally attached. Flag it.
```

## 6 Pillars Integration

Pass the opportunity through the 6 Pillars of Asymmetric Execution
(see `references/frameworks/asymmetric-execution.md`):

| Pillar | Check | Score (0/1/2) |
|--------|-------|---------|
| Convexity | Is the payoff structure non-linear? (capped loss, uncapped upside) | 0/1/2 |
| Asymmetry | Is the mispricing structural, not just unnoticed? | 0/1/2 |
| Optionality | Can first steps be reversed? Is there a $0 exit? | 0/1/2 |
| Reflexivity | Does success create more success? Self-reinforcing loop? | 0/1/2 |
| Structural Edge | Is the advantage rule-based (not luck-based)? | 0/1/2 |
| Friction | What % of returns get eaten by costs/slippage/time? | 0/1/2 |

**Compute**: `Systemic Edge = (C × R × S × O × A) / (1 + F)`. Range 0-32.
**Pass threshold**: ≥ 8, with A ≥ 1 (Asymmetry mandatory) and F ≤ 1 (Friction capped).

If 3+ pillars score 0 → REJECT regardless of other checks.

## Familiarity Trap Counter-Patterns

The AI will naturally generate ideas that look like the most common business
patterns in its training data. This is the **familiarity trap**. Actively
counter it:

| Familiar default | What to ask instead |
|-----------------|---------------------|
| SaaS subscription | Is there a one-time payment service? A done-for-you deliverable? |
| Content monetization | Is there a direct buyer who will pay before content exists? |
| Marketplace | Is there a service that doesn't need two-sided liquidity? |
| AI wrapper | Is there a real operational problem that AI happens to help with? |
| Freelance on Upwork | Can you find one direct client through your network? |
| Affiliate marketing | Can you do something with higher intent and fewer middlemen? |
| Newsletter | Who's the buyer if you have 0 subscribers? Don't default to audience-building. |
| Niche community | What's the monetization path that doesn't require 6+ months? |

**If the final 3-5 survivors are all familiar defaults**, trigger ECR
re-expansion: go back to Phase 1 with explicit instruction to find
non-default candidates.

## Pre-Mortem (Mandatory for PASS Verdicts)

Before declaring PASS, the agent MUST run a pre-mortem:

```
Assume it's 6 months from now. This opportunity failed.

The 3 most likely causes:
1. <specific failure mode>
   Leading indicator (month 1): <observable signal>
   Leading indicator (month 2): <observable signal>
2. <specific failure mode>
   Leading indicator (month 1): <observable signal>
   Leading indicator (month 2): <observable signal>
3. <specific failure mode>
   Leading indicator (month 1): <observable signal>
   Leading indicator (month 2): <observable signal>

Kill threshold:
- If [specific metric] is not achieved by [specific date], abandon.
- If [specific signal] appears, abandon immediately.
```

If the agent cannot articulate 3 plausible failure modes, the analysis is
incomplete. Either dig deeper or downgrade to FLAG.

## 5-Minute Bias Audit Checklist

Before finalizing any verdict, run this 5-check routine. Each check forces
a specific cognitive bias to surface. This is separate from the 5 Hard
Checks above — those evaluate the opportunity; these evaluate your
thinking about the opportunity.

### 1. Confirmation Bias Check
**Question**: What evidence would prove me wrong?
- If you can't articulate specific disconfirming evidence, you haven't
  looked for it. Run the failure-case search in `references/research-protocols.md`.
- If you found disconfirming evidence and dismissed it, ask why. "Their
  situation was different" is often rationalization.

### 2. Sunk Cost Check
**Question**: Would I start this today if I hadn't already invested in it?
- This applies to time invested in research, not just money.
- If the answer is "no," the analysis is being driven by sunk cost, not
  expected value. Kill or radically restructure.

### 3. Anchoring Check
**Question**: Am I anchored to the first number/idea I heard?
- The first market size, first competitor price, first user count — these
  anchor all subsequent thinking.
- Force a re-derivation: "If I'd never heard [anchoring number], what
  would I estimate?"
- Common anchors: the user's stated budget, the first competitor's pricing,
  the first TAM figure from a Google result.

### 4. Availability Check
**Question**: Is this decision based on recent events or base rates?
- Recent = the last 3 things you read, the most vivid case study, the
  most recent failure story.
- Base rates = the actual statistical frequency of this outcome.
- Force base-rate thinking: "Of 100 opportunities like this, how many
  succeed?" If you don't know the base rate, that's a flag — you're
  reasoning from anecdotes.

### 5. Overconfidence Check
**Question**: What's my 90% confidence interval for the key prediction?
- Force a range, not a point estimate. "100 signups" becomes "30-300 signups."
- If the range is too narrow (< 2x spread), you're overconfident.
- If you can't articulate the range, you haven't thought about variance.
- Apply calibration adjustment from `references/calibration-protocol.md`
  if available. Most agents are 15-20% overconfident by default.

### Checklist Output

```
### Bias Audit Checklist

| Check | Result | Notes |
|-------|--------|-------|
| Confirmation bias | ✅/⚠️/❌ | [disconfirming evidence found + considered] |
| Sunk cost | ✅/⚠️/❌ | [would I start today?] |
| Anchoring | ✅/⚠️/❌ | [what was the anchor? did I re-derive?] |
| Availability | ✅/⚠️/❌ | [base rate vs recent anecdote] |
| Overconfidence | ✅/⚠️/❌ | [90% CI: X to Y] |

If 2+ checks score ❌ → downgrade PASS to FLAG, FLAG to REJECT.
```

## Disconfirming Evidence Requirement (MANDATORY)

No PASS verdict is valid without explicit disconfirming evidence search.

See `references/research-protocols.md` "Failure-Case Search" section.
The 5 mandatory queries MUST be run and results reported before the
verdict is finalized.

```
### Disconfirming Evidence Search Results

| Query | Result | Implication |
|-------|--------|-------------|
| "[idea] failed" | [summary] | [weakens/strengthens/neutral] |
| Adjacent graveyard search | [summary] | [implication] |
| Counter-signal search | [summary] | [implication] |
| Incumbent response search | [summary] | [implication] |
| Market size reality check | [summary] | [implication] |

If no failures found: flag as "higher uncertainty, NOT higher confidence"
(see anti-pattern in research-protocols.md).
```

A PASS verdict without this section is invalid. The skill MUST run the
failure-case search before PASS.

## Adversarial Audit Pass (MANDATORY for PASS verdicts)

After the standard checks, bias checklist, and disconfirming evidence
search, the skill MUST run an adversarial pass before finalizing PASS.

See `references/adversarial-audit.md` for the full protocol. Summary:

1. **Switch to adversary mode** (or dispatch adversary sub-agent in Deep Dive)
2. **Adversary's mandate**: kill the opportunity. Not be fair — find the
   strongest case against it.
3. **Adversary constructs 3-5 specific attacks**, each with evidence and
   reasoning (not box-ticking)
4. **Adversary identifies the single strongest failure case**
5. **Adversary verdict**: KILLED / SURVIVED / COULDN'T BREAK IT

### Verdict Adjustment

- KILLED → downgrade PASS to FLAG (or REJECT if attacks are devastating)
- SURVIVED → PASS stands, adversarial notes appended to output
- COULDN'T BREAK IT (with genuine effort) → PASS stands, confidence +5%

A weak or performative adversary (rubber-stamp or reflexive killer) is
detected by checking: did it run all 5 disconfirming searches? Did it
construct at least 3 specific attacks? If not, the adversarial pass was
invalid and must be re-run.

### Why This Matters

The anti-bias audit is self-graded by the same reasoning that produced
the idea. A model that just generated an idea is not a neutral judge of
that idea. Checklists get satisficed ("eh, ✅ good enough"); an adversary
has to construct an actual argument. This is a cheap structural fix with
a big quality payoff.

## Output

```
### Anti-Bias Audit Results

| Check | Verdict | Notes |
|-------|---------|-------|
| Uncertainty Class | Known/Risk/Knightian | |
| Saturation | ✅/⚠️/❌ | [Why] |
| Moat | ✅/⚠️/❌ | [What prevents copying] |
| Capital | ✅/⚠️/❌ | [How much, where from] |
| Novelty | ✅/⚠️/❌ | [How non-obvious] |
| Asymmetry | ✅/⚠️/❌ | [The specific advantage, or "autonomous mode — not assessed"] |
| Sunk Cost | ✅/⚠️/❌ | [Ego check passed?] |
| 6 Pillars | Score X/32 | [Pillar breakdown] |
| Pre-Mortem | ✅/⚠️/❌ | [3 failure modes articulated] |
| Bias Checklist | ✅/⚠️/❌ | [5 checks: confirmation, sunk cost, anchoring, availability, overconfidence] |
| Disconfirming Evidence | ✅/⚠️/❌ | [5 failure-case queries run, results reported] |
| Adversarial Audit | SURVIVED/KILLED/COULDN'T BREAK | [3-5 attacks, strongest case] |
| Risk of Ruin (Lens 08) | ✅/⚠️/❌ | [Survival capacity, position size] |
| **Overall** | **PASS/FLAG/REJECT** | |

**If FLAG**: What needs to change for this to become viable.
**If REJECT**: Why, and a pivot suggestion if applicable.

### Pre-Mortem Watch List
1. [failure mode 1] → [month-1 leading indicator]
2. [failure mode 2] → [month-1 leading indicator]
3. [failure mode 3] → [month-1 leading indicator]

Kill threshold: [specific metric + date]

## Cross-Session Learning Record

After the user acts (or doesn't) on this opportunity, record the outcome
for future sessions:

```
# Outcome Record (auto-prompted if >14 days old and action_taken is null)
Opportunity: [brief name]
Date reviewed: YYYY-MM-DD
Verdict: PASS/FLAG/REJECT
Tier: 1/2/3
Action taken: [started / skipped / investigated / other]
Actual outcome: [success / failure / ongoing / abandoned]
What was wrong about the analysis: [what the audit missed]
```

Store in `~/.local/state/opencode/business-mindset-outcomes.jsonl`
One JSONL entry per review. Future sessions read this to calibrate confidence
(see SKILL.md "Outcomes Feedback Loop" section).
```

---

## Decision Protocol

### Exact Question This Lens Answers
"Does this opportunity survive hard scrutiny, or is it the AI defaulting
to familiar patterns?"

### Data Required
- All other lenses' outputs (this is the gate, runs last)
- 5 hard checks completed (saturation, moat, capital, novelty, asymmetry)
- Sunk cost reflection
- 6 pillars score
- Exponential tier (Lens 07)
- Pre-mortem (3 failure modes)
- Bias checklist (5 checks)
- Disconfirming evidence search (5 queries)
- Adversarial audit pass
- Risk of ruin (Lens 08)

### Confidence Threshold
- **PASS**: All hard checks ✅ or ⚠️ (no ❌), 6 pillars ≥8 with A≥1 and F≤1, pre-mortem articulated, bias checklist ≥3✅, adversary SURVIVED or COULDN'T BREAK, risk of ruin PASS
- **FLAG**: 1-2 hard checks ❌, or 6 pillars 4-7, or bias checklist 2❌, or adversary KILLED (but attacks addressable), or risk of ruin FLAG
- **REJECT**: Saturation ❌, or moat ❌, or 6 pillars <4, or bias checklist ≥3❌, or adversary KILLED with devastating attacks, or risk of ruin REJECT, or Safety Floor violation

### Conflict Resolution Rules
- **Lens 06 is the final gate.** It overrides all other lenses. If Lens 06 says REJECT, the opportunity is rejected regardless of what other lenses say.
- When Lens 06 disagrees with Lens 07 (Exponential):
  - Anti-bias REJECT + exponential Tier 1 → **reject anyway**. A "moonshot" that fails saturation/moat is a fantasy.
  - Anti-bias PASS + exponential Tier 3 → **pass as Tier 3**. Linear businesses are valid; just set expectations.
- When Lens 06 disagrees with the adversarial audit:
  - If adversary KILLED and Lens 06 says PASS → **downgrade to FLAG**. Present both arguments to user.
  - If adversary COULDN'T BREAK and Lens 06 says FLAG → **consider upgrade to PASS**. Genuine survival is strong evidence.
- When Lens 06 disagrees with Lens 08 (Risk of Ruin):
  - Risk of ruin REJECT always wins. Survival trumps opportunity. No exceptions.
- When in doubt:
  - Default to FLAG, not PASS. The cost of a false PASS (pursuing a bad opportunity) is higher than the cost of a false FLAG (delaying a good one).
