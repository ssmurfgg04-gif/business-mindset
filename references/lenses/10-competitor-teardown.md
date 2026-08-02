# Lens 10: Competitor Teardown — Where Is the Incumbent Weak?

<lens>
<core_question>
Who are the real competitors (direct, indirect, substitutes), where are they
structurally weak, and can they respond if I attack that weakness?
</core_question>

<when_to_use>
- User asks "who are my competitors?" or "how do I beat [incumbent]?"
- User is evaluating whether an opportunity is defensible
- User wants to enter an existing market
- After Lens 02 (Demand Gap) confirms demand, before Lens 06 (Anti-Bias) finalizes
- During strategy review for an existing business
- When user says "is this saturated?" — saturation is a competitor question
</when_to_use>

<when_not_to_use>
- Pre-idea (no opportunity to evaluate competitors for)
- True blue ocean (no competitors exist — but verify, true blue oceans are rare)
- When user has no intention of competing (lifestyle monopoly, niche of one)
</when_not_to_use>
</lens>

## Core Philosophy

<principle>
Most competitor analysis fails because it lists competitors and their features.
That's a taxonomy, not an analysis. A real teardown identifies **where the
incumbent cannot respond** — the structural weakness that lets a newcomer win
even when the incumbent has more resources, brand, and customers.

Christensen's insight in *The Innovator's Dilemma*: incumbents lose not because
they're stupid or slow, but because responding to the disruptive threat would
require cannibalizing their existing business. The newcomer wins because the
incumbent **cannot** respond, not because they **will not**.
</principle>

## The 5-Stage Teardown Protocol

<teardown_protocol>

### Stage 1: DISCOVER — Find ALL competitors (not just the obvious ones)

Most competitor analyses miss 60% of the actual competitive set because they
only look at direct competitors. The 7 categories of competitor:

<competitor_categories>
1. **Direct competitors** — same product, same customer (Cursor vs Copilot)
2. **Adjacent category** — different product, same job (Notion vs Google Docs — both "document creation")
3. **Substitutes** — different solution, same outcome (Calendly vs back-and-forth email — both "schedule meetings")
4. **Build-vs-buy** — the spreadsheet, the manual process, the internal tool (often the biggest competitor for B2B SaaS)
5. **Open-source** — free alternative (Postgres vs Oracle, Linux vs Windows)
6. **International** — competitor in another geography who could expand
7. **Platform** — the platform itself might enter (Shopify apps vs Shopify native; Twitter clients vs Twitter)

The most dangerous competitor is usually in category 3 (substitute) or 4
(build-vs-buy), not category 1 (direct). Customers solve their problem with
whatever works, including "not solving it."
</competitor_categories>

<discovery_methods>
- Google the problem, not the solution ("how do I [job]" not "[product category]")
- Search Reddit/HN for the problem — what do people recommend?
- Search GitHub for repos addressing the problem
- Check ProductHunt launches in the category
- Search Crunchbase for funded companies in the space
- Check G2/Capterra category pages
- Ask 10 potential customers what they use today (the answer is often "nothing" or "Excel")
- Search LinkedIn for companies hiring for relevant roles
- Check SimilarWeb for traffic to category leaders
</discovery_methods>

### Stage 2: MAP — Build the competitive matrix

<competitive_matrix>
For each competitor, capture:

