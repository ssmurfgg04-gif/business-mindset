# Real-World Verification Protocol — Mandatory Before Any PASS

## The Problem This Solves

The skill's anti-bias audit (Lens 06) includes "disconfirming evidence search"
but in practice this is often performed as "I searched and didn't find
failures" — which is worthless. The skill doesn't actually RUN searches; it
relies on the agent's memory, which is biased toward not finding what it
doesn't want to find.

**Real-world verification means actually executing searches** against:
1. GitHub (does this already exist as open-source?)
2. Product Hunt (has this been launched recently?)
3. Google (is the market saturated?)
4. Reddit/HN (are people already complaining about alternatives?)
5. Crunchbase (are funded companies already doing this?)
6. App stores (for mobile apps)

**If you don't actually run these searches, you're not verifying — you're
assuming.** And assuming kills opportunities that look novel but are saturated.

## The Mandatory Verification Protocol

<protocol>
Before any PASS verdict, the skill MUST execute these 6 searches and report
results. A PASS without this protocol is INVALID.

### Search 1: GitHub Direct Competitor Search

**Tool**: GitHub API (`https://api.github.com/search/repositories`)

**Queries** (run 3-5 variants):
```
curl "https://api.github.com/search/repositories?q=[KEYWORD 1]&sort=stars&order=desc&per_page=10"
curl "https://api.github.com/search/repositories?q=[KEYWORD 2]&sort=stars&order=desc&per_page=10"
curl "https://api.github.com/search/repositories?q=[KEYWORD 3]&sort=stars&order=desc&per_page=10"
```

**What to extract**:
- Total count of repos matching
- Top 10 by stars (name, star count, description, last update)
- Any repo with >500 stars (serious competitor)
- Any repo updated in last 30 days (active competitor)

**Decision rules**:
- 0 repos found → market might not exist (verify demand separately)
- 1-10 repos, all <100 stars → early market, room for new entrant
- 10-50 repos, some 100-1000 stars → established market, need differentiation
- 50+ repos OR any repo >1000 stars → **SATURATED. Need 10x better or different wedge.**
- Any repo >5000 stars → **LIKELY REJECT.** Unless you have counter-positioning they can't copy.

### Search 2: Product Hunt Search

**Tool**: Product Hunt API or site search (`https://www.producthunt.com/search?q=[KEYWORD]`)

**Queries**:
```
Search Product Hunt for [KEYWORD 1]
Search Product Hunt for [KEYWORD 2]
```

**What to extract**:
- Number of products matching
- Top products (upvotes, launch date)
- Recent launches (last 90 days)

**Decision rules**:
- 0 products → either novel or no market
- 1-5 products, low upvotes → early market
- 5-20 products → established market
- 20+ products OR any with 1000+ upvotes → **SATURATED.**

### Search 3: Google Direct Competitor Search

**Tool**: Web search

**Queries**:
```
"[KEYWORD] software"
"[KEYWORD] tool"
"[KEYWORD] alternative"
"best [KEYWORD] 2026"
```

**What to extract**:
- Number of results
- Top 10 results (are they dedicated products or articles?)
- Ad presence (are people paying for ads = commercial intent)
- "Alternative" articles (existing category = established market)

**Decision rules**:
- No dedicated products in top 10 → early market or no market
- 1-3 dedicated products → early market
- 4-10 dedicated products → established market
- "Best [X] 2026" articles → **SATURATED.** Category exists, has buyers' guides.

### Search 4: Reddit/HN Sentiment Search

**Tool**: Web search with site: operators

**Queries**:
```
site:reddit.com "[KEYWORD]" "alternative" OR "recommend"
site:news.ycombinator.com "[KEYWORD]" "Ask HN"
"[KEYWORD]" "frustrated" OR "hate" OR "looking for"
```

**What to extract**:
- Are people asking for recommendations? (demand exists)
- Are people frustrated with existing tools? (wedge exists)
- Are people recommending the same tools? (market consolidated)

**Decision rules**:
- No threads → market might not exist
- Threads but no recommendations → early market, room
- Threads with 5+ consistent recommendations → **market consolidated, hard to break in**
- Threads with "I wish there was..." → wedge exists

### Search 5: Crunchbase/Funding Search

**Tool**: Crunchbase search or web search for funding

