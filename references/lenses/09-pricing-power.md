# Lens 09: Pricing Power — Can I Raise Prices Without Losing Customers?

<lens>
<core_question>
Does this opportunity have pricing power — the ability to raise prices without
proportionally losing customers — and what pricing structure captures the maximum
fraction of value created?
</core_question>

<when_to_use>
- User asks "what should I charge?" or "how should I price this?"
- User is designing pricing tiers for a SaaS / service / product
- User wants to increase prices on an existing product
- User is comparing pricing models (subscription vs one-time vs usage)
- After Lens 02 (Demand Gap) confirms demand, before Lens 06 (Anti-Bias) finalizes
- During business model evaluation alongside Lens 04 (Leverage)
</when_to_use>

<when_not_to_use>
- Pre-idea (no opportunity to price yet)
- Pure commodity plays with no differentiation (pricing is set by the market)
- Non-revenue decisions (org structure, hiring)
</when_not_to_use>
</lens>

## Core Philosophy

<principle>
Pricing is the highest-leverage decision in any business. A 1% price improvement
delivers more profit than a 1% improvement in any other variable (volume, cost,
mix). Yet most founders underprice systematically — Patrick McKenzie's "charge
more" is the single most repeated advice in software business for a reason.

Pricing power is the test of whether you have a real business. If you can't raise
prices 10% without losing 10% of customers, you don't have a moat — you have a
commodity with a logo.
</principle>

## The 6 Pricing Strategy Archetypes

Use the decision tree to pick the right archetype. Do NOT default to subscription
SaaS — that's the AI familiarity trap.

<pricing_decision_tree>
```
Is the value measurable per unit of usage?
├── YES → Can usage vary 10x+ between customers?
│   ├── YES → USAGE-BASED PRICING (Snowflake, AWS, Twilio)
│   └── NO → OUTCOME-BASED PRICING (performance fees, % of savings)
└── NO → Is there a clear market anchor?
    ├── YES → COMPETITIVE PRICING (but with a twist — see below)
    └── NO → Is the value quantifiable in dollars?
        ├── YES → VALUE-BASED PRICING (most SaaS, consulting)
        └── NO → FREEMIUM (if distribution is the moat) or COST-PLUS (last resort)
```

### When each archetype wins

| Archetype | When it wins | When it fails | Examples |
|-----------|-------------|---------------|----------|
| **Value-based** | Value quantifiable, customers heterogeneous | Value vague, customers homogeneous | Stripe (0.29% + $0.30 — % of transaction), Vercel |
| **Usage-based** | Usage varies 10x+, customers want fairness | Usage is binary or constant | AWS, Snowflake, Twilio, Datadog |
| **Outcome-based** | Outcome is measurable and attributable | Outcome is delayed or shared | Performance SEO, % of savings (EnergyEfficiency) |
| **Competitive** | Market anchor exists, you're a fast-follower | You have differentiation | Amazon retail (price intelligence), airlines |
| **Freemium** | Distribution is the moat, marginal cost ~0 | High marginal cost, low conversion | Slack, Dropbox, Notion personal |
| **Cost-plus** | Last resort. Government contracts, commodities | Software, services, anything with leverage | Defense contracting, raw materials |
</pricing_decision_tree>

## SaaS Pricing Playbook

### Tier Design (Good / Better / Best)

<tier_design>
The 3-tier architecture works because of the **decoy effect** — the middle tier
makes the expensive tier look reasonable. But the math matters.

**Price ratios must be non-linear:**
- Good → Better: ~3.4x price (not 2x — too close, no perceived jump)
- Better → Best: ~3.0x price (the jump to "enterprise" should feel significant)
- Total range: Good to Best = ~10x

**Revenue distribution target:**
- Good (free or cheap): 70% of users, 10% of revenue (the funnel)
- Better (mid): 25% of users, 50% of revenue (the workhorse)
- Best (enterprise): 5% of users, 40% of revenue (the profit center)

If your mid-tier isn't 40-60% of revenue, your tier design is broken.

