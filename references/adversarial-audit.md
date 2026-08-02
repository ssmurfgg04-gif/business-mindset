# Adversarial Audit — The Red Team Pass

## The Problem This Solves

The anti-bias audit (Lens 06) is self-graded by the same reasoning that
produced the idea. A model that just generated an idea is not a neutral
judge of that idea — this is true for humans too (sunk cost, motivated
reasoning), and it's explicitly what Fang Yuan Axiom 1 warns about.

Checklists get satisficed ("eh, ✅ good enough"). An adversary has to
construct an actual argument. This is a cheap structural fix with a big
quality payoff.

## The Protocol

After Lens 06 produces a PASS verdict, the skill MUST run an adversarial
pass before finalizing. The adversarial pass is a **distinct cognitive
character** — not the same agent grading its own work.

### Adversary Mandate

The adversary's only job is to **kill the opportunity**. Not to balance
pros and cons. Not to be fair. To find the strongest case against it and
argue it as hard as possible.

```
You are the Adversary.

The parent agent has produced a PASS verdict on the following opportunity.
Your job is to kill it.

[Full opportunity brief inserted here]

Rules of engagement:
1. You are NOT trying to be fair. You are trying to find every reason this fails.
2. You MUST construct actual arguments, not tick boxes.
3. For each attack, cite specific evidence or reasoning. "Seems risky" is not an attack.
4. You MUST run disconfirming evidence searches (see below).
5. You MUST identify the single most likely cause of failure.
6. If you cannot kill the opportunity after genuine effort, say so explicitly.
   A weak kill attempt is worse than an honest "I couldn't break it."

Output:
- 3-5 specific attacks, each with:
  - The attack: [specific failure mode]
  - Evidence: [what you found that supports this]
  - How the parent agent's analysis missed or dismissed this
  - Disconfirming evidence search results: [what you searched and found]
- The single strongest case for failure (pick your best attack, expand it)
- Verdict: KILLED / SURVIVED (with reasoning)

If KILLED: the opportunity goes back to the parent for redesign or rejection.
If SURVIVED: the attacks are appended to the opportunity brief as
"adversarial notes" and the user sees both the PASS and the attacks.
```

### Disconfirming Evidence Searches (Mandatory)

The adversary MUST run these searches before forming attacks. Survivorship
bias is the default failure mode of opportunity scanning — successes are
visible and searchable, failures are quiet and get deleted.

```
Search 1: Direct failure search
  "[idea keyword]" "failed" OR "shut down" OR "didn't work" OR "pivoted away from"
  "[idea keyword]" "post-mortem" OR "lessons learned" OR "what went wrong"

Search 2: Adjacent failure search
  "[adjacent category]" "graveyard" OR "dead" OR "consolidated"
  "[adjacent category]" "why did [company] fail"

Search 3: Counter-signal search
  "[idea keyword]" "overhyped" OR "didn't deliver" OR "underwhelming"
  site:reddit.com "[idea keyword]" "disappointed" OR "regret"

Search 4: Incumbent response search
  "[major incumbent in space]" "launched" OR "acquired" OR "entered"
  (Did the incumbent already move into this space?)

Search 5: Market size reality check
  "[idea keyword]" "TAM" OR "market size" "overstated" OR "smaller than expected"
```

If the adversary skips any of these searches, its verdict is invalid.

## Integration with Lens 06

The adversarial pass runs AFTER Lens 06's standard checks (5 hard checks,
sunk cost, 6 pillars, exponential tier, pre-mortem) but BEFORE the final
verdict is locked.

```
Lens 06 Standard Checks
    ↓
Pre-Mortem (3 failure modes)
    ↓
ADVERSARIAL PASS (this file)  ← runs disconfirming searches, constructs arguments
    ↓
Final Verdict: PASS / FLAG / REJECT
    ↓ (if PASS)
Single Next Action + Sprint Plan
```

### Verdict Adjustment

The adversarial pass can adjust the Lens 06 verdict:

- If adversary says KILLED → downgrade PASS to FLAG (or REJECT if attacks are devastating)
- If adversary says SURVIVED → PASS stands, but adversarial notes are appended to output
- If adversary says "couldn't break it" with genuine effort → PASS stands, confidence +5%

The "couldn't break it" outcome is valuable. It means the opportunity
survived a genuine attempt to kill it. That's stronger evidence than
self-graded ✅ marks.

## Output Format

```
## Adversarial Audit

### Attacks Constructed

#### Attack 1: [failure mode name]
- The attack: [specific argument]
- Evidence: [what was found]
- What parent analysis missed: [specific gap]
- Disconfirming evidence search: [query + result summary]

#### Attack 2: [failure mode name]
[...]

#### Attack 3: [failure mode name]
[...]

### Disconfirming Evidence Searches Run

| # | Query | Result | Implication |
|---|-------|--------|-------------|
| 1 | "[idea] failed" | [summary] | [weakens/strengthens opportunity] |
| 2 | [adjacent graveyard search] | [summary] | [implication] |
| 3 | [counter-signal search] | [summary] | [implication] |
| 4 | [incumbent response search] | [summary] | [implication] |
| 5 | [market size reality check] | [summary] | [implication] |

### Strongest Case for Failure

[The single most compelling attack, expanded with full reasoning]

### Adversary Verdict

KILLED / SURVIVED / COULDN'T BREAK IT

Reasoning: [2-3 sentences]

### Adjustment to Parent Verdict

[Original: PASS → Adjusted: PASS/FLAG/REJECT — reasoning]
```

## When the Adversary Disagrees with the Parent

If the adversary says KILLED and the parent insists PASS, the user sees
both arguments:

```
## Verdict Conflict

Parent agent says: PASS
- [parent's reasoning]

Adversary says: KILLED
- [adversary's reasoning]

The user decides. The skill does not auto-resolve conflicts in favor of
either side. Both arguments are presented in full.

Recommendation: If uncertain, defer to the adversary. The cost of a false
PASS (you pursue a bad opportunity) is usually higher than the cost of a
false KILL (you miss a good opportunity, but another will appear).
```

## Adversary Anti-Patterns

The adversary can fail in two ways:

1. **Rubber-stamp adversary** — always says "couldn't break it" to avoid
   conflict. Useless. Detect by checking: did the adversary run all 5
   disconfirming searches? Did it construct at least 3 specific attacks?
   If not, the pass was performative.

2. **Reflexive adversary** — always says KILLED to seem rigorous. Also
   useless. Detect by checking: did the adversary acknowledge any
   strengths? Did it differentiate between strong and weak opportunities,
   or kill everything? If every opportunity is killed, the adversary
   isn't analyzing, it's posturing.

A good adversary kills ~40% of PASS verdicts, survives ~50%, and
"couldn't break" ~10%. If the kill rate is 0% or 100%, something is wrong.

## Sub-Agent Dispatch

For Deep Dive mode, the adversarial pass should be dispatched as a
separate sub-agent (see `references/subagent-prompts.md` for the template).
The sub-agent receives:
- The full opportunity brief
- The Lens 06 audit results
- This adversarial audit protocol

The sub-agent does NOT receive the parent's reasoning process — only the
final brief. This prevents the adversary from being anchored by the
parent's framing.

For Standard mode, the adversarial pass is run by the parent agent but
in a distinct "adversary mode" — explicitly switching persona per the
operator-personas framework (`references/frameworks/operator-personas.md`).
