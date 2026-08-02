# Lens 15: Capital Allocation & Finance — How Do I Fund and Allocate Capital to This?

<lens>
<core_question>
How should this opportunity be funded (bootstrapped, debt, equity, revenue-based),
and once funded, how do I allocate capital to maximize compounding returns?
</core_question>

<when_to_use>
- User asks "how do I fund this?" or "should I raise money?"
- User is considering bootstrapping vs raising VC
- User has capital and wants to allocate it across opportunities
- User is evaluating fundraising strategy (seed, Series A, debt, revenue-based)
- User wants to understand financial engineering (convertible notes, SAFEs, term sheets)
- For ongoing businesses doing capital allocation review
</when_to_use>

<when_not_to_use>
- Pre-opportunity (nothing to fund)
- Zero-capital validation experiments (Lens 08 covers survival)
- Personal finance (out of scope — see negative_trigger)
</when_not_to_use>
</lens>

## Core Philosophy

<principle>
Capital allocation is the CEO's primary job (Buffett, Bezos). Everything else
is delegation. Most founders obsess over product and ignore capital allocation
— and it kills them.

Two principles govern this lens:
1. **Match funding to opportunity** (Buffett): Don't raise VC for a lifestyle
   business. Don't bootstrap a moonshot. The funding mechanism must fit the
   opportunity's exponential tier (Lens 07).
2. **Allocate like an owner** (Buffett/Munger): Every dollar deployed must
   earn above its cost of capital. Reinvest only when ROIC > cost of capital.
   Otherwise, distribute.
</principle>

## Part 1: Funding Strategy

<funding_strategy>

### The Funding Decision Tree

```
What is the exponential tier (Lens 07)?
├── Tier 1 (Moonshot, 100x+ potential)
│   ├── Network/credentials for VC? → Raise VC (Series Seed/A)
│   └── No VC network? → Bootstrap to $1M ARR, then raise Series A
├── Tier 2 (Scalable Linear, 10-50x potential)
│   ├── Capital-efficient (SaaS, services)? → Bootstrap
│   ├── Needs growth capital? → Revenue-based financing (Pipe, Capchase)
│   └── Proven model, scaling? → Series A if VC accelerates
└── Tier 3 (Linear, lifestyle)
    └── Bootstrap. Debt for specific assets. No VC.
```

### Funding Options Compared

| Option | Cost | Control | Best for | Worst for |
|---|---|---|---|---|
| **Bootstrapping** | Time | Full | Tier 2-3, services, niche SaaS | Moonshots requiring scale |
| **Friends & Family** | Low ($25-250K) | High | Pre-revenue validation | If relationships can survive loss |
| **Angel** | Equity 5-15% | High | Seed stage, $250K-2M | If angels can't add value |
| **VC Seed** | Equity 15-25% | Medium | Tier 1, scaling plays | Tier 2-3, lifestyle |
| **VC Series A+** | Equity 20-40% | Lower | Proven PMF, scaling | Pre-PMF, unproven model |
| **Debt (bank loan)** | Interest 6-12% | Full | Asset purchase, working capital | Startups without collateral |
| **Revenue-based** | % of revenue (2-5x) | Full | SaaS with >$1M ARR | Pre-revenue, volatile revenue |
| **Crowdfunding** | Equity or rewards | Medium | Consumer products, community | B2B, niche |
| **Grants** | Free | Full | R&D, deep tech | Most businesses (not eligible) |

### When to raise VC (and when NOT to)

#### Raise VC when:
- Tier 1 opportunity (Lens 07) — moonshot potential
- Winner-take-all market (network effects, scale advantages)
- PMF confirmed, scaling requires capital
- You have access to top-tier VCs (not just any VC)
- You're willing to give up control and aim for $1B+ outcome