| Dimension | What to capture | Source |
|---|---|---|
| Company + product | Name, product line | Website |
| Pricing | All tiers, annual/monthly, hidden enterprise pricing | Pricing page, sales call |
| Target customer | Who they sell to (segment, size, geography) | Messaging, case studies |
| Positioning | How they describe themselves | Homepage hero, meta description |
| Key features | Top 10 features (not all — that's noise) | Feature page |
| Missing features | What they DON'T have | Feature page gaps, G2 complaints |
| Strengths | What they're known for | Reviews, case studies |
| Weaknesses | What customers complain about | G2, Reddit, Trustpilot |
| Funding/revenue | Funding history, estimated revenue | Crunchbase, ZoomInfo |
| Team size | Headcount, key roles | LinkedIn, careers page |
| Tech stack | What they build on | BuiltWith, job postings |
| Traffic | Monthly visitors, traffic sources | SimilarWeb, Ahrefs |
| SEO keywords | What they rank for | Ahrefs, Semrush |
| Hiring patterns | What roles they're hiring (signals direction) | Job postings |
| Customer sentiment | NPS proxy, review scores | G2, Capterra |
| Churn signals | Reddit complaints, Glassdoor eng complaints | Reddit, Glassdoor |
| Recent moves | Last 6 months of product/strategy changes | Changelog, blog, press |

The matrix is the input to analysis. Don't skip rows — missing data is signal
("we couldn't find their pricing" = they hide it = enterprise-only sales motion).
</competitive_matrix>

### Stage 3: ANALYZE — Find the structural weakness

<analysis_framework>
This is the heart of the teardown. Apply 4 lenses to each competitor:

#### Lens A: Helmer's 7 Powers (competitive moat analysis)

For each competitor, score 0/1/2 on each of Helmer's 7 Powers:

| Power | What to check | Score 0 (no power) | Score 2 (strong power) |
|---|---|---|---|
| **Scale** | Lower unit cost from volume? | Commodity, no scale advantage | 10x scale advantage, cost leader |
| **Network** | Value increases with users? | Linear business | Strong 2-sided network effects |
| **Counter-positioning** | Newcomer's model incumbent can't copy? | Incumbent could copy in 90 days | Incumbent copying would destroy their business |
| **Switching costs** | Cost to switch away? | Easy switch (1 day) | High switch (months, data lock-in, retraining) |
| **Branding** | Premium pricing from brand? | Generic brand, price-taker | Brand commands 30%+ premium |
| **Cornered resource** | Exclusive access to something valuable? | No exclusive resources | Exclusive IP, data, license, talent |
| **Process power** | Better process that's hard to replicate? | Standard processes | Proprietary process, lower cost or higher quality |

A competitor with 3+ Powers at score 2 is **nearly impossible to displace
head-on**. Don't attack there. Either find a different angle or pick a different
market.

A competitor with 0-1 Powers at score 2 is **vulnerable**. Find the angle.

#### Lens B: Jobs to Be Done (Christensen)

What job is the customer hiring the competitor to do? Map all jobs, including
ones the competitor doesn't realize they're being hired for.

Example: Customers hire McDonald's not just for "food" but for "predictable
experience for my kids while traveling." A competitor attacking on "better food"
misses the job; a competitor attacking on "predictable experience for kids"
(SlotCanyon kids' meal toys, Chick-fil-A playgrounds) wins.

The job the competitor DOESN'T know they're being hired for is the vulnerability.

#### Lens C: Aggregation Theory (Stratechery / Ben Thompson)

Is the incumbent an aggregator (controls demand, commoditizes suppliers) or a
linear business (controls supply, sells direct)?

- **Aggregators** (Google, Facebook, Uber) win by controlling demand. Attack
  them by sub-segmenting demand they can't serve well, or by verticalizing a
  niche they commoditize.
- **Linear businesses** (old media, traditional SaaS) win by controlling supply.
  Attack them by aggregating demand they can't reach, or by disintermediating.

#### Lens C: Innovator's Dilemma analysis

Is there a smaller market the incumbent **cannot** go downmarket to serve
because it would cannibalize their premium business?

Examples:
- Salesforce couldn't serve SMBs without cannibalizing enterprise — HubSpot won SMB.
- Bloomberg Terminal couldn't serve individual investors without cannibalizing $24K/yr terminal — Robinhood won retail.
- NYT couldn't serve short-form news without cannibalizing long-form — Twitter won short-form.

The vulnerability: the incumbent's existing business model **prevents** them
from responding, even if they see the threat.
</analysis_framework>

### Stage 4: PREDICT — Will the incumbent respond?

<reaction_prediction>
4 questions to predict incumbent response:

#### 1. CAN they respond?
Structural constraints that prevent response:
- **Regulatory burden** (banks can't ship fast due to compliance)
- **Technical debt** (legacy stack can't add features)
- **Existing revenue to protect** (cannibalization risk)
- **Brand positioning** (luxury brand can't go downmarket)
- **Organizational structure** (P&L structure prevents cross-team collaboration)
- **Contractual obligations** (exclusivity deals, customer contracts)

If the incumbent has 2+ structural constraints, they likely CANNOT respond
effectively. This is the green light.

#### 2. WILL they respond?
Incentive to respond:
- **Revenue at risk**: if your attack threatens >5% of their revenue, they'll respond
- **Strategic importance**: if your attack threatens a strategically critical segment, they'll respond
- **Ego/founder pride**: founders respond to threats even when economics don't justify it
- **Public attention**: if your attack gets press, they're forced to respond

If they WILL respond, model how (lower price, copy feature, acquire you, sue you).

#### 3. WHEN will they respond?
- **Lean startup incumbent**: 3-6 month response window
- **Enterprise incumbent**: 12-24 month response window (good for niche plays)
- **State-owned / regulated**: may not need to respond (different incentives)

Your window of opportunity is the time between your launch and their response.
For a 12-24 month window, you can build durable advantage. For a 3-6 month
window, you need to either be uncopyable (counter-positioning) or accept you'll
be acquired.

#### 4. HOW will they respond?
- **Lower price**: hard to fight if they have scale advantage
- **Copy feature**: easy to fight if you have counter-positioning (they can copy the feature, not the model)
- **Acquire you**: best outcome in some cases
- **Acquire a competitor**: bad — they get distribution you can't match
- **Sue you**: rare, but happens (IP litigation)

#### Incumbent Reaction Scorecard

| Signal | Score |
|---|---|
| CAN'T respond (2+ structural constraints) | +2 (your advantage) |
| CAN respond but slowly (12+ months) | +1 |
| CAN respond fast (3-6 months) | -1 |
| WON'T respond (low revenue at risk) | +2 |
| WILL respond (high revenue at risk) | -2 |
| Counter-positioning (they can't copy without self-harm) | +3 |
| No counter-positioning (they can copy directly) | -1 |

Total: +5 or higher → attack. 0 to +4 → attack with caution. Negative → don't attack head-on.
</reaction_prediction>

### Stage 5: EXPLOIT — Where do you attack?

<exploitation_strategy>
Based on the analysis, identify the attack vector:

#### Attack vector 1: Underserved segment
The incumbent serves the profitable middle of the market. Attack the segment
they under-serve (too small for them, too weird for them, too low-margin for
them). Christensen's classic disruption.

#### Attack vector 2: Counter-positioning
Offer a business model the incumbent can't copy without cannibalizing
themselves. Examples:
- Salesforce (SaaS) vs on-premise CRM (couldn't go SaaS without killing services revenue)
- Robinhood (free) vs brokerages (couldn't go free without killing commissions)
- Netflix (streaming) vs Blockbuster (couldn't go streaming without killing stores)

#### Attack vector 3: Better job match
The incumbent is hired for one job but customers are using them for another.
Build for the actual job, not the official job. Example: Notion hired for
"wiki" but used for "all docs" — built for all docs.

#### Attack vector 4: Aggregation play
If the incumbent is a linear business (controls supply), aggregate demand they
can't reach. If the incumbent is an aggregator, sub-segment demand they
commoditize.

#### Attack vector 5: Process advantage
Build a proprietary process (lower cost or higher quality) that's hard to
replicate. Takes years but durable. Examples: Toyota Production System,
Amazon fulfillment, Stripe's API reliability.

#### Attack vector 6: Cornered resource
Secure exclusive access to something valuable (data, IP, talent, license).
The strongest moat but the hardest to build.
</exploitation_strategy>
</teardown_protocol>

## Under-the-Radar Competitor Discovery Checklist

<discovery_checklist>
35 signals to check, organized by category:

### Signals from the competitor itself
1. Company blog (what are they writing about?)
2. Changelog/release notes (what are they shipping?)
3. Job postings (what are they hiring for? signals direction)
4. Leadership team changes (LinkedIn)
5. Funding announcements (Crunchbase)
6. Conference talks by their team
7. GitHub activity (if open source)
8. Customer case studies (who are their marquee customers?)

### Signals from their customers
9. G2/Capterra reviews (especially cons and 1-star)
10. Reddit complaints (r/[competitor], r/[category])
11. Twitter/X complaints about them
12. Trustpilot reviews
13. Glassdoor reviews (engineering — signals internal problems)
14. Customer churn indicators (LinkedIn — who used to list them as employer?)

### Signals from the market
15. Google Trends for the category
16. SimilarWeb traffic trends
17. Ahrefs/Semrush keyword rankings (what are they ranking for?)
18. ProductHunt launches in the category
19. YC batches with similar companies
20. a16z/Sequoia/Benchmark portfolio pages (thesis signals)

### Signals from adjacent categories
21. What's the substitute? (Different solution, same job)
22. What's the build-vs-buy? (Spreadsheet, manual process)
23. What's the open-source alternative?
24. What's the international alternative?
25. What did people do before this category existed?

### Signals from their weakness
26. What features do customers request that they don't have?
27. What segments do they explicitly NOT serve?
28. What use cases do they discourage?
29. What do they charge extra for (where they're extractive)?
30. What's their support SLA (where are they underinvesting)?

### Meta-signals
31. Has anyone tried this before and failed? (Post-mortem search)
32. Are VCs funding or defunding this category?
33. Are there regulatory changes coming that affect them?
34. What's the talent flow? (Are their best people leaving?)
35. What do their investors say in board observer blogs?

Run this checklist for every major competitor. Missing a category = blind spot.
</discovery_checklist>

## Few-Shot Examples

<examples>

### Example 1: Entering the project management market (positive)

<example>
<situation>
User wants to build a project management tool. "There's already Asana, Monday, Jira — is it too saturated?"
</situation>

<thinking>
Let me run the teardown. The user is asking a saturation question, but saturation is competitor analysis.

Stage 1 DISCOVER:
Direct: Asana, Monday, Jira, ClickUp, Notion, Linear, Trello
Adjacent: Slack (has some PM), GitHub Projects, Google Sheets
Substitute: Spreadsheets, email, sticky notes
Build-vs-buy: Internal tools (the biggest competitor — most teams don't use a PM tool)
Open-source: OpenProject, Taiga
International: Teambition (China), Wrike (Europe-origin)

The "saturated" intuition is wrong — most teams DON'T use a PM tool. The biggest competitor is "nothing."

Stage 2 MAP: (skipped for brevity — would build full matrix)

Stage 3 ANALYZE — Helmer 7 Powers for Asana (the market leader):
- Scale: 2 (huge user base, but PM tools don't have strong scale economics)
- Network: 1 (some network effects via team invitations, but weak)
- Counter-positioning: 0 (Asana could copy any feature)
- Switching costs: 2 (data lock-in, workflow configuration)
- Branding: 2 (strong brand)
- Cornered resource: 0
- Process power: 0

Total: 7/14. Vulnerable. No counter-positioning, no cornered resource, no process power.

JTBD analysis: What job are customers hiring Asana for? Officially: "manage projects." Actually (per Reddit/G2 complaints): "make my boss feel like we're organized." The actual job is **status reporting up**, not **work management down**. Asana is bad at the actual job because it's optimized for the official job.

Stage 4 PREDICT — Can Asana respond?
- Regulatory burden: no
- Technical debt: moderate (legacy stack, but they ship)
- Existing revenue to protect: yes — they can't simplify without losing enterprise customers
- Brand positioning: yes — they're "enterprise PM," can't go simple

Asana CANNOT easily build a simple tool optimized for status reporting — it would cannibalize their enterprise positioning. This is the counter-positioning opening.

Stage 5 EXPLOIT:
Attack vector: Counter-positioning + underserved segment.
Build: a PM tool that's actually a status-reporting tool. Optimize for "what did I do this week, what's blocking me, what's next" — not for Gantt charts. Target: IC engineers and designers who hate PM tools. Price: $5/user/mo (Asana is $10-25).

Asana can't respond because their enterprise customers want complexity. The simpler tool would confuse the enterprise buyer.
</thinking>

<answer>
NOT saturated. The PM market has 10+ tools, but most teams don't use any. The biggest competitor is "nothing."

Vulnerability: Asana and peers optimize for the official job ("manage projects") but customers hire them for the actual job ("report status up"). The actual job is underserved.

Attack: build a status-reporting-first tool for IC engineers/designers. $5/user/mo. Asana can't respond because simplifying would cannibalize enterprise positioning (counter-positioning).

This is a Christensen-style disruption: attack the underserved low end with a simpler, cheaper, better-fit tool. The incumbent can't follow without destroying their premium business.

Verdict: opportunity is viable. Pass to Lens 06 for anti-bias check.
</answer>
</example>

### Example 2: Entering the CRM market (negative — too defensible)

<example>
<situation>
User wants to build "a better Salesforce for SMBs." Asks if the teardown supports it.
</situation>

<thinking>
Stage 1 DISCOVER: Salesforce is the incumbent. Direct: HubSpot, Pipedrive, Zoho. Substitute: spreadsheets.

Stage 3 ANALYZE — Helmer 7 Powers for Salesforce:
- Scale: 2 (massive scale, cost leader at enterprise)
- Network: 2 (AppExchange ecosystem — strong 2-sided network)
- Counter-positioning: 0
- Switching costs: 2 (data, integrations, training — years to switch)
- Branding: 2 (Salesforce = CRM)
- Cornered resource: 2 (exclusive enterprise relationships, AppExchange)
- Process power: 1 (some sales process advantage)

Total: 11/14. Nearly impregnable at enterprise.

But the user said "for SMBs." Let me check Salesforce's SMB position:
- Salesforce Essentials exists but is deprioritized (revenue is enterprise)
- SMB churn is high (Salesforce is too complex for SMBs)
- HubSpot already won SMB CRM

The SMB attack vector is already taken by HubSpot. HubSpot has:
- Scale: 1 (smaller than Salesforce but SMB scale)
- Network: 1 (smaller app ecosystem)
- Counter-positioning: 2 (inbound marketing native — Salesforce can't copy without alienating sales-led customers)
- Switching costs: 2 (data, integrations)
- Branding: 2 (HubSpot = SMB CRM)
- Cornered resource: 1 (inbound marketing IP)
- Process power: 1

Total: 10/14. Also strong.

The user is trying to attack a market with TWO well-defended incumbents. Salesforce owns enterprise; HubSpot owns SMB. There's no obvious gap.

Stage 4 PREDICT: Both CAN and WILL respond to a credible threat. Salesforce can go downmarket (they have Essentials); HubSpot can copy any feature.

Stage 5 EXPLOIT: The only viable attack is a sub-segment HubSpot under-serves. Examples:
- CRM for specific vertical (real estate, healthcare, legal) — but those exist
- CRM for solopreneurs — but Pipedrive serves this
- CRM with embedded AI agent — possible, but Salesforce is shipping Einstein

The teardown doesn't support the opportunity. The user should either find a more specific wedge or pick a different market.
</thinking>

<answer>
Teardown does NOT support the opportunity. Salesforce (enterprise) and HubSpot (SMB) both score 10-11/14 on Helmer's 7 Powers. Both can and will respond to threats. No counter-positioning available — both have copied each other's features for years.

The "better Salesforce for SMB" positioning is a trap. Either:
1. Find a specific vertical HubSpot under-serves (rare — they've expanded into most)
2. Find a counter-positioning wedge (AI-native CRM? but Salesforce is shipping Einstein)
3. Pick a different market

Verdict: REJECT. The market is defensible against head-on attack. Pass to Lens 06 for anti-bias confirmation.
</answer>
</example>

### Example 3: Vertical SaaS opportunity (positive)

<example>
<situation>
User wants to build "SaaS for independent pharmacy inventory management." Is the teardown favorable?
</situation>

<thinking>
Stage 1 DISCOVER:
Direct: McKesson Pharmacy Manager, BestRx, PioneerRx (all legacy, on-prem)
Adjacent: generic inventory SaaS (TradeGecko, Cin7) — but not pharmacy-specific
Substitute: spreadsheet + phone calls to distributors
Build-vs-buy: most independent pharmacies use spreadsheet + manual reorder
Open-source: none
International: pharmacy is heavily regulated per-country, no international competition

Stage 3 ANALYZE — PioneerRx (market leader in independent pharmacy software):
- Scale: 1 (some scale in independent pharmacy, but niche)
- Network: 0 (no network effects)
- Counter-positioning: 0
- Switching costs: 2 (regulatory compliance, data, training)
- Branding: 1 (known in pharmacy, not beyond)
- Cornered resource: 2 (relationships with pharmacy schools, certification bodies)
- Process power: 0

Total: 6/14. Vulnerable. No network effects, no counter-positioning, no process power.

JTBD: What job are pharmacies hiring PioneerRx for? Officially: "manage pharmacy operations." Actually: "comply with regulation without thinking about it." The actual job is compliance automation, not operations management.

Stage 4 PREDICT:
- Regulatory burden: HIGH (PioneerRx is FDA/DEP compliant; rebuilding that is years of work — but the newcomer has to do it too, not the incumbent responding)
- Technical debt: HIGH (PioneerRx is on-prem, legacy stack — can't ship modern features)
- Existing revenue to protect: moderate (they could ship cloud, but it would cannibalize on-prem revenue)
- Brand positioning: weak (they're "the old pharmacy software")

PioneerRx CAN'T respond fast — they're technically constrained by legacy stack. They WILL respond eventually (12-24 months) but slowly.

Stage 5 EXPLOIT:
Attack vector: Counter-positioning + underserved segment + cornered resource.
- Counter-positioning: cloud-native + modern UX (PioneerRx can't go cloud without killing on-prem revenue)
- Underserved segment: independent pharmacies underserved by enterprise tools built for chains
- Cornered resource: build exclusive integration with major distributors (McKesson, Cardinal, ABC) before PioneerRx notices

This is a real opportunity. The incumbent is vulnerable on multiple dimensions.
</thinking>

<answer>
Teardown SUPPORTS the opportunity. PioneerRx scores 6/14 on Helmer's 7 Powers — vulnerable. They have technical debt (on-prem legacy), can't respond fast, and the actual job (compliance automation) is underserved.

Attack: cloud-native, modern UX, exclusive distributor integrations. PioneerRx can't follow without cannibalizing on-prem revenue (counter-positioning).

Window: 12-24 months before they respond seriously. Build durable advantage (distributor integrations, pharmacy school relationships) in that window.

Verdict: PASS. Pass to Lens 06 for anti-bias, Lens 09 for pricing (pharmacies will pay premium for compliance automation).
</answer>
</example>
</examples>

## Edge Cases

<edge_cases>
### Edge 1: No competitors found
Either you've found a blue ocean (rare — verify by checking substitutes and
build-vs-buy) or you haven't searched hard enough. The latter is more likely.
Re-run the discovery checklist with the 35 signals.

### Edge 2: Competitor is a platform (AWS, Shopify, Apple App Store)
You can't attack the platform directly — they own the rules. Either build on
the platform (and accept platform risk), or build off-platform and accept
reduced distribution. Don't pretend you can fight the platform.

### Edge 3: Competitor is open-source
Open-source competitors have a structural advantage (free) and a structural
weakness (no support, no SLA, no roadmap). Attack the weakness — offer
managed/hosted/support/predictable-roadmap. Don't compete on price.

### Edge 4: Competitor is the build-vs-buy (spreadsheet)
The hardest competitor to beat, because switching cost is zero (they built it
themselves). You have to offer 10x the value of their spreadsheet, or find
customers who haven't built the spreadsheet yet.

### Edge 5: Multiple incumbents with different strengths
Common in mature markets. Don't try to beat all of them — pick one to attack
and one to ignore. The one you attack should be the one with the most
structural weakness (lowest Helmer score, most technical debt, most
cannibalization risk).

### Edge 6: Competitor is a substitute you don't recognize
"Uber is a taxi company" missed that Uber's real competitor was car ownership.
"Netflix is a DVD company" missed that their real competitor was cable TV.
Always ask: what's the customer's actual job, and what else solves it?
</edge_cases>

## Weak Link: What Kills This Teardown?

<weak_link>
```
Did you check all 7 competitor categories (not just direct)?
  NO → Blind spot. Re-run discovery.
  YES → continue

Did you score each major competitor on all 7 Powers?
  NO → Analysis incomplete. Can't identify vulnerability.
  YES → continue

Did you identify the actual job (vs the official job)?
  NO → You're attacking the wrong vector.
  YES → continue

Can the incumbent respond structurally (no constraints)?
  YES → Your attack will be copied. Need counter-positioning or different angle.
  NO → You have a window. Move fast.

Is there a counter-positioning wedge (business model they can't copy)?
  NO → Head-on attack. High risk. Need 10x better product or 10x lower price.
  YES → Durable advantage. Proceed.

Have you checked international/open-source/substitutes?
  NO → You may be missing a threat from outside the obvious competitive set.
  YES → Teardown complete.
```
</weak_link>

## Decision Protocol

<decision_protocol>
### Exact Question This Lens Answers
"Who are the real competitors, where are they structurally weak, and can they
respond if I attack that weakness?"

### Data Required
- All 7 competitor categories surveyed (direct, adjacent, substitute, build-vs-buy, open-source, international, platform)
- Helmer 7 Powers scored for top 3 competitors
- JTBD analysis (official job vs actual job)
- Incumbent reaction scorecard
- Counter-positioning wedge identified (or confirmed absent)

### Confidence Threshold
- **Deploy (attack)**: ≥75% confidence, Helmer score ≤8 for target incumbent, counter-positioning identified, reaction scorecard +3 or higher
- **Flag (further research)**: 50-75% confidence, Helmer score 9-11, unclear counter-positioning, reaction scorecard 0 to +2
- **Discard**: <50% confidence, or Helmer score ≥12 for all incumbents, or no counter-positioning possible, or reaction scorecard negative

### Conflict Resolution Rules
- When Lens 10 (Competitor) disagrees with Lens 02 (Demand):
  - Demand present + saturated competitors → **vertical wedge**. Find a segment incumbents under-serve.
  - Demand present + no competitors → **verify**. True blue oceans are rare. Re-run discovery.
- When Lens 10 disagrees with Lens 06 (Anti-Bias):
  - If teardown says "saturated" and anti-bias says "PASS" → **trust teardown**. Anti-bias misses competitor dynamics.
- When Lens 10 disagrees with Lens 07 (Exponential):
  - Vulnerable incumbent + counter-positioning + exponential potential → **Tier 1 candidate**. Classic disruption.
  - Vulnerable incumbent + counter-positioning + linear economics → **Tier 2**. Profitable disruption, not venture-scale.
- When no counter-positioning is available:
  - Head-on attack requires 10x better product OR 10x lower price. Both are hard. Usually REJECT.
</decision_protocol>

## Output

<output>
```
### Competitor Teardown

#### Competitor Discovery (all 7 categories)
| Category | Competitor | Notes |
|---|---|---|
| Direct | | |
| Adjacent | | |
| Substitute | | |
| Build-vs-buy | | |
| Open-source | | |
| International | | |
| Platform | | |

#### Helmer 7 Powers Scorecard (top 3 competitors)
| Power | [Competitor 1] | [Competitor 2] | [Competitor 3] |
|---|---|---|---|
| Scale | /2 | /2 | /2 |
| Network | /2 | /2 | /2 |
| Counter-positioning | /2 | /2 | /2 |
| Switching costs | /2 | /2 | /2 |
| Branding | /2 | /2 | /2 |
| Cornered resource | /2 | /2 | /2 |
| Process power | /2 | /2 | /2 |
| **Total** | **/14** | **/14** | **/14** |

#### JTBD Analysis
- Official job (what competitor says they do):
- Actual job (what customers hire them for):
- Gap between official and actual job: [vulnerability or not]

#### Incumbent Reaction Scorecard
| Signal | Score |
|---|---|
| CAN'T respond (structural constraints) | |
| CAN respond fast | |
| WON'T respond (low revenue at risk) | |
| WILL respond (high revenue at risk) | |
| Counter-positioning available | |
| **Total** | **/10** |

#### Attack Vector
- Selected vector: [underserved segment / counter-positioning / better job match / aggregation / process / cornered resource]
- Rationale: [why this vector against this incumbent]

#### Window of Opportunity
- Estimated incumbent response time: [3-6 months / 6-12 months / 12-24 months / can't respond]
- What to build in that window: [specific durable advantages]

#### Teardown Verdict
- Vulnerable incumbent identified? YES/NO
- Counter-positioning wedge available? YES/NO
- Attack vector clear? YES/NO
- **Verdict**: ATTACK / CAUTION / DO NOT ATTACK
```
</output>

## Source

Distilled from `/references/research-pricing-competitor.md` which contains the
full 5-stage protocol, Helmer 7 Powers deep dive, 5 worked teardown examples
(Stripe vs PayPal, Notion vs Evernote, Slack vs Teams, Snowflake vs Oracle,
Figma vs Adobe), and 90+ sources.
