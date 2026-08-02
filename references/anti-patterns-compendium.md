# Anti-Patterns Compendium — Failure Modes Catalog

A catalog of the most common ways businesses fail, organized by category.
Each anti-pattern: what it looks like, why it fails, the fix, and a real example.

Use this as a reference during Lens 06 (Anti-Bias) adversarial audit, pre-mortem
analysis, and quarterly framework audits.

Synthesized from all research streams.

## Category 1: Opportunity Identification Anti-Patterns

<opportunity_antipatterns>

### 1. Solution Looking for a Problem
**What it looks like**: "I built this cool thing, now who needs it?"
**Why it fails**: Without a validated problem, there's no demand.
**Fix**: Start from Lens 02 (Demand Gap). Find the problem first.
**Example**: Color Labs ($41M raised) built a photo-sharing app nobody asked for. Shut down in 1 year.

### 2. "X for Y" Without a Wedge
**What it looks like**: "We're the Uber for dog walking" / "Notion for restaurants"
**Why it fails**: The "X for Y" framing copies the surface, not the wedge. The original X succeeded because of a specific structural advantage, not the category.
**Fix**: Lens 10 (Competitor Teardown). Find YOUR specific wedge, not someone else's.
**Example**: Dozens of "Uber for X" startups 2014-2016. Almost all dead by 2018.

### 3. Falling in Love with the Idea
**What it looks like**: Founder defends the idea against all evidence. Doesn't run experiments. Dismisses negative feedback.
**Why it fails**: Reality always wins. The founder wastes years on a doomed idea.
**Fix**: Pre-mortem (Lens 06). Disconfirming evidence search (research-protocols.md). Adversarial audit.
**Example**: Quibi raised $1.75B on the assumption people wanted 10-minute premium video on phones. Dismissed all signals that they didn't. Shut down in 6 months.

### 4. Trend Surfing Without Structural Change
**What it looks like**: "AI is hot, let's build an AI [thing]"
**Why it fails**: Trends without structural change are hype. When hype fades, the business dies.
**Fix**: Lens 01 (Signal Scan). Distinguish structural from hype signals.
**Example**: 100s of "AI-powered" SaaS companies 2023-2024 with no real AI moat. Most will die when "AI" stops being a funding magnet.

### 5. Confirming Bias in Customer Interviews
**What it looks like**: Founder asks leading questions, hears what they want, declares PMF.
**Why it fails**: False PMF signal leads to premature scaling.
**Fix**: Mom Test methodology (Rob Fitzpatrick). Ask about past behavior, not future intent.
**Example**: Every failed startup ever. "Everyone we talked to said they'd use it!"

### 6. Ignoring Willingness to Pay
**What it looks like**: "People love the idea!" — but no one will pay.
**Why it fails**: Love ≠ demand. Demand = willingness to pay.
**Fix**: Lens 02 demand clarity spectrum. Require payment signals before building.
**Example**: Many "free" apps with millions of users that never monetize.

### 7. Building for Yourself
**What it looks like**: "I have this problem, so others must too."
**Why it fails**: N=1 isn't a market. Your problem may be unique to you.
**Fix**: Validate with 10+ independent potential customers.
**Example**: Many developer tools built by developers for developers, that no one else uses.

### 8. Chasing Saturated Markets Without Differentiation
**What it looks like**: "Let's build a CRM / project management tool / email client."
**Why it fails**: Saturated markets have incumbents with moats. Head-on attack fails.
**Fix**: Lens 10. Find counter-positioning wedge or pick different market.
**Example**: Hundreds of CRM startups dead. Salesforce + HubSpot have the moats.

### 9. Mistaking Feature for Business
**What it looks like**: Building a feature that should be part of a bigger product, trying to sell it standalone.
**Why it fails**: Customers want integrated solutions, not bolt-on features.
**Fix**: Check if incumbents could add this feature in 90 days. If yes, no business.
**Example**: Many "AI writing assistant" startups that are just ChatGPT wrappers. Will be absorbed into existing tools.

### 10. Trend Anti-Signals (Following the Herd)
**What it looks like**: Building what YC just funded, what VCs are talking about, what's trending on Twitter.
**Why it fails**: By the time it's a trend, it's saturated. The alpha is gone.
**Fix**: Lens 01. Look for signals 6-12 months before they trend.
**Example**: NFT marketplaces in 2021. Everyone built one. 99% dead.
</opportunity_antipatterns>

