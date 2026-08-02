# Calibration Dataset — 12 Opportunities Tested Against Real-World Verification

This dataset records the skill's analysis of 12 diverse opportunities, with
**actual GitHub search results** run on 2026-07-31. It serves as:

1. **Calibration data** — future analyses can compare against these baselines
2. **Reference examples** — shows how the verification protocol works in practice
3. **Honest record** — includes opportunities the skill REJECTED based on real data

## The Critical Lesson

<lesson>
The skill's first real-world test (the "solo-dev AI context CLI") revealed a
critical flaw: the skill produced a confident PASS verdict without actually
verifying the opportunity existed in reality. When GitHub searches were run,
the "opportunity" had 427+ competing repos, including 3 with >1,000 stars
(largest: 19,514 stars).

**The fix**: The real-world verification protocol
(`references/real-world-verification.md`) now makes actual searches mandatory
before any PASS verdict. This dataset is the first run of that corrected
pipeline.

**The lesson for the skill**: Frameworks don't search the web. The agent
does. And the agent is biased toward confirming its own analysis. Only
mandatory real searches counteract this.
</lesson>

## Dataset Summary

| # | Opportunity | GitHub repos | Top competitor (stars) | Saturation | Verdict |
|---|-------------|--------------|------------------------|------------|---------|
| 1 | AI context management CLI | 114+129+184+106 = 533 | 19,514 (context-mode) | -11 | **REJECT** |
| 2 | EU AI Act compliance tool | 133 | 235 (sbom-tools) | -3 | FLAG (need wedge) |
| 3 | SOC 2 automation for indie | 83 | 4,299 (ciso-assistant) | -7 | **REJECT** |
| 4 | Substack churn reduction | 0 | None | +2 | FLAG (verify market exists) |
| 5 | Stripe Agent SDK wrapper | 0 | None | +3 | FLAG (early, build fast) |
| 6 | AI dispatch for HVAC/plumbing | 6 | 0 (all early) | +1 | FLAG (early, verify demand) |
| 7 | Token cost dashboard | 420 | 1,146 (TokenTracker) | -8 | **REJECT** |
| 8 | Vercel-for-AI-models hosting | 14 | 241 (guide, not product) | +1 | FLAG (capital-intensive) |
| 9 | Boring business roll-up tech | 1 | 0 | +2 | FLAG (execution-heavy) |
| 10 | AI content authenticity | 411 | 27 (early) | -4 | FLAG (crowded early) |
| 11 | Newsletter monetization | 1 | 0 | +2 | FLAG (fuzzy WTP) |
| 12 | Vertical AI for legal | 19 | 19 (low) | +1 | FLAG (regulatory barrier) |

**Summary**: 3 REJECT (saturated), 9 FLAG (need wedge or validation), 0 clean PASS.

This is the honest result. Most opportunities are either saturated or need
significant differentiation. Clean PASS opportunities are rare — and the
skill should reflect that reality, not manufacture false confidence.

---

## Opportunity 1: AI Context Management CLI

### Original analysis (FLAWED — pre-verification)
The skill produced a confident PASS verdict. Tier 2 (Scalable Linear). Single
Next Action: build the CLI.

### Real-world verification (ACTUAL GitHub searches)
```
Query 1: "ai context management cli" → 114 repos
  Top: chainofdive/ravenclaw (13 stars) — DIRECT competitor, early

Query 2: "token cost cli ai" → 129 repos
  Top: getagentseal/codeburn (9,051 stars) — DIRECT, dominant
  Top: xiufengsun/TokenTracker (1,146 stars) — DIRECT
  Top: agentforce314/clawcodex (819 stars) — DIRECT

Query 3: "context window coding ai" → 184 repos
  Top: mksglu/context-mode (19,514 stars) — DIRECT, dominant
  Top: matt1398/claude-devtools (3,779 stars) — DIRECT
  Top: graykode/abtop (3,401 stars) — DIRECT

Query 4: "ai context budget token" → 106 repos
  Multiple direct competitors with 17-261 stars
```

### Saturation score
- 2 repos >5000 stars: -6
- 1 repo >1000 stars: -2
- 3 queries with 50+ repos: -3
- **Total: -11 (SATURATED — REJECT)**

### Corrected verdict: **REJECT**
The opportunity is real (demand exists) but already served by dominant
open-source competitors. To enter, you'd need 10x better execution or a wedge
the incumbents structurally can't serve. The skill's original PASS was wrong
because it didn't verify.

### What the skill learned
- The disconfirming evidence search MUST be actual searches, not memory
- "I didn't find failures" ≠ "I searched and found no competitors"
- Dominant open-source competitors (>1000 stars) are a near-fatal signal

