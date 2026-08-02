# Lens 12: Business Operations — What's Actually Needed to Run This?

<lens>
<core_question>
Beyond the opportunity itself, what operational infrastructure is required to
actually run this business — legal, financial, team, technology, compliance —
and which pieces are blocking vs deferrable?
</core_question>

<when_to_use>
- After an opportunity passes Lens 06 (anti-bias) and the user is ready to act
- When user says "what do I need to start?" or "what am I missing?"
- During execution sprint planning (Lens 11 → execution sprints)
- When transitioning from validation to commitment
- For existing businesses doing operational review
</when_to_use>

<when_not_to_use>
- Pre-opportunity (nothing to operate yet)
- Pure market analysis (use Lens 01-03)
- The user is just exploring, not committing
</when_not_to_use>
</lens>

## Core Philosophy

<principle>
Most business frameworks focus on finding opportunities and ignore the
operational reality of running them. A great opportunity fails in execution
because the operator didn't set up the legal entity, didn't understand tax
obligations, didn't have the right contracts, didn't hire correctly, didn't
comply with regulations.

This lens is the "what does Monday morning look like?" lens. It maps the
operational stack and identifies which pieces are blocking (must do before
starting) vs deferrable (can do later).

The rule: don't let operational ignorance kill a good opportunity. But also
don't let operational over-engineering delay action. Set up the minimum
viable operations, then iterate.
</principle>

## The Operational Stack

<operational_stack>

### Layer 1: Legal Foundation (BLOCKING for revenue)

<legal_foundation>
#### Entity formation
- **Sole proprietorship**: default if you do nothing. No protection. OK for testing, NOT OK for revenue.
- **LLC**: $50-500 to form, 1-2 weeks. Pass-through tax, liability protection. **Default recommendation for solo operators.**
- **S-Corp election**: LLC can elect S-Corp status for tax savings once profit >$50K/yr. Costs more in accounting.
- **C-Corp**: Required if raising VC. Double taxation. Don't form unless raising institutional capital.
- **Delaware C-Corp**: Standard for VC-backed startups. Stripe Atlas incorporates in DE for $500.

**Decision tree**:
```
Raising VC? → Delaware C-Corp (Stripe Atlas $500)
Profitable solo / small team? → LLC in your home state
Testing, no revenue yet? → Sole prop is fine (upgrade to LLC before first $)
```

#### Co-founder agreements (if applicable)
- **Vesting**: 4-year vest, 1-year cliff. Standard. Non-negotiable.
- **IP assignment**: All IP assigned to company. Prevents "I built it on weekends, it's mine" disputes.
- **Roles and decision rights**: Who decides what. Specific.
- **Exit clauses**: What happens if someone leaves. Buyback terms.

**Common mistake**: Skipping the operating agreement because "we're friends."
Friendship ends, dispute starts, no agreement = lawsuit. Use Clerky or Stripe Atlas templates.

#### Contracts
- **Customer contracts**: B2B needs MSA (master services agreement). B2C needs TOS.
- **Privacy policy**: Required by GDPR/CCPA even if you don't collect "sensitive" data.
- **NDA**: Rarely needed for early-stage. Don't over-lawyer.
- **Contractor agreements**: 1099s need explicit IP assignment or they own their work.

#### IP protection
- **Trademarks**: File for company name and product name. $250-1000/each via USPTO TEK Plus.
- **Copyrights**: Automatic on creation. Register only if you'll sue.
- **Patents**: $10-30K, 2-4 years. Don't bother for software unless you have a true invention. Defensive only.
- **Trade secrets**: NDA + access control. Free.
</legal_foundation>

### Layer 2: Financial Foundation (BLOCKING for revenue)

<financial_foundation>
#### Banking
- **Business checking**: Required for any revenue. Don't commingle personal/business.
- **Business savings**: For tax reserves (see below).
- **Credit card**: For expenses. Builds business credit.
- **Merchant account**: Stripe / PayPal / Square for accepting payments.

**Setup time**: 1-2 weeks. Do this BEFORE first customer.

#### Accounting
- **Bookkeeping**: Track every transaction. Software: QuickBooks, Xero, Wave (free).
- **Chart of accounts**: Standardized categories. Don't invent your own.
- **Monthly close**: Reconcile accounts, generate P&L and balance sheet. Takes 2-4 hours/month.
- **Annual CPA review**: $1-3K. Worth it. Catches mistakes before IRS does.