### Feature gating principles
- Gate by **value metric** (seats, records, API calls), not by arbitrary feature
- Gate by **use case** (personal / team / enterprise), not by power-user features
- Don't gate **core workflow** — gate **scale and advanced features**
- The free tier must be genuinely useful, not a crippled demo

### Common tier design mistakes
- 2 tiers (no decoy effect, binary choice)
- 4+ tiers (decision paralysis)
- Linear pricing (no jump between tiers, no reason to upgrade)
- Gating core features (free tier is useless, no top-of-funnel)
- Free tier too generous (no reason to upgrade, expensive to host)
</tier_design>

### Pricing Page Best Practices

<pricing_page>
1. **Show annual pricing prominently** with the discount visible (default to annual, toggle to monthly)
2. **Anchor with the most expensive tier first** (decoy effect)
3. **Highlight the recommended tier** ("Most popular" badge on mid-tier)
4. **Use value metrics, not feature lists** as the primary comparison axis
5. **Show social proof** (logos, customer count) near pricing
6. **Make the CTA low-friction** (free trial, demo, contact sales — match the tier)
7. **Hide "Contact Us" only for true enterprise** — not for mid-tier
8. **A/B test the page**, not just the prices
</pricing_page>

## Pricing Psychology Catalog

<psychology_tactics>
Each tactic: what it is, why it works, when to use, when NOT to use, ethical line.

### 1. Anchoring
- **What**: Show a high number first to make subsequent numbers feel small
- **Why works**: First number sets reference point; everything judged relative to it
- **Use**: Show annual price first (10x monthly), show enterprise tier first, show "list price" before discount
- **Don't use**: If the anchor is implausible (customers dismiss it, lose trust)
- **Ethical line**: Real anchors only. Fake "was $1000 now $99" destroys trust.

### 2. Decoy Effect
- **What**: Add a third option designed to be dominated, making the target option look better
- **Why works**: Customers avoid dominated options; the comparison makes the target win
- **Use**: 3-tier pricing where the mid-tier is "obviously better value" than the cheap tier
- **Don't use**: If the decoy is too obviously bad (customers feel manipulated)
- **Example**: The Economist's famous $125 print / $125 digital+print / $59 digital. The middle option (dominated by digital+print at same price) drives digital+print purchases.
- **Ethical line**: Decoys should be real products someone might reasonably buy.

### 3. Charm Pricing ($9.99 vs $10)
- **What**: Prices ending in 9 read as "much cheaper" than round numbers
- **Why works**: Left-digit effect — $9.99 reads as "$9 and change" not "$10"
- **Use**: B2C, impulse purchases, anything < $100
- **Don't use**: B2B enterprise (looks unprofessional — use $99, $499, $999 for B2B mid-tier; round numbers for enterprise)
- **Ethical line**: None — this is a near-universal cognitive bias, not deception

### 4. Price Framing
- **What**: "$30/month" feels different from "$360/year" or "$1/day"
- **Why works**: Smaller time unit = smaller perceived cost
- **Use**: Frame monthly for acquisition, annual for retention ("only $1/day")
- **Don't use**: Don't switch framing mid-funnel — creates distrust
- **Ethical line**: Always show both monthly and annual clearly

### 5. Bundling
- **What**: Sell multiple products together at a discount vs sum of parts
- **Why works**: Customers can't unbundle to evaluate; perceive bonus value
- **Use**: When you have multiple products and the bundle drives attach rate
- **Don't use**: If customers want only one product — bundling forces them to overpay
- **Ethical line**: Bundle must be optional; don't kill the standalone product

### 6. Three-Tier Decoy (special case)
- **What**: The middle tier exists primarily to push customers to the top tier
- **Why works**: Eliminates the "most expensive" feeling by adding a "more expensive" option
- **Use**: When your real target is the top tier
- **Don't use**: If you actually want mid-tier adoption — the decoy will cannibalize it

### 7. Scarcity / Urgency
- **What**: "Only 3 left at this price" or "offer ends Friday"
- **Why works**: Loss aversion — fear of missing out drives action
- **Use**: Genuine scarcity (limited beta spots, real deadline)
- **Don't use**: Fake scarcity (customers detect it, trust evaporates)
- **Ethical line**: Scarcity must be real. Fake countdowns are fraud.

