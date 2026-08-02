# Lens 03: Arbitrage Pattern — Where Is Value Systematically Mispriced?

## Core Question
Where is value being created in one place and not recognized, accessible, or priced correctly in another?

## When to Use
- User asks "where can I buy low and sell high"
- User asks about market inefficiencies
- User wants to find low-competition pricing opportunities
- User has domain knowledge in a specific area

## The 7 Arbitrage Types

### 1. Information Arbitrage
You know something others don't, or can find/process it faster.

**Search targets**: Niche databases, unindexed documents, specialized knowledge
that isn't widely accessible.

**Examples**: Parsing municipal filings before they hit mainstream news,
aggregating pricing data across fragmented markets.

### 2. Geographic Arbitrage
Same thing costs different amounts in different places.

**Search targets**: Price comparisons across regions, cross-border demand
mismatches, remote work rate differences.

**Examples**: Selling US digital services to EU clients at EU rates,
sourcing products from lower-cost regions.

### 3. Regulatory Arbitrage
Rules create artificial barriers, costs, or advantages.

**Search targets**: New regulations, compliance requirements, licensing gaps,
industry-specific legal changes.

**Examples**: GDPR compliance tools, accessibility auditing, industry-specific
regulatory reporting.

### 4. Temporal Arbitrage
The same thing is worth more at a different time.

**Search targets**: Seasonal patterns, early bird opportunities, trend
prediction, pre-ordering.

**Examples**: Buying off-season and selling in-season, pre-ordering products
before they blow up.

### 5. Platform Arbitrage
Different platforms price or distribute the same value differently.

**Search targets**: Cross-platform price differences, API pricing tiers,
platform-specific features/gaps.

**Examples**: Using one platform's free tier to generate content for another,
arbitraging platform subsidies.

### 6. Skill Arbitrage
Your skill set is worth more in a different industry or context.

**Search targets**: Skills in high-paying industries that can be applied to
lower-competition niches, or vice versa.

**Examples**: A developer applying web dev skills to biotech data pipelines,
a marketer applying DTC tactics to B2B industrial.

### 7. Attention Arbitrage
Attention is underpriced in one channel and overpriced in another.

**Search targets**: Niche communities with high engagement but low monetization,
platforms/influencers undervaluing their audience.

**Examples**: Building in emerging platforms before ad rates rise,
partnering with niche creators whose rates haven't caught up to their
engagement quality.

## Search Strategy Per Type

| Type | Search Pattern |
|------|----------------|
| Information | `[domain] data not publicly available`, `[domain] hard to find` |
| Geographic | `[product] price [country A] vs [country B]` |
| Regulatory | `new [industry] regulation 2026`, `[industry] compliance burden` |
| Temporal | `[industry] seasonal patterns`, `[product] price history` |
| Platform | `[platform A] vs [platform B] pricing`, `[platform] API limitations` |
| Skill | `[skill] in [industry A] vs [industry B] salary` |
| Attention | `[platform] engagement rates [niche]`, `[creator] sponsorship rates` |

## What to Extract

| Arbitrage Type | Evidence Required | Example |
|----------------|------------------|---------|
| Information | Proof of access gap | "This data is public but scattered across 50 PDFs" |
| Geographic | Specific price difference | "Same SaaS sells for 2x in EU" |
| Regulatory | Specific rule + cost | "New ESRS rule affects 50K companies" |
| Temporal | Timing pattern | "Pricing resets quarterly, predictable dip" |
| Platform | Platform limitation | "Shopify doesn't handle X, Zapier is expensive" |
| Skill | Rate comparison | "AI engineers charge $200/hr, but this is just API calls" |
| Attention | Engagement/monetization gap | "Substack writer with 80% open rate charges $50 CPM" |

## Bias Warnings
- Crypto arbitrage is the most commonly suggested. Unless the user explicitly
  asks, skip it. It's saturated, capital-intensive, and competitive.
- Geographic arbitrage often ignores import/export friction. Flag this.
- Regulatory arbitrage has a shelf life — rules get closed eventually.
- Platform arbitrage risks platform dependency (they can change TOS anytime).
- If many people can see the same arbitrage, it's not arb anymore. Verify.

## ECR Phase Discipline

### Expansion Phase Output (generate 15-20+)
List 15-20+ raw arbitrage candidates across all 7 types. No filtering. Each:
- Arbitrage type (1-7)
- Description: <one-line>
- Evidence: <specific data point or quote>
- Source: <URL>

### Contraction Phase Output (reduce to 3-5)
Apply weak-link elimination + stakeholder conflict analysis. Reduce to 3-5
survivors with explicit kill reasons.

## Weak Link: What Kills This Arbitrage?

