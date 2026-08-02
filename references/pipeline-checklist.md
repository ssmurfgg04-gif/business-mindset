# Pipeline Execution Checklist — Mandatory Pre-Verdict Compliance

## The Problem This Solves

<problem>
The skill now has 15+ mandatory steps across 16 lenses, 4 verification protocols,
and 8 frameworks. The v0.5.0 failure proved that having the frameworks isn't
enough — the agent must actually EXECUTE them. Without a checklist, the agent
will skip steps silently, producing confident verdicts from incomplete analysis.

**The pilot's rule**: No takeoff until every checklist item is verified. Same
for the skill: no verdict until every mandatory step is executed and reported.

This file is the execution enforcement mechanism. Every PASS/FLAG/REJECT
verdict MUST include the completed checklist. A verdict without the checklist
is invalid.
</problem>

## The Mandatory Checklist

<checklist>
Before producing any verdict, the agent MUST complete and report this checklist.
Each item: EXECUTED / SKIPPED (with reason) / N/A.

### Phase 0: Setup
- [ ] **0.1 Mode selected** (Quick Check / Standard / Deep Dive)
- [ ] **0.2 Operator context loaded** (intake OR autonomous defaults)
- [ ] **0.3 Domain playbook loaded** (tech-saas / services / physical-products / boring-business / none)
- [ ] **0.4 Frameworks loaded** (fang-yuan + operator-personas + operator-wisdom + mental-models)

### Phase 1: Expansion (ECR Phase 1)
- [ ] **1.1 Lens 01 expansion**: 15-20+ raw signals generated
- [ ] **1.2 Lens 02 expansion**: 15-20+ raw demand gaps generated
- [ ] **1.3 Lens 03 expansion** (if applicable): 15-20+ arbitrage candidates
- [ ] **1.4 No premature contraction** (expansion quota enforced before any elimination)

### Phase 2: Contraction (ECR Phase 2)
- [ ] **2.1 Weak-link elimination applied** per lens
- [ ] **2.2 Kill log documented** (every killed candidate has a one-sentence reason)
- [ ] **2.3 3-5 survivors per lens** identified

### Phase 3: Real-World Verification (MANDATORY — no exceptions)
- [ ] **3.1 GitHub search executed** (actual API calls, 3+ query variants)
- [ ] **3.2 GitHub results reported** (total repos, top competitor stars)
- [ ] **3.3 Commercial search executed** (web search for commercial competitors)
- [ ] **3.4 Commercial results reported** (named competitors, funding if known)
- [ ] **3.5 Saturation score computed** (0 to -11+ range)
- [ ] **3.6 Saturation verdict applied** (≤-9 = REJECT, -6 to -8 = needs wedge)
- [ ] **3.7 If search couldn't be executed**: FLAGGED as "verification incomplete"

### Phase 4: Demand Validation (MANDATORY for PASS)
- [ ] **4.1 Reddit mining executed** (7-query protocol, target subreddits identified)
- [ ] **4.2 Reddit results reported** (WTP signals, workaround evidence, frequency)
- [ ] **4.3 Customer interview protocol prepared** (7 Mom Test questions ready)
- [ ] **4.4 If interviews conducted**: 10+ interviews, scored 0/1/2 on 5 dimensions
- [ ] **4.5 If interviews NOT conducted**: FLAGGED as "interview validation incomplete"
- [ ] **4.6 Sean Ellis test** (if existing product): ≥40% "very disappointed" = PMF

### Phase 5: Distribution Pre-Gate (Lens 16 — MANDATORY)
- [ ] **5.1 Distribution audit completed** (5 questions answered)
- [ ] **5.2 Distribution assets assessed** (owned vs rented, current vs buildable)
- [ ] **5.3 Channel engineering plan** (primary, secondary, tertiary channels)
- [ ] **5.4 Distribution moat assessment** (compounds? owned? replicable? network effect?)
- [ ] **5.5 Distribution risk assessment** (platform dependency <40%?)
- [ ] **5.6 Distribution-first filter** (6 questions, all must pass for PROCEED)

### Phase 6: Anti-Bias Gate (Lens 06)
- [ ] **6.1 Knightian Uncertainty classified** (Known / Risk / Knightian)
- [ ] **6.2 5 Hard Checks** (saturation, moat, capital, novelty, asymmetry)
- [ ] **6.3 Sunk Cost Reflection** (would I start this today?)
- [ ] **6.4 6 Pillars Score** (C, R, S, O, A, F — compute Systemic Edge)
- [ ] **6.5 Exponential Tier** (Lens 07: 10 signals, 3 veto, tier rating)
- [ ] **6.6 Risk of Ruin** (Lens 08: Kelly criterion, survival capacity)
- [ ] **6.7 Pre-Mortem** (3 failure modes, leading indicators, kill thresholds)
- [ ] **6.8 5-Minute Bias Checklist** (confirmation, sunk cost, anchoring, availability, overconfidence)
- [ ] **6.9 Disconfirming evidence search** (5 failure-case queries, results reported)

