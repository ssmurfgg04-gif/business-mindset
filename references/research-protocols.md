# Research Protocols — Source-Specific Strategies

This file defines how to search each source type for business research.
Read this before dispatching any research sub-agents.

---

## Web Search

### Tool
`websearch` (built-in)

### Best For
- Market size and trends
- Competitor identification
- Funding/VC activity
- Pricing data
- Customer complaints and reviews
- Exponential-potential signals (network effects, marginal cost trends)

### Query Patterns
```
Market overview:
  [industry] market size growth rate [year]
  [industry] major companies revenue

Competitor:
  [company] pricing review
  [company] vs [company]

Customer sentiment:
  [product] complaints reddit
  [product] review "I wish" OR "missing"
  site:reddit.com/r/[niche] [topic]

Trends:
  [industry] trends [year]
  emerging [domain] technology
  [industry] disruption innovation

Regulatory:
  [industry] regulation changes [year]
  new compliance requirements [industry]

Exponential-potential signals (for Lens 07):
  [company] "network effects" compounding
  [company] marginal cost per user trend
  [industry] power law distribution outcomes
  [company] cohort retention curve NRR
  [space] "tipping point" OR "pre-chasm" OR "beachhead"
  [company] gross margin over time

Anti-pattern validation (for Lens 07):
  [company] unit economics contribution margin
  [company] CAC payback period trend
  [company] churn rate by cohort
  [company] "manual" OR "human-in-the-loop" scale
  [company] subsidy OR "burn rate" runway
```

### Limits
- Use 3-5 searches per research question
- Don't iterate endlessly — cap total searches at 20 per session
- Cite sources with URLs when possible

---

## GitHub Search

### Tool
`gh_grep` MCP (search) or GitHub API (`curl api.github.com`)

### Best For
- Underserved tooling gaps
- Rapidly growing repos in a domain
- Niche open-source tools that could be SaaS-ified
- Feature requests indicating market demand
- Maintainer frustration = business opportunity
- Permissionless leverage signals (fast-growing code projects)

### Query Patterns
```
Find repos with growth:
  [keyword] language:TypeScript stars:>100 pushed:>2025-01-01

Find underserved tooling:
  [keyword] language:Python  (look at issue templates for feature requests)
  topic:[domain] topic:cli topic:tool

Find hiring signals:
  [company] careers (check what roles they're hiring for)

Find integration gaps:
  [platform] integration [other platform] (what's missing?)

Find permissionless leverage signals:
  [keyword] language:TypeScript stars:>500 pushed:>2026-01-01
  (fast-growing repos = code leverage working at scale)
```

### What to Extract
- Repo stars + growth rate (fast growth = market signal)
- Issue labels like "feature request", "enhancement" with lots of 👍
- README complaints or "missing" sections
- Alternatives/comparison tables
- Recent forks with significant changes
- Marginal cost indicators (does the project scale without proportional maintainer growth?)

---

## Arxiv Search

### Tool
`webfetch` on `https://api.arxiv.org` or Google Scholar search

### Best For
- Emerging research that creates new markets
- Technology shifts with commercial applications
- Academic surveys of industry pain points
- Quantified claims about market needs
- Pre-chasm technology identification (Lens 07 Signal 8)

### Query Patterns
```
site:arxiv.org [domain] survey [year]
site:arxiv.org [domain] application
site:arxiv.org [technology] benchmark
site:arxiv.org [domain] review limitations challenges
```