```
Is the arbitrage still open?
  If the window opened > 6 months ago -> likely saturated. Eliminate unless
  there's a clear barrier to entry (capital, expertise, access).

What prevents someone from copying this?
  Nothing -> Eliminate. It's not arbitrage, it's a temporary price gap.
  Capital barrier -> Viable if user has capital. Flag otherwise.
  Expertise barrier -> Viable. Time-limited but real.
  Access barrier -> Best kind. Structural advantage.

What happens when the incumbent notices?
  If you're arb'ing a platform, they will close the hole.
  If you're arb'ing a regulated gap, regulators will close it.
  Estimate the shelf life. Under 6 months -> high risk.

Is this regulatory arbitrage?
  YES -> How long until the rule changes? Is enforcement active?
         Passive enforcement -> longer shelf life.
         Active enforcement -> shorter. May already be too late.

Does this require scale to be profitable?
  YES + no capital -> Eliminate. Thin-margin arbitrage at small scale is
                     a losing game after friction costs.
  NO -> Better. Can be profitable at any size.

Does this arbitrage create exponential potential (Lens 07)?
  YES if: arbitrage is structural (regulatory, forced participant), can be
          encoded in software (permissionless leverage), and creates a
          reflexive loop (each new compliance win makes the next easier).
  NO if: arbitrage is informational, requires labor leverage, single-shot.
```

## Stakeholder Conflict: Predicting Incumbent Reaction

Most frameworks ignore how incumbents will *react* to your entry. If you
identify a real arbitrage, the incumbent likely has more resources, data,
and leverage than you. Model their reaction:

```
Incumbent type:
  Lean startup -> Will pivot into your space fast. Assume 3-6 month window.
  Enterprise -> Slow to react. 12-24 month window. Good for niche plays.
  State-owned -> May not need to react. Different incentive structure.

Incumbent's constraint:
  Regulatory burden -> Heavy. Slows response. Advantage for you.
  Technical debt -> Heavy. Slows response. Advantage for you.
  Existing revenue to protect -> They'll fight to defend it. Risk for you.
  Brand reputation to protect -> They'll fight dirty. Risk for you.

Your best defense:
  Invisibility (small enough to ignore until too late)
  Speed (iterate faster than they can respond)
  Niche (too small for them to care about)
  Regulatory capture (they can't respond because of rules)

Eliminate if: incumbent can crush you within 3 months with no downside to them.
Keep if: incumbent is structurally constrained from responding effectively.
```

## Time Horizon Tagging

| Arbitrage Type | Typical Shelf Life |
|---|---|
| Information | 1-6 months (closes when others notice) |
| Geographic | 6-24 months (closes when competitors enter) |
| Regulatory | 6-36 months (depends on rule enforcement) |
| Temporal | Recurring (predictable cycle) |
| Platform | 3-12 months (closes when platform updates TOS) |
| Skill | 12-36 months (closes when labor market adjusts) |
| Attention | 6-18 months (closes when ad rates adjust) |

## Output

### Expansion Phase
List 15-20+ arbitrage candidates across all 7 types.

### Contraction Phase
List 3-5 surviving candidates, each with:
- Arbitrage type
- Evidence (specific data point)
- Shelf life estimate
- Incumbent reaction analysis
- Time-to-monetization horizon
- Kill reason for the 10-15 eliminated (one sentence each)

---

## Decision Protocol

### Exact Question This Lens Answers
"Where is value systematically mispriced — and is the mispricing
structural (durable) or merely unnoticed (will close)?"

### Data Required
- Specific price/cost differential with numbers (not "it's cheaper")
- Identified forced participant (who MUST act and why)
- Shelf life estimate (how long until the arb closes)
- Incumbent reaction analysis (can they crush you?)
- Failure-case search: have others tried this arb and failed?

### Confidence Threshold
- **Deploy (execute arb)**: ≥80% confidence, structural mispricing, shelf life >12 months, barrier to entry identified
- **Flag (monitor)**: 60-80% confidence, apparent mispricing, shelf life 6-12 months
- **Discard**: <60% confidence, or shelf life <6 months with no barrier

### Conflict Resolution Rules
- When Lens 03 (Arbitrage) disagrees with Lens 06 (Anti-Bias):
  - Anti-bias wins. An arb that fails saturation/moat is a temporary price gap, not a real opportunity.
- When Lens 03 disagrees with Lens 07 (Exponential):
  - Arb present + exponential low → **one-shot play, not a business**. Accept Tier 3, bank the profit, don't build a company around it.
  - Arb present + exponential high → **rare; structural arb + reflexive loop**. Tier 1 candidate.
- When multiple arb types apply to the same opportunity:
  - Structural arbitrage (regulatory, access) > temporal > informational. Structural lasts longest.
- When stakeholder conflict analysis says incumbent can crush you in <3 months:
  - REJECT regardless of arb quality. The arb is real but un-capturable.
