# Business Fundamentals Reference — Legal, Tax, Accounting, Hiring, Compliance

A practical reference for the operational fundamentals of running a business.
This is not legal advice — consult professionals for your specific situation.
But this is the baseline knowledge every operator needs.

Synthesized from `/references/research-business-operations.md`.

## 1. Legal Entity Formation

<entity_formation>

### Decision Tree
```
Raising VC? → Delaware C-Corp (use Stripe Atlas, $500)
Profitable solo / small team? → LLC in your home state ($50-500)
Testing, no revenue yet? → Sole proprietorship is OK (upgrade to LLC before first $)
Already profitable LLC >$50K/yr? → Consider S-Corp election for tax savings
```

### Entity Types Compared

| Type | Cost | Liability protection | Tax | When to use |
|---|---|---|---|---|
| Sole prop | $0 | None | Pass-through | Testing only. Upgrade before revenue. |
| LLC | $50-500 | Yes | Pass-through | Default for solo/small business |
| S-Corp | $50-500 + accounting | Yes | Pass-through + salary requirement | LLC profitable >$50K/yr |
| C-Corp | $500-2000 | Yes | Double taxation | Raising VC, planning to scale big |
| Delaware C-Corp | $500 (Stripe Atlas) | Yes | Double taxation | VC-backed startups (standard) |

### Formation Steps (LLC)
1. Choose state (home state for simplicity; Delaware for VC ambition)
2. File Articles of Organization ($50-500, 1-2 weeks)
3. Get EIN from IRS (free, instant, online)
4. Open business bank account (need EIN + Articles)
5. Create Operating Agreement (template from Clerky or NOLO)
6. File beneficial ownership report (new 2024 requirement, free)

### Common Mistakes
- **Don't form a C-Corp unless raising VC** — double taxation eats 20%+ of profit
- **Don't form in Delaware if you're a solo LLC** — pay franchise tax + registered agent for no benefit
- **Don't skip the operating agreement** — without it, default state rules apply (usually bad)
- **Don't commingle personal/business finances** — pierces the corporate veil, loses liability protection

</entity_formation>

## 2. Co-Founder Agreements

<cofounder_agreements>
If you have a co-founder, you MUST have a written agreement. Friendship is not
a substitute.

### Required Elements
- **Equity split**: Document the reasoning. 50/50 is rarely right; consider who brought the idea, who's full-time, who put in capital.
- **Vesting**: 4-year vest, 1-year cliff. Standard. Non-negotiable. Prevents "co-founder leaves after 3 months, keeps 50%" disaster.
- **IP assignment**: All IP assigned to company. Prevents "I built it on weekends, it's mine" disputes.
- **Roles and decision rights**: Who decides what. Be specific. "Product decisions: [name]. Hiring decisions: [name]."
- **Exit clauses**: What happens if someone leaves. Buyback terms. Good leaver / bad leaver.
- **Dispute resolution**: Mediation first, then arbitration. Avoid litigation.

### Tools
- Clerky: incorporation + founder documents ($200-500)
- Stripe Atlas: incorporation + founder documents ($500)
- CoFoundersLab: agreement templates (free)

### Common Mistakes
- "We're friends, we'll figure it out" — friendship ends, dispute starts, no agreement = lawsuit
- 50/50 split with no tiebreaker — decision paralysis when you disagree
- No vesting — co-founder leaves after 3 months, keeps 50%, kills company
- Skipping IP assignment — co-founder claims they own the code
</cofounder_agreements>

## 3. Accounting Basics

<accounting>
If you can't read your financial statements, you can't run a business.

### The 3 Statements You Must Understand

#### P&L (Profit & Loss)
- **Revenue** (top line)
- **COGS** (cost of goods sold — direct costs of delivering product)
- **Gross profit** = Revenue - COGS
- **Gross margin** = Gross profit / Revenue (SaaS target: >70%)
- **Operating expenses** (Sales & marketing, R&D, G&A)
- **Operating income** = Gross profit - OpEx
- **Net income** = Operating income - taxes - interest

#### Balance Sheet
- **Assets** (cash, receivables, IP, equipment)
- **Liabilities** (payables, debt, deferred revenue)
- **Equity** = Assets - Liabilities
- Snapshot at a moment in time. Should balance (hence the name).

#### Cash Flow Statement
- **Operating cash flow** (cash from running the business)
- **Investing cash flow** (cash from buying/selling assets)
- **Financing cash flow** (cash from raising/paying debt/equity)
- **Net change in cash**
- THE most important for early-stage. Profit ≠ Cash. Many profitable businesses go bankrupt from poor cash management.

### Bookkeeping
- **Software**: QuickBooks ($30-200/mo), Xero ($13-70/mo), Wave (free)
- **Process**: Connect bank accounts, categorize transactions monthly, reconcile
- **Monthly close**: 2-4 hours/month. Generate P&L, balance sheet, cash flow.
- **Annual CPA review**: $1-3K. Catches mistakes before IRS does.