**Queries**:
```
"[KEYWORD]" funding OR raised OR series
"[KEYWORD]" startup OR company
site:crunchbase.com "[KEYWORD]"
"[KEYWORD] competitor" OR "[KEYWORD] alternative"
```

**What to extract**:
- Number of funded companies in the space
- Total funding raised
- Recent rounds (last 12 months)
- **Commercial competitors NOT on GitHub** (this is the gap that caught the MCP registry)

**Decision rules**:
- 0 funded companies → either novel or VCs don't see the market
- 1-3 funded companies → market validated, room for more
- 4-10 funded companies → **crowded, need strong differentiation**
- 10+ funded companies OR any with >$50M raised → **LIKELY SATURATED.**

**CRITICAL (v0.5.1 addition)**: The GitHub search catches open-source saturation but misses commercial competitors. The MCP registry test case proved this — GitHub showed 1 repo, 0 stars, but Smithery (funded commercial registry) existed and the adversarial pass had to catch it.

**If commercial search cannot be executed (rate limit, etc.)**: FLAG the opportunity as "commercial verification incomplete — proceed with caution." Do NOT produce a PASS verdict without commercial verification. The data wins.

### Search 5b: Direct Competitor Web Search (v0.5.1 addition)

**Tool**: Web search for direct commercial competitors

**Queries** (run at least 3):
```
"[KEYWORD] software"
"[KEYWORD] tool pricing"
"[KEYWORD] alternative to [known competitor]"
"best [KEYWORD] 2026"
```

**What to extract**:
- Named commercial competitors (not just open-source)
- Pricing pages (proves commercial viability AND saturation)
- "Alternative" articles (proves category exists)
- Recent launches (ProductHunt, TechCrunch)

**Decision rules**:
- 0 named commercial competitors → early market (verify demand separately)
- 1-3 commercial competitors → early market, room for differentiation
- 4-10 commercial competitors → established market
- 10+ commercial competitors OR any with >$10M ARR → **SATURATED**
- Any competitor with >$50M funding → **LIKELY REJECT** (they can outspend you)

### Search 6: App Store Search (for mobile apps)

**Tool**: App Store / Google Play search

**Queries**:
```
Search App Store for [KEYWORD]
Search Google Play for [KEYWORD]
```

**What to extract**:
- Number of apps matching
- Top apps (ratings, review count, last update)
- Free vs paid split

**Decision rules** (same as GitHub):
- 0 apps → market might not exist
- 1-10 apps, low ratings/reviews → early market
- 10-50 apps → established market
- 50+ apps OR any with 10K+ reviews → **SATURATED.**
</protocol>

## The Verification Decision Matrix

<matrix>
Based on the 6 searches, compute a saturation score:

| Signal | Score |
|--------|-------|
| GitHub: any repo >5000 stars | -3 (near-fatal) |
| GitHub: any repo >1000 stars | -2 |
| GitHub: 50+ repos total | -1 |
| Product Hunt: 20+ products | -2 |
| Product Hunt: any product 1000+ upvotes | -1 |
| Google: "best [X] 2026" articles exist | -2 |
| Google: 10+ dedicated products | -2 |
| Reddit: 5+ consistent recommendations | -1 |
| Crunchbase: 10+ funded companies | -2 |
| Crunchbase: any company >$50M raised | -1 |
| App Store: 50+ apps | -2 |
| App Store: any app 10K+ reviews | -1 |

**Saturation score thresholds**:

| Score | Verdict | Action |
|-------|---------|--------|
| 0 to -2 | LOW saturation | Proceed with confidence |
| -3 to -5 | MODERATE saturation | Need clear differentiation wedge |
| -6 to -8 | HIGH saturation | Need 10x better OR counter-positioning |
| -9 or worse | SATURATED | **REJECT** unless extraordinary wedge |

## Real Example: The "Solo-Dev AI Context CLI" Failure

<real_example>
**The opportunity I identified**: Open-source CLI for solo-dev AI context/token management.

**The verification (actually run)**:

### GitHub search results:
```
"ai context management cli": 114 repos
Top results:
- alexei-led/k8s-mcp-server: 213 stars (adjacent)
- chainofdive/ravenclaw: 13 stars — "Work context management for AI coding agents" (DIRECT competitor, early)

"token cost cli ai": 129 repos
Top results:
- getagentseal/codeburn: 9,051 stars — "Free, local tool to track AI coding token usage" (DIRECT, dominant)
- xiufengsun/TokenTracker: 1,146 stars (DIRECT)
- agentforce314/clawcodex: 819 stars (DIRECT)

"context window coding ai": 184 repos
Top results:
- mksglu/context-mode: 19,514 stars — "Context window optimization for AI coding agents" (DIRECT, dominant)
- matt1398/claude-devtools: 3,779 stars (DIRECT)
- graykode/abtop: 3,401 stars (DIRECT)
- bassimeledath/dispatch: 411 stars (DIRECT)

"ai context budget token": 106 repos
- Multiple direct competitors with 17-261 stars
```

### Saturation score:
- GitHub: any repo >5000 stars → -3 (codeburn at 9,051)
- GitHub: any repo >5000 stars → -3 (context-mode at 19,514)
- GitHub: 50+ repos total → -1 (114 repos)
- GitHub: 50+ repos total → -1 (129 repos)
- GitHub: 50+ repos total → -1 (184 repos)
- GitHub: any repo >1000 stars → -2 (TokenTracker at 1,146)

**Total saturation score: -11 (SATURATED — REJECT)**

### What the skill SHOULD have said:

The opportunity I identified is **SATURATED**. There are direct competitors with 9,000-19,000 stars. The skill failed to catch this because it didn't actually run the GitHub searches — it relied on "I didn't find failures" instead of "I searched and found 427 repos including 3 with >1000 stars."

**The correct verdict**: REJECT. The opportunity exists but is already served by dominant open-source competitors. To enter, you'd need 10x better execution or a wedge the incumbents structurally can't serve.

**Lesson**: The skill's disconfirming evidence search MUST be actual searches, not memory. This protocol makes that mandatory.
</real_example>

## Integration with Lens 06

<integration>
The real-world verification protocol runs as part of Lens 06 (Anti-Bias Audit),
AFTER the bias checklist and BEFORE the adversarial audit.

```
Lens 06 flow:
1. 5 Hard Checks (saturation, moat, capital, novelty, asymmetry)
2. Sunk Cost Reflection
3. 6 Pillars Score
4. Pre-Mortem
5. 5-Minute Bias Checklist
6. REAL-WORLD VERIFICATION (this protocol — MANDATORY)
7. Adversarial Audit Pass
8. Final Verdict
```

**If the real-world verification produces saturation score ≤ -9, the verdict
is REJECT — regardless of what any other check says.**

The skill cannot override this. The data wins.

## The Enforcement Mechanism

<enforcement>
The skill enforces this protocol by requiring the agent to report:

```
### Real-World Verification Results

#### GitHub Search
| Query | Total repos | Top repo (stars) | Saturation signal |
|-------|-------------|------------------|-------------------|
| [query 1] | [N] | [name] ([stars]) | [score] |
| [query 2] | [N] | [name] ([stars]) | [score] |
| [query 3] | [N] | [name] ([stars]) | [score] |

#### Product Hunt Search
[results + score]

#### Google Search
[results + score]

#### Reddit/HN Search
[results + score]

#### Crunchbase Search
[results + score]

#### App Store Search (if applicable)
[results + score]

### Saturation Score: [total]
### Verdict: [PROCEED / NEEDS WEDGE / REJECT]
```

**If this section is missing from the output, the PASS verdict is invalid.**

The agent MUST actually execute these searches (via curl for GitHub API, web
search for others) and report real results — not "I believe the market is..."
but "I searched and found [N] repos, top competitor has [X] stars."

## Why This Matters

<why_it_matters>
The skill has all the right frameworks — anti-bias, adversarial, disconfirming
evidence. But frameworks don't search the web. The agent does. And the agent
is biased toward confirming its own analysis.

This protocol forces the agent to actually look. The data either confirms or
kills the opportunity. No more "I couldn't find disconfirming evidence" when
the agent didn't actually search.

**The skill's #1 failure mode was assuming novelty without verifying. This
protocol fixes that.**

Real-world verification is the difference between a skill that produces
plausible-sounding analysis and a skill that produces correct analysis.
</why_it_matters>