---

## Opportunity 2: EU AI Act Compliance Tool

### Real-world verification
```
Query: "eu ai act compliance tool" → 133 repos
  Top: sbom-tool/sbom-tools (235 stars) — adjacent (SBOM, not AI Act specific)
  Top: Hiepler/EuConform (123 stars) — DIRECT competitor
  Top: GenAI-Gurus/awesome-eu-ai-act (79 stars) — resource list, not product
```

### Saturation score
- 50+ repos: -1
- Top competitor 100-500 stars (moderate): -1
- Existing direct competitor with 123 stars: -1
- **Total: -3 (MODERATE — need wedge)**

### Verdict: **FLAG**
Market exists, early competitors present but not dominant. Need clear wedge:
- Vertical specialization (specific industry)
- SMB focus (incumbents may be enterprise)
- Compliance automation (vs just classification)

### What the skill would recommend
If pursuing: identify what EuConform (123 stars) does poorly, build 10x better
for specific segment. Don't build generic — build for [specific industry]
compliance teams.

---

## Opportunity 3: SOC 2 Automation for Indie SaaS

### Real-world verification
```
Query: "soc2 compliance automation" → 83 repos
  Top: intuitem/ciso-assistant-community (4,299 stars) — DIRECT, dominant
  Top: strongdm/comply (1,565 stars) — DIRECT, focused on SOC2
  Top: theopenlane/core (279 stars) — DIRECT, multi-framework
```

### Saturation score
- 1 repo >1000 stars: -2
- 1 repo >1000 stars: -2 (second one)
- Top competitor >4000 stars: -3 (additional, dominant)
- **Total: -7 (HIGH saturation)**

### Verdict: **REJECT**
The market is served by dominant open-source competitors. Vanta/Drata dominate
commercial; ciso-assistant dominates open-source. To enter, you'd need 10x
better or a wedge (e.g., SOC 2 specifically for 1-person SaaS at $50/mo —
but unit economics likely don't work).

### What the skill learned
- Even "indie-focused" positioning doesn't save you when open-source has 4,000+ stars
- SOC 2 is a crowded category — the wedge must be extreme

---

## Opportunity 4: Substack Churn Reduction Tool

### Real-world verification
```
Query: "substack churn reduction" → 0 repos
Query: "substack churn retention" → 0 repos
```

### Saturation score
- 0 repos: +2 (no competitors found)
- **Total: +2 (LOW saturation — but verify market exists)**

### Verdict: **FLAG**
No competitors found, but that could mean:
1. Genuinely novel (rare)
2. No market (more likely — Substack may not have enough churn-reduction demand)
3. Market exists but isn't on GitHub (Substack creators aren't on GitHub)

### What the skill would recommend
Before building: validate demand directly with Substack creators. Survey 50+
creators with >5K subs. If >30% say they'd pay for churn reduction, proceed.
If not, the market doesn't exist.

---

## Opportunity 5: Stripe Agent SDK Wrapper

### Real-world verification
```
Query: "stripe agent sdk wrapper" → 0 repos
Query: "stripe ai agent payment" → 0 repos
```

### Saturation score
- 0 repos: +2 (no competitors found)
- Stripe SDK is new (released 2026): +1 (timing advantage)
- **Total: +3 (LOW saturation — early window)**

### Verdict: **FLAG (build fast)**
No competitors found. Stripe Agent SDK is new (2026), so the window is open.
But:
1. The window will close (Stripe may build it themselves, or competitors emerge)
2. Need to move fast (ship in 30 days)
3. Distribution is the challenge (reaching AI agent developers)

### What the skill would recommend
If pursuing: ship minimal wrapper in 30 days. Target: AI agent developers
(reach via GitHub, HN, AI dev Discord). Risk: Stripe ships native version
in 6-12 months.

---

## Opportunity 6: AI Dispatch for HVAC/Plumbing

### Real-world verification
```
Query: "ai dispatch hvac plumbing" → 6 repos
  Top: philippemart/trade-services-ai (0 stars) — DIRECT, very early
  Top: olu3242/VeloCity-Field-service- (0 stars) — adjacent
  Top: dwayne-brown-jr/switchboard (0 stars) — DIRECT, AI phone agent
```

### Saturation score
- All repos 0 stars: +1 (very early market)
- **Total: +1 (LOW saturation — early market)**

### Verdict: **FLAG (verify demand)**
Very early market — no dominant competitors. But:
1. Need to verify demand (do HVAC/plumbing businesses want AI dispatch?)
2. Distribution is hard (reaching local service businesses)
3. Domain expertise required (HVAC/plumbing workflows)