## Category 2: Pricing Anti-Patterns

<pricing_antipatterns>

### 11. Underpricing
**What it looks like**: Charging 1/3 to 1/10 of value delivered.
**Why it fails**: Leaves money on table, signals low value, attracts worst customers, can't afford CAC.
**Fix**: Lens 09. Double the price. If you lose <20% of customers, you're still ahead.
**Example**: Most SaaS startups. Patrick McKenzie's "charge more" exists for a reason.

### 12. Cost-Plus Pricing for Software
**What it looks like**: "Server cost is $X, charge $X + 30%"
**Why it fails**: Software has ~0 marginal cost. Cost-plus = massive underpricing.
**Fix**: Value-based pricing.
**Example**: Most early-stage SaaS underpricing because they don't understand value.

### 13. Free Tier Too Generous
**What it looks like**: Free tier solves the whole problem for most users.
**Why it fails**: No reason to upgrade, expensive to host, attracts free-riders.
**Fix**: Free tier should solve smaller user's problem, not same problem at smaller scale.
**Example**: Many SaaS that never monetize because free is "good enough."

### 14. Copying Competitor Pricing
**What it looks like**: "Competitor charges $X, so we'll charge $X"
**Why it fails**: Their cost structure, value prop, and customer mix are different.
**Fix**: Price on YOUR value to YOUR customers.
**Example**: Every "we're 20% cheaper than [incumbent]" pitch that fails.

### 15. Pricing for Features Instead of Value
**What it looks like**: "We have 50 features, charge $50"
**Why it fails**: Features ≠ value. 10 useless features don't justify higher price.
**Fix**: Price on outcome.
**Example**: Many "all-in-one" tools that charge for feature count, lose to focused tools.

### 16. Linear Tier Pricing
**What it looks like**: $10 / $20 / $30 tiers
**Why it fails**: No decoy effect, no reason to upgrade to top tier.
**Fix**: Non-linear ratios (3.4x, 3.0x).
**Example**: Many early SaaS with 3 monthly tiers at $10/20/30 — top tier gets no uptake.

### 17. Never Raising Prices
**What it looks like**: Same pricing for 3+ years.
**Why it fails**: Real prices fall with inflation, signals weak pricing power, leaves 20-40% revenue on table.
**Fix**: Annual 5-10% increases (Lens 09 protocol).
**Example**: Most bootstrapped SaaS that haven't raised prices in years.

### 18. Annual Discount Too Small
**What it looks like**: "Save 10% with annual" (1.2 months free)
**Why it fails**: Not enough incentive to commit, customers stay monthly, churn risk stays high.
**Fix**: 20% annual discount (standard for SaaS).
**Example**: Many SaaS with weak annual uptake because discount is too small.

### 19. Hiding Pricing
**What it looks like**: "Contact us for pricing" on everything
**Why it fails**: Friction kills conversion, customers assume too expensive or too cheap.
**Fix**: Show pricing for self-serve and mid-tier. "Contact us" only for enterprise.
**Example**: Many B2B SaaS that force sales calls for $50/mo product.

### 20. Wrong Pricing Metric
**What it looks like**: Per-seat pricing when usage doesn't scale with seats
**Why it fails**: Customers share logins (revenue leak) or under-adopt (churn risk).
**Fix**: Match pricing metric to value metric.
**Example**: Many dev tools charging per seat when 1 person uses heavily. Should be per-API-call or per-record.
</pricing_antipatterns>

## Category 3: Growth & Scaling Anti-Patterns

<growth_antipatterns>

### 21. Premature Scaling
**What it looks like**: Hiring sales/marketing before PMF, spending on acquisition before retention works.
**Why it fails**: Burns capital, no growth because leaky bucket. 74% of startup failures.
**Fix**: Lens 13. Confirm PMF (Sean Ellis ≥40%, retention flattens) before scaling.
**Example**: Quibi (raised $1.75B, spent on marketing before validating demand).