### Tax Reserves
- Set aside **30-40% of profit** for taxes from day 1
- Don't touch this money. It's not yours.
- Quarterly estimated taxes (April 15, June 15, September 15, January 15)
- Federal: 21% (C-Corp) or pass-through rate (LLC/S-Corp)
- State: 0-12% depending on state
- Sales tax: separate reserve if applicable

### Common Mistakes
- DIY accounting to save $200/mo — costs $5-20K in penalties later
- Not tracking from day 1 — reconstructing 6 months of transactions is hell
- Confusing profit with cash — profitable businesses go bankrupt from poor cash flow
- Not setting aside tax reserves — tax surprise = business death
</accounting>

## 4. Tax Obligations

<tax>
### Federal Income Tax
- C-Corp: 21% flat
- LLC/S-Corp: pass-through to personal return at individual rates
- S-Corp: must pay "reasonable salary" subject to payroll tax; rest is distributions (no payroll tax)

### State Income Tax
- Varies 0% (Wyoming, Nevada, Texas) to 12% (Iowa)
- Some states have franchise tax (Delaware: $300/yr minimum)
- Nexus: if you have employees or property in a state, you may owe tax there

### Sales Tax
- **Post-Wayfair (2018)**: states can require collection based on "economic nexus"
- Threshold: typically >$100K sales OR >200 transactions in a state
- Use TaxJar ($19-300/mo) or Avalara to track and remit
- Marketplace facilitator: Amazon/Shopify collect on your behalf for marketplace sales
- Direct sales: YOU collect and remit

### Payroll Tax
- Employer: 7.65% (6.2% Social Security + 1.45% Medicare)
- Employee: 7.65% (same breakdown)
- FUTA: 0.6% on first $7K
- SUTA: varies by state, 1-6% on first $7K-50K
- Use Gusto ($39-149/mo) or Rippling to handle

### International
- VAT (EU): 19-27% depending on country. Register via MOSS or local tax authority.
- GST (Australia, India, etc.): similar to VAT
- Withholding tax: foreign customers may withhold tax on payments to you

### Common Mistakes
- Ignoring sales tax for 2 years → $50K+ in back taxes + penalties
- Treating contractors as employees → IRS reclassification = back taxes + penalties
- Not paying quarterly estimates → underpayment penalties
- Not understanding nexus → owing tax in states you didn't know about
</tax>

## 5. Hiring

<hiring>
### Employee vs Contractor (1099 vs W-2)

#### IRS Test (3 categories)
1. **Behavioral control**: Do you control how/when/where they work? → W-2
2. **Financial control**: Do they have their own business, multiple clients, set their own rates? → 1099
3. **Relationship type**: Written contract, benefits, permanence → factors toward W-2

**Rule of thumb**: If they work only for you, on your schedule, with your tools, they're W-2. Calling them 1099 doesn't make it so.

#### Misclassification Risk
- IRS reclassification = back taxes + penalties + interest
- State labor departments also enforce
- Risk increases with audit (more likely if you file 1099s for full-time workers)