**Common mistake**: DIY accounting to save $200/mo. Costs $5-20K in tax penalties or audit defense later.

#### Tax obligations
- **Federal income tax**: 21% for C-Corp, pass-through for LLC/S-Corp
- **State income tax**: Varies 0-12%
- **Sales tax**: Collect in states where you have nexus. Post-Wayfair, all states with economic nexus. Use TaxJar/Avalara.
- **Payroll tax**: 7.65% employer + 7.65% employee + FUTA + SUTA. Use Gusto/ADP.
- **Quarterly estimated taxes**: For pass-through entities. April/June/Sep/Jan.

**Tax reserve rule**: Set aside 30-40% of profit for taxes. Don't touch it.

#### Financial statements (the 3 you must understand)
1. **P&L (Profit & Loss)**: Revenue - expenses = profit. Monthly.
2. **Balance sheet**: Assets = liabilities + equity. Snapshot at moment in time.
3. **Cash flow statement**: Cash in vs cash out. THE most important for early-stage.

**If you can't read these 3, you can't run a business.** Learn them.

#### Insurance
- **General liability**: $40-80/mo. Required for most B2B contracts.
- **Professional liability (E&O)**: $60-150/mo. Required for services businesses.
- **Workers comp**: Required once you have W-2 employees. $30-200/mo per employee.
- **Cyber liability**: $100-300/mo. For SaaS handling customer data.
- **D&O (directors & officers)**: $1-3K/yr. Required if you have a board or raise VC.

**Don't skip**: general liability + professional liability (if services).
</financial_foundation>

### Layer 3: Team Foundation (BLOCKING when hiring)

<team_foundation>
#### Employee vs contractor
- **1099 contractor**: No payroll tax, no benefits, no liability. But: limited control, IP risk, IRS misclassification risk.
- **W-2 employee**: Full liability, payroll tax, benefits. But: full control, IP assignment, loyalty.

**IRS test**: 3 categories — behavioral control, financial control, relationship type. If you control how/when/where they work, they're W-2.

**Common mistake**: Treating full-time workers as 1099s to save 30%. IRS reclassification = back taxes + penalties + interest. Use Gusto or Rippling to handle correctly.

#### First 10 hires (sequence matters)