### What the skill would recommend
If pursuing: talk to 20 HVAC/plumbing business owners first. If >30% want AI
dispatch and would pay, proceed. Distribution: trade associations, Facebook
groups (where these businesses hang out), cold outreach.

---

## Opportunity 7: Token Cost Dashboard

### Real-world verification
```
Query: "token cost dashboard" → 420 repos
  Top: xiufengsun/TokenTracker (1,146 stars) — DIRECT, dominant
  Top: nateherkai/token-dashboard (651 stars) — DIRECT
  Top: mikehasa/agentacct (538 stars) — DIRECT
```

### Saturation score
- 1 repo >1000 stars: -2
- 2 repos >500 stars: -2
- 50+ repos: -1
- 100+ repos: -1
- 400+ repos: -2
- **Total: -8 (HIGH saturation)**

### Verdict: **REJECT**
The token cost dashboard market is heavily saturated. Multiple competitors
with 500-1,146 stars. Same as Opportunity 1 — the AI dev tooling space is
crowded.

---

## Opportunity 8: Vercel-for-AI-Models Hosting

### Real-world verification
```
Query: "ai model hosting vercel" → 14 repos
  Top: iSoumyaDey/Awesome-Web-Hosting-2026 (241 stars) — guide, not product
  Top: Gsync/chatsync (2 stars) — adjacent
  Top: animexteam/telebothost-mcp (2 stars) — adjacent
```

### Saturation score
- <50 repos: +1
- Top "competitor" is a guide, not product: +1
- **Total: +2 (LOW saturation)**

### Verdict: **FLAG (capital-intensive)**
No dominant open-source competitor. But:
1. Capital-intensive (GPU hosting requires significant capital)
2. Existing commercial competitors (RunPod, Baseten, Modal, Replicate)
3. Not viable for solo operator with $0-$500 capital

### What the skill would recommend
REJECT for solo operator (capital requirement too high). Would be viable for
team with $500K+ seed funding.

---

## Opportunity 9: Boring Business Roll-Up Tech Enablement

### Real-world verification
```
Query: "boring business roll up" → 1 repo (irrelevant)
Query: "local service business ai saas" → 0 repos
```

### Saturation score
- 0 relevant repos: +2
- **Total: +2 (LOW saturation)**

### Verdict: **FLAG (execution-heavy)**
No competitors in open-source. But:
1. This is an execution play, not a product play
2. Requires acquiring/operating boring businesses
3. Capital-intensive (acquiring businesses)
4. Not viable for solo operator with $0-$500

### What the skill would recommend
REJECT for solo operator. Would be viable for operator with $100K+ capital
and operational expertise in local services.

---

## Opportunity 10: AI Content Authenticity Verification

### Real-world verification
```
Query: "ai content authenticity" → 411 repos
  Top: Ram-nishal/ai-content-authenticity-detector-using-metadata (27 stars)
  Top: mrvaudebhardwaj/JobShield-AI (13 stars)
  Top: Sachin-deepak-S/Retrace-AI (13 stars)
```

### Saturation score
- 400+ repos: -2
- Top competitor <50 stars: +1 (no dominant player)
- **Total: -4 (MODERATE-HIGH saturation, but no dominant player)**

### Verdict: **FLAG (crowded early market)**
Many competitors (411 repos) but none dominant (top is 27 stars). This means:
1. Market exists (people are building)
2. No winner yet (opportunity for someone to win)
3. But: crowded, hard to differentiate
4. Commoditization risk (AI detection is becoming a feature, not product)

### What the skill would recommend
FLAG. If pursuing, need extreme differentiation (e.g., authenticity for
specific industry like journalism, legal evidence). Don't build generic.

---

## Opportunity 11: Newsletter Monetization Beyond Ads

### Real-world verification
```
Query: "newsletter monetization owned" → 1 repo
  Top: closermethod/newsletter-growth-mcp (0 stars) — adjacent
```

### Saturation score
- 0 direct competitors: +2
- **Total: +2 (LOW saturation)**

### Verdict: **FLAG (fuzzy WTP)**
No direct competitors. But:
1. Fuzzy willingness to pay (newsletter creators are cheap)
2. Market may not exist at scale
3. Adjacent tools (beehiiv, ConvertKit) may add features

### What the skill would recommend
FLAG. Before building: validate WTP with 50+ newsletter creators with >5K
subs. If >30% would pay $20-50/mo, proceed. If not, market doesn't exist.

---

## Opportunity 12: Vertical AI for Legal

### Real-world verification
```
Query: "vertical ai legal" → 19 repos
  Top: ncasias/fb (19 stars) — irrelevant
  Top: zoom/arlo (12 stars) — irrelevant
  Top: scope-bid/scope-mcp (1 star) — adjacent (litigation dispatch)
```