### 22. Channel Diversification Prematurely
**What it looks like**: "We'll do SEO + paid + outbound + partnerships simultaneously."
**Why it fails**: Dilution. One channel at 3:1 beats five at 1:1.
**Fix**: Lens 13 Stage 1. One channel until saturated, then add second.
**Example**: Many early-stage startups with "growth teams" doing 5 things poorly.

### 23. Hiring VP of Sales Too Early
**What it looks like**: Hiring VP of Sales at $250K+ before PMF or sales motion defined.
**Why it fails**: VP can't succeed without playbook. Founder must sell first.
**Fix**: Founder sells until pitch is repeatable. Then hire VP to scale.
**Example**: Many Series A startups that hire CRO too early, burn $500K+ on failed hire.

### 24. Building "Growth Team" Before PMF
**What it looks like**: Hiring 3 growth marketers at Stage 0.
**Why it fails**: Growth team can't grow without PMF. They optimize the leaky bucket.
**Fix**: Lens 13. Stage 1 = 1 specialist. Stage 2 = growth team.
**Example**: Many pre-PMF startups with growth teams that produce nothing.

### 25. Expanding to New Segments Prematurely
**What it looks like**: "We serve SMB, let's also do enterprise."
**Why it fails**: Different segments need different product, pricing, sales motion. Dilution.
**Fix**: Nail current ICP first. Lens 13 Stage 1 = "don't expand segments."
**Example**: Many SaaS that try SMB + enterprise simultaneously, fail at both.

### 26. Raising Too Much Capital
**What it looks like**: Raising $20M Series A when $5M would do.
**Why it fails**: Forces growth-at-all-costs, destroys unit economics discipline, dilutes founder.
**Fix**: Raise minimum needed + 6 months runway. Stay capital-efficient.
**Example**: WeWork (raised too much, grew unprofitably, IPO disaster).

### 27. Multiple Products Too Early
**What it looks like**: "Our core product is growing, let's launch 3 more."
**Why it fails**: Focus dilution. Core product needs all resources.
**Fix**: Lens 13 Stage 2 = "don't launch multiple products."
**Example**: Many SaaS that launch 3 products, none of which win.

### 28. Chasing Virality Without Network Effects
**What it looks like**: "We'll add referral loops, viral growth!"
**Why it fails**: Virality requires network effects. Without it, referrals don't compound.
**Fix**: Verify network effects exist (Lens 07 Signal 7) before building viral loops.
**Example**: Many SaaS with referral programs that produce <5% of signups.

### 29. Ignoring Retention to Focus on Acquisition
**What it looks like**: "We need more leads!" while churn is 8% monthly.
**Why it fails**: Leaky bucket. No amount of acquisition fixes retention.
**Fix**: Lens 13 Stage 0. Fix retention before scaling acquisition.
**Example**: Most failed SaaS — focused on top-of-funnel while bleeding customers.

### 30. Expanding Internationally Too Early
**What it looks like**: "We're going global!" at $2M ARR.
**Why it fails**: International requires localization, compliance, support — overhead that kills early-stage focus.
**Fix**: Lens 13 Stage 2+. Internationalize only after domestic market is saturated.
**Example**: Many SaaS that opened EU office at $3M ARR, burned $1M on overhead.
</growth_antipatterns>

## Category 4: Operations Anti-Patterns

<operations_antipatterns>

### 31. Skipping Entity Formation
**What it looks like**: Operating as sole proprietorship with revenue.
**Why it fails**: Personal liability. Lawsuit or debt can take personal assets.
**Fix**: Form LLC before first $ of revenue. ($50-500, 1-2 weeks.)
**Example**: Many freelancers who get sued and lose personal savings.

### 32. Commingling Personal/Business Finances
**What it looks like**: Using personal bank account for business revenue.
**Why it fails**: Pierces corporate veil, loses liability protection. Tax nightmare.
**Fix**: Separate business bank account from day 1.
**Example**: Many small businesses that lose LLC protection in lawsuits.

### 33. Not Setting Aside Tax Reserves
**What it looks like**: Spending all revenue, getting surprised by tax bill.
**Why it fails**: Tax surprise = business death. Can't pay = penalties + interest.
**Fix**: Set aside 30-40% of profit from day 1. Don't touch.
**Example**: Many bootstrapped businesses that go under from unexpected tax bills.