#### Do NOT raise VC when:
- Tier 2-3 opportunity (you'll be pushed to grow unsustainably)
- Lifestyle business (you don't need to be a unicorn)
- PMF not confirmed (raising pre-PMF = premature scaling, 74% failure)
- You value control over growth speed
- You're in a niche market (VCs won't fund small markets)
- You can't raise from top-tier (mediocre VCs add negative value)

### Term Sheet Basics

#### Convertible Note (debt that converts to equity)
- **Discount**: 20-30% off next round price
- **Cap**: Maximum valuation at conversion (protects early investors)
- **Interest**: 2-8% (usually accrues, paid in equity)
- **Maturity**: 12-24 months (if no round, converts at terms)
- **Pros**: Fast, simple, defers valuation
- **Cons**: Cap can hurt founders if round is at lower valuation

#### SAFE (Simple Agreement for Future Equity)
- YC's invention — like convertible note but not debt
- **Discount** and/or **Cap** (same as note)
- **No interest, no maturity** (cleaner than note)
- **Pros**: Simplest, fastest, founder-friendly
- **Cons**: Can stack up — multiple SAFEs at different caps gets messy

#### Priced equity (Series A+)
- **Valuation**: Pre-money + investment = post-money
- **Liquidation preference**: 1x non-participating is standard. >1x or
  participating is investor-friendly, push back.
- **Pro-rata**: Right to invest in future rounds. Standard.
- **Board composition**: 1 founder, 1 investor, 1 independent is standard.
  Don't give investors board control.
- **Vesting**: You'll re-vest your founder shares (4yr, 1yr cliff). Standard.
- **Anti-dilution**: Broad-based weighted average is standard. Full ratchet
  is investor-friendly, push back.
- **Information rights**: Standard. Don't fight.
- **Liquidation > 1x or participating preferred**: Push back hard. Caps your
  upside while protecting their downside.

#### The term sheet math
At Series A:
- Pre-money: $10M
- Raise: $3M
- Post-money: $13M
- Investors own: $3M / $13M = 23%

**Watch the "option pool shuffle"** — VCs often require 10-20% option pool
created pre-money. This dilutes only founders, not investors. Negotiate
post-money pool if possible.

### Bootstrapping Math

If you bootstrap:
- Time to first $: 1-6 months (faster than raising)
- Growth rate: slower (no capital for paid acquisition)
- Risk: lower (no investor pressure, no dilution)
- Outcome: $1-10M business (vs $100M+ with VC, but with 10x failure rate)

**The bootstrap vs VC math**:
- 100 bootstrappers: 80 build $1-5M businesses (lifestyle), 15 build $5-50M
  (great), 5 build $50M+ (rare)
- 100 VC-funded: 60 fail, 30 build $10-100M, 8 build $100M-1B, 2 build $1B+
  (power law)

Which path? Depends on your risk tolerance, ambition, and the opportunity's
exponential tier.
</funding_strategy>

## Part 2: Capital Allocation (Buffett/Munger Style)

<capital_allocation>

### The Capital Allocation Framework

Once you have capital (revenue, raised, or personal), how do you allocate it?

**Buffett's rule**: Reinvest only when ROIC > cost of capital. Otherwise,
distribute (or in startup context, hold as runway).

#### The 5 capital allocation options:

1. **Reinvest in the core business** (R&D, sales, marketing)
   - Allocate when: marginal ROIC > 25% (every $1 invested returns >$1.25/yr)
   - Don't allocate when: marginal ROIC < cost of capital (15-20% for startups)

2. **Acquire customers** (paid acquisition, sales hires)
   - Allocate when: CAC payback <12 months, LTV:CAC >3:1
   - Don't allocate when: CAC > LTV (you're buying unprofitable growth)

3. **Build assets** (product, brand, audience, data)
   - Allocate when: asset compounds over time (audience grows, brand strengthens)
   - Don't allocate when: asset depreciates (one-off content, features nobody uses)

4. **Acquire companies/competitors**
   - Allocate when: acquisition adds capability or market you can't build
   - Don't allocate when: acquiring for revenue (most acquisitions destroy value)

5. **Hold as cash/runway**
   - Allocate when: no option above meets hurdle rate
   - Don't allocate when: you're hoarding out of fear, not strategy

### The Hurdle Rate

Every capital allocation decision must clear a hurdle rate:

- **Startup hurdle**: 30-50% (cost of capital is high — VC expects 10x returns)
- **Bootstrapper hurdle**: 20-30% (cost of capital is opportunity cost)
- **Mature business hurdle**: 10-15% (WACC + risk premium)

If a proposed investment (new feature, new hire, new channel) doesn't clear
the hurdle, don't make it. Hold the capital.

### Capital Allocation Anti-Patterns

#### 1. Growth at all costs
"We need to grow 100% YoY regardless of unit economics."
**Why fails**: CAC > LTV. Every new customer destroys value. Burn rate
unsustainable. WeWork, MoviePass, Blue Apron.

**Fix**: Grow only when LTV:CAC >3:1 and CAC payback <12 months.

#### 2. Hoarding cash
"We're profitable but not reinvesting. Just holding cash."
**Why fails**: Cash earns ~5% in bank. Cost of capital is 20-50%. You're
losing 15-45% per year on idle capital.

**Fix**: Reinvest in the core, acquire customers profitably, or distribute
to founders.

#### 3. Over-hiring
"We raised $20M, let's hire 30 people."
**Why fails**: Productivity per employee drops. Culture breaks. Runway
burns faster. Premature scaling (74% of failures).

**Fix**: Hire 1-2/month max. Each hire must have clear ROIC justification.

