# Golden Output Example — Worked Opportunity Brief

This is a complete worked example showing the expected output format and
depth. New agent instances should reference this when generating their own
opportunity briefs.

## Input

User message: "Find me an opportunity in AI dev tools for solo developers. I
have weekends free, $200 to spend, and want to validate something in 30 days."

Mode: Standard (default)
Intake: minimal (provided in message)

---

## Output

```
# Opportunity Brief: AI Dev Tools for Solo Developers

## Uncertainty Class
**Risk** — AI dev tools is a known category with calculable probabilities.
Multiple comparable companies exist (Cursor, Replit, Continue.dev). The
specific opportunity space within the category is more uncertain.

## Mode
Standard

## Time Horizon
- Validation: 7-30 days
- First revenue: 30-90 days
- Exit horizon: 6-24 months (acquisition target if traction emerges)

## Signal Summary
AI dev tools funding hit $2.3B in 2025 across 47 deals (Crunchbase). GitHub
issue analysis shows 230+ open feature requests across 12 popular AI coding
tools mentioning "context management" or "token budget" — a category
underserved by the major players focused on autocomplete. Reddit
r/LocalLLaMA and r/coding show weekly complaints about token costs when
using AI coding assistants on large codebases. Solo developers
specifically (not enterprise teams) are an underserved segment — most
funded tools optimize for team workflows.

## Lens Analysis

### Lens 01 (Signal Scan) — Expansion Output: 18 raw signals
[Full expansion list in appendix; top 5 listed here]
1. Cursor raised $900M Series C at $9B valuation (Dec 2025) — market validation
2. GitHub Copilot Enterprise launched but requires org-level commitment
3. Reddit: 47 weekly complaints about token costs on large repos
4. Arxiv: 12 papers on context-window optimization for code (2025)
5. Continue.dev (open-source) has 340 open issues mentioning "context strategy"
[+13 more across funding, hiring, GitHub, arxiv, social]

### Lens 02 (Demand Gap) — Expansion Output: 15 raw gaps
[Top 5]
1. "I pay $20/mo for Cursor but it forgets my codebase structure" (Reddit, weekly pattern)
2. "No good tool for managing context across multiple repos" (GitHub issue, 87 upvotes)
3. "Wish I could see token cost before sending a prompt" (Reddit, recurring)
4. "Why is there no AI coding tool for solo devs that doesn't require a team plan?" (HN, monthly)
5. "I manually copy-paste relevant files into ChatGPT because Cursor's context is too aggressive" (Reddit, daily)
[+10 more]

### Lens 03 (Arbitrage Pattern) — Contraction survivors: 4
After weak-link elimination (14 killed), survivors:
1. Skill arbitrage: solo-dev pain is underserved because funded tools optimize for teams
2. Information arbitrage: token-cost data is scattered, no aggregator
3. Platform arbitrage: open-source AI coding tools have integration gaps
4. Temporal arbitrage: 6-month window before major tools ship context management

### Lens 06 (Anti-Bias Audit) — applied to top 2 survivors
[Full table below]

### Lens 07 (Exponential Potential) — applied to finalist
[Full table below]

## Weak-Link Elimination

| # | Candidate | Weak Link | Verdict |
|---|-----------|-----------|---------|
| 1 | Build a Cursor competitor | No distribution wedge, $9B-funded incumbents | ELIMINATED |
| 2 | Token-cost dashboard extension | Zero moat, copyable in a weekend | ELIMINATED |
| 3 | Context-management CLI for solo devs | Distribution unclear, but wedge exists | SURVIVED |
| 4 | Newsletter on AI dev tools | Requires 6+ mo audience build, low asymmetry | ELIMINATED |
| 5 | Token-cost comparison site | Commoditized, ad-dependent | ELIMINATED |
| 6 | Open-source context manager + paid Pro tier | Permissionless leverage, code leverage | SURVIVED |
| 7-15 | [various] | [kill reasons documented] | ELIMINATED |

## The Opportunity

**Build an open-source CLI tool that gives solo developers visibility and
control over their AI coding assistant's context window — specifically
token cost per query, context-selection strategy, and cross-repo context
management. Monetize via a hosted Pro tier ($9/mo) with sync, team-sharing
of context strategies, and analytics.**

Wedge: solo developers are underserved by team-optimized tools. The CLI is
permissionless leverage (code) with near-zero marginal cost. Open-source
distribution solves the cold-start problem via GitHub stars and developer
word-of-mouth.

## Anti-Bias Audit

| Check | Verdict | Notes |
|-------|---------|-------|
| Uncertainty Class | Risk | Known category, calculable probabilities |
| Saturation | warning | AI dev tools is crowded, but solo-dev niche is underserved |
| Moat | warning | Open-source + accumulated context strategies (data moat over time) |
| Capital | pass | $200 covers domain + hosting for 3 months |
| Novelty | warning | CLI for context management is non-obvious; specific angle is novel |
| Asymmetry | pass | Solo-dev pain is real, $0 capital wedge, distribution via GitHub |
| Sunk Cost | pass | No prior investment; fresh start |
| 6 Pillars | 14/32 | (see below) |
| Pre-Mortem | pass | 3 failure modes articulated |
| **Overall** | **PASS (flag moat + novelty)** | |

## 6 Pillars Score

| Pillar | Score | Why |
|--------|-------|-----|
| Convexity (C) | 2 | Code leverage: ~0 marginal cost per user. Upside uncapped (entire solo-dev market). |
| Reflexivity (R) | 1 | GitHub stars drive discoverability; Pro users share strategies -> network effect, but slow loop. |
| Structural Edge (S) | 1 | Solo-dev niche is underserved, but not rule-protected. Incumbents can move in. |
| Optionality (O) | 2 | First step (build CLI, ship on GitHub) is fully reversible at $0 cost. |
| Asymmetry (A) | 2 | Forced participant: solo devs hitting token-cost pain weekly. Mispricing: incumbents optimize for teams, not solos. |
| Friction (F) | 1 | Time to first user: 2-4 weeks (GitHub distribution). CAC: low (organic). Exit: trivial (open-source, no contracts). |
| **Systemic Edge** | **(2*1*1*2*2)/(1+1) = 8/2 = 4/32** | Below 8 threshold, but Asymmetry is 2 (passes veto) and Friction is 1 (passes cap). |

**Verdict**: Score 4 is below the 8 threshold. The reflexive loop and
structural edge are weak. This is a Tier 2 (Scalable Linear) opportunity,
not a moonshot. Worth pursuing for a solo operator with weekends + $200,
but not a venture-scale bet.

## Exponential Potential (Lens 07)

| Signal | Score | Evidence |
|--------|-------|----------|
| Power-Law Tail (veto) | 1 | Realistic ceiling: $1-5M ARR exits (acquisition by Cursor/GitHub). Not 100x, but 10-20x on time invested. Passes veto at 1. |
| Convex Payoff (veto) | 2 | Downside capped at ~$200 + 30 weekends. Upside uncapped if Pro tier scales or acquisition happens. |
| Permissionless Leverage | 2 | Pure code leverage. Doubling users = ~0 marginal cost. |
| Zero Marginal Cost on Core | 2 | CLI distribution via GitHub. Pro tier sync has small server cost but <5% of revenue. |
| Algorithmic Scaling | 1 | Server costs scale with Pro users, but slowly. Could optimize further. |
| Reflexive Loop | 1 | GitHub stars -> discoverability -> more stars. Weak loop; depends on sustained novelty. |
| Network Effects | 1 | Shared context strategies (Pro feature) creates weak 2-sided network. Pre-tipping-point. |
| Pre-Chasm Position | 2 | No major tool serves solo-dev context management. Beachhead exists. |
| MTP | 0 | "Context management for solo devs" is segmentation, not transformative purpose. Fails MTP. |
| Asymmetric Bet (veto) | 2 | Downside capped at $200 + weekends. Kill criteria: <100 GitHub stars in 60 days -> abandon. |
| **Total** | **14/20** | |
| **Tier** | **Tier 2 — Scalable Linear** | Veto signals all >= 1, total 14 is in Tier 1 range (14-20), but reflexivity/network effects are weak -> demoted to Tier 2. |

**Tier reasoning**: Score 14 would normally be Tier 1 (Moonshot), but two
critical signals (Reflexivity 1, Network Effects 1) are weak. Without a
strong reflexive loop, this is a great linear business but not exponential.
Demoted to Tier 2 — Scalable Linear. This is the correct tier for a solo
operator; Tier 1 would require a network-effects story we don't have.

## Anti-Pattern Scan

| Anti-Pattern | Present? | Notes |
|---|---|---|
| Linear growth with optimism bias | not present | Honest about 10-20x ceiling, not claiming 1000x |
| Negative unit economics | not present | Pro tier margin is ~95% |
| Permissioned leverage dressed as permissionless | not present | Pure code leverage |
| Performed convexity | not present | Pitch matches financials |
| Badge networks | not present | No badge/login-as-network-effect |
| Platform dependency | possible | Distribution depends on GitHub; TOS change is a risk. Mitigation: mirror to GitLab, build email list. |
| Subsidy-driven growth | not present | No paid acquisition planned |
| Concave hardware | not present | Pure software |
| Reflexivity without downside model | not present | Pre-mortem below |
| Linear cost structure hidden | not present | Server costs scale slowly |

**Most concerning**: Platform dependency on GitHub. Mitigation: mirror repo
to GitLab from day 1, build an email list of Pro users (owned channel).

## Pre-Mortem

Assume it's January 2027 (6 months from now). The CLI failed.

**Three most likely causes:**

1. **Cursor or Continue.dev ships native context management, eliminating the wedge.**
   - Month-1 leading indicator: incumbents announce context-management feature in changelogs or roadmap
   - Month-2 leading indicator: GitHub issues about context management on incumbent repos start closing
   - Kill threshold: if Cursor ships context management before we hit 500 GitHub stars -> abandon or pivot to a different wedge

2. **Distribution never materializes — GitHub stars plateau at 50.**
   - Month-1 leading indicator: <20 stars after first week, no organic shares on HN/Reddit
   - Month-2 leading indicator: <50 stars total, no inbound Pro inquiries
   - Kill threshold: <100 stars by day 60 -> abandon

3. **Solo-dev segment is too small to monetize — Pro conversion is <1%.**
   - Month-1 leading indicator: even engaged users don't click Pro CTA
   - Month-2 leading indicator: <5 Pro signups after 200 active CLI users
   - Kill threshold: <2% Pro conversion after 30 days of active-user measurement -> pivot pricing or abandon

**Kill threshold (overall)**: <100 GitHub stars by day 60 AND <5 Pro signups
by day 90 -> abandon. Either alone is a flag; both is a kill.

## Execution Path

**Step 1 (Day 1-7)**: Build minimal CLI. Single command: `ctx budget <path>`
that scans a codebase and reports token count if sent to common AI models.
Ship on GitHub with a clear README. Post on HN "Show HN" and r/LocalLLaMA.

**Step 2 (Day 8-21)**: If >30 stars by day 14, build Pro tier MVP — context
strategy sync + token cost history. Pre-sell at $9/mo with a 14-day trial.
Target: 5 paid signups by day 30.

**Step 3 (Day 22-30)**: If 5+ paid signups, commit. If <2 paid, run user
interviews (5 solo devs) to understand why. Pivot pricing, positioning, or
abandon based on what you learn.

**Means audit (effectuation):**
- Bird-in-hand: technical skill (assumed — can build CLI), $200, weekends, GitHub account
- Affordable loss: $200 + 30 weekends = ~$2K equivalent. Acceptable.
- Crazy quilt: reach out to 3 solo-dev-focused newsletters/podcasts for early coverage
- Lemonade: if Cursor ships context management mid-build, pivot to "the
  open-source alternative that doesn't lock you into their cloud"
- Pilot-in-the-plane: ship weekly, iterate based on GitHub issues

**Distribution channel**: GitHub organic (primary), HN/Reddit launch (initial
spike), 3 newsletter/podcast partnerships (sustained), email list (owned).

## Outcomes Record

```json
{
  "opportunity": "Solo-dev AI context CLI",
  "date_reviewed": "2026-07-31",
  "verdict": "PASS (flag moat + novelty)",
  "tier": "2 — Scalable Linear",
  "systemic_edge_score": 4,
  "exponential_score": 14,
  "action_taken": null,
  "actual_outcome": null,
  "what_analysis_missed": null,
  "kill_threshold": "<100 GitHub stars by day 60 AND <5 Pro signups by day 90"
}
```

## Sources

1. Crunchbase — AI dev tools funding 2025 (https://news.crunchbase.com/...)
2. Cursor Series C — TechCrunch (https://techcrunch.com/...)
3. Reddit r/LocalLLaMA search "token cost" (https://reddit.com/...)
4. Reddit r/coding search "AI coding" (https://reddit.com/...)
5. GitHub issue search across Continue.dev, Cursor, Aider (https://github.com/...)
6. Arxiv search "context window code" 2025 (https://arxiv.org/...)
7. HN search "Ask HN AI coding solo" (https://hn.algolia.com/...)
[+ 11 more in expansion phase]
```

---

## Notes on This Example

- **ECR discipline**: 18 signals + 15 gaps expanded before contraction. 14
  kill reasons documented. No premature collapse.
- **6 Pillars + Lens 07 together**: 6 Pillars says 4/32 (below threshold);
  Lens 07 says 14/20 (Tier 1 range). The integration logic demotes to Tier 2
  because reflexivity/network effects are weak. Both lenses agree this is
  worth pursuing but not a moonshot.
- **Pre-mortem is specific**: leading indicators are observable, kill
  thresholds have dates and metrics.
- **Execution path is concrete**: 3 steps with day-by-day plan, means audit,
  distribution channel, kill criteria.
- **Honest about platform dependency**: anti-pattern scan flags GitHub
  dependency; mitigation is concrete (mirror to GitLab, build email list).

This is the depth and concreteness expected from every opportunity brief.