### What to Extract
- Papers that describe new capabilities (these create markets)
- Papers that quantify a problem (cite numbers)
- Papers that survey industry challenges (validate demand)
- Author affiliations (who's investing in this research?)
- Citation velocity (fast-rising citations = pre-chasm signal)

---

## Social Signal Mining

### Tool
`websearch` with `site:` prefixes

### Best For
- Real complaints and frustrations (Reddit, HN)
- Early demand signals
- Community-validated pain points
- Pricing complaints (indicates willingness to pay for alternatives)
- Reflexivity loop indicators (narrative formation around a category)

### Query Patterns
```
Reddit complaints:
  site:reddit.com [product/industry] "I wish" OR "why can't" OR "frustrated"
  site:reddit.com [product/industry] "anyone else" OR "am I the only one"

Hacker News:
  site:news.ycombinator.com [topic] "Ask HN"
  site:news.ycombinator.com [topic] Show HN  (what are people building?)

Review sites:
  site:trustpilot.com [company]
  site:g2.com [category]
  site:capterra.com [category] "worst" OR "missing"

Niche forums:
  site:[niche-forum.com] [pain point]
  site:[niche-forum.com] "help" OR "suggestion"

Reflexivity / narrative indicators:
  [category] "changing everything" OR "this changes"
  [category] "tipping point" OR "crossing the chasm"
  [space] "the next [big company]"
```

### What to Extract
- Exact quotes showing pain points
- Frequency (one person vs. recurring theme)
- Context (what's the workaround?)
- Willingness-to-pay signals ("I'd happily pay for X")
- Narrative formation ("the next Stripe", "the OpenAI of X") — early reflexivity

---

## VC & Funding Signal Mining

### Tool
`websearch` with targeted queries

### Best For
- Where institutional capital is flowing (validated by people risking real money)
- What sectors are being funded vs. ignored (anti-signal)
- Which business models VCs are underwriting
- Who is raising (competitive intelligence)
- Power-law tail signals (which bets have 100x+ potential per the smart money)

### Query Patterns
```
Funding rounds:
  [industry] venture capital funding 2026
  [industry] series A B C rounds 2026
  [technology] startup funding investment

YC batch analysis:
  Y Combinator W26 batch [industry]
  YC S25 companies [category]
  Y Combinator most funded startups 2026

VC thesis:
  [VC firm] investment thesis 2026
  [VC firm] portfolio [industry]
  what [VC type] investors are looking for 2026

Anti-signal (ignored spaces):
  [industry] "lack of investment" OR "underfunded"
  [industry] "no VC interest" OR "bootstrapped profitable"

Exit signals:
  [industry] acquisition 2026
  [industry] IPO filing 2026
  [industry] SPAC merger 2026

Power-law tail validation (for Lens 07):
  [company] "100x" OR "moonshot" investor thesis
  [VC firm] "fund-returning" thesis
  [space] total addressable market "trillion"
```

### What to Extract
- Total funding flowing into a space (signal: validation)
- Number of competing funded startups (signal: crowding risk)
- Bootstrapped companies growing without VC (signal: it works without funding)
- Recent acquisitions (signal: exit path exists)
- Series/A/B ratio (high A-to-B ratio = many funded, few succeeding = graveyard)
- VC thesis pages from known firms (tells you where smart money is hunting)
- Fund-returning bets (the ones VCs publicly identify as their power-law tail)

### Warning
- VC funding validates a *market hypothesis*, not a business. Many funded
  companies fail. Don't assume funding = safety.
- The spaces VCs ignore are often more profitable for bootstrapped operators.
- VC-backed companies can afford to lose money for years. You can't. Don't
  compete on their terms.
- A "fund-returning" VC thesis is itself a reflexivity signal — the narrative
  can drive the outcome. Track both the thesis AND the underlying fundamentals.

---

## Cross-Source Validation

A signal is weak if it comes from one source. Aim for:

| Confidence | Sources Required | Example |
|------------|-----------------|---------|
| LOW | 1 source | "One Reddit thread complains about X" |
| MEDIUM | 2-3 independent sources | "Reddit + GitHub issues + blog post all mention X" |
| HIGH | 3+ diverse sources + spend evidence | "Reddit, G2, and Twitter complaints + people paying for manual X" |

For exponential-potential validation (Lens 07), require:
- Power-law tail: identified by ≥1 source explicitly OR by inference from market structure
- Convex payoff: structural analysis (not just claim)
- Network effects: ≥2 independent sources confirming the loop type

---

## Failure-Case Search (MANDATORY before any PASS verdict)

Survivorship bias is the default failure mode of opportunity scanning.
Successes are visible and searchable; failures are quiet and get deleted.
The skill MUST search for failure cases before any PASS verdict.

This is the difference between "we couldn't find disconfirming evidence"
and "we looked for disconfirming evidence and didn't find it." The former
is worthless; the latter is signal.

### The 5 Mandatory Failure-Case Queries

Run these for every opportunity that reaches the anti-bias gate:

```
1. Direct failure search:
   "[idea keyword]" "failed" OR "shut down" OR "didn't work" OR "pivoted away from"
   "[idea keyword]" "post-mortem" OR "lessons learned" OR "what went wrong"

2. Adjacent failure search:
   "[adjacent category]" "graveyard" OR "dead" OR "consolidated"
   "[adjacent category]" "why did [company] fail"

3. Counter-signal search:
   "[idea keyword]" "overhyped" OR "didn't deliver" OR "underwhelming"
   site:reddit.com "[idea keyword]" "disappointed" OR "regret"

4. Incumbent response search:
   "[major incumbent in space]" "launched" OR "acquired" OR "entered"
   (Did the incumbent already move into this space?)

5. Market size reality check:
   "[idea keyword]" "TAM" OR "market size" "overstated" OR "smaller than expected"
```

### What to Extract

| Signal | What it means | Action |
|--------|---------------|--------|
| Multiple recent failures in the exact space | Market doesn't want this, or unit economics don't work | REJECT unless you have a specific structural difference |
| Failures from 5+ years ago | Market may have changed; failures may not apply | Investigate what changed |
| Failures from underfunded/unknown operators | Execution failure, not market failure | Continue, but note the execution bar |
| Failures from well-funded operators | Market or structural problem | High alarm — REJECT unless you have a wedge they lacked |
| Incumbent already moved into the space | You're late | REJECT unless you can out-execute the incumbent (rare) |
| No failures found | Either truly novel, or you didn't search hard enough | Search harder. True novelty is rare. |

### Anti-Pattern: "No failures found" as confirmation

If you run the 5 queries and find no failures, that is NOT confirmation
that the opportunity is good. It's more likely that:
- You didn't search hard enough (try more query variants)
- The space is too new to have failures yet (higher uncertainty)
- Failures exist but aren't documented publicly (ask practitioners)

The correct interpretation of "no failures found" is: **higher uncertainty,
not higher confidence.** Flag this in the anti-bias audit.

### Integration with Adversarial Audit

The failure-case search is run by the Adversary persona during the
adversarial audit pass (see `references/adversarial-audit.md`). The
Adversary MUST run all 5 queries and report results before forming its
verdict.

### Budget Allocation

The 5 failure-case queries are IN ADDITION to the standard search budget.
Reserve 5 searches from the 20-search budget for failure cases, OR extend
the budget to 25 for Standard mode and 40 for Deep Dive mode.

---

## Search Budget

- Cap total search calls at 20 per research session (25 with failure-case queries)
- Spend budget proportionally to research phase:
  - Exploration: 40% (broad, 5-8 searches across sources)
  - Deep dive: 35% (focused, 5-7 searches on promising signals)
  - Validation: 15% (2-3 searches to verify top findings)
  - Failure-case: 10% (5 mandatory queries — see above)
- If a signal is strong after 2 independent sources, move to validation.
  Don't keep searching "for confirmation."
- For Deep Dive mode (see SKILL.md): budget extends to 40 searches across
  sub-agents (including 5 failure-case queries per sub-agent). Sub-agents
  should report their search count for synthesis.

---

## Programmatic MCP Data Source Bindings

When executing research protocols, prioritize these programmatic Model Context Protocol (MCP) servers and APIs when available in the environment:

1. **Tavily / Brave Search MCP:** For high-signal real-time market data, trend synthesis, and web scraping.
2. **GitHub MCP (`gh_grep`, repo search):** For scanning open-source developer tooling demand, open issues, and fast-growing libraries.
3. **Reddit MCP / Exa Search:** For extracting unvarnished customer complaints, "I wish someone made" threads, and consumer sentiment gaps.
4. **SQLite / Knowledge Graph MCP:** For caching and structuring multi-lens research findings across iterative sessions.