#### 4. Acquiring for revenue
"We'll acquire [company] to add $5M ARR."
**Why fails**: Most acquisitions destroy value (McKinsey: 70% fail). Cultural
integration, customer churn, talent flight.

**Fix**: Acquire for capability (talent, IP, market position), not revenue.

#### 5. Premature paid acquisition
"Let's pour $50K/month into Google Ads."
**Why fails**: Pre-PMF, CAC is catastrophic. Conversion rate low. Burn cash
on unprofitable customers.

**Fix**: Confirm PMF (Sean Ellis ≥40%, retention flattens) before scaling
paid acquisition.

### The Monthly Capital Allocation Review

Buffett reviews capital allocation weekly. Bezos reviews Amazon's reinvestment
weekly. You should review monthly:

1. **What's our runway?** (cash / monthly burn)
2. **What's our ROIC on the core business?** (gross margin / total invested)
3. **What's our marginal ROIC?** (next $100K invested — where does it go?)
4. **Are we reinvesting above hurdle?** (if not, why are we holding cash?)
5. **Are we over-investing in any category?** (hiring, paid, R&D)
6. **What would we cut if runway dropped to 6 months?** (pre-define cuts)

This review catches capital allocation drift before it becomes fatal.
</capital_allocation>

## Part 3: Financial Engineering for Founders

<financial_engineering>

### The 3 Financial Statements You Must Understand

#### P&L (Profit & Loss)
- Revenue - COGS = Gross Profit
- Gross Profit - OpEx (S&M, R&D, G&A) = Operating Income
- Operating Income - Interest - Taxes = Net Income

**For SaaS**:
- Gross margin target: >70% (hosting + support costs)
- S&M as % of revenue: 30-50% (scaling), 20-30% (mature)
- R&D as % of revenue: 20-40% (scaling), 15-25% (mature)
- G&A as % of revenue: 10-20% (scaling), 5-15% (mature)

#### Balance Sheet
- Assets = Liabilities + Equity
- **Assets**: cash, receivables, IP, equipment
- **Liabilities**: payables, deferred revenue, debt
- **Equity**: founder + investor shares

**Watch**: Deferred revenue (cash collected but not yet earned). It's a
liability, not revenue. High deferred revenue = healthy cash flow but
obligation to deliver.

#### Cash Flow Statement
- **Operating**: cash from running the business (P&L + non-cash items ± working capital)
- **Investing**: cash from buying/selling assets (equipment, acquisitions)
- **Financing**: cash from raising/paying debt/equity

**Critical**: Profit ≠ Cash. Many profitable businesses go bankrupt from
poor cash flow. Track cash flow weekly in early stage.

### SaaS Metrics That Matter

| Metric | Formula | Benchmark |
|---|---|---|
| MRR/ARR | Monthly/Annual Recurring Revenue | Track growth rate |
| NRR | (Starting MRR + expansion - churn - downgrade) / Starting MRR | ≥110% enterprise |
| GRR | (Starting MRR - churn - downgrade) / Starting MRR | ≥90% |
| LTV | ARPU × gross margin × (1 / churn rate) | ≥3x CAC |
| CAC | Total S&M spend / new customers acquired | <12mo payback |
| LTV:CAC | LTV / CAC | ≥3:1 |
| CAC payback | CAC / (monthly gross margin per customer) | <12 months |
| Magic Number | (Quarterly ARR growth × 4) / prior quarter S&M | ≥0.5 good, ≥1.0 excellent |
| Rule of 40 | Growth rate % + profit margin % | ≥40 |
| Burn multiple | Net burn / net new ARR | <1.5 good, <1.0 excellent |
| Gross margin | (Revenue - COGS) / Revenue | ≥70% SaaS |
| NPS | % promoters - % detractors | ≥40 |

### Runway Management

**Runway = Cash / Monthly Burn**

- **18+ months**: Healthy. Can absorb setbacks.
- **12-18 months**: OK. Plan next raise 6 months out.
- **6-12 months**: Caution. Cut non-essential. Plan raise immediately.
- **<6 months**: Emergency. Cut to skeleton. Raise or sell.

**The "always be raising" principle**: Even with 18 months runway, have
relationships with 5+ investors. You raise on your timeline, not when
desperate.

### Unit Economics Deep Dive

**Per-customer economics**:
```
Revenue per customer (ARPU): $X
- COGS per customer: $Y (hosting, support)
= Gross margin per customer: $X - Y
- CAC: $Z
= Net contribution per customer: $X - Y - Z

Over customer lifetime (LTV):
Gross margin per month × (1 / monthly churn) = LTV

If LTV > 3x CAC: healthy
If LTV < 3x CAC: broken — fix pricing (Lens 09) or CAC (Lens 13)
```