For a bootstrapped software business:
1. **Hire 1**: Senior engineer (you can't ship fast enough alone)
2. **Hire 2**: Customer success / support (you can't do support + build)
3. **Hire 3**: Second engineer (specialization: frontend/backend split)
4. **Hire 4**: Marketing/growth (you've built it, now distribute it)
5. **Hire 5**: Sales (if B2B, once you have product-market signal)
6. **Hire 6-10**: Engineers (product velocity)

For a services business:
1. **Hire 1**: First practitioner (you can't serve all clients alone)
2. **Hire 2**: Operations/PM (you can't deliver + manage)
3. **Hire 3-5**: More practitioners
4. **Hire 6**: Sales (you've proven the model, now scale it)
5. **Hire 7-10**: More practitioners + ops

**Common mistake**: Hiring sales too early (before PMF). Or hiring engineers too late (after PMF, when you can't ship fast enough).

#### Compensation
- **Salary**: Benchmark via Pave, Carta, Levels.fyi. Pay 60-80th percentile for early-stage (you can't compete on salary, compete on equity).
- **Equity**: First hire 0.5-1.5%, declining with each subsequent hire. 4-year vest, 1-year cliff. Use Carta or Pulley.
- **Benefits**: Health insurance (employer pays 50-100%), 401(k) with 3-4% match, unlimited PTO (actually better for employer — no accrued liability).

**Carta benchmark data**: First hire median equity = 1.5% (Carta 8,000+ grants analyzed).

#### Culture
- **Write it down**: 5-7 principles. Not "we value excellence" — specific ("we ship weekly, we write before we meet, we say the hard thing").
- **Hire for it**: Reference checks specifically ask about cultural principles.
- **Fire against it**: When someone violates a principle, address it. Repeated violation = exit.

**Common mistake**: "Culture fit" hiring = homogeneity. Hire for culture ADD, not culture fit.
</team_foundation>

### Layer 4: Technology Foundation (BLOCKING for product)

<technology_foundation>
#### Stack choices
- **Don't over-architect**: Use the boring stack you know. Novelty is a tax.
- **Monolith first**: Don't build microservices. Monolith until it hurts, then split.
- **Managed services**: Use Stripe (payments), Auth0/Clerk (auth), Vercel/Render (hosting), Postgres (database). Don't build what you can buy.
- **Monitoring**: Sentry (errors), Logtail (logs), PostHog (analytics). Set up on day 1.

**Common mistake**: Building custom auth, custom payments, custom CMS. Each takes 2-4 weeks. Use managed services.

#### Security baseline
- **HTTPS everywhere**: Free via Let's Encrypt
- **Password hashing**: bcrypt or argon2. Never MD5/SHA1.
- **Secrets management**: Never commit secrets. Use .env + git-crypt or Doppler.
- **Backup**: Daily automated. Test restore quarterly.
- **SOC 2**: Required for enterprise sales. $30-50K + 3-6 months. Use Vanta/Drata ($7-10K/yr) to automate.

**Don't skip**: HTTPS, password hashing, secrets management. Everything else can wait.
</technology_foundation>

### Layer 5: Compliance Foundation (BLOCKING by regulation)

<compliance_foundation>
#### GDPR (EU customers)
- **Privacy policy**: Required. Clear, plain language.
- **Cookie consent**: Required if you use any non-essential cookies.
- **Data Subject Rights**: Right to access, delete, export. Must respond in 30 days.
- **Data Processing Agreement (DPA)**: Required for B2B.
- **Fines**: Up to 4% of global revenue. Not theoretical.

#### CCPA (California customers)
- **Privacy policy**: Required.
- **"Do Not Sell My Personal Information"** link: Required if you "sell" data (broad definition).
- **Opt-out requests**: Must honor within 15 days.

#### HIPAA (health data)
- **Don't touch health data without compliance review**. $100-$50K per violation.
- **BAA (Business Associate Agreement)**: Required with any vendor touching PHI.
- **Specialized hosting**: AWS/GCP HIPAA-eligible services only.

#### SOC 2 (enterprise SaaS)
- **Type 1**: Point-in-time audit. $15-30K, 2-3 months.
- **Type 2**: Continuous audit over 6-12 months. $30-50K, 6-12 months.
- **Required for**: Enterprise sales, regulated industries.
- **Use Vanta/Drata**: $7-10K/yr, automates 80% of compliance work.

#### Sales tax (US)
- **Economic nexus**: Post-Wayfair (2018), collect in states where you have >$100K sales or >200 transactions.
- **Use TaxJar/Avalara**: Don't manually track 50 states' rules.
- **Marketplace facilitator**: Amazon/Shopify collect for you on their platform. Direct sales = you collect.

**Common mistake**: Ignoring sales tax for 2 years, then owing $50K in back taxes + penalties. Set up on day 1 of revenue.
</compliance_foundation>
</operational_stack>

## What's BLOCKING vs Deferrable

<blocking_deferrable>
| Item | Status | When to address |
|---|---|---|
| LLC formation | BLOCKING | Before first $ of revenue |
| Business bank account | BLOCKING | Before first $ of revenue |
| Privacy policy | BLOCKING | Before launch |
| Customer contracts | BLOCKING (B2B) | Before first B2B customer |
| Bookkeeping setup | BLOCKING | Day 1 of revenue |
| Tax reserve | BLOCKING | Day 1 of revenue (set aside 30-40%) |
| General liability insurance | BLOCKING (services) | Before first B2B contract |
| Trademark filing | Deferrable | Within 6 months of launch |
| Co-founder agreement | BLOCKING (if cofounder) | Day 1 of partnership |
| SOC 2 | Deferrable | When pursuing enterprise deals |
| HIPAA | BLOCKING (if health data) | Before touching any PHI |
| Patents | Deferrable | Only if true invention, years 1-3 |
| 401(k) | Deferrable | After hire #5 |
| D&O insurance | Deferrable | When raising VC or adding board |
| Workers comp | BLOCKING (when W-2) | Before first W-2 hire |
</blocking_deferrable>

## Few-Shot Examples

<examples>

### Example 1: Solo SaaS founder (positive)

<example>
<situation>
Solo founder validated an opportunity (open-source CLI + paid Pro tier). Asks "what do I need to set up before launching?"
</situation>

<thinking>
Let me map the operational stack for this case.

BLOCKING (before launch):
1. LLC formation — $50-200, 1-2 weeks. Protects personal assets. Don't launch as sole prop.
2. Business bank account — 1 week. Separate personal/business. Required by Stripe.
3. Stripe account — 1 day. Accepts payments. Use Stripe Atlas if also incorporating.
4. Privacy policy — 1 day (use Termly or similar). Required for any web presence.
5. TOS — 1 day. Required for paid product.
6. Bookkeeping — set up Wave (free) or QuickBooks. Track from day 1.
7. Tax reserve — set aside 30% of all revenue. Don't commingle.

DEFERRABLE (within first 90 days):
- Trademark filing ($250-1000) — file once name is stable
- General liability insurance — only needed if B2B contracts require
- Accountant — find one before first quarterly tax filing
- E&O insurance — only if enterprise customers require

NOT NEEDED (until specific trigger):
- SOC 2 — only if pursuing enterprise deals
- Workers comp — only when hiring W-2
- 401(k) — only after hire #5
- Patents — probably never for software CLI

The total blocking cost: ~$300-500 (LLC + bank + Stripe setup + privacy policy template). Time: 1-2 weeks.

Common mistake to flag: don't over-engineer. Don't file for patents. Don't get SOC 2. Don't hire a lawyer to draft custom TOS (use templates). Set up the minimum, launch, iterate.
</thinking>

<answer>
**BLOCKING (set up in weeks 1-2, before launch)**:
1. Form LLC ($50-200 in your state, or use Stripe Atlas $500 for Delaware LLC)
2. Open business bank account (Mercury, Brex, or local credit union)
3. Set up Stripe for payments
4. Privacy policy + TOS (use Termly or iubenda — $10-50/mo, generate in 1 day)
5. Set up Wave (free) or QuickBooks for bookkeeping
6. Open business savings for tax reserve (set aside 30% of all revenue)

**DEFERRABLE (within first 90 days)**:
- Trademark filing ($250-1000) — file once you've validated the name
- Find a CPA (ask in local business community) — before first quarterly tax
- General liability insurance ($40-80/mo) — only if B2B contracts require

**DON'T DO (until specific trigger)**:
- SOC 2 ($30-50K) — only if enterprise deals require
- Patents ($10-30K) — almost never worth it for software CLI
- Workers comp — only when hiring W-2
- D&O insurance — only if raising VC

**Total blocking cost**: $300-500 + 1-2 weeks
**Total blocking time**: ~20 hours of setup work

Don't over-engineer. The goal is to launch, not to have perfect operations. You'll iterate.
</answer>
</example>

### Example 2: B2B SaaS with first enterprise deal (positive)

<example>
<situation>
Founder has a working SaaS product. First enterprise customer ($100K ARR deal) wants SOC 2, custom MSA, and DPA. Founder asks "what do I need to close this deal?"
</situation>

<thinking>
Enterprise deal = enterprise operational requirements. Let me map what's needed.

For this specific deal:
1. SOC 2 — the customer is asking for it. This is a 6-12 month process normally, but you can:
   - Use Vanta or Drata ($7-10K/yr) to automate the collection
   - Get SOC 2 Type 1 (point-in-time) in 2-3 months for $15-30K
   - Some customers accept "SOC 2 in progress" with a letter from auditor
   - Some customers accept alternative: ISO 27001 (similar cost, different framework)

2. Custom MSA — enterprise will redline your standard TOS. You need a lawyer.
   - Don't use a big firm ($800/hr). Use a startup-focused firm ($300-500/hr) or Patchwork (fixed-fee)
   - Budget $5-15K for MSA negotiation
   - Common redlines: limitation of liability, IP indemnification, data breach notification, termination for convenience

3. DPA (Data Processing Agreement) — required by GDPR if customer is EU or if you process any personal data on their behalf
   - Standard template from IAPP or your law firm
   - Must align with your subprocessors (Stripe, AWS, etc.) — they have their own DPAs you incorporate

4. Cyber liability insurance — enterprise will require this in MSA
   - $1-3M coverage
   - $100-300/mo for early-stage SaaS
   - Required before contract signing

5. Security questionnaire — enterprise will send a 100-300 question security review
   - Vanta/Drata auto-fills 80% of this
   - Budget 4-8 hours for the rest

Total cost to close this deal: $25-50K (SOC 2 + lawyer + insurance + Vanta). 
The deal is $100K ARR. Margin ~85%. So $85K gross profit. Net of $25-50K setup = $35-60K first-year profit. Worth it IF the deal closes and IF it leads to more enterprise deals.

The trap: don't do this for one $100K deal. Do this if you're committing to enterprise as a channel.
</thinking>

<answer>
**To close this enterprise deal, you need**:

1. **SOC 2 Type 1** ($15-30K, 2-3 months via Vanta/Drata)
   - Negotiate: customer may accept "SOC 2 in progress" with auditor letter
   - Alternative: ISO 27001 (similar cost, globally recognized)

2. **Lawyer for MSA negotiation** ($5-15K)
   - Use startup-focused firm, not BigLaw
   - Budget 2-4 weeks for redline cycle
   - Common sticking points: limitation of liability (cap at 1x fees), IP indemnification (you indemnify for YOUR IP, not theirs)

3. **DPA** (template, ~$500-2K from lawyer or IAPP)
   - Must align with subprocessors (Stripe, AWS, etc.)
   - Required by GDPR

4. **Cyber liability insurance** ($100-300/mo, $1-3M coverage)
   - Required by MSA
   - Get before signing

5. **Security questionnaire response** (4-8 hours, Vanta auto-fills 80%)

**Total cost**: $25-50K + 2-3 months
**Deal value**: $100K ARR, $85K gross profit
**First-year net**: $35-60K

**Strategic question**: is this one deal, or are you committing to enterprise?
- One deal: negotiate hard, ask customer to share SOC 2 cost, or accept lower deal value
- Enterprise channel: invest in the infrastructure, it pays off across many deals

**Warning**: don't do this for one deal. The unit economics only work if you're committing to enterprise as a channel. Otherwise, sell to mid-market and skip SOC 2.
</answer>
</example>
</examples>

## Edge Cases

<edge_cases>
### Edge 1: International operations
Each country has different rules. Don't assume US rules apply. Common gotchas:
- EU: GDPR applies even to US companies with EU customers
- UK: separate data protection regime post-Brexit
- Canada: PIPEDA, similar to GDPR
- Brazil: LGPD, GDPR-like
- China: PIPL, strict data localization

If you have customers in a country, you probably need to comply with that country's laws. Get local counsel.

### Edge 2: Regulated industries
Healthcare (HIPAA), finance (SEC, FINRA), legal (state bar), education (FERPA),
defense (ITAR). Don't enter these without compliance counsel. The operational
overhead is 20-40% of revenue.

### Edge 3: Marketplaces and two-sided platforms
Additional legal considerations: 1099-K reporting for sellers, marketplace
facilitator tax, payment processing compliance (PCI-DSS), seller verification
(KYC/AML if sellers handle money).

### Edge 4: Crypto / blockchain
Regulatory nightmare. SEC, CFTC, FinCEN, state money transmitter licenses.
Don't enter without specialized counsel. Most "crypto businesses" are actually
unregistered securities businesses — that's a felony.

### Edge 5: AI products
EU AI Act (2026 enforcement) categorizes AI by risk. High-risk AI has
significant compliance. US: state laws (Illinois BIPA for biometrics, California
AI transparency). Have an AI policy and document training data provenance.

### Edge 6: Solo operator with no revenue yet
Minimum viable operations: sole prop is fine for testing. BUT: upgrade to LLC
before first $ of revenue. Don't accept payments as a sole prop — liability
isn't worth the $50-200 savings.
</edge_cases>

## Weak Link: What Kills This Operational Setup?

<weak_link>
```
Did you form an entity before accepting revenue?
  NO → Personal liability. Form LLC immediately.
  YES → continue

Did you separate business and personal finances?
  NO → Commingling pierces corporate veil. Set up business bank account.
  YES → continue

Did you set aside tax reserves?
  NO → Tax surprise = business death. Set aside 30-40% from day 1.
  YES → continue

Did you get contracts in place before hiring?
  NO → IP disputes, misclassification risk. Use contractor/employee agreements.
  YES → continue

Did you comply with applicable regulations (GDPR/HIPAA/SOC 2)?
  NO → Fines exceed revenue. Get compliance counsel.
  YES → continue

Did you set up accounting from day 1?
  NO → You don't know your numbers. Set up bookkeeping immediately.
  YES → Operations are sound.
```
</weak_link>

## Decision Protocol

<decision_protocol>
### Exact Question This Lens Answers
"What operational infrastructure is required to run this business, and which
pieces are blocking vs deferrable?"

### Data Required
- Business model (B2B/B2C, services/product, marketplace, etc.)
- Customer type (consumer, SMB, enterprise, regulated industry)
- Geographic scope (US, EU, global)
- Hiring plan (solo, first hire, scaling team)
- Revenue model (subscription, one-time, services, marketplace)

### Confidence Threshold
- **Deploy (proceed with setup)**: ≥80% confidence, blocking items identified and addressable in <2 weeks
- **Flag (proceed with caveats)**: 60-80% confidence, some blocking items require longer or external counsel
- **Discard**: <60% confidence, or blocking items are intractable (e.g., regulated industry without compliance path)

### Conflict Resolution Rules
- When Lens 12 (Operations) disagrees with execution sprints:
  - Operations wins on BLOCKING items. Don't launch without entity + bank + privacy policy.
  - Sprints win on DEFERRABLE items. Don't delay launch for SOC 2.
- When Lens 12 disagrees with Lens 09 (Pricing):
  - Pricing may need to account for operational costs (e.g., enterprise deals require SOC 2 = $30K, so price enterprise at premium)
- When Lens 12 disagrees with Lens 08 (Risk of Ruin):
  - Risk of ruin wins. If operational setup requires capital the user can't afford, REJECT the opportunity.
</decision_protocol>

## Output

<output>
```
### Business Operations Analysis

#### Business Model Summary
- Type: [B2B SaaS / B2C / services / marketplace / etc.]
- Customer: [consumer / SMB / enterprise / regulated]
- Geography: [US / EU / global]

#### Operational Stack Assessment

| Layer | Item | Status | Priority | Cost | Time |
|---|---|---|---|---|---|
| Legal | LLC formation | [done/needed] | BLOCKING | $[X] | [N] days |
| Legal | Contracts (MSA/TOS) | [done/needed] | BLOCKING | $[X] | [N] days |
| Legal | IP protection | [done/needed] | DEFERRABLE | $[X] | [N] days |
| Financial | Business banking | [done/needed] | BLOCKING | $0 | [N] days |
| Financial | Bookkeeping | [done/needed] | BLOCKING | $[X]/mo | [N] days |
| Financial | Tax reserve | [done/needed] | BLOCKING | 30% revenue | ongoing |
| Financial | Insurance | [done/needed] | [BLOCKING/DEFERRABLE] | $[X]/mo | [N] days |
| Team | [N/A if solo] | | | | |
| Technology | Stack | [done/needed] | BLOCKING | $[X]/mo | [N] days |
| Technology | Security baseline | [done/needed] | BLOCKING | $0 | [N] days |
| Compliance | [GDPR/CCPA/SOC 2/HIPAA] | [done/needed] | [BLOCKING/DEFERRABLE] | $[X] | [N] days |

#### Blocking Items (must do before launch)
1. [item + cost + time]
2. [item + cost + time]
3. [item + cost + time]

#### Deferrable Items (within first 90 days)
1. [item + trigger]
2. [item + trigger]

#### Total Setup Cost
- Financial: $[X]
- Time: [N] hours / [N] weeks

#### Common Mistakes to Avoid
1. [mistake specific to this business type]
2. [mistake specific to this business type]

#### Operational Verdict
- Setup is BLOCKING: [N] items, $[X], [N] weeks
- Once blocking items resolved: PROCEED to launch
- Deferrable items: address within 90 days
```
</output>

## Source

Synthesized from `/references/research-business-operations.md` which contains
the full operational stack, growth-by-stage playbook, metrics reference, hiring
playbook, top 20 failure modes, and 125 sources.