### Saturation score
- <50 repos: +1
- No dominant competitor: +1
- **Total: +2 (LOW saturation)**

### Verdict: **FLAG (regulatory barrier)**
No dominant open-source competitor. But:
1. High regulatory barrier (legal industry is regulated)
2. Distribution is hard (reaching law firms)
3. Liability risk (AI giving wrong legal advice)
4. Existing commercial competitors (Harvey, Eve, etc. — funded)

### What the skill would recommend
FLAG. If pursuing, need:
- Domain expertise (legal background or co-founder with one)
- Regulatory compliance review
- Liability insurance
- Distribution via legal bar associations

Not viable for solo operator without legal domain expertise.

---

## Calibration Insights

<insights>
After running the corrected pipeline on 12 opportunities:

### 1. Most opportunities are saturated or need significant wedge
- 3 of 12 (25%) were REJECT (saturated)
- 9 of 12 (75%) were FLAG (need wedge or validation)
- 0 of 12 (0%) were clean PASS

**Implication**: The skill should rarely produce clean PASS verdicts. If it
does, the verification probably wasn't thorough enough. Clean PASS opportunities
are rare — and the skill should reflect that reality.

### 2. The "AI dev tools" space is heavily saturated
- Opportunity 1 (context management): 533 repos, top 19,514 stars — REJECT
- Opportunity 7 (token dashboard): 420 repos, top 1,146 stars — REJECT

**Implication**: AI dev tools is one of the most crowded categories. The skill
should default to skepticism for any AI dev tool opportunity.

### 3. "Boring" and unsexy markets are less saturated
- Opportunity 6 (HVAC/plumbing AI): 6 repos, all 0 stars — early market
- Opportunity 9 (boring business roll-up): 0 repos — open market

**Implication**: The skill's bias toward "interesting" AI/tech opportunities
misses less-crowded unsexy markets. Future analyses should explicitly check
unsexy adjacent markets.

### 4. Zero competitors can mean "no market" not "blue ocean"
- Opportunity 4 (Substack churn): 0 repos — but may not have market
- Opportunity 5 (Stripe Agent wrapper): 0 repos — but SDK is new

**Implication**: "0 competitors found" is ambiguous. It could mean blue ocean
(rare) or no market (common). The skill must validate demand separately when
no competitors exist.

### 5. Capital requirement is a common disqualifier
- Opportunity 8 (Vercel for AI): needs $500K+ for GPU hosting
- Opportunity 9 (roll-up): needs $100K+ for acquisitions
- Opportunity 12 (legal AI): needs regulatory/legal expertise

**Implication**: Many opportunities exist but aren't viable for solo operators
with $0-$500. The skill's autonomous defaults ($0 capital) should reject these
automatically.

### 6. The skill's original bias toward "AI dev tools" was wrong
The first real-world test produced "solo-dev AI context CLI" as the finalist.
Actual GitHub search showed 533 repos with dominant competitors. The skill
was biased toward the AI dev tool category because:
- The test was run by an AI (bias toward AI tools)
- AI dev tools get a lot of press (availability bias)
- AI dev tools seem "cool" (founder ego bias)

**Implication**: The skill needs to actively counter its bias toward AI/tech
opportunities. The anti-patterns-compendium should include "AI dev tool bias"
as a specific anti-pattern.
</insights>

## Updated Confidence Adjustments

Based on this calibration dataset, future analyses should apply these
confidence adjustments:

| Pattern | Adjustment |
|---------|------------|
| AI dev tool opportunity | -20% confidence (saturated category) |
| Opportunity with 0 GitHub competitors | -10% confidence (may not have market) |
| Opportunity requiring >$5K capital | Auto-REJECT for solo operator defaults |
| Opportunity in regulated industry | -15% confidence (barrier too high) |
| "Boring"/unsexy market | +10% confidence (less crowded) |

These adjustments feed into the calibration protocol
(`references/calibration-protocol.md`) for ongoing calibration.

## The Meta-Lesson

<meta_lesson>
The skill had all the right frameworks — anti-bias, adversarial, disconfirming
evidence. But it still produced a wrong PASS verdict on the first real test.
The problem wasn't the frameworks. The problem was that frameworks don't
search the web. The agent does. And the agent is biased toward confirming
its own analysis.

**The fix wasn't more frameworks. It was mandatory real searches.**

This is the meta-lesson for AI cognition engines: the gap between "having
the right framework" and "doing the right thing" is execution. The skill
must enforce execution of verification, not just awareness of the need for it.

The real-world verification protocol
(`references/real-world-verification.md`) is the enforcement mechanism. This
calibration dataset is the proof that it works.
</meta_lesson>