### 8. Payment Framing
- **What**: "Pay annually" framed as saving 20% vs "pay monthly" framed as 25% more
- **Why works**: Framing as savings (gain) > framing as surcharge (loss)
- **Use**: Always frame annual as "save 20%" not monthly as "costs 25% more"
- **Ethical line**: The math should be honest (annual really is 20% cheaper)
</psychology_tactics>

## Price Increase Protocol

<price_increase>
The hardest pricing decision is raising prices on existing customers. Most
founders never do it, leaving 20-40% of revenue on the table.

### When to increase prices
- Annual review (minimum) — prices should rise with inflation + value delivered
- After a major feature release (value has increased)
- When churn is below industry benchmark (customers are staying — you're underpriced)
- When NRR is high (expansion is masking underpricing)
- When sales cycle is short (demand exceeds supply at current price)

### How much to increase (by band)

| Band | Increase | Grandfathering | Communication lead time |
|------|----------|----------------|------------------------|
| **Small** | 3-5% | None (apply to all) | 30 days |
| **Medium** | 5-15% | 6 months for existing | 60 days |
| **Large** | 15-30% | 12 months for existing | 90 days |
| **Restructure** | >30% or new model | Grandfather indefinitely OR offer transition credit | 120 days |

### The 6-step protocol

1. **Announce early** — give customers lead time. Surprise increases destroy trust.
2. **Frame as value, not cost** — "We've added [features X, Y, Z] since you joined. New pricing reflects this."
3. **Grandfather existing customers** — at least 6 months. Ideally 12. Loyal customers should not be punished.
4. **Offer annual lock-in** — "lock in current pricing for 12 months if you switch to annual now"
5. **Personal outreach for top accounts** — don't let enterprise customers learn about increases via email
6. **Watch churn for 60 days** — if churn spikes >2x baseline, you overcorrected. Consider partial rollback.

### Common mistakes
- **Never raising prices** — leaves 20-40% of revenue on the table, signals weak pricing power
- **Raising on everyone simultaneously** — disproportionate churn from price-sensitive segment
- **Raising without grandfathering** — destroys trust, triggers mass cancellations
- **Raising without communication** — surprise = betrayal
- **Raising too much at once** — >30% in one increase triggers flight response
- **Raising without value justification** — "because our costs went up" is not a reason customers accept
</price_increase>

## The 10 Pricing Anti-Patterns

<anti_patterns>
Each: what it is, why it fails, the fix.

### 1. Underpricing (most common)
- **What**: Charging 1/3 to 1/10 of what the market will bear
- **Why fails**: Leaves money on table, signals low value, attracts worst customers
- **Fix**: Double the price. If you lose <20% of customers, you're still ahead. Test higher.

### 2. Cost-plus pricing for software
- **What**: "Our server cost is $X, so we charge $X + 30%"
- **Why fails**: Ignores value delivered. Software has ~0 marginal cost; cost-plus = underpricing.
- **Fix**: Price on value (what the customer saves or earns), not cost.

### 3. Free tier too generous
- **What**: Free tier solves the whole problem for most users
- **Why fails**: No reason to upgrade, expensive to host, attracts free-riders not customers
- **Fix**: Free tier should solve the problem for a smaller user (usage limits) or simpler use case (fewer features), not the same problem at smaller scale.

### 4. Pricing without distribution
- **What**: "Great pricing, but no one sees it"
- **Why fails**: Pricing is downstream of distribution. A great price nobody sees = $0.
- **Fix**: Solve distribution first (Lens 05). Then price.

### 5. Copying competitor pricing
- **What**: "Competitor charges $X, so we'll charge $X"
- **Why fails**: Their cost structure, value prop, and customer mix are different from yours
- **Fix**: Price on YOUR value to YOUR customers. Use competitor pricing only as a sanity check.

### 6. Pricing for features, not value
- **What**: "We have 50 features, so we charge $50"
- **Why fails**: Features don't equal value. 10 useless features don't justify higher price.
- **Fix**: Price on the outcome the features enable, not the feature count.

### 7. Linear tier pricing
- **What**: $10 / $20 / $30 tiers
- **Why fails**: No decoy effect, no reason to upgrade to top tier, no perceived jump
- **Fix**: Non-linear ratios (3.4x, 3.0x as above)

### 8. Annual discount too small
- **What**: "Save 10% with annual" (1.2 months free)
- **Why fails**: Not enough incentive to commit; customers stay on monthly, churn risk stays high
- **Fix**: 20% annual discount (2.4 months free). Standard for SaaS. Some go higher.

### 9. Hiding pricing
- **What**: "Contact us for pricing" on everything
- **Why fails**: Friction kills conversion; customers assume you're too expensive or too cheap
- **Fix**: Show pricing for self-serve and mid-tier. "Contact us" only for true enterprise.

### 10. Per-seat pricing when usage doesn't scale with seats
- **What**: Charging per seat for a tool where 1 person uses it heavily
- **Why fails**: Customers share logins (revenue leak) or under-adopt (churn risk)
- **Fix**: Match pricing metric to value metric. If usage scales with data, charge per record. If with seats, charge per seat. If with outcomes, charge per outcome.
</anti_patterns>

## Practitioner Wisdom

<practitioner_principles>
Distilled from Patrick Campbell (ProfitWell), Madhavan Ramanujam (Simon-Kucher),
Patrick McKenzie (patio11), Lincoln Murphy, Tom Tunguz, Sean Ellis.

### 1. "Charge more." — Patrick McKenzie
The most underpriced segment in software is everything. If you're embarrassed to
quote your price, you're at the right price. If customers say yes immediately,
you're too cheap.

### 2. "Price is the signal of value, not the cost of production." — Ramanujam
Customers don't care about your costs. They care about the value they receive.
Price communicates value. Low price signals low value (and attracts customers
who don't value you).

### 3. "The free tier is a marketing channel, not a product." — Campbell
Free users are not customers — they're leads. Design the free tier to convert,
not to serve. If free users are happy and never convert, the free tier is broken.

### 4. "Pricing is the only P of marketing that produces revenue. The other Ps produce cost." — Ramanujam
Product, Place, Promotion all cost money. Pricing produces money. Yet most
companies spend 100x more time on product than on pricing.

### 5. "Raise prices annually. Inflation + value delivered = floor for increase." — McKenzie
If you don't raise prices annually, you're effectively cutting them (real prices
fall with inflation). Annual increases of 5-10% should be automatic.

### 6. "The customer who complains about price is not your customer." — McKenzie
If a customer leaves because you raised prices 10%, they were never a real
customer — they were a price-sensitive opportunist. Real customers pay for value.

### 7. "Usage-based pricing aligns incentives. Subscription misaligns them." — Tunguz
Subscription: customer wants to use less (get their money's worth), you want
them to use more (justify the price). Usage-based: both want the same thing —
more usage, more value. Alignment reduces churn and support burden.

### 8. "The biggest pricing mistake is never testing." — Campbell
Most companies set a price once and never change it. Pricing should be A/B
tested continuously. Even small improvements compound.
</practitioner_principles>

## Few-Shot Examples

<examples>
Each example shows the reasoning process, not just the answer.

### Example 1: Solo dev building a developer tool (positive)

<example>
<situation>
Solo dev building a CLI tool that helps developers debug API integrations. Considering $9/mo pricing.
</situation>

<thinking>
Let me work through this. The user defaults to $9/mo, which is the most common SaaS price — that itself is a flag (familiarity trap, Lens 06).

Who's the buyer? Developers debugging APIs. Their time costs $50-200/hr. If this tool saves them 1 hour/month, the value is $50-200. Pricing at $9 captures <20% of value — massive underpricing.

Pricing strategy: value-based (the value is quantifiable — time saved).
Tier design: free tier (limited to 50 API calls/day — enough to try, not enough for daily work), pro tier ($29/mo — captures ~30% of value for a solo dev), team tier ($99/mo/seat — for teams sharing debug configs).

Why $29 and not $9? At $9, the customer perceives low value. At $29, they perceive "real tool." The customer who won't pay $29 won't pay $9 either — they're not a customer.

Pricing psychology: anchor with annual ($290/yr, "save 17%"). Mid-tier at $29 is the target. Team tier at $99 is the decoy-creator — makes $29 look reasonable.

Risk: at $29, conversion may drop vs $9. But even at 1/3 the conversion, revenue per customer is 3.2x — net positive. And the customers who do convert are higher quality (less support burden, lower churn).
</thinking>

<answer>
Recommended pricing: Free (50 calls/day) / Pro $29/mo or $290/yr / Team $99/mo/seat.

Don't default to $9. Price on value (developer time saved). The Pro tier at $29 captures ~30% of value delivered to a solo developer. The Team tier creates a decoy that makes Pro look reasonable and captures teams willing to pay per seat.

Test: ship at $29, measure conversion. If conversion > 3% of free-tier users, you're at the right price. If <1%, try $19. If >5%, you're underpricing — try $39.

Anti-pattern check: don't charge per-feature (you only have one feature). Don't copy competitor pricing (most dev tools underprice). Don't offer annual discount <20% (no incentive to commit).
</answer>
</example>

### Example 2: Services business pricing (positive)

<example>
<situation>
Consultant charging $100/hr for marketing strategy. Considering raising to $150/hr.
</situation>

<thinking>
Hourly billing is itself an anti-pattern (punishes efficiency). But let me address the immediate question first.

$100/hr to $150/hr is a 50% increase. That's in the "Large" band (15-30%+) per the protocol — wait, actually >30%, so it's "Restructure" territory. The protocol says: grandfather indefinitely OR offer transition credit, 120-day communication lead time.

But for a consultant with a few clients (not a SaaS with thousands), the protocol is different. Personal outreach to each client. Frame as: "My rates haven't changed in 18 months. In that time, I've added [X, Y, Z capabilities]. New rate effective in 90 days for new engagements; existing engagements continue at current rate until [date]."

The bigger question: should this be hourly at all? Value-based pricing for consulting is far superior. Instead of $150/hr, the consultant should price by outcome: "$5,000 for a marketing strategy audit" or "$15,000 for a 90-day engagement with defined deliverables."

Why value-based wins:
1. Removes the "how many hours did this take?" question
2. Captures the full value (a great strategy is worth $50K+ to the client; 50 hours at $150/hr = $7.5K — massive underpricing)
3. Aligns incentives (consultant wants to deliver value fast, not bill more hours)
4. Filters clients (clients who pay for outcomes are better than clients who pay for time)
</thinking>

<answer>
Short answer: Yes, raise to $150/hr — but use the protocol. 90-day notice, personal outreach, grandfather existing engagements.

Longer answer: Stop billing hourly. Move to value-based pricing:
- Marketing strategy audit: $5,000 (1-week engagement, defined deliverable)
- 90-day strategy + implementation: $15,000-$25,000 (depending on scope)
- Ongoing advisory: $2,000-$5,000/month retainer

Frame by outcome, not time. The client doesn't care if the audit takes you 10 hours or 40 hours — they care about the quality of the strategy. Capture the value, not the hours.
</answer>
</example>

### Example 3: Underpricing detection (negative example)

<example>
<situation>
SaaS company pricing at $19/mo, growing 20% YoY, NRR 95%, churn 8% monthly. CEO thinks pricing is fine.
</situation>

<thinking>
Let me check the signals:
- NRR 95%: below 100% means existing customers are worth less over time. Healthy SaaS NRR is 110%+ (expansion > churn).
- Churn 8% monthly: that's ~60% annual churn. Way too high. Industry benchmark for SMB SaaS is 3-5% monthly, enterprise 1-2%.
- Growth 20% YoY: anemic for SaaS (should be 50%+ at this stage).

These are all signals of underpricing:
- Low NRR: customers don't expand (no upgrade path, or upgrade isn't worth it)
- High churn: customers don't perceive enough value to stay (price-sensitive segment)
- Slow growth: CAC may be too high relative to LTV (low price = low LTV = can't afford CAC)

The CEO thinks pricing is "fine" because no one complains. But customers not complaining about price ≠ pricing is right. Customers complain about price when it's too HIGH. They silently leave when it's too LOW (low price signals low value, attracts worst customers who churn).

The test: what happens if you raise prices 30%? If you lose <15% of customers, you're ahead (revenue per customer up 30%, customer count down 15%, net +10% revenue). The customers who leave are the price-sensitive ones you didn't want anyway.
</thinking>

<answer>
The pricing is NOT fine. These signals all indicate underpricing:
- NRR 95% (should be 110%+)
- Churn 8% monthly (should be 3-5%)
- Growth 20% YoY (should be 50%+)

Recommendation: raise prices 30% on new customers immediately. Grandfather existing for 6 months. Watch churn for 60 days — if it spikes >2x baseline, you overcorrected (but the math says you won't).

The customers who leave were the price-sensitive segment with high churn anyway. The customers who stay will have higher LTV, justifying higher CAC, enabling faster growth.

The CEO's "no one complains" is the underpricing signal, not the all-clear.
</answer>
</example>
</examples>

## Edge Cases

<edge_cases>
### Edge 1: Regulated industries (healthcare, finance, legal)
Standard pricing psychology may be illegal or unethical. Consult compliance counsel
before applying anchoring, decoy, or scarcity tactics. Some industries require
price disclosure, prohibit differential pricing, or mandate cost-plus.

### Edge 2: Marketplaces and two-sided platforms
Pricing must consider both sides. Taxing one side too heavily kills liquidity.
Often: subsidize the scarcer side, charge the abundant side. (E.g., free for
sellers, charge buyers; or free for diners, charge restaurants.)

### Edge 3: Government / enterprise procurement
Procurement processes may require specific pricing structures (fixed-fee, T&M,
cost-plus). Don't fight this — adapt. But still negotiate hard on the structure
you're forced into.

### Edge 4: International pricing
Purchasing power parity matters. $29/mo in the US is fine; in India, it's a
premium product. Consider PPP-adjusted pricing for global self-serve. (Stripe
supports this natively.)

### Edge 5: Pre-revenue startups
You can't test pricing without customers. But you CAN test willingness-to-pay
via pre-orders, surveys (Van Westendorp), and "fake door" landing pages. Don't
price blind.

### Edge 6: Products with network effects
Pricing must account for adoption externality. Early users create value for
later users. Often: subsidize early users (free or paid), monetize late users.
But beware — if free users never convert, you've built a charity, not a business.

### Edge 7: Commoditized markets
If you have no differentiation, pricing is set by the market. Your only lever
is cost reduction. Don't pretend you have pricing power if you don't — pass
Lens 06 (Anti-Bias) and Lens 10 (Competitor Teardown) first.
</edge_cases>

## Weak Link: What Kills This Pricing?

<weak_link>
```
Does the customer perceive the value?
  NO → No pricing strategy works. Fix value perception first (or find different customers).
  YES → continue

Is the value quantifiable in dollars?
  NO → Value-based pricing impossible. Use competitive or freemium.
  YES → continue

Is there a clear pricing metric that scales with value?
  NO → Pricing will feel arbitrary. Find a metric (seats, records, API calls, outcomes).
  YES → continue

Can the customer afford the price that captures 30% of value?
  NO → Wrong customer segment. Either go down-market (lower price, higher volume) or up-market (higher price, lower volume).
  YES → continue

Will raising prices 10% lose more than 10% of customers?
  YES → You have a commodity, not pricing power. Pass to Lens 10 (Competitor Teardown) to find differentiation.
  NO → You have pricing power. Price aggressively.

Is there a free-rider problem (free tier too generous)?
  YES → Tighten free tier. Free should be a funnel, not a product.
  NO → continue

Are you pricing for features instead of value?
  YES → Restructure around value metric.
  NO → Pricing is sound.
```
</weak_link>

## Decision Protocol

<decision_protocol>
### Exact Question This Lens Answers
"Does this opportunity have pricing power, and what pricing structure captures
maximum value without leaving money on the table or alienating customers?"

### Data Required
- Customer willingness-to-pay data (Van Westendorp, pre-orders, surveys)
- Competitor pricing (3-5 competitors minimum)
- Customer value quantification (what does this save/earn the customer?)
- Cost structure (marginal cost per unit, CAC, support cost)
- Cohort data (if existing product): NRR, churn by pricing tier, expansion rate

### Confidence Threshold
- **Deploy (commit to pricing)**: ≥75% confidence, value quantified, pricing metric identified, competitor benchmarked
- **Flag (test pricing)**: 50-75% confidence, value not fully quantified, single pricing metric unclear
- **Discard**: <50% confidence, or no identifiable pricing metric, or customer can't afford value-capturing price

### Conflict Resolution Rules
- When Lens 09 (Pricing) disagrees with Lens 02 (Demand):
  - Demand present + no pricing power → **commodity play**. Either find differentiation (Lens 10) or accept Tier 3.
  - Demand present + pricing power → **strong opportunity**. Both lenses agree.
- When Lens 09 disagrees with Lens 04 (Leverage):
  - Pricing power + permissioned leverage → **service business with premium pricing**. Tier 2-3, profitable.
  - Pricing power + permissionless leverage → **Tier 1 candidate**. Rare and valuable.
- When Lens 09 disagrees with Lens 06 (Anti-Bias):
  - Anti-bias wins. A pricing strategy built on a saturated play is a race to the bottom.
- When Lens 09 disagrees with Lens 07 (Exponential):
  - Strong pricing power + low exponential → **great Tier 2 business**. Profitable, just not venture-scale.
  - Weak pricing power + high exponential → **risky**. The exponential depends on volume that pricing can't capture.
</decision_protocol>

## Output

<output>
```
### Pricing Power Analysis

#### Pricing Strategy Selection
- Recommended archetype: [value-based / usage-based / outcome-based / competitive / freemium / cost-plus]
- Rationale: [why this archetype fits]

#### Pricing Structure
- Tier 1 (Free/Entry): $[X] — [gating logic]
- Tier 2 (Mid): $[Y] — [gating logic, target revenue share]
- Tier 3 (Enterprise): $[Z] — [gating logic, target revenue share]
- Annual discount: [%]

#### Value Capture Analysis
- Value delivered to customer: $[V]/month
- Price charged: $[P]/month
- Value capture ratio: [P/V]% (target: 20-40%)
- Verdict: [underpricing / appropriate / overpricing]

#### Pricing Psychology Tactics Applied
1. [tactic + how applied]
2. [tactic + how applied]

#### Anti-Pattern Scan
| Anti-pattern | Present? | Fix |
|---|---|---|
| Underpricing | ✅/❌ | |
| Cost-plus | ✅/❌ | |
| Free tier too generous | ✅/❌ | |
| Pricing without distribution | ✅/❌ | |
| Copying competitor | ✅/❌ | |
| Pricing for features | ✅/❌ | |
| Linear tiers | ✅/❌ | |
| Annual discount <20% | ✅/❌ | |
| Hiding pricing | ✅/❌ | |
| Wrong pricing metric | ✅/❌ | |

#### Price Increase Plan (if existing product)
- Current price: $[X]
- Recommended price: $[Y] ([%] increase)
- Band: [small/medium/large/restructure]
- Grandfathering: [duration]
- Communication lead time: [days]
- Projected revenue impact: [+/- %]

#### Pricing Power Verdict
- Can raise prices 10% without losing 10% of customers? [YES/NO]
- If NO → commodity, not pricing power. Flag for differentiation work (Lens 10).
- If YES → pricing power confirmed. Set Tier 2 expectations (profitable, not necessarily exponential).
```
</output>

## Source

Distilled from `/references/research-pricing-competitor.md` which contains the
full pricing decision tree, Simon-Kucher frameworks, ProfitWell benchmarks,
90+ sources, and 5 worked teardown examples.