### Phase 7: Adversarial Audit (MANDATORY for PASS)
- [ ] **7.1 Adversary persona engaged** (or sub-agent dispatched)
- [ ] **7.2 3-5 specific attacks constructed** (with evidence, not box-ticking)
- [ ] **7.3 Single strongest failure case identified**
- [ ] **7.4 Adversary verdict** (KILLED / SURVIVED / COULDN'T BREAK IT)
- [ ] **7.5 Verdict adjustment applied** (KILLED → downgrade PASS to FLAG)

### Phase 8: Multi-Persona Synthesis
- [ ] **8.1 Operator (Fang Yuan) analysis** (cold rational)
- [ ] **8.2 Steward analysis** (relational/reputational factors) — if applicable
- [ ] **8.3 Adversary analysis** (already done in Phase 7)
- [ ] **8.4 Synthesis** (how personas integrated, disagreements presented)

### Phase 9: Domain Confidence Adjustments
- [ ] **9.1 Domain characteristics identified** (named category? regulated? capital-intensive? etc.)
- [ ] **9.2 Confidence adjustments applied** (stack: e.g., AI dev tool for healthcare = -45%)
- [ ] **9.3 80/20 rejection rule check** (is this in the 80% that should be rejected?)

### Phase 10: Final Verdict
- [ ] **10.1 All mandatory phases executed** (or skipped with documented reason)
- [ ] **10.2 Verdict produced** (PASS / FLAG / REJECT)
- [ ] **10.3 If PASS**: Single Next Action + 2-week sprint plan + decision journal prompt
- [ ] **10.4 If FLAG**: what needs to change for PASS
- [ ] **10.5 If REJECT**: why, and pivot suggestion
- [ ] **10.6 Outcomes record** (JSONL entry for calibration tracking)

### Phase 11: Output Compliance
- [ ] **11.1 Reasoning trace included** (which phases executed, which skipped, why)
- [ ] **11.2 Checklist included in output** (this file, completed)
- [ ] **11.3 All mandatory sections present** (per output format in SKILL.md)
</checklist>

## The Reasoning Trace

<reasoning_trace>
Every verdict MUST include a reasoning trace showing which steps were executed,
which were skipped, and why. This makes the skill auditable.

**Format**:
```
### Reasoning Trace

| Phase | Step | Status | Notes |
|-------|------|--------|-------|
| 0 | Mode selected | EXECUTED | Deep Dive |
| 0 | Operator context | EXECUTED | Autonomous defaults ($0, 10-15 hrs/wk) |
| 0 | Domain playbook | EXECUTED | boring-business |
| 1 | Lens 01 expansion | EXECUTED | 18 signals |
| 1 | Lens 02 expansion | EXECUTED | 16 gaps |
| 2 | Weak-link elimination | EXECUTED | 30 killed, 4 survivors |
| 3 | GitHub search | EXECUTED | 3 queries, 114+129+184 repos, top 19,514★ |
| 3 | Commercial search | EXECUTED | 2 named competitors (Smithery, mcp.so) |
| 3 | Saturation score | EXECUTED | -11 → REJECT |
| 4 | Reddit mining | SKIPPED | Rate limited; FLAGGED as incomplete |
| 4 | Customer interviews | SKIPPED | No access to buyers; FLAGGED |
| 5 | Distribution pre-gate | EXECUTED | FAILS — no owned distribution |
| 6 | Anti-bias gate | SKIPPED | Rejected at Phase 3 (saturation) |
| 7 | Adversarial audit | SKIPPED | Rejected at Phase 3 |
| 8 | Multi-persona | SKIPPED | Rejected at Phase 3 |
| 9 | Confidence adjustments | EXECUTED | AI dev tool -20%, named category -20% = -40% |
| 10 | Final verdict | EXECUTED | REJECT (saturation -11 + distribution fail) |

### Skipped Steps Justification
- Phase 4 (Reddit/interviews): Rate limited on web search. Flagged as incomplete.
  Would not change verdict (already REJECT at Phase 3).
- Phases 6-8: Not executed because Phase 3 saturation score (-11) triggers
  automatic REJECT. No need to run further analysis on a saturated opportunity.
```

**The principle**: If a step is skipped, the reason must be documented. If
the reason is "rate limited" or "no access," the verdict must be FLAGGED
accordingly. Silent skipping is forbidden.
</reasoning_trace>

## Skip Rules

<skip_rules>
Some steps can be legitimately skipped. The rules:

### Auto-REJECT skips (no need to continue)
If any of these trigger, skip remaining phases and produce REJECT:
- Phase 3 saturation score ≤ -9
- Phase 5 distribution-first filter fails (6 questions, any critical fail)
- Phase 6.6 Risk of Ruin REJECT (can't survive losing the bet)
- Phase 6.2 Hard Check: saturation ❌ OR moat ❌
- Phase 9 confidence adjustments ≤ -50% (e.g., AI dev tool for healthcare)

### Legitimate skips (with documentation)
- **Rate limited on search**: FLAG as "verification incomplete," don't PASS
- **No access to buyers for interviews**: FLAG as "interview validation incomplete"
- **Quick Check mode**: Phases 1-5, 7-9 can be skipped (only Phase 6 runs)
- **Domain N/A**: Skip domain playbook if none applies

### Forbidden skips (always mandatory)
These CANNOT be skipped regardless of mode or rate limits:
- Phase 3 (real-world verification) — if can't execute, FLAG, don't PASS
- Phase 5 (distribution pre-gate) — always runs
- Phase 6.1 (Knightian classification) — always runs
- Phase 6.6 (Risk of Ruin) — always runs for capital/time commitments
- Phase 10 (verdict with reasoning trace) — always runs
- Phase 11 (output compliance) — always runs

### The rule
**If you can't execute a mandatory step, you can't produce PASS.** You can
produce FLAG ("verification incomplete") or REJECT (if other factors warrant),
but not PASS. PASS requires complete verification.
</skip_rules>

## Output Template

<output_template>
Every Opportunity Brief MUST end with:

```
### Pipeline Execution Checklist

| Phase | Steps | Executed | Skipped | Notes |
|-------|-------|----------|---------|-------|
| 0 Setup | 4 | [N] | [N] | [reasons] |
| 1 Expansion | 4 | [N] | [N] | [reasons] |
| 2 Contraction | 3 | [N] | [N] | [reasons] |
| 3 Real-World Verification | 7 | [N] | [N] | [reasons] |
| 4 Demand Validation | 6 | [N] | [N] | [reasons] |
| 5 Distribution Pre-Gate | 6 | [N] | [N] | [reasons] |
| 6 Anti-Bias Gate | 9 | [N] | [N] | [reasons] |
| 7 Adversarial Audit | 5 | [N] | [N] | [reasons] |
| 8 Multi-Persona | 4 | [N] | [N] | [reasons] |
| 9 Confidence Adjustments | 3 | [N] | [N] | [reasons] |
| 10 Final Verdict | 6 | [N] | [N] | [reasons] |
| 11 Output Compliance | 3 | [N] | [N] | [reasons] |

### Compliance Verdict
- [ ] All mandatory phases executed (or skipped with documented reason)
- [ ] No silent skips
- [ ] Reasoning trace included
- [ ] Verdict consistent with checklist (PASS requires all mandatory passes)

### If PASS: required conditions met
- [ ] Phase 3 saturation score > -6
- [ ] Phase 4 demand validated (Reddit OR interviews)
- [ ] Phase 5 distribution pre-gate passed
- [ ] Phase 6 all hard checks passed
- [ ] Phase 7 adversary SURVIVED or COULDN'T BREAK
- [ ] Phase 9 confidence adjustments > -30%
```

**Without this checklist, the verdict is invalid.**
</output_template>

## The Audit Trail

<audit_trail>
The checklist serves three purposes:

### 1. Self-enforcement
The agent must complete the checklist before producing a verdict. This forces
execution of all mandatory steps. Can't skip what you have to report.

### 2. User audit
The user can see exactly what was executed, what was skipped, and why. If the
user sees "Phase 3 SKIPPED — rate limited" on a PASS verdict, they know the
verdict is unreliable.

### 3. Calibration data
Over time, the checklists accumulate as data. Patterns emerge:
- Which phases are most often skipped? (indicates access problems)
- Which skip reasons are most common? (indicates infrastructure gaps)
- Which verdicts with skipped steps later proved wrong? (indicates which
  skips are actually OK vs which are fatal)

This feeds back into the calibration protocol
(`references/calibration-protocol.md`).
</audit_trail>

## Integration with SKILL.md

<integration>
The pipeline checklist is referenced in SKILL.md's Important Constraints:

> **MANDATORY: Pipeline Execution Checklist**
> (`references/pipeline-checklist.md`) must be completed and included in
> every Opportunity Brief output. A verdict without the completed checklist
> is invalid. Every skipped step must have a documented reason. If a
> mandatory step cannot be executed (rate limit, no access), the verdict
> must be FLAGGED, not PASS.

This is the execution enforcement layer. The frameworks define WHAT to think
about; the checklist enforces THAT you think about it.
</integration>
