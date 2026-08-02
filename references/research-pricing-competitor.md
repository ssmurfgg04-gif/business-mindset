# Research: Pricing Strategy & Competitor Teardown
**Task ID:** 1-D
**Source for:** Lens 09 (Pricing Power) and Lens 10 (Competitor Teardown) — AI Business Cognition Engine
**Author:** Research Subagent (retry)
**Date:** 2025

This document is the operational source material for two cognitive lenses that
the business-mindset skill uses to evaluate pricing decisions and competitor
landscapes. Every method below is concrete and actionable — no platitudes.

---

# PART A — PRICING (Lens 09: Pricing Power)

## 1. Pricing Strategy Decision Tree

Choose a pricing model by walking this tree. The right answer depends on
**three variables**: (a) can you measure the value you create per customer,
(b) does usage vary widely across customers, (c) are you attacking an
incumbent or seeding a new category.

```
START
  │
  ├── Can you quantify value created per customer (revenue lift, time saved,
  │   cost avoided) in dollars?
  │     │
  │     ├── YES → Is that value highly variable per customer?
  │     │           │
  │     │           ├── YES → OUTCOME-BASED / VALUE-BASED
  │     │           │          (charge % of measurable outcome — e.g., Stripe
  │     │           │           0.29%+$0.30, Vanta charges per monitored app,
  │     │           │           HubSpot tiers by contacts). DEFAULT FOR B2B SaaS.
  │     │           │
  │     │           └── NO  → VALUE-BASED FLAT (tie price to a value metric
  │     │                      that scales with use — seats, GB processed,
  │     │                      API calls). The value metric must move when the
  │     │                      customer gets more value.
  │     │
  │     └── NO  → Does usage vary widely across customers?
  │                 │
  │                 ├── YES → USAGE-BASED / CONSUMPTION (Snowflake, AWS, Twilio)
  │                 │          — customer pays only for what they use. Best
  │                 │          when the floor of usage is unpredictable (new
  │                 │          customers, spiky workloads). Pair with a small
  │                 │          base fee to stabilize revenue.
  │                 │
  │                 └── NO  → Is the market already price-anchored?
  │                             │
  │                             ├── YES → COMPETITIVE PARITY ± 10–20%
  │                             │          (anchor on leader's price, discount
  │                             │          if you're a follower, premium if you
  │                             │          have a defensible feature).
  │                             │
  │                             └── NO  → COST-PLUS as a sanity check only.
  │                                        Cost-plus tells you the *floor*,
  │                                        never the *price*. If cost-plus is
  │                                        your primary method, you are leaving
  │                                        30–60% of revenue on the table
  │                                        (Campbell / ProfitWell benchmark).
  │
  └── Attacking an incumbent or seeding new category?
        │
        ├── Attacking → FREEMIUM or low-cap free tier
        │               (Notion, Slack, Figma model). Requires: low marginal
        │                serving cost, viral collaboration loop, conversion
        │                funnel that can hit ≥2% free→paid. If conversion
        │                economics don't pencil, use a 14-day free trial
        │                instead.
        │
        └── Seeding new category → PENETRATION then SKIMMING
                                    (launch at a low price to seed the market,
                                     raise prices aggressively once category
                                     awareness is established). Bezos: "Your
                                     margin is my opportunity."
```

### Decision rules of thumb
- **B2B SaaS, $5k–$50k ACV:** value-based with a value metric (seats, contacts, records). This is the ProfitWell default for ~70% of B2B SaaS.
- **Infrastructure / developer tools:** usage-based with optional base commitment (the OpenView 2024 study: 46% of SaaS now use UBP, up from 24% in 2018).
- **Marketplace or platform:** take rate (% of GMV) + optional subscription for sellers.
- **Pre-PMF:** free or pay-what-you-want. Goal is signal, not revenue. Once PMF is found (Sean Ellis 40% test), transition to value-based within 90 days.
- **Never:** cost-plus as the *primary* method. Cost-plus is a floor, not a price.

---

## 2. SaaS Pricing Playbook

### 2.1 Tier Design — Good / Better / Best

The G/B/B (3-tier) model is dominant in B2B SaaS for one reason: it forces
the customer into a comparison frame instead of a "buy / don't buy" frame.
The third tier is essential as a decoy (see §3.2).

**Tier architecture:**

| Tier | Name | Target | Price Anchor | Feature Cut |
|------|------|--------|--------------|-------------|
| 1 — Good | "Starter" / "Basic" | Solo user, small team | Lowest | Just enough to deliver the core job. Limits on volume (seats, records, runs). No SSO, no audit logs, no priority support. |
| 2 — Better | "Pro" / "Growth" | Team of 5–50 | 2.5–4× Tier 1 | Removes volume caps. Adds collaboration, integrations, advanced analytics. **Where 60–80% of revenue should sit.** |
| 3 — Best | "Enterprise" / "Business" | 50+ users, procurement-led | 4–10× Tier 2 | SSO, audit logs, RBAC, SLA, dedicated CSM, custom contracts. **Used as a price anchor, not a primary seller.** |

**Empirical regularities (from Maxio, OpenView, Stripe data):**
- 3 tiers is the modal structure. 4 tiers works for marketplaces with clear buyer segments; 5+ tiers causes decision paralysis and reduces conversion.
- Tier 2 (the middle) should win 60–80% of customers by count, 50–70% by revenue. If Tier 1 wins >50%, your entry tier is too generous or Tier 2 is over-priced.
- The price ratio between tiers should be **non-linear**: if Tier 1 = $29, Tier 2 should be $99 (3.4×), Tier 3 should be $299 (10.3×). Linear ratios ($29 / $59 / $89) collapse the decoy effect.
- Always include a 4th hidden "Contact Us" tier for enterprise — captures procurement-led deals above the published ceiling.

### 2.2 Pricing Page Best Practices

The pricing page is the highest-leverage piece of real estate on a SaaS site.
ProfitWell research: pricing page design changes alone move conversion 15–30%.

1. **Lead with the value metric**, not the price. "Per seat, per month" before "$29". The customer needs to understand the *unit* before they can judge the *price*.
2. **Default to monthly billing** with annual as a clearly-displayed toggle. Annual defaults depress self-serve conversion ~20% (customers want the option to leave).
3. **Show the "most popular" badge on Tier 2**, not Tier 3. Badging Tier 3 screams "we want to upsell you" and depresses Tier 1/2 conversion.
4. **Feature checklist, not paragraph descriptions.** Side-by-side feature matrix beats prose. Use ✓ / ✗ / "Add-on" as the three states.
5. **Comparison anchor against a named competitor** when you're the price leader. "vs. Competitor X at $199" only works if you've actually benchmarked.
6. **Put the FAQ below the fold.** Above the fold: tiers, CTAs, key differentiators. FAQ answers objections; don't lead with objections.
7. **Mobile-first single-column layout.** Pricing pages that break on mobile lose 30%+ of B2C and SMB conversion.
8. **A/B test the price, not just the layout.** Price elasticity is the highest-leverage test. Most companies A/B test button color and never test price — that's a mistake.

### 2.3 Annual vs Monthly — The Math

Standard SaaS pricing convention: **annual = 10× monthly** (i.e., 2 months free). This is the "default" — but the math argues for testing.

**Why annual wins for the vendor:**
- CAC payback accelerates by ~2 months (cash collected up front).
- Churn drops ~30–50% (annual plans churn at ~5–10%/yr vs ~5–10%/mo for monthly).
- NRR improves: expansion happens inside a 12-month commit, not month-to-month.
- Sales motion: annual contracts are financeable (you can get a loan against them), monthly is not.

**Why monthly wins for the vendor:**
- Lower activation friction. Self-serve SaaS conversion drops 20% when annual is the default.
- Higher list price effective rate. If annual = 10× monthly, you're effectively discounting 17% (2/12). If your churn is low (<3%/mo), monthly billing at full price collects more revenue per customer-year.

**Decision rule:**
- If your monthly net dollar retention is **≥ 100%** AND monthly churn **≤ 5%**: keep monthly as the default. The 2-month "free" isn't worth the conversion hit.
- If monthly churn **> 7%**: push annual hard. The 17% discount is much cheaper than losing the customer in month 4.
- If you sell to enterprise / procurement: annual only. Procurement doesn't sign monthly contracts.

**Hybrid (best practice):** monthly default with annual displayed as a "Save 17%" toggle. Customer chooses, you capture both segments.

---

## 3. Pricing Psychology Catalog

Every tactic below has been replicated in academic and industry research.
Use them — they work. Use them ethically — lying about a price anchor
destroys trust and triggers refund requests.

### 3.1 Charm Pricing ($9.99 vs $10)
- **Mechanism:** left-digit bias. The brain processes the leftmost digit first; $9.99 is read as "nine-something," not "ten."
- **Effect:** 5–15% conversion lift on consumer products; weaker in B2B (procurement rounds).
- **When to use:** consumer SaaS, e-commerce, anything bought by an individual.
- **When NOT to use:** enterprise B2B above $1,000 ACV. Charm pricing signals "cheap" — wrong signal for a $50k/yr tool. Use round numbers ($5,000/yr, not $4,999).
- **Source:** NetSuite / psychological pricing literature; Schindler & Kibarian 1996 replication.

### 3.2 The Decoy Effect (Asymmetric Dominance)
- **Mechanism:** Add a third, dominated option that makes one of the original two options look better by comparison.
- **Classic example (Ariely, Economist):**
  - Web only: $59
  - Print only: $125
  - Print + Web: $125
  - The "Print only" is the decoy — nobody buys it, but it makes "Print + Web" look like a steal. Without the decoy, 68% bought Web only. With the decoy, 84% bought Print + Web.