### First 10 Hires (Software Business)
1. Senior engineer (you can't ship fast enough alone)
2. Customer success / support (you can't do support + build)
3. Second engineer (specialization: frontend/backend)
4. Marketing/growth (you've built, now distribute)
5. Sales (if B2B, once PMF signal)
6-10: Engineers (product velocity)

### First 10 Hires (Services Business)
1. First practitioner (you can't serve all clients alone)
2. Operations/PM (you can't deliver + manage)
3-5: More practitioners
6: Sales (you've proven model, now scale)
7-10: More practitioners + ops

### Compensation Benchmarks

| Role | Seed stage | Series A | Series B+ |
|---|---|---|---|
| Senior engineer | $120-180K + 0.5-1.5% equity | $150-220K + 0.25-0.75% | $180-280K + 0.1-0.4% |
| Sales (AE) | $80-120K base + $80-120K OTE | $120-180K base + $120-180K OTE | $150-250K base + $150-250K OTE |
| Marketing | $80-140K + 0.25-0.75% | $120-200K + 0.1-0.4% | $150-300K + 0.05-0.2% |
| Customer success | $60-100K | $80-130K | $100-180K |

**Equity data**: Carta's 8,000+ grant analysis. First hire median: 1.5%.

### Hiring Process
1. Write a job description that doesn't suck (specific responsibilities, must-have vs nice-to-have)
2. Source: referrals > LinkedIn > AngelList > recruiters (last resort, 20-30% fee)
3. Phone screen (30 min, cultural + basic fit)
4. Work sample (real task, paid, 2-4 hours)
5. Onsite (3-5 interviews, include peers)
6. Reference checks (call 3-5 references, ask "would you hire them again?")
7. Offer (24-48 hour expiry, written)

### Common Mistakes
- Hiring too fast (desperation) — bad hire costs 6-12 months of runway
- Hiring too slow (perfectionism) — you lose good candidates to faster movers
- Skipping reference checks — "their resume looked great"
- Hiring for "culture fit" (= people like me) instead of "culture add" (= what's missing)
- Not firing fast enough — bad hire poisons team, costs more to keep than to fire
</hiring>

## 6. Insurance

<insurance>
### Types

| Insurance | Cost (early-stage) | When required |
|---|---|---|
| General liability | $40-80/mo | Most B2B contracts require |
| Professional liability (E&O) | $60-150/mo | Services businesses, B2B contracts |
| Workers comp | $30-200/mo per employee | Required once you have W-2 employees |
| Cyber liability | $100-300/mo | SaaS handling customer data, enterprise contracts |
| D&O (directors & officers) | $1-3K/yr | When you have a board or raise VC |
| Key person | $50-200/mo | When a key person's death would kill the business |

### Don't Skip
- General liability + professional liability (if services)
- Workers comp (when you have W-2)
- Cyber liability (if handling customer data for enterprise)

### Don't Bother (until specific trigger)
- D&O (until VC raises or board)
- Key person (until you have investors who'd care)
- Property insurance (until you have physical assets worth insuring)
</insurance>

## 7. Compliance

<compliance>
### GDPR (EU customers)
- **Privacy policy**: Required. Clear, plain language.
- **Cookie consent**: Required for non-essential cookies.
- **Data Subject Rights**: Access, delete, export. Respond in 30 days.
- **DPA**: Required for B2B data processing.
- **Fines**: Up to 4% of global revenue. Real enforcement.

### CCPA (California customers)
- Privacy policy required
- "Do Not Sell My Personal Information" link (if selling data, broadly defined)
- Opt-out requests honored in 15 days

### HIPAA (health data)
- **Don't touch health data without compliance review**
- BAA required with any vendor touching PHI
- Specialized hosting (AWS/GCP HIPAA-eligible)
- Fines: $100-$50K per violation

### SOC 2 (enterprise SaaS)
- Type 1: point-in-time audit, $15-30K, 2-3 months
- Type 2: continuous audit, $30-50K, 6-12 months
- Use Vanta ($7-10K/yr) or Drata — automates 80%
- Required for: enterprise sales, regulated industries

### PCI-DSS (credit card data)
- If you use Stripe/Braintree, you're SAQ-A (simplest)
- If you handle card data directly, full PCI-DSS compliance required
- Don't handle card data directly — use Stripe

### Sales Tax (US)
- Post-Wayfair (2018): economic nexus rules
- Collect in states where you have >$100K sales or >200 transactions
- Use TaxJar or Avalara

### Common Compliance Mistakes
- Ignoring GDPR because "we're US-only" — applies if you have EU customers
- Skipping SOC 2 until enterprise deal requires it — 6-12 month lag kills deals
- Treating contractors as employees — IRS reclassification
- Not collecting sales tax — back taxes + penalties + interest
</compliance>

## 8. IP Protection

<ip>
### Trademarks
- File for company name and product name
- USPTO TEK Plus: $250/class
- Use an attorney: $500-1500 total
- File within 6 months of launch
- International: Madrid Protocol ($1000+ per country)

### Copyrights
- Automatic on creation (in US)
- Register only if you'll sue ($35-55)
- Important for content businesses (courses, books, media)

### Patents
- $10-30K, 2-4 years
- Software patents: rarely worth it (most are obvious, hard to enforce)
- Defensive only: prevents competitors from patenting the same thing
- Don't bother for software unless you have a true invention

### Trade Secrets
- NDA + access control = free
- Works for: algorithms, customer lists, processes, formulas
- Risk: once disclosed, can't be un-disclosed

### Open Source Considerations
- If you use GPL/AGPL code, your product may need to be open-sourced
- Use MIT/Apache licensed code liberally
- Have an open-source license policy
</ip>

## 9. Quick Setup Checklist

<checklist>
For a new solo business (first 2 weeks):

- [ ] Form LLC ($50-500, 1-2 weeks)
- [ ] Get EIN (free, instant)
- [ ] Open business bank account (Mercury, Brex, or local credit union)
- [ ] Open business savings for tax reserve
- [ ] Set up Stripe for payments
- [ ] Set up bookkeeping (Wave free, or QuickBooks $30+/mo)
- [ ] Generate privacy policy (Termly, iubenda, $10-50/mo)
- [ ] Generate TOS (same tools)
- [ ] Set aside 30-40% of first revenue for taxes
- [ ] Get general liability insurance ($40-80/mo, NEXT or Hiscox)

For first hire (when ready):
- [ ] Set up payroll (Gusto $39-149/mo)
- [ ] Get workers comp insurance
- [ ] Write employment agreement (template from Clerky)
- [ ] Set up IP assignment
- [ ] Set up benefits (health insurance, 401k)

For enterprise deals (when needed):
- [ ] Start SOC 2 process (Vanta/Drata, 6-12 months)
- [ ] Get cyber liability insurance
- [ ] Engage startup lawyer for MSA negotiation ($5-15K)
- [ ] Generate DPA
</checklist>

## Source

Synthesized from `/references/research-business-operations.md` which contains
detailed operational stack, benchmarks, and 125 sources.