### 34. Treating Contractors as Employees
**What it looks like**: Full-time workers classified as 1099 to save payroll tax.
**Why it fails**: IRS reclassification = back taxes + penalties + interest.
**Fix**: Use IRS test. If behavioral/financial/relationship control = W-2.
**Example**: Uber, Doordash ongoing battles. Many small businesses audited.

### 35. DIY Accounting
**What it looks like**: "I'll save $200/mo by doing my own books."
**Why it fails**: Costs $5-20K in penalties later. CPA catches what you miss.
**Fix**: Use bookkeeping software + annual CPA review.
**Example**: Many businesses that discover 2 years of mis-categorized transactions.

### 36. Skipping Insurance
**What it looks like**: "We don't need insurance, we're careful."
**Why it fails**: One lawsuit = bankruptcy. One data breach = bankruptcy.
**Fix**: General liability + professional liability (services) + cyber (SaaS).
**Example**: Many small businesses bankrupted by single lawsuit.

### 37. No Co-Founder Agreement
**What it looks like**: "We're friends, we'll figure it out."
**Why it fails**: Friendship ends, dispute starts, no agreement = lawsuit.
**Fix**: Written agreement with vesting, IP assignment, exit clauses.
**Example**: 65% of startup failures involve co-founder conflict (Wasserman).