**Cohort analysis**: Track LTV by cohort (when they signed up). If newer
cohorts have lower LTV, your business is degrading. Investigate.
</financial_engineering>

## Part 4: Practitioner Wisdom

<practitioner_principles>

### 1. "The first $100K is the hardest." — Buffett
Compounding is the most powerful force, but it requires starting. Get to
$100K however you can. After that, compounding does the work.

### 2. "Be fearful when others are greedy, greedy when others are fearful." — Buffett
Counter-cyclical capital allocation. When VCs are throwing money at AI,
be cautious. When VC funding dries up, that's when the best deals are made.

### 3. "Our favorite holding period is forever." — Buffett
Build assets that compound, not trades that flip. The tax efficiency and
compounding of long-term holdings beats short-term gains.

### 4. "Reinvest only when ROIC > cost of capital." — Buffett/Munger
Capital allocation discipline. Don't reinvest just because you have cash.
Reinvest when the marginal dollar earns above its cost.

### 5. "The investor who says 'this time is different,' when in fact 95% of the time it isn't, has uttered among the four most costly words in annals of investment." — Templeton
Beware narrative-driven capital allocation. If your thesis requires "this
time is different," it probably isn't.

### 6. "Diversification is protection against ignorance. It makes little sense if you know what you're doing." — Buffett
For operators (not investors), focus beats diversification. One great
business compounds more than 5 mediocre ones.

### 7. "Capital allocation is the CEO's primary job." — Buffett/Bezos
Everything else is delegation. If you're not spending 20%+ of your time on
capital allocation, you're abdicating your primary role.

### 8. "The companies that fail are the ones that run out of cash." — Every investor ever
Profitable companies go bankrupt from poor cash management. Track cash
weekly. Plan runway 12+ months ahead.

### 9. "Don't raise money unless you have to. And if you have to, raise more than you need." — Founder wisdom
Raising money has high cost (dilution, control, pressure). Don't raise
unless necessary. But when you do raise, raise enough to never have to
raise again (18+ months runway minimum).

### 10. "The best capital allocation decision is often 'no.'" — Munger
Saying no to mediocre investments preserves capital for great ones. Most
"opportunities" don't clear the hurdle rate. Pass.
</practitioner_principles>

## Decision Protocol

<decision_protocol>
### Exact Question
"How should this be funded, and how do I allocate capital to maximize returns?"

### Data Required
- Exponential tier (Lens 07)
- Capital requirement (Lens 08)
- Pricing and unit economics (Lens 09)
- Growth stage (Lens 13)
- Current financials (revenue, gross margin, burn, runway)

### Confidence Threshold
- **Deploy (commit to funding strategy)**: ≥80% confidence, tier identified, unit economics understood
- **Flag (proceed with caution)**: 60-80%, some metrics unclear
- **Discard**: <60%, can't determine funding fit or unit economics broken

### Conflict Resolution
- Lens 15 (Finance) + Lens 07 (Exponential): Tier 1 → VC fit. Tier 2-3 → bootstrap or revenue-based.
- Lens 15 + Lens 08 (Risk of Ruin): Risk of ruin wins. Don't take funding that risks ruin.
- Lens 15 + Lens 13 (Growth): Don't raise growth capital before PMF. Premature scaling kills.
</decision_protocol>

## Output

<output>
```
### Capital Allocation & Finance Analysis

#### Funding Strategy
- Recommended: [bootstrap / angel / VC seed / VC Series A / debt / revenue-based]
- Rationale: [based on tier, stage, unit economics]
- Dilution if raising: [%]

#### Unit Economics
- ARPU: $[X]
- Gross margin: [%]
- CAC: $[Y]
- LTV: $[Z]
- LTV:CAC: [ratio]
- CAC payback: [N months]
- Verdict: [healthy / broken / fixable]

#### Runway
- Current cash: $[X]
- Monthly burn: $[Y]
- Runway: [N months]
- Status: [healthy / caution / emergency]

#### Capital Allocation Plan
- Reinvest in core: [% of available capital, expected ROIC]
- Acquire customers: [% of available capital, expected CAC:LTV]
- Build assets: [% of available capital, asset type]
- Hold as runway: [% of available capital]
- Hurdle rate: [%]

#### Term Sheet Review (if raising)
- Instrument: [SAFE / convertible note / priced equity]
- Valuation/cap: $[X]
- Dilution: [%]
- Liquidation preference: [1x non-participating / other]
- Board: [composition]
- Red flags: [any unfavorable terms]

#### Financial Health Verdict
- Unit economics: [healthy / broken]
- Runway: [healthy / caution / emergency]
- Capital allocation: [disciplined / drifting]
- Overall: [PROCEED / FIX FIRST / EMERGENCY]
```
</output>