- **SaaS application:** Tier 3 (Enterprise) is often the decoy. If Tier 1 = $29 and Tier 2 = $99, adding a Tier 3 at $299 with only marginally more features than Tier 2 makes Tier 2 look like the obvious choice.
- **Effect:** 20–35% lift in Tier 2 selection (Launchmystore benchmark).
- **Test first:** A bad decoy (one that's actually attractive) cannibalizes. The decoy must be *strictly* dominated by the target option.

### 3.3 Anchoring
- **Mechanism:** The first number mentioned becomes the reference point. All subsequent numbers are judged relative to it.
- **Application 1 — Show the most expensive tier first.** Reading order matters. Customers who see $299 first then $99 perceive $99 as cheap; customers who see $29 first then $99 perceive $99 as expensive.
- **Application 2 — Anchor on a competitor's price.** "Comparable tools cost $499/mo. Ours is $199." This works only if the comparison is true — false anchors trigger refunds.
- **Application 3 — Anchor on the cost of not solving the problem.** "The average sales team loses $48k/yr to missed follow-ups. Our tool costs $4,800/yr." The cost-of-inaction anchor is the most underused and most powerful.
- **Effect:** 15–40% lift in willingness-to-pay (Simon-Kucher benchmarks).

### 3.4 Framing
- **Mechanism:** The same number is perceived differently depending on how it's framed.
- **Frame 1 — Per-month vs per-day.** "$30/month" sounds bigger than "$1/day." For low-price consumer SaaS, framing as daily cost can lift conversion 10–20%.
- **Frame 2 — Loss vs gain.** "Don't lose $4,800/yr" beats "Save $4,800/yr." Loss aversion is ~2× as strong as gain motivation (Kahneman & Tversky).
- **Frame 3 — Bundling vs unbundling.** "10 features for $99" beats "10 features, individually $20 each = $200." The bundle looks like a deal even when the unbundled prices are fictional. Be honest — don't invent fake unbundled prices.
- **Frame 4 — Annual as monthly-equivalent.** "$1,200/year" → display as "$100/month, billed annually." Reduces sticker shock and lets the customer compare to monthly alternatives.

### 3.5 Bundling
- **Mechanism:** Combine multiple products into one price. Works when customers have heterogeneous valuations (Customer A values item 1 at $80 and item 2 at $20; Customer B values them at $20 and $80. Sell separately → max revenue $80 each. Bundle at $100 → both buy, revenue $200).
- **Pure bundle** (one price, all features): Microsoft Office, Adobe Creative Cloud. Works when you have broad product suite.
- **Mixed bundle** (items available separately OR bundled at discount): Slack + Slack AI. Captures both spectrum ends.
- **Anti-pattern:** bundling when customers only want one item and feel forced to pay for what they don't use → drives them to a competitor with a single-product offering.

### 3.6 The Three-Tier Decoy Architecture (combining 3.2 + 3.3)
The recommended SaaS structure:
1. **Tier 1 (Good):** Slightly under-featured. Acts as the anchor — its existence makes Tier 2 feel reasonable. **Don't expect >30% of revenue here.**
2. **Tier 2 (Better):** The target. Best value-per-dollar. This is what you want most customers to pick. **Aim for 60–80% of revenue.**
3. **Tier 3 (Best):** Over-priced relative to its additional features. Acts as a price ceiling and a decoy that makes Tier 2 look like a deal. **5–15% of revenue, but its presence lifts Tier 2 conversion 20–30%.**

### 3.7 Scarcity & Urgency
- "Limited to first 100 customers" / "Pricing locked for early customers"
- Effective for launch pricing, dangerous for steady-state. Misuse destroys trust.
- The only ethical version: **grandfather early customers at their launch price forever** — this is a real, enforceable commitment, not a fake scarcity trick.

### 3.8 Payment Framing
- Credit card required for trial → reduces trial signups 40–60%, but those who do trial convert 2–3× higher. Net effect: usually positive for revenue, negative for top-of-funnel.
- Reverse trial (free premium for 14 days, then downgrade to free tier, not to nothing) → 30–50% better LTV than opt-in upgrade trial (Pixabay / 2023 ProfitWell data).

---

## 4. Price Increase Protocol

Price increases are the highest-ROI action a SaaS company can take: a 1%
price increase produces an ~11% operating profit increase (McKinsey /
Simon-Kucher). They are also the most-feared. The fear is mostly wrong.
Baremetrics and Wingback both report: well-communicated increases of
10–20% produce <2% incremental churn.

### 4.1 The Six-Step Protocol

**Step 1 — Decide how much.**
- 3–5% increase: customers barely notice. No grandfathering needed, but communicate anyway. (Monetizely benchmark, 2025.)
- 5–15% increase: noticeable. Grandfather existing customers for 6–12 months; new pricing for new customers only.
- 15–30% increase: significant. Grandfather existing customers indefinitely OR for 12 months with explicit migration plan; expect 2–5% churn.
- >30% increase: reframe as a new product or a new tier. Do NOT call it a price increase; call it a v2 launch. Forced migration acceptable.

**Step 2 — Decide who gets grandfathered.**
- Default rule: grandfather all existing customers at their current price for at least 12 months. This converts the increase from "we're raising your price" to "new customers pay more, you're protected."
- Saastr benchmark: grandfathered customers typically pay 10–20% less than new customers — this is a feature, not a bug. The gap creates urgency for new prospects ("lock in the current price before the next increase").
- **Anti-pattern:** indefinite grandfathering. After 2–3 years, ~30% of your base is paying 30%+ below market, distorting your unit economics. Sunset grandfathering with explicit end dates.

**Step 3 — Decide when.**
- Best timing: **after a product launch, after a feature drop, or after an annual review.** The increase is bundled with new value.
- Worst timing: at renewal for enterprise customers (they'll re-negotiate everything). Increase at month 9 of a 12-month contract, not at renewal.
- Avoid: increases more than once per 12 months. Multiple small increases feel like nickel-and-diming; one larger annual increase is acceptable.

**Step 4 — Communicate.**
- Lead time: **6 months for major changes (>15%), 3 months for moderate (5–15%), 1 month for minor (<5%).** (Rework libraries benchmark.)
- The email must contain, in this order:
  1. **The "why"** — new features, infrastructure investment, support team growth. Make it concrete (e.g., "we shipped 47 features last year").
  2. **The "what"** — exact new price, effective date, link to FAQ.
  3. **The "what this means for you"** — explicit grandfathering terms OR explicit migration timeline. Do not make the customer figure this out.
  4. **The "how to lock in"** — if applicable, offer an annual upgrade or multi-year commit at the old price for a limited window (creates urgency, rewards loyal customers).
- Send 3 emails: T-90 days (heads up), T-30 days (specifics), T-7 days (last chance). Multiple touchpoints reduce the "I didn't see this" complaint.

**Step 5 — Build the off-ramp.**
- For the first 60 days after the increase, have a special-process for any customer who churns citing price. Offer them a 6-month extension at old price, no questions asked. Recover 40–60% of price-driven churn (Baremetrics).
- This is operationally expensive but reputationally critical. The 5 customers you save will tell the 50 who almost left.

**Step 6 — Measure & iterate.**
- Track 3 metrics for 90 days post-increase:
  - Incremental churn % (vs baseline)
  - NRR for affected cohort
  - New customer ACV (should jump if your value metric is right)
- If churn >3% above baseline, you raised too much or communicated poorly. Roll back is harder than just not raising — but a partial rollback (cap the increase at 10% instead of 20%) preserves trust.

### 4.2 Common Price-Increase Anti-Patterns
- **The "silent" increase** — only raising for new customers without telling existing ones. Works for 6 months, then explodes when a customer notices via G2 / Capterra / your pricing page. Communicate even what doesn't change.
- **The "annual creep"** — 5% per year, every year, no new features. Customers tolerate 1 year, churn in year 2. Tie increases to value, not to inflation.
- **The "headline" increase** — raising the published price but discounting 50% in negotiation. Trains customers to never pay list. Worse than not raising.
- **The "tier collapse"** — eliminating a popular low tier to force upgrades. The customers you lose are rarely the ones you wanted to keep. Keep the tier, raise its price, make it less attractive — let customers self-select up.

---

## 5. Top 10 Pricing Anti-Patterns (with fixes)

| # | Anti-Pattern | Why It Fails | Fix |
|---|---|---|---|
| 1 | **Cost-plus pricing** | Ignores value created. Caps your revenue at your cost structure. If your costs drop 30%, you drop your price 30% — leaving money on the table. | Use cost-plus only as a *floor check*. Set price by willingness-to-pay research (Van Westendorp, conjoint, customer interviews). |
| 2 | **Underpricing to "win the market"** | Attracts price-sensitive customers who churn at the smallest friction. Destroys gross margin, can't fund sales/support. Competes on the dimension where incumbents win. | Use ProfitWell's "willingness-to-pay" research. The right price is typically 2–3× what founders initially guess. (Patrick McKenzie: "Charge more.") |
| 3 | **Wrong value metric** | Pricing per seat when value scales with usage (or vice versa). Customers feel gouged or under-served; expansion revenue caps. | Find the metric that grows when the customer gets more value. Test by asking: "if our customer tripled in size, would our revenue triple?" If not, wrong metric. |
| 4 | **Too many tiers (5+)** | Decision paralysis. Hick's Law. Customers either default to the cheapest or leave. | 3 tiers + 1 "Contact Us" enterprise option. No more. If you need finer segmentation, use add-ons, not tiers. |
| 5 | **Feature-based pricing instead of value-based** | "Premium tier has 50 features vs. 40 features." Customers don't want features; they want outcomes. | Price by outcome: records managed, transactions processed, alerts resolved. Features are the *mechanism* for delivering the outcome, not the unit of value. |
| 6 | **No annual option / no monthly option** | Forces customers into a billing cadence that doesn't match their procurement cycle. Loses both ends. | Always offer both, with annual at a 17–20% discount (2 months free). Default to monthly for self-serve, annual for sales-led. |
| 7 | **Hiding the price ("Contact Us")** | Signals "you can't afford it" to SMBs; signals "we'll negotiate" to enterprises. Filters out prospects who would have self-served. | Publish prices up to your enterprise tier. Use "Contact Us" only for true custom / $100k+ deals. |
| 8 | **Discounting instead of value-adding** | "20% off" trains the customer to wait for the next discount. Compresses margin without changing perceived value. | Discount only for commitments (annual, multi-year, large volume). For tire-kickers, add value (free onboarding, extra seats) rather than cutting price. |
| 9 | **Never raising prices** | Grandfathering indefinite + never raising new-customer price = price drifts below market. After 3 years, your unit economics are broken. | Annual price review. Raise for new customers every 12 months. Grandfather existing for 12 months, then migrate. |
| 10 | **Pricing decided by founder intuition / committee** | Founders systematically underprice by 2–4× (ProfitWell data). Pricing-by-committee averages to the lowest common denominator. | Use willingness-to-pay research. Run Van Westendorp surveys with 100+ target customers before any major price decision. |

---

## 6. Practitioner Principles (the people who actually move the numbers)

### 6.1 Patrick Campbell (ProfitWell / Paddle)
1. **"Your pricing is the most important thing you'll ever do."** Pricing has 2–4× more leverage on revenue than acquisition, retention, or expansion. A 1% price improvement drives ~11% profit improvement; a 1% acquisition improvement drives ~3%.
2. **Use a value metric.** "If you can't point to one number that scales with the value the customer gets, you have a pricing problem, not a marketing problem."
3. **Re-price every 6–12 months.** Pricing decays. Customer value grows faster than price does. The gap is your leak.
4. **Segment by willingness-to-pay, not by company size.** Two companies of the same size can have 5× different WTP. Segment on the *job to be done*, not the demographics.

### 6.2 Madhavan Ramanujam (Simon-Kucher, "Monetizing Innovation")
1. **"Don't ask what price customers are willing to pay — ask what they need, value, and are willing to pay for."** The willingness-to-pay question is secondary to the willingness-to-pay-for-*what* question.
2. **Price before you build, not after.** The biggest monetization mistake is building the product and then figuring out the price. Price as part of product design — feature prioritization is a pricing decision.
3. **Feature-differentiate, don't just tier-differentiate.** Three tiers with the same features but different volumes is a missed opportunity. Each tier should serve a distinct buyer with distinct needs.
4. **The 9-step Monetizing Innovation framework:** (1) identify distinct customer segments; (2) identify feature willingness-to-pay by segment; (3) brainstorm pricing models; (4) segment-feature matrix; (5) differentiate the offering by feature; (6) survey willingness-to-pay; (7) determine price metric; (8) determine price level; (9) review with stakeholder check. (Source: book summary, Amazon.)

### 6.3 Patrick McKenzie (patio11 / Kalzumeus)
1. **"Charge more."** Almost every software founder underprices by 2–5×. The market-clearing price is almost always higher than the founder's intuition.
2. **"Pricing is marketing."** The price signals who you're for. A $19/mo tool says "hobbyist"; a $1,900/mo tool says "professional team." Same product, different signal → different customers.
3. **"Name your plans wisely."** "Starter / Pro / Enterprise" sells better than "Tier 1 / 2 / 3." Plan names tell the customer where they fit.
4. **"Make it easy to experiment with plans."** Pricing should be a knob you turn quarterly, not a once-a-decade rewrite. Build the billing infrastructure to support price tests.
5. **"Notify customers about pricing changes."** Not because the contract requires it (often it doesn't) — because surprise destroys trust. Trust is worth more than the price increase.
6. **"Give an off-ramp."** When you raise prices, give existing customers a path to keep their price for a defined period. The retention lift exceeds the price-delay cost.

### 6.4 Kyle Poyar (OpenView / Growth Unhinged)
1. **Usage-based pricing is winning because subscriptions hide value.** When a customer uses 10% of their seat licenses, they feel they're overpaying. UBP aligns what they pay with what they get.
2. **Hybrid (small base fee + usage) beats pure usage.** Pure UBP creates revenue volatility; pure subscription leaves money on the table for heavy users. Hybrid stabilizes both.
3. **The "land" motion needs a free or low-cost entry.** Snowflake, AWS, Datadog all start free or near-free. The expansion happens inside the product, not via sales.
4. **Product-led growth (PLG) and UBP are not the same thing.** You can do PLG with subscriptions (Slack, Notion). You can do UBP with sales-led (Snowflake). The two decisions are independent.

### 6.5 Lincoln Murphy (Sixteen Ventures)
1. **"Pricing is marketing."** (Same as McKenzie — this is consensus.) The price you set defines the customer you attract.
2. **Value-based pricing requires getting close to the customer's economics.** If you can't articulate how your product makes or saves the customer $X, you have no basis for a price.
3. **Discounts are a tax on lazy sales.** A 20% discount means the sales rep didn't sell value; they sold price. Train sales to sell the outcome, not the discount.

### 6.6 Tom Tunguz (SaaStr / theory of SaaS metrics)
1. **CAC payback period is the single most important pricing-adjacent metric.** If your CAC payback is >18 months, you're either underpricing or selling to the wrong segment.
2. **Gross margin determines your pricing flexibility.** A 90% gross margin SaaS can afford to discount 50% for land. A 50% gross margin services business cannot.
3. **NRR > 100% is the only sustainable SaaS state.** If NRR < 100%, you're losing customers faster than you're expanding them — and price increases alone can't fix it.

### 6.7 Sean Ellis (GrowthHackers, "Hacking Growth")
1. **Freemium only works if your product has a viral or network loop.** Without it, free users never become paid users — they just consume support cost.
2. **The "must-have" test (40% would-be-disappointed):** if <40% of users would be "very disappointed" without your product, you don't have PMF yet. Don't price aggressively until you do.
3. **Free trials convert better than freemium when the value is immediately obvious.** 14-day free trial of the full product > permanent free tier of a stripped-down product, for tools with a clear "aha" moment in week 1.

---

# PART B — COMPETITOR TEARDOWN (Lens 10: Competitor Teardown)

The goal of a competitor teardown is not to copy the competitor. It is to
**predict their next move** so you can either (a) outflank them, (b) be
somewhere they can't follow, or (c) ride in their wake. Every section below
is structured to produce a *prediction*, not just a description.

## 1. The Five-Stage Protocol: Discover → Map → Analyze → Predict → Exploit

### Stage 1 — DISCOVER

**Goal:** Identify every plausible competitor — direct, indirect, and
"replacement" — including the ones you don't know you don't know about.

**Methods:**

1. **Customer interview method (highest signal).** Ask 20 of your customers and 20 of your lost prospects: "What tools did you evaluate before choosing us? What did you almost use instead?" Christensen's JTBD framing: "What were you trying to get done when you hired us?" — the answer reveals non-obvious substitutes (a spreadsheet, a consultant, doing nothing).
2. **Search-based method.** For your top 20 keywords (commercial-intent queries, not category queries), capture the top 10 organic results and all paid advertisers. Repeat quarterly. The paid advertisers are the most aggressive competitors — they're spending to acquire the same intent.
3. **Review-site enumeration.** G2, Capterra, TrustRadius, Trustpilot. Filter by your category. Cross-reference — a product on all four with 100+ reviews is a serious player; a product on one with 5 reviews is noise.
4. **Backlink / SEO overlap.** Ahrefs and SEMrush both report "competing domains" — sites that rank for the same keywords as you. This surfaces competitors you've never heard of who are quietly capturing search demand.
5. **Job-posting intelligence (Stage 1 use).** Search competitor career pages and LinkedIn. A company you've never heard of that's hiring 5 SDRs in your category is a competitor now.
6. **Hiring patterns of *your customers' customers*.** If your customer base is e-commerce brands, and you see your customers hiring "AI shopping assistant integration specialists," that's a signal that a new category of competitor is emerging that you need to track.
7. **Conference attendee & sponsor lists.** SaaS-specific conferences (Saastr, B2B SaaS, MicroConf) and category-specific events. Sponsors = players with marketing budgets. Attendees (from public lists) = players in stealth / early stage.
8. **Crunchbase / Pitchbook funding filter.** Filter for your category + last-12-months funding. Every funded company in your space is either a competitor or a future acquisition target.
9. **GitHub / OSS scan.** Open-source projects in your category — even small ones — can become commercial competitors (Postgres → Supabase, SQLite → Turso). Star count growth >10%/mo is a leading indicator.
10. **Reddit / HN / X mentions.** Search "your-category-alternative" or "your-competitor-alternative" on r/SaaS, r/sysadmin, r/devops, Hacker News. The "alternative" question is asked when customers are unhappy with the incumbent.

**Tools:** SimilarWeb (traffic + competing sites), Ahrefs/SEMrush (SEO overlap), G2/Capterra (review-site enumeration), Crunchbase (funding), LinkedIn Talent Insights (hiring), Google Alerts / Talkwalker (mention tracking).

**What to extract:** A complete list of competitors with: name, URL, founding year, funding stage, headcount, estimated revenue (if available), primary buyer persona, value metric, list price, and one-line "why customers pick them."

### Stage 2 — MAP

**Goal:** Position competitors against each other on dimensions that matter
to the buyer, not dimensions that matter to you.

**Methods:**

1. **JTBD competitive map (Christensen).** Don't map "products like ours" — map "things customers hire to get the same job done." The milkshake example: a milkshake's competitors aren't other milkshakes; they're bananas, donuts, and coffee — anything hired for the "give me something to do during a long commute" job. *Your competitors are everything that gets the same job done, including doing nothing.*
2. **2×2 strategic positioning map.** Pick two axes that matter to the buyer (e.g., "ease of use" × "depth of features", or " SMB-friendly" × "enterprise-ready"). Plot every competitor. Empty quadrants are opportunities.
3. **Value-metric map.** X-axis: how they charge (per seat, per usage, per outcome, flat). Y-axis: how much. Reveals pricing white space.
4. **Buyer-persona map.** Who are they actually selling to? Read their case studies, G2 reviews (filter by reviewer role), job postings (are they hiring SMB SDRs or enterprise AEs?). One competitor may play in 3 segments you're not in.
5. **Capability / feature matrix.** Feature checklist across all competitors. Don't include every feature — include the 15–20 features that buyers actually mention in interviews. Anything else is vanity.
6. **Stratechery aggregator map.** Where on the value chain do they sit? Are they an aggregator (Google, Facebook), a supplier (NYT content), a platform (Apple App Store), a marketplace (Uber)? Their position determines their move set.

**What to extract:** A positioning map showing where each competitor plays, where they don't, and the white space. White space = where you can build without being attacked.

### Stage 3 — ANALYZE

**Goal:** Reverse-engineer the competitor's strategy, moat, cost structure,
and constraint. The output is a one-page "competitor brief."

**Methods:**

1. **Helmer 7 Powers analysis (full protocol in §4 below).** Determine which (if any) of the 7 Powers the competitor has. A competitor with no Power is fragile; a competitor with 2+ Powers is durable.
2. **Reverse-engineer their unit economics from public data.** For public companies: 10-K, S-1, earnings calls. For private companies: headcount × average salary (Glassdoor / Levels.fyi), estimated ARR per employee (a strong SaaS runs $150–300k ARR/employee), funding / burn rate (Crunchbase). Sanity check: headcount growth >50%/yr + recent funding round > $30M = burning to scale; flat headcount + small funding = bootstrapped or profitable.
3. **Reverse-engineer their pricing from public data + sales calls.** Pricing page, G2 reviews (mention price), customer interviews ("what are you paying?"). Mystery-shop their sales process if B2B mid-market+. Note the discounts offered — discount depth = pricing weakness.
4. **Read every public talk by their founder / CEO / Head of Product.** Keynotes, podcasts, conference talks. Founders reveal strategy in talks 6–18 months before they show up in product. (Notable example: Patrick Collison's 2014 essays foreshadowed Stripe's expansion into issuing, capital, and identity.)
5. **Analyze their changelog / release notes.** A competitor shipping 3 releases/week is in execution mode; one shipping 3/month is in maintenance mode. The *content* of releases tells you their roadmap.
6. **Analyze their hiring as a roadmap leak.** Job postings are public strategic signals:
   - Hiring 5+ ML engineers → AI features coming in 6–12 months.
   - Hiring a Head of Enterprise Sales → moving upmarket.
   - Hiring in Brazil / Germany / Japan → international expansion.
   - Hiring a Head of Pricing / Monetization → repricing coming.
   - Hiring compliance / SOC 2 / ISO 27001 lead → going enterprise.
   - Hiring for a brand-new product area (e.g., "Senior PM, Fraud Detection") → new product line coming. Look for the job posting that doesn't fit the current product.
7. **Customer review mining.** G2/Capterra/Glassdoor. Negative reviews of the competitor = your sales play. Positive reviews of the competitor = what you have to beat. Employee Glassdoor reviews = internal morale / strategy execution (high churn in the exec team = strategy is unstable).
8. **SEO / traffic analysis.** SimilarWeb + Ahrefs traffic trends. A competitor whose organic traffic dropped 40% in 6 months is in trouble (algorithm update, lost backlinks, or product decay). A competitor whose paid traffic is growing fast but organic is flat = burning money on ads without retention.

**Tools:** BuiltWith / Wappalyzer (their tech stack), Crunchbase (funding + investors), Glassdoor / Levels.fyi (comp + morale), SimilarWeb (traffic + sources), Ahrefs / SEMrush (keyword overlap), Wayback Machine (pricing / page history — shows what they tested), CB Insights (teardown reports), Stratechery archives (positioning analysis).

**What to extract:** A 1-page competitor brief covering: identity, Powers, pricing, target segment, recent moves, financial position, organizational health, predicted next move, our counter-move.

### Stage 4 — PREDICT

**Goal:** Forecast the competitor's next 6–18 month moves. This is the
hardest stage and the one that creates the most value.

**Framework A — Competitor Response Profile (Porter / Umbrex).**
Score each competitor on 4 dimensions:
1. **Objectives:** Are they maximizing growth, profit, market share, or exit value? (Read their board composition + investor letters if public. Read their Glassdoor reviews for "OKR" leaks.)
2. **Assumptions:** What do they believe about themselves and the market? (Read founder talks. "We're the premium brand" → they won't compete on price. "We're the developer-first tool" → they won't ship a no-code UI.)
3. **Strategy:** What's their current moat and motion? (Reverse-engineered from Stage 3.)
4. **Resources:** How much money, headcount, brand equity, distribution can they deploy? (Crunchbase + headcount + revenue estimates.)

**The prediction rules:**
- A competitor with strong resources + a strategy that's working + objectives aligned with attacking you → **they will respond.** Plan around it.
- A competitor with strong resources but a strategy that's working elsewhere (different segment) → **they will respond only if you cross their segment.**
- A competitor with weak resources but a working strategy → **they will respond asymmetrically** (PR, lawsuits, ecosystem plays — they can't out-build you but can out-narrative you).
- A competitor with weak resources and a failing strategy → **they won't respond meaningfully.** Don't waste effort planning for them.

**Framework B — Innovator's Dilemma disruption check (Christensen).**
Ask: does our move look like a low-end disruption to the competitor? If yes:
- Will they respond by matching us in the low-end segment? **Almost never.** The Innovator's Dilemma says incumbents flee upmarket, not down. They'll cede the low end and try to add features at the top.
- Will they spin up a separate brand/subsidiary to attack us? Sometimes (IBM PC, Saturn by GM). Often fails because the subsidiary inherits the parent's cost structure.
- Will they acquire us or a competitor? Often the eventual move. Plan for the M&A outcome.

**Framework C — When can't they respond? (the asymmetry finder).**
The most valuable competitive intelligence is the answer to "what would it
cost the competitor to respond to our move, and can they afford it?"
- **Channel conflict:** they can't sell direct without alienating their reseller channel. (Salesforce vs Siebel — Siebel's reseller channel prevented them from going SaaS fast.)
- **Margin cannibalization:** responding would require them to cut their own margins below what their public-market investors will tolerate. (Incumbent public SaaS vs. a new low-cost entrant.)
- **Architectural lock-in:** their existing customers are locked into an architecture that doesn't allow the new feature. Rewriting is multi-year. (Oracle vs. Snowflake — Oracle's installed base couldn't move to cloud-native fast enough.)
- **Brand constraint:** their brand is positioned in a way that makes the new move incoherent. (Patek Philippe can't launch a $200 watch without destroying the brand.)
- **Org structure:** the competitor's product org is siloed; shipping the new feature requires 3 P&L owners to agree. Takes 18 months.

**What to extract:** A prediction table: For each major competitor × each of your next 6–12 month moves, write one of: "won't respond," "will respond in 6 mo," "will respond in 12+ mo," "will respond asymmetrically (PR/lawsuit/M&A)." This becomes your strategic roadmap input.

### Stage 5 — EXPLOIT

**Goal:** Convert the prediction into action. Each prediction maps to a
specific play.

**Plays:**

1. **If they won't respond for 12+ months:** move fast, capture share, build switching costs before they wake up. (Stripe vs. banks in 2012–2016.)
2. **If they will respond by adding features (upmarket flight):** Don't chase them upmarket — they'll win there. Hold the low-end / mid-market and expand horizontally into adjacent segments they're ignoring. (The Christensen disruption play.)
3. **If they will respond asymmetrically (PR / lawsuit):** Pre-empt with transparency. Publish your method, your pricing, your data. Asymmetric attacks work best in information asymmetry; transparency disarms them. (Stripe's transparency about fees, eligibility, and outage postmortems defanged bank-lobby attacks.)
4. **If they will acquire:** Position yourself for acquisition. Optimize for the metric the acquirer cares about (usually customer count in a strategic segment, not revenue). Track the M&A precedent prices in your category.
5. **If they will respond by discounting:** Don't match the discount — match the value. Add features, services, integrations. Customers who switch for price will switch back for the next price cut; customers who switch for value stay.
6. **If they are slow due to architectural / channel / brand lock-in:** lean into the lock-in. Make your product the obvious choice for the customers their lock-in excludes. (Cloud-native vs. on-prem in 2010–2020.)

---

## 2. Incumbent Reaction Prediction

This is the single most under-developed skill in most strategy teams. The
question to answer: **"If we make this move, what will the incumbent do
in the next 18 months?"**

### 2.1 The Four-Question Reaction Predictor

For each incumbent competitor, answer:

**Q1 — Can they respond? (capability)**
- Do they have the engineering capacity? (Check headcount, recent product velocity from changelogs, the % of eng working on the area you're attacking.)
- Do they have the capital? (Public: balance sheet. Private: last funding round + burn rate. Bootstrapped: likely yes if they're profitable, no if they're not.)
- Do they have the distribution? (Existing customer base, sales team, partner channel — can they reach your customers without building new GTM?)
- Do they have the brand permission? (Would customers believe them in this category? Microsoft launching a design tool gets skepticism; Figma launching one gets instant credibility.)

**Q2 — Will they respond? (incentive)**
- Does responding cannibalize their existing revenue? (If yes, they'll delay. The Innovator's Dilemma.)
- Does responding fit their stated strategy? (Read the last 3 earnings calls. If they've publicly committed to a different direction, they can't easily pivot without losing credibility.)
- Does responding conflict with their channel / partners / installed base? (Channel conflict is the #1 incumbent-paralysis cause.)
- Will their investors / board support the response? (Public company: would the response require a guidance cut? Private: would it require a down round?)

**Q3 — When will they respond? (timing)**
- **0–3 months:** only if they already have the feature in development. Check their changelog, hiring (PM hires 6–12 months before ship), and patent filings (12–24 months lead time).
- **3–9 months:** if they have the engineering capacity and a clear strategic motivation. Most product responses land here.
- **9–18 months:** if they need architectural changes, channel re-alignment, or M&A integration.
- **18+ months / never:** if architectural / brand / channel / margin lock-in prevents them. The most exploitable situation.

**Q4 — How will they respond? (form)**
- **Feature match:** the default. Expected if they have capacity + incentive + no lock-in.
- **Acquisition:** if they can't build fast enough and have capital. Track which companies they've acquired historically — pattern matches their preference.
- **Pricing attack:** if their cost structure allows them to undercut. Rare in B2B SaaS (margin compression hurts them more than you), common in consumer / infrastructure.
- **Marketing / PR attack:** the "FUD" play. Common when they can't respond in product. Counter with transparency.
- **Lawsuit:** rare but increasing in AI / data / IP-intensive categories. Watch their patent portfolio and litigation history.
- **Channel lock-in / exclusive deals:** common in marketplaces and platforms. They pay partners to not work with you.

### 2.2 The "Can't Respond" Catalog (Asymmetry Finder)

Most valuable strategic insight: **where is the incumbent structurally
unable to respond?**

| Lock-in type | Example | How to exploit |
|---|---|---|
| Channel conflict | Siebel couldn't go SaaS without angering its integrator channel. | Sell direct, build your own channel from their neglected integrators. |
| Margin cannibalization | Oracle couldn't cut on-prem database prices to match Snowflake without crashing their public-market multiple. | Price at half their level; they can't follow. |
| Architectural lock-in | SAP's R/3 architecture couldn't move to multi-tenant SaaS without rewrite. | Build cloud-native; they need 5+ years to catch up. |
| Brand constraint | IBM can't launch a $50/mo SMB tool without diluting the enterprise brand. | Own the SMB segment; they can't enter without breaking their positioning. |
| Org silo | Microsoft Office vs. Google Docs: Office org couldn't ship a free browser-based product without three P&L owners agreeing. | Move faster than their internal politics. |
| Public-market guidance | A public incumbent can't cut prices 30% without warning Wall St. | Use the public-company constraint against them. |
| Regulated-installed-base | Banks couldn't move to cloud-native infrastructure because of compliance audits on existing systems. | Sell to greenfield customers; don't try to migrate their base. |

### 2.3 The "Will Respond" Warning Signs

Conversely, expect a rapid response if:
- The competitor has hired a senior PM/eng leader in this area in the last 6 months (visible on LinkedIn).
- The competitor has a pattern of fast-following (look at their last 3 product launches — were they me-too or original?).
- The competitor's growth has stalled and they're under investor pressure to respond (read their last earnings call transcript).
- The competitor has made a related acquisition in the last 12 months (they're integrating, not greenfield-building).
- The competitor's CEO has publicly committed to this category in a talk or earnings call.

---

## 3. Under-the-Radar Competitor Discovery Checklist

The most dangerous competitors are the ones you don't see coming. Use this
checklist monthly to catch them early.

### 3.1 Customer-side signals
- [ ] **Lost-deal analysis:** in your last 20 losses, what tool did they pick? Any repeats? Any unknown names?
- [ ] **Won-deal analysis:** in your last 20 wins, what tools did they evaluate? Any unknown names?
- [ ] **Customer churn interviews:** when a customer churns, ask "what are you using instead?" — even if they say "nothing," dig. They're often using a spreadsheet, a consultant, or a tool they didn't mention.
- [ ] **"How did you hear about us?"** field in your signup form. Track mentions of competitor names — sometimes prospects come to you because they're also evaluating the competitor.

### 3.2 Search-side signals
- [ ] **Google Search Console "queries" report:** what queries are people searching when they find you? Look for "your-competitor vs" or "your-competitor alternative" queries — those name competitors you should know about.
- [ ] **Google Autosuggest:** type "your-category " into Google and see what autosuggests. Type "your-competitor-name " and see if "vs" or "alternative" appears.
- [ ] **Ahrefs / SEMrush "competing domains" report:** surfaces sites ranking for the same keywords. Set up quarterly comparison.
- [ ] **Google Trends:** track your category term + competitor names. A rising unknown is a signal.

### 3.3 Hiring-side signals
- [ ] **LinkedIn job search:** search for your category + "PM" / "engineer" / "founder." Filter by last-30-days postings. Note unfamiliar companies.
- [ ] **AngelList / Wellfound:** filter by your category + recently-funded. Stealth companies often show up here before they show up anywhere else.
- [ ] **Your own alumni:** where did your last 5 departed employees go? If 3 went to the same company, that company is in your space.

### 3.4 Funding-side signals
- [ ] **Crunchbase alert:** set up a saved search for your category + last-30-days funding. Read weekly.
- [ ] **Y Combinator batch list:** every batch, filter for your category. YC companies in your space are 2–4 years from being meaningful competitors.
- [ ] **a16z / Sequoia / Bessemer portfolio pages:** they invest in patterns. If 2 of them have a portfolio company in your category in the last 12 months, the category is heating up.

### 3.5 Community-side signals
- [ ] **Reddit:** search r/SaaS, r/sysadmin, r/devops, your sub-category sub, for "alternative" or "vs" posts. The "what should I use instead of X?" question reveals the demand-side competitor landscape.
- [ ] **Hacker News:** search for "Show HN" + your category keywords in the last 12 months. New launches show up here first.
- [ ] **Indie Hackers / MicroConf community:** solo / small-team competitors. Easy to dismiss; dangerous because they're scrappy and fast.
- [ ] **Discord / Slack communities** in your category: members drop product recommendations constantly. lurk and note names.

### 3.6 OSS / developer-side signals
- [ ] **GitHub topic pages:** for your category, sort by stars + recent activity. A project gaining 100+ stars/month is a candidate.
- [ ] **Hacker News "Show HN" archive:** search for your category. Repeat launches indicate momentum.
- [ ] **Awesome-lists** in your category on GitHub: the maintained ones list every notable project.
- [ ] **OSS commercial-ization patterns:** Postgres → Supabase, SQLite → Turso, Vector → Datadog. Watch OSS projects that recently took venture funding — they're about to become commercial competitors.

### 3.7 Geo signals
- [ ] **Non-US competitors:** many categories have strong European / Asian competitors invisible from a US-centric view. Check local review sites (e.g., Capterra country filters, local SaaS directories).
- [ ] **Cross-border talent flow:** a competitor hiring US sales leaders from abroad = planning US entry.

---

## 4. Helmer 7 Powers Application Guide

Hamilton Helmer's 7 Powers framework (from "7 Powers: The Foundations of
Business Strategy") is the most rigorous taxonomy of sustained competitive
advantage. Use it on every competitor — and on yourself. The question
isn't "do they have features?" It's "do they have Power?"

The 7 Powers, applied to competitor analysis:

### Power 1 — Scale Economies
**Definition:** Per-unit cost declines as business size grows. The leader has a structural cost advantage.
**How to detect in a competitor:**
- Are they ≥2× the scale of the next-largest player in a fixed-cost-heavy business (data centers, sales force, content production, regulatory compliance)?
- Does their gross margin increase as they grow? (Public SaaS gross margin should climb 3–5pp from $10M → $100M ARR if scale economies are real.)
**Application:** A competitor with scale economies can underprice you sustainably. Do NOT compete on price. Compete on a dimension where their scale doesn't help (segment specificity, speed, niche feature depth).
**Example:** Amazon AWS — scale economies in data center costs. You cannot out-price AWS; you can out-serve a specific segment.

### Power 2 — Network Economies
**Definition:** Value of the product increases as user base grows. Each new user adds value to all existing users.
**How to detect:**
- Does the product have a true network effect (more users = more value), or just virality (more users = lower CAC)?
- Multi-sided networks (marketplaces, social platforms) are stronger than single-sided.
- Look at the activity ratio: do power users / total users stay flat or grow as the network scales? Decay = network is hollowing.
**Application:** A competitor with strong network effects has a near-insurmountable lead in their core market. Don't attack the network head-on. Attack an adjacent market where the network doesn't extend, or wait for the network to decay (cognitive load, spam, demographic shift).
**Example:** Facebook's social graph was an unbreakable Power in 2012. By 2020, the graph hollowed out (older demographics, spam) and TikTok's algorithmic feed (a different Power — counter-positioning) overtook it.

### Power 3 — Counter-Positioning
**Definition:** The competitor adopts a new, superior business model that incumbents can't copy without cannibalizing their existing business.
**How to detect:**
- Is the competitor using a fundamentally different business model (SaaS vs. on-prem, DTC vs. retail, free vs. paid)?
- Would the incumbent have to destroy their existing revenue to copy it?
- Is the new model structurally better (lower cost, better UX, faster cycle), not just cheaper?
**Application:** A competitor with counter-positioning will keep winning until the incumbent either (a) spins up an isolated subsidiary to copy the model (usually fails — see IBM PC, Saturn by GM), or (b) gets acquired / dies. Bet against the incumbent; bet with the counter-positioner.
**Example:** Netflix vs. Blockbuster (streaming vs. retail rental). Blockbuster couldn't copy without destroying its retail footprint. Tesla vs. incumbent OEMs (vertical DTC vs. dealer model).

### Power 4 — Switching Costs
**Definition:** Customers face high cost (financial, technical, behavioral) to switch to a competitor.
**How to detect:**
- Is the product deeply integrated into the customer's workflow (APIs, data schemas, training, third-party extensions)?
- Does the customer's data live inside the product in a non-portable format?
- Are there multi-year contracts with termination penalties?
- Is the product used by multiple stakeholders whose training investment is high?
**Application:** A competitor with high switching costs has predictable retention and can raise prices annually without churn. To break in, you need either (a) a greenfield customer (no switching cost), (b) a moment of customer pain (the competitor's failure, M&A uncertainty, pricing shock), or (c) a bridge strategy (parallel run, automated migration, free migration service).
**Example:** Salesforce's switching costs are legendary — once a sales team's pipeline is in Salesforce, leaving is a multi-quarter IT project. HubSpot broke in by selling to SMBs (greenfield) and growing up with them.

### Power 5 — Branding
**Definition:** The brand carries information that lowers customer acquisition cost and increases willingness-to-pay.
**How to detect:**
- Do customers pay a price premium for the brand vs. equivalent private-label products? (Apple vs. Android, Nike vs. unbranded.)
- Is the brand associated with a specific emotional / identity value, not just functional utility?
- Does the brand have a long history of consistent positioning? (Brands are built over years, not quarters.)
**Application:** A competitor with brand Power can charge 20–100% premium and customers will pay. To compete, you either (a) compete on a different dimension (functionality, price, service) where brand doesn't apply, or (b) out-brand them in a niche (Dollar Shave Club vs. Gillette — smaller niche, sharper brand).
**Example:** Notion's brand among designers and PMs is a Power — they pay $10/user/month for a tool that has functional equivalents at $5. The brand premium is real.

### Power 6 — Cornered Resource
**Definition:** The competitor has preferential access to a scarce, valuable resource.
**How to detect:**
- Exclusive IP (patents, trademarks, trade secrets).
- Exclusive data (Google's search logs, Bloomberg's financial data).
- Exclusive talent (a key researcher, a designer, a team that can't be replicated).
- Exclusive physical access (a mine, a spectrum license, a port).
- Exclusive regulatory approval (FDA orphan drug, FAA certification).
**Application:** A competitor with a cornered resource can sustain margins in a way you can't. To compete, you either (a) find a substitute resource (often hard), (b) wait for the resource to expire (patents expire, talent leaves), or (c) compete in an adjacent market where the resource doesn't apply.
**Example:** NVIDIA's CUDA ecosystem is a cornered resource — a decade of developer lock-in. AMD can't easily replicate. Intel's response: compete on price / different workload, but the resource stays with NVIDIA.

### Power 7 — Process Power
**Definition:** The competitor's internal processes (org structure, production method, decision-making) are structurally better than rivals', and hard to copy.
**How to detect:**
- Sustained operational metrics better than peers (e.g., Toyota's defect rate vs. US automakers in the 1980s).
- Employee tenure / satisfaction above industry average (the process is institutionalized, not founder-dependent).
- The process is embedded in culture, not in documentation — that's why it can't be easily copied.
**Application:** A competitor with Process Power will keep improving faster than you. To compete, you either (a) accept a structural cost / quality disadvantage and play in a segment where it doesn't matter, or (b) adopt their process — which usually requires a multi-year transformation and probably a new leadership team.
**Example:** Toyota Production System vs. US automakers. It took GM 20+ years and the NUMMI joint venture to even begin copying. Most companies never can.

### How to Apply: The Competitor Power Scorecard

For each competitor, score 0 / 1 / 2 on each Power:
- 0 = no evidence of this Power
- 1 = some evidence / emerging Power
- 2 = clear, durable Power

| Competitor | Scale | Network | Counter-Pos | Switching | Brand | Cornered | Process | **Total** |
|---|---|---|---|---|---|---|---|---|
| Competitor A | 2 | 1 | 0 | 2 | 1 | 0 | 1 | **7** |
| Competitor B | 0 | 0 | 2 | 1 | 0 | 0 | 0 | **3** |
| You | 0 | 0 | 1 | 1 | 1 | 1 | 0 | **4** |

**Interpretation:**
- **0–2:** No Power. Fragile. Can be displaced by anyone with 1+ Power.
- **3–5:** Some Power. Defensible in their niche, vulnerable to broader attacks.
- **6–9:** Strong Power. Hard to displace. Attack only where their Powers don't extend.
- **10+:** Dominant Power. Don't attack head-on. Wait for Powers to decay (every Power has a half-life).

**Strategic implication:** Your goal is to identify which Power you can build that no competitor has, OR which Power you can erode in a competitor (network hollowing, brand dilution, talent flight from a cornered resource). If you have zero Powers, your strategy is to build one — fast. Without a Power, growth is just spending money.

---

## 5. Real Teardown Examples

Five worked examples showing the protocol end-to-end. Each is condensed;
the full teardowns are in the cited sources.

### 5.1 Stripe vs. PayPal (2010–2026)

**Stage 1 — Discover:** In 2010, PayPal was the dominant online payment processor (~90% market share among developers). Stripe entered as a developer-first API challenger.

**Stage 2 — Map:** Stripe's positioning was "7 lines of code to accept payments" (developer-centric, ease-of-integration). PayPal's was "consumer wallet for online shopping" (consumer-centric, fraud-protection). The JTBD map revealed these were *different jobs* — Stripe served "I'm a developer and I want to add payments to my app"; PayPal served "I'm a consumer and I want to pay without entering my card."

**Stage 3 — Analyze:**
- PayPal's Power: Network Economies (consumer wallet network) + Scale Economies (fraud infrastructure). High.
- PayPal's lock-in: consumer brand, merchant acquisition channel (PayPal button on every e-commerce site), parent company (eBay) channel.
- Stripe's counter-positioning: pure API for developers, no consumer wallet. PayPal couldn't copy without cannibalizing the consumer wallet.
- Stripe's Powers in 2012: Counter-Positioning (only). By 2020: Counter-Positioning + Branding (developer brand) + Switching Costs (once Stripe is integrated, switching is costly).

**Stage 4 — Predict:** PayPal couldn't respond by copying the developer-first model without rebuilding their API surface and alienating their consumer base. They tried (PayPal for Developers, Braintree acquisition in 2013) — partial response. Predicted: PayPal would acquire or partner rather than out-build. Confirmed: 2024–2026 Stripe-PayPal acquisition talks (consortium led by Stripe + Advent).

**Stage 5 — Exploit:** Stripe captured developer mindshare from 2012–2018 by being the easiest integration. By the time PayPal/Braintree caught up on developer experience, Stripe had switching costs (Issuing, Capital, Atlas, Billing, Identity — full-stack platform). The teardown lesson: a counter-positioned entrant can build switching costs *during the window when the incumbent can't respond*.

### 5.2 Notion vs. Evernote (2015–2023)

**Stage 1 — Discover:** Evernote was the dominant note-taking app (100M+ users by 2015). Notion entered as a "block-based workspace" challenger.

**Stage 2 — Map:** JTBD: Evernote = "remember everything I read / see." Notion = "build a system to organize my team's work." Different jobs.

**Stage 3 — Analyze:**
- Evernote's Power: Switching Costs (decades of user notes locked in proprietary format) + Branding (the "second brain" brand).
- Notion's counter-positioning: collaborative, block-based, multi-tool (notes + docs + database + wikis). Evernote couldn't copy without becoming a different product.
- Notion's Powers: Counter-Positioning + Branding (designer / PM darling) + Network Economies (templates marketplace) by 2020.

**Stage 4 — Predict:** Evernote would try to add collaboration features (they did — Evernote Spaces, 2018, failed). They'd eventually be acquired or fade. Confirmed: Bending Spoons acquired Evernote in 2022; Notion reached $10B valuation in 2021.

**Stage 5 — Exploit:** Notion didn't attack Evernote's note-taking core. They built a multi-tool workspace and let users self-migrate. The teardown lesson: in a switching-cost-locked market, attack an adjacent job where the incumbent's lock-in doesn't apply, then expand into the incumbent's core once you have switching costs of your own.

### 5.3 Slack vs. Microsoft Teams (2016–2024)

**Stage 1 — Discover:** Slack (2013 launch) was the dominant team-chat tool by 2016. Microsoft launched Teams in 2017, bundled with Office 365.

**Stage 2 — Map:** JTBD: Slack = "real-time team communication, replace email." Teams = "the Office 365 collaboration layer." The same job, different distribution.

**Stage 3 — Analyze:**
- Slack's Powers: Network Economies (per-team, not global) + Branding + Switching Costs (integration ecosystem).
- Microsoft's Powers: Scale Economies + Switching Costs (Office suite) + Cornered Resource (Office customer base) + Counter-Positioning (bundled pricing — "free with Office 365").
- Slack's lock-in: per-team network effect is strong but each team is isolated.
- Microsoft's lock-in: enterprise Office contracts, multi-year, $M-scale.

**Stage 4 — Predict:** Microsoft would bundle Teams into Office 365 at zero marginal cost, making Slack's paid product uncompetitive for any enterprise already on Office. Slack could not respond on price (their cost structure required paid seats). Predicted: Slack would either be acquired or lose the enterprise segment. Confirmed: Salesforce acquired Slack in 2020 for $27.7B; Teams surpassed Slack in daily active users by 2019 and has continued to pull away in enterprise.

**Stage 5 — Exploit (or in Slack's case, survive):** Slack couldn't out-distribute Microsoft. The teardown lesson: when an incumbent with scale + cornered resource (distribution) bundles against you, you cannot win on the same axis. Either redefine the category (Slack didn't) or get acquired (Slack did). The window to compete was 2013–2017; Microsoft closed it in 2018.

### 5.4 Snowflake vs. Oracle / Teradata (2014–2023)

**Stage 1 — Discover:** Oracle and Teradata dominated the on-prem data warehouse market. Snowflake launched in 2014 as cloud-native.

**Stage 2 — Map:** JTBD: "store and query large datasets for analytics." Same job, different architecture.

**Stage 3 — Analyze:**
- Oracle's Powers: Scale Economies + Switching Costs (decades of installed base + Oracle DBA certifications + Oracle applications stack) + Cornered Resource (enterprise sales relationships).
- Snowflake's counter-positioning: cloud-native, separation of storage and compute, consumption-based pricing. Oracle would have to cannibalize on-prem license revenue (the cash cow) to copy.
- Snowflake's Powers by 2020: Counter-Positioning + Scale Economies (cloud infra) + Network Economies (Snowflake Marketplace data sharing).

**Stage 4 — Predict:** Oracle would (a) try to relaunch their own cloud DW (Autonomous Data Warehouse, 2017 — partial response), (b) deny Snowflake is meaningfully different (Larry Ellison's public dismissals 2018–2020), (c) eventually accept and try to compete on price / bundling. Confirmed across all three.

**Stage 5 — Exploit:** Snowflake captured greenfield cloud workloads (no switching cost) and grew up. Oracle's installed base couldn't migrate fast (architectural + compliance + DBA training lock-in). The teardown lesson: architectural counter-positioning wins against incumbents whose installed base is structurally immobile.

### 5.5 Figma vs. Adobe (2016–2024)

**Stage 1 — Discover:** Adobe (Illustrator, Photoshop, Sketch) dominated design tools. Figma launched in 2016 as browser-based, collaborative.

**Stage 2 — Map:** JTBD: "design interfaces, collaboratively." Figma served the "collaboratively" part better; Adobe served the "design" part with deeper tools.

**Stage 3 — Analyze:**
- Adobe's Powers: Scale Economies + Switching Costs (Creative Cloud lock-in) + Branding + Cornered Resource (designer mindshare via Illustrator/Photoshop).
- Figma's counter-positioning: browser-native, real-time multiplayer, component system. Adobe would have to cannibalize Creative Cloud desktop revenue to copy.
- Figma's Powers by 2021: Counter-Positioning + Network Economies (per-team) + Switching Costs (Figma files, components, plugins).

**Stage 4 — Predict:** Adobe would (a) try to ship a competitor (Adobe XD, 2017 — partial response, failed to catch up), (b) acquire Figma (announced Sept 2022, $20B — the largest-ever private SaaS acquisition), (c) the acquisition would face regulatory scrutiny and might fail (it did — abandoned Dec 2023). All three confirmed.

**Stage 5 — Exploit:** Figma captured the new generation of designers (collaboration-first, browser-first) that Adobe's installed base didn't serve. Adobe's switching costs (decades of Illustrator/Photoshop training) didn't apply to new designers entering the field. The teardown lesson: when an incumbent's switching costs protect the existing user base but don't extend to new users, the entrant captures the new generation and out-grows the incumbent.

---

## BIBLIOGRAPHY

### PRICING

#### Patrick Campbell / ProfitWell / Paddle
- Patrick Campbell: Pricing, Retention, and Growth — https://businessofsoftware.org/talks/pricing-retention-and-growth-strategies
- Value Based Pricing (Patrick Campbell, Profitwell) — https://www.cloudsoftwareassociation.com/2019/09/17/patrick-campbell-profitwell-talk
- B2B SaaS Pricing 101 with Patrick Campbell of ProfitWell (Reddit) — https://www.reddit.com/r/ProductManagement/comments/10fxasu/b2b_saas_pricing_101_with_patrick_campbell_of
- Boost startup revenue with value metric pricing — https://ltse.com/insights/product-pricing-for-startups-value-metrics
- ProfitWell's Patrick Campbell On The Art And Science Of Pricing (Intercom) — https://www.intercom.com/blog/podcasts/profitwells-patrick-campbell-on-the-art-and-science-of-pricing
- SaaS Pricing 101 (Alphalist) — https://alphalist.com/blog/saas-pricing-101
- Key Metrics for Value-Based Pricing in SaaS (Baremetrics) — https://baremetrics.com/blog/key-metrics-value-based-pricing-saas

#### Madhavan Ramanujam / Simon-Kucher / Monetizing Innovation
- The art and science of pricing (YouTube) — https://www.youtube.com/watch?v=A6veeCbKIzw
- Drive Your Growth and Monetize Your Innovations (Simon-Kucher) — https://www.simon-kucher.com/en/insights/drive-your-growth-monetize-your-innovations
- Monetizing Innovation Skill (PMP Prompt) — https://pmprompt.com/skills/monetizing-innovation
- 5 Key Takeaways from Monetizing Innovation (Medium) — https://medium.com/@pranavbhatblog/5-key-takeaways-from-the-book-monetizing-innovation-ba4630cb0539
- Monetizing Innovation (Amazon) — https://www.amazon.com/Monetizing-Innovation-Companies-Design-Product/dp/1119240867
- Monetizing Innovation — Interview with Simon-Kucher (Marketing Journal) — https://www.marketingjournal.org/monetizinginnovation
- Lenny Rachitsky on Madhavan Ramanujam (LinkedIn) — https://www.linkedin.com/posts/lennyrachitsky_the-art-and-science-of-pricing-madhavan-activity-7006665785796440065-pzqB

#### SaaS Tier Design / Good-Better-Best
- Tiered Pricing Strategy Guide for SaaS (Maxio) — https://www.maxio.com/blog/tiered-pricing-examples-for-saas-businesses
- Your Ultimate Guide to SaaS Pricing Models (Revenera) — https://www.revenera.com/blog/software-monetization/saas-pricing-models-guide
- The Best and Worst SaaS Pricing Models (Insight2Profit) — https://www.insight2profit.com/the-best-and-worst-saas-pricing-models
- How to create an effective SaaS pricing strategy (Recurly) — https://recurly.com/blog/how-to-create-an-effective-saas-pricing-strategy
- The Art and Science of Tiered Pricing (OpenView) — https://openviewpartners.com/blog/tiered-pricing-optimization
- A Complete Guide to SaaS Pricing Strategies (Schematic) — https://schematichq.com/blog/saas-pricing-strategies
- Tiered pricing 101 (Stripe) — https://stripe.com/resources/more/tiered-pricing-101-a-guide-for-a-strategic-approach

#### Van Westendorp Price Sensitivity Meter
- Van Westendorp Price Sensitivity Meter Questions (Quantilope) — https://www.quantilope.com/resources/examples-of-van-westendorp-price-sensitivity-questions
- Van Westendorp's Price Sensitivity Meter (Wikipedia) — https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter
- Van Westendorp Price Sensitivity Meter Tool (Conjointly) — https://conjointly.com/products/van-westendorp
- A Guide To The Van Westendorp Pricing Model (Forbes) — https://www.forbes.com/sites/rebeccasadwick/2020/06/22/how-to-price-products
- Van Westendorp Pricing Model (Sawtooth Software) — https://sawtoothsoftware.com/resources/blog/posts/van-westendorp-pricing-sensitivity-meter
- How To Use The Van Westendorp PSM (SurveyMonkey) — https://www.surveymonkey.com/market-research/resources/van-westendorp-price-sensitivity-meter
- Van Westendorp for Pricing Research (OpinionX) — https://www.opinionx.co/blog/van-westendorp-pricing-guide

#### Price Increase Protocol & Grandfathering
- Arguments against "Grandfathering" when raising prices (Reddit r/SaaS) — https://www.reddit.com/r/SaaS/comments/1c9myur/arguments_against_grandfathering_when_raising
- What is Grandfathering in SaaS Pricing? (Chargebee) — https://www.chargebee.com/resources/glossaries/what-is-grandfathering
- Grandfathering Strategy: Managing Pricing Changes (Rework) — https://resources.rework.com/libraries/saas-growth/grandfathering-strategy
- How to Raise SaaS Prices Without Losing Customers (Baremetrics) — https://baremetrics.com/blog/saas-price-increase-how-to-raise-prices-without-upsetting-customers
- (Mostly) Everything You Need to Know About Grandfathering (Wingback) — https://www.wingback.com/blog/everything-you-need-to-know-about-grandfathering-in-saas
- Grandfathering vs Forced Migration (Monetizely) — https://www.getmonetizely.com/articles/grandfathering-vs-forced-migration-the-strategic-approach-to-price-changes-for-existing-customers
- Grandfathering in SaaS Pricing (SaaS WTF) — https://www.saas.wtf/p/grandfathering-saas-pricing
- Grandfathering in B2B SaaS (Parseur) — https://parseur.com/blog/grandfathering-b2b-saas

#### Pricing Psychology
- 5 Psychological Pricing Tactics That Attract Customers (NetSuite) — https://www.netsuite.com/portal/resource/articles/ecommerce/psychological-pricing.shtml
- Psychological pricing strategies (Easy.tools) — https://www.easy.tools/blog/psychological-pricing
- Psychological Pricing: Strategies & Examples (Impact Analytics) — https://www.impactanalytics.ai/blog/psychological-pricing
- 9 Psychological Pricing Hacks, Decoded (Medium) — https://medium.com/the-saas-growth-blog/9-psychological-pricing-hacks-decoded-e9449234332d
- Positioning decoy pricing to shape customer value perception (Simon-Kucher) — https://www.simon-kucher.com/en/insights/positioning-decoy-pricing-shape-how-customers-perceive-value
- Ecommerce Pricing Psychology: 12 Tactics (Launchmystore) — https://launchmystore.io/blog/psychology-ecommerce-pricing-strategies
- Psychological pricing (Wikipedia) — https://en.wikipedia.org/wiki/Psychological_pricing

#### Patrick McKenzie (patio11)
- Ramit Sethi and Patrick McKenzie On Why Your Customers Would Be Happier If You Charged More — https://www.kalzumeus.com/2012/09/21/ramit-sethi-and-patrick-mckenzie-on-why-your-customers-would-be-happier-if-you-charged-more
- Marketing For People Who Would Rather Be Building Stuff (kalzumeus) — https://www.kalzumeus.com/2013/04/24/marketing-for-people-who-would-rather-be-building-stuff
- 7 Powerful Pricing Tips from Patrick McKenzie (Glance.fyi) — https://www.glance.fyi/blog/pricing-patio11
- The Black Arts of SaaS Pricing (Kalzumeus Training) — https://training.kalzumeus.com/newsletters/archive/saas_pricing
- Lessons from Patrick McKenzie (Antoine Buteau) — https://www.antoinebuteau.com/lessons-from-patrick-mckenzie
- Leveling Up – Patrick McKenzie (MicroConf 2015, YouTube) — https://www.youtube.com/watch?v=-Tg48MVnBeQ
- You Can Probably Stand To Charge More — https://www.kalzumeus.com/2006/08/14/you-can-probably-stand-to-charge-more
- From $30/mo to $75K Deals With SaaS Pricing Tiers (SaaSClub podcast) — https://saasclub.io/podcast/patrick-mckenzie-kalzumeus

#### Freemium Economics (Sean Ellis / Andrew Chen)
- The Cold Start Problem by Andrew Chen (summary) — https://andrewclark.co.uk/product-book-summaries/the-cold-start-problem
- The Cold Start Problem (full PDF, Andrew Chen) — https://andrewchen.com/wp-content/uploads/2022/01/ColdStartProb_9780062969743_AS0928_cc20_Final.pdf
- Growth Loops vs Funnels (TechPlato) — https://www.techplato.agency/blog/41-growth-loops-vs-funnels
- Startup Bootcamp Resources (HBS) — https://www.hbs.edu/entrepreneurship/mba/courses/startup-bootcamp/resources
- Growth Insights — Lessons from 100+ Growth Leaders — https://www.growthtalent.org/insights

#### Usage-Based Pricing
- The State of Usage-Based Pricing: 2nd Edition (OpenView) — https://openviewpartners.com/blog/state-of-usage-based-pricing
- The usage-based pricing reading list (M3ter) — https://www.m3ter.com/blog/the-usage-based-pricing-reading-list
- Usage-Based Pricing: The next evolution (OpenView) — https://openviewpartners.com/usage-based-pricing
- The state of usage-based pricing in SaaS (Growth Unhinged / Kyle Poyar) — https://www.growthunhinged.com/p/the-state-of-usage-based-pricing
- How to Scale With Usage Based Pricing (Pitch) — https://pitch.com/presentations/How-to-Scale-With-Usage-Based-Pricing-4xKtH6094zeW5uCNQT4sWPrR
- How Will Usage-Based Pricing Impact Your Finance Team? (Subscript / Kyle Poyar) — https://www.subscript.com/the-dive/usage-based-pricing
- SaaS companies quickly replacing subscriptions with usage-based pricing (CFO Dive) — https://www.cfodive.com/news/saas-companies-quickly-replacing-subscriptions-with-usage-based-pricing/609497
- Everything you need to know about SaaS Pricing with Kyle Poyar (YouTube) — https://www.youtube.com/watch?v=WQMQ4XPTJ_U

#### Pricing Anti-Patterns
- The worst B2B SaaS pricing errors (Software Pricing) — https://softwarepricing.com/blog/the-three-worst-b2b-saas-pricing-errors-and-how-to-avoid-them
- Why a Cost Plus Pricing Strategy is Still Important in SaaS (GetCheddar) — https://www.getcheddar.com/blog/cost-plus-pricing-for-saas
- 5 SaaS Pricing Mistakes to Avoid (Sixteen Ventures / Lincoln Murphy) — https://sixteenventures.com/pricing-mistakes
- The 5 SaaS Pricing Mistakes You're Probably Making (OpenView) — https://openviewpartners.com/blog/5-saas-pricing-mistakes
- The Pricing Mistakes that SaaS Start-ups Make (Medium) — https://medium.com/@davidhart.xyz/the-pricing-mistakes-that-saas-start-ups-make-e89e47526333
- The Hidden Cost of Bad Pricing: Lessons from Founders (Hypepotamus) — https://www.hypepotamus.com/we-asked-pricing-experts-costly-startup-pricing-mistakes
- 14 Pricing Mistakes to Avoid (NetSuite) — https://www.netsuite.com/portal/resource/articles/crm/pricing-mistakes.shtml
- 5 Common SaaS Pricing Mistakes and How to Avoid Them (Monetizely) — https://www.getmonetizely.com/articles/5-common-saas-pricing-mistakes-and-how-to-avoid-them

### COMPETITOR TEARDOWN

#### Hamilton Helmer 7 Powers
- 7 Powers & Playing to Win (Roger Martin, Medium) — https://rogermartin.medium.com/7-powers-playing-to-win-936cfdb94f86
- 7 Powers: The Foundations of Business Strategy (Tyastunggal) — https://tyastunggal.com/p/7-powers-the-foundations-of-business
- ELI5: Hamilton Helmer's 7 Powers (Reddit) — https://www.reddit.com/r/explainlikeimfive/comments/1dncm5e/eli5_hamilton_helmers_7_powers_of_business
- 7 Powers: The Foundations of Business Strategy (Amazon) — https://www.amazon.com/7-Powers-Foundations-Business-Strategy/dp/0998116319
- 7 Powers: Hamilton Helmer's Strategy Framework (Aydoo) — https://www.aydoo.services/en/articles/7-powers-hamilton-helmer
- Notes on 7 Powers (Jacob Wallenberg) — https://jacobwallenberg.com/posts/notes-on-7-powers
- Diving Deep Into Helmer's 7 Powers Using Company Examples (Quartr) — https://quartr.com/insights/edge/diving-deep-into-helmers-7-powers-using-company-examples
- Hamilton Helmer is the author of 7 Powers (Lenny Rachitsky, LinkedIn) — https://www.linkedin.com/posts/lennyrachitsky_hamilton-helmer-is-the-author-of-7-powers-activity-7192923019701358594-pI1h

#### Christensen Jobs To Be Done
- Jobs to Be Done Theory (Christensen Institute) — https://www.christenseninstitute.org/theory/jobs-to-be-done
- The Jobs to Be Done Framework & Real-World Examples (HBS Online) — https://online.hbs.edu/blog/post/jobs-to-be-done-examples
- Clayton Christensen, Jobs-to-be-Done & Competing (Thrv) — https://www.thrv.com/blog/clayton-christensen-jobs-to-be-done
- Jobs to Be Done (Strategyn / Tony Ulwick) — https://strategyn.com/jobs-to-be-done
- Clay Christensen's Jobs to Be Done framework (FullStory) — https://www.fullstory.com/blog/clayton-christensen-jobs-to-be-done-framework-product-development
- Jobs to Be Done: comparing different frameworks (GoPractice) — https://gopractice.io/product/jobs-to-be-done-the-theory-and-the-frameworks
- Six Steps to Put Christensen's JTBD Theory into Practice (Forbes) — https://www.forbes.com/sites/stephenwunker/2012/02/07/six-steps-to-put-christensens-jobs-to-be-done-theory-into-practice
- The Ultimate Guide to Jobs To Be Done Theory (Viima) — https://www.viima.com/blog/jobs-to-be-done

#### Stratechery Aggregation Theory
- Aggregation Theory (Stratechery / Ben Thompson) — https://stratechery.com/concept/aggregation-theory
- Aggregation Theory (main page) — https://stratechery.com/aggregation-theory
- Lessons from Ben Thompson (Antoine Buteau) — https://www.antoinebuteau.com/lessons-from-ben-thompson
- Stratechery: Aggregation Theory (TLDR Sec summary) — https://tldrsec.com/p/blog-stratechery-aggregation-theory
- Aggregator's AI Risk | Stratechery (YouTube) — https://www.youtube.com/watch?v=s8Q7uI2REI0
- Aggregation Theory (Stratechery 2015 essay) — https://stratechery.com/2015/aggregation-theory
- The Problem with Aggregation Theory (Stratechery) — https://stratechery.com/2019/the-problem-with-aggregation-theory-demand-at-scale-supplier-power-and-value

#### Competitor Hiring Patterns / LinkedIn Job Posting Intelligence
- Smarter Competitor Analysis with Job Data and Hiring (LinkedIn) — https://www.linkedin.com/pulse/your-competitors-telling-you-strategy-through-job-descriptions-qn5gf
- How to Analyze Comparable Job Postings (LinkedIn) — https://www.linkedin.com/top-content/recruitment-hr/job-posting-optimization/how-to-analyze-comparable-job-postings
- Competitor Talent Analysis (LinkedIn) — https://www.linkedin.com/top-content/recruitment-hr/headhunting-strategies/competitor-talent-analysis
- Track Hiring Trends & Growth Signals With LinkedIn Data (ScrapeBadger) — https://scrapebadger.com/blog/how-to-track-hiring-trends-and-company-growth-signals-with-linkedin-data
- Competitor Job Postings Reveal (LinkedIn post by Derek Keefe) — https://www.linkedin.com/posts/dkeefe_ever-wonder-what-company-job-postings-reveal-activity-7389617090774753280-0RTI
- Competitive Intelligence in Hiring (GetAura) — https://blog.getaura.ai/competitive-intelligence-in-hiring
- Competitor Job Posting Analysis & Hiring Intelligence (Foresight IQ) — https://www.foresightiq.co/sources/job-posting-intelligence
- Competitor Hiring Analysis: Decode Market Strategy (Intervue) — https://www.intervue.io/blog/competitor-hiring-analysis-how-job-postings-reveal-market-strategy

#### Competitor SEO & Traffic Analysis
- Data Accuracy of Similarweb, Ahrefs, and Semrush (Promodo) — https://www.promodo.com/blog/data-accuracy-at-similarweb-ahrefs-and-semrush
- Ahrefs vs Semrush vs Similarweb traffic estimates (Reddit r/bigseo) — https://www.reddit.com/r/bigseo/comments/os22b5/ahrefs_vs_semrush_vs_similarweb_traffic_estimates
- similarweb.com Website Traffic, Ranking, Analytics (Semrush) — https://www.semrush.com/website/similarweb.com/overview
- SEMrush vs Ahrefs vs Similarweb for Keyword Research (Ampifire) — https://ampifire.com/blog/semrush-vs-ahrefs-vs-similarweb-for-keyword-research-reviews-pricing
- Semrush vs Similarweb 2026 (StyleFactory) — https://www.stylefactoryproductions.com/blog/semrush-vs-similarweb
- Similarweb vs Semrush: Which Tool Wins? (Search Monitor) — https://www.thesearchmonitor.com/similarweb-vs-semrush
- Similarweb vs Semrush (Cybernews) — https://cybernews.com/marketing-tools/similarweb-vs-semrush
- Accuracy of Ahrefs, Semrush, and Similarweb (Collaborator) — https://collaborator.pro/blog/research-semrush-similarweb-ahrefs
- Best Competitor Website Analysis Tools in 2026 (PageCrawl) — https://pagecrawl.io/blog/competitor-website-analysis-tools-guide
- Best Competitor Analysis Tools (Shane Barker) — https://shanebarker.com/blog/competitor-analysis-tools
- Top 10 Best Competitor Software of 2026 (WorldMetrics) — https://worldmetrics.org/best/competitor-software

#### Innovator's Dilemma & Disruption Theory
- The Innovator's Dilemma (Wikipedia) — https://en.wikipedia.org/wiki/The_Innovator%27s_Dilemma
- The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail (HBS Faculty) — https://www.hbs.edu/faculty/Pages/item.aspx?num=46
- Disruptive Innovation Theory (Christensen Institute) — https://www.christenseninstitute.org/theory/disruptive-innovation
- Should It Be Called The Incumbent's Dilemma? (Consulting Accountant) — http://theconsultingaccountant.com/rethinking-the-innovators-dilemma-should-it-be-called-the-incumbents-dilemma
- The Innovator's Dilemma (SWE Magazine) — https://swe.org/magazine/innovators-dilemma
- Disruptive Innovation -- Clayton Christensen (Reddit r/TheMotte) — https://www.reddit.com/r/TheMotte/comments/c1hz3m/disruptive_innovation_clayton_christensen_and_the
- Why Great Companies Fail in The Face of Disruption (Scribd) — https://www.scribd.com/document/1006492346/4-Why-Great-Companies-Fail-in-the-Face-of-Disruption-the-Innovators-Dilemma
- Is Christensen's Theory of 'Disruptive Innovation' Still Relevant? (Tandfonline) — https://www.tandfonline.com/doi/full/10.1080/08956308.2023.2211898

#### Incumbent Reaction Prediction / Competitor Response Profile
- Competitive Response Case Interview: Complete Guide (Hacking the Case Interview) — https://www.hackingthecaseinterview.com/pages/competitive-response-case-interview
- Competitive response cases in consulting interviews (PrepLounge) — https://www.preplounge.com/en/case-interview-basics/competitive-response
- Competitor Response Profile Framework (Umbrex) — https://umbrex.com/resources/frameworks/marketing-frameworks/competitor-response-profile-framework
- New Product Announcement Signals and Incumbent Reactions (Wharton, 1995) — https://faculty.wharton.upenn.edu/wp-content/uploads/2012/06/New-Product-Announcement-Signals-and-Incumbent-Reactions.pdf
- Competitor Response Prediction (LinkedIn) — https://www.linkedin.com/top-content/business-strategy/competitive-advantage-analysis/competitor-response-prediction
- Competitor Response Profiles (Jerry Grzegorzek, Medium) — https://medium.com/@jerrygrzegorzek/competitor-response-profiles-8886579753c4
- How would you structure this case? Competitor launches new product (PrepLounge) — https://www.preplounge.com/consulting-forum/how-would-you-structure-this-case-competitor-launches-new-product-12158
- Competitive Response Playbook (Productboard) — https://www.productboard.com/product-management-prompts-library/competitive-response-playbook

#### Under-the-Radar Competitor Discovery
- The 4 Types of Competitors — and the 5th Nobody Tracks (Unkover) — https://unkover.com/blog/types-of-competitors
- How to Find Competitors You Don't Know About (5 Methods) (Cotera) — https://cotera.co/articles/how-to-find-competitors-you-dont-know-about
- How to Identify Your Competitors (ScaleMath) — https://scalemath.com/blog/identify-your-competitors
- How Do You Stack Up? Competitor Analysis (Boston Digital) — https://www.bostondigital.com/insights/how-do-you-stack-competitor-analysis
- Uncover Local Competitors Hiding in Plain Sight (Yext) — https://www.yext.com/blog/uncover-local-competitors-hiding-in-plain-sight-with-scout

#### Real Teardown Case Studies
- Stripe vs PayPal: A Tale of Two Sides of the Network (LinkedIn / Jas Shah) — https://www.linkedin.com/posts/jas-shah_%F0%9D%97%9B%F0%9D%97%BF%F0%9D%97%AE%F0%9D%97%B8%F0%9D%97%B6%F0%9D%97%BB%F0%9D%97%B4-%F0%9D%97%A6%F0%9D%98%81%F0%9D%97%BF%F0%9D%97%B6%F0%9D%97%BD%F0%9D%97%B2-%F0%9D%97%94%F0%9D%97%A1%F0%9D%98%83-activity-7483080786104213504-VIRj
- What Should Stripe Keep, Rebuild or Reinvent If It Bought PayPal (Jas Shah Substack) — https://jasshah.substack.com/p/stripe-paypal-acquition-deep-dive
- Stripe Teardown: How The $36B Payments Company Is (CB Insights) — https://www.cbinsights.com/research/report/stripe-teardown
- Stripe vs PayPal 2026 (Tech Insider) — https://tech-insider.org/stripe-vs-paypal-2026
- Stripe vs. PayPal: Which is best? (Zapier) — https://zapier.com/blog/stripe-vs-paypal
- Why PayPal makes sense for Stripe now (Tearsheet) — https://tearsheet.co/10-q/why-paypal-makes-sense-for-stripe-now
- Stripe vs PayPal: How to choose the right payment processor (Primer) — https://primer.io/blog/stripe-vs-paypal
- Stripe vs PayPal (Tridenstechnology) — https://tridenstechnology.com/stripe-vs-paypal
- 11 AI competitor analysis tools for product teams in 2026 (Figma) — https://www.figma.com/resource-library/ai-competitor-analysis-tools
- Product Strategy Lessons from Notion, Stripe & Google (YouTube) — https://www.youtube.com/watch?v=AMUe4wBvNpw
- Top 10 Competitive Analysis Templates for Product Designers (Notion) — https://www.notion.com/templates/collections/top-10-competitive-analysis-templates-for-product-designers
- Canva and Their Next BIG Positioning Move (Positioning Expert) — https://positioningexpert.com/blog/canva-positioning-owning-market
- 10-min Content Teardown: Figma (Superpath) — https://www.superpath.co/blog/10-min-content-teardown-figma
- How Figma's Strategy Weaponizes Design (Michael Goitein, Substack) — https://michaelgoitein.substack.com/p/how-figmas-strategy-weaponizes-design
- How Stripe, Google, Canva, Cloudflare and Higgsfield Are Actually Selling in 2026 (SaaStr) — https://www.saastr.com/how-stripe-google-canva-cloudflare-and-higgsfield-are-actually-selling-in-2026

---

**End of document.**