### 38. Hiring for "Culture Fit"
**What it looks like**: "They're a great culture fit!" (= they're like me)
**Why it fails**: Homogeneity. No diversity of thought. Groupthink.
**Fix**: Hire for culture ADD (what's missing), not culture FIT (what's comfortable).
**Example**: Many startups with homogeneous teams that miss market shifts.

### 39. Not Firing Fast Enough
**What it looks like**: Keeping a bad hire for 6+ months "to give them a chance."
**Why it fails**: Bad hire poisons team, costs more to keep than to fire.
**Fix**: Performance plan (30 days), then fire if no improvement.
**Example**: Most founders' biggest regret is not firing faster.

### 40. Over-Engineering Tech Stack
**What it looks like**: "We need microservices, Kubernetes, custom auth."
**Why it fails**: Wastes 2-4 weeks per component. Use managed services.
**Fix**: Monolith + managed services (Stripe, Auth0, Vercel, Postgres).
**Example**: Many startups that spend 6 months on infrastructure instead of product.
</operations_antipatterns>

## Category 5: Founder Psychology Anti-Patterns

<founder_antipatterns>

### 41. Sunk Cost Fallacy
**What it looks like**: "We've invested 2 years, we can't give up now."
**Why it fails**: Past investment is irrelevant to future expected value.
**Fix**: Fang Yuan Axiom 1 (zero emotion). "Would I start this today?"
**Example**: Many founders who waste years on doomed ideas.

### 42. Founder Ego
**What it looks like**: "I'm the smartest, I don't need advice."
**Why it fails**: Blind spots. No one is smart enough alone.
**Fix**: Mentor, peer group, advisory board. Listen to disconfirming voices.
**Example**: Elizabeth Holmes (Theranos), Adam Neumann (WeWork).

### 43. Analysis Paralysis
**What it looks like**: Endless research, no action.
**Why it fails**: No learning without action. Markets don't wait.
**Fix**: Single Next Action (execution-sprints.md). 48-hour decision deadline.
**Example**: Many would-be founders who never start.

### 44. Shiny Object Syndrome
**What it looks like**: Starting 3 new projects before finishing the first.
**Why it fails**: Focus dilution. Nothing gets done.
**Fix**: Lens 11. Pick ONE. Kill the others (or defer).
**Example**: Many founders with 5 half-finished projects.

### 45. Avoiding Hard Conversations
**What it looks like**: Not firing, not giving negative feedback, not addressing co-founder conflict.
**Why it fails**: Problems compound. Team loses respect.
**Fix**: Radical candor. Address issues within 48 hours.
**Example**: Most founder regrets involve conversations they avoided.

### 46. Not Taking Care of Health
**What it looks like**: 100-hour weeks, no sleep, no exercise.
**Why it fails**: Burnout. Bad decisions. Health collapse.
**Fix**: Lens 08 burnout check. Sleep, exercise, time off are non-negotiable.
**Example**: Many founders who burn out and quit, or have health crises.

### 47. Isolation
**What it looks like**: No peer group, no mentor, no one to talk to.
**Why it fails**: Loneliness drives bad decisions. No perspective.
**Fix**: Founder peer group (IndieHackers, YC, etc.). Therapist. Mentor.
**Example**: Most successful founders cite peer group as critical.

### 48. Comparing to Other Founders
**What it looks like**: "They raised $50M, I'm failing."
**Why it fails**: Survivorship bias. You see their highlights, not their struggles.
**Fix**: Compare to your past self, not others.
**Example**: Many founders who quit because they feel inadequate.
</founder_antipatterns>

## Category 6: Fake Exponential Anti-Patterns

<fake_exponential_antipatterns>

### 49. Linear Growth with Optimism Bias
**What it looks like**: "We're growing 30% YoY, we'll be huge!"
**Why it fails**: Linear growth rate ≠ power-law tail. 30% grower at $1M = $13M in 10 years. Great business, not exponential.
**Fix**: Lens 07. Check power-law tail potential.

### 50. Negative Unit Economics Disguised as "Investing In Growth"
**What it looks like**: WeWork, MoviePass, Blue Apron.
**Why it fails**: Math doesn't improve with scale. CAC stays high, margin stays negative.
**Fix**: Lens 09. Verify unit economics improve with scale before claiming exponential.

### 51. Permissioned Leverage Dressed As Permissionless
**What it looks like**: "AI agency scaling via hiring."
**Why it fails**: Labor leverage scales linearly with hires, not exponentially.
**Fix**: Lens 04. Verify leverage is permissionless (code/media).

### 52. Performed Convexity
**What it looks like**: Theranos, FTX. Pitch decks describe convex payoffs; financials don't deliver.
**Why it fails**: The pitch curve is convex; reality is flat or fraudulent.
**Fix**: Lens 06 adversarial audit. Cross-check pitch against financials.

### 53. Badge Networks Mistaken For Network Effects
**What it looks like**: "Verified" badges or logins as "network effects."
**Why it fails**: Badges add value to badge-holder, not to network.
**Fix**: Lens 07. Verify each new user adds disproportionate value.

### 54. Platform Dependency Mistaken For Ownership
**What it looks like**: "Building on TikTok/Shopify/App Store."
**Why it fails**: Platform owns the exponential, not you. One TOS change = death.
**Fix**: Lens 05. Build toward owned channels.

### 55. Subsidy-Driven Growth
**What it looks like**: "$10M ARR in 18 months!" via below-market pricing.
**Why it fails**: Won't sustain at market prices.
**Fix**: Verify growth without subsidies. Stripe/NVIDIA didn't need subsidies.

### 56. Reflexivity Without Downside Model
**What it looks like**: "Adoption is exploding, network effects compounding!"
**Why it fails**: Reflexive businesses crash as fast as they rise. No exit plan.
**Fix**: Lens 07. Pre-define what breaks the loop.
**Example**: Crypto winter, social media saturation.
</fake_exponential_antipatterns>

## How to Use This Compendium

<usage>
1. **During Lens 06 adversarial audit**: Scan the relevant category for anti-patterns that apply. Use as attack vectors.

2. **During pre-mortem**: For each anti-pattern, ask "could this happen to us?" If yes, add to pre-mortem failure modes.

3. **During quarterly framework audit**: Check if any past decisions matched anti-patterns. If so, add to calibration learnings.

4. **During opportunity sifting (Lens 11)**: Use anti-patterns as additional kill criteria. If an opportunity matches an anti-pattern, flag for rejection.

5. **During customer interviews**: Listen for anti-pattern signals. "I wish someone would build X" without willingness to pay = anti-pattern #6.

The compendium is a living document. Add new anti-patterns as you discover them in your own decisions or in observed failures.
</usage>

## Source

Synthesized from all 5 research streams:
- `/references/research-opportunity-identification.md` (14 anti-patterns)
- `/references/research-pricing-competitor.md` (10 pricing anti-patterns)
- `/references/research-business-operations.md` (top 20 failure modes)
- `/references/research-operator-wisdom.md` (14 operator anti-patterns)
- `/references/exponential-research.md` (10 fake exponential anti-patterns)
