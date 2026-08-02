# Domain Playbook: Tech / SaaS

How the business-mindset lenses adapt for software, SaaS, and digital
products. This is the "default" domain the skill was originally built
for, so most lens logic applies directly. This playbook notes the
specific adaptations.

## Domain Characteristics

- **Marginal cost**: ~0 on the core product (code/media leverage)
- **Distribution**: Often the primary challenge, not the build
- **Capital requirement**: Low to start, can scale with revenue
- **Speed advantage**: High — solo operators can ship in days, incumbents
  need quarters
- **Regulation**: Generally light, except for specific verticals (fintech,
  healthtech, edtech with student data)
- **Network effects**: Possible but not automatic; most SaaS are linear
  with switching costs, not network-effect businesses

## Lens Adaptations

### Lens 01 (Signal Scan) — Tech/SaaS specific signals
- **GitHub star velocity** (>100/month in a niche = signal)
- **Hacker News launch reception** (top 10 = strong signal, ignored = weak)
- **VC funding in adjacent categories** (validates market, but watch for crowding)
- **API rate-limit complaints** (indicates power-user demand)
- **Open-source project commercialization** (a popular OSS project going
  SaaS is a strong signal of validated demand)

### Lens 02 (Demand Gap) — Tech/SaaS specific gaps
- **GitHub issues with high 👍 but no implementation** = validated demand
- **Stack Overflow questions with no good answers** = tooling gap
- **"I pay $X for [tool] but it's terrible"** = willingness-to-pay validated
- **Manual workaround blog posts** ("how to do X with Y and Z duct-taped
  together") = automation opportunity

### Lens 03 (Arbitrage) — Tech/SaaS specific arbitrages
- **Skill arbitrage**: Applying skills from a high-paying industry to a
  lower-competition niche (e.g., fintech engineers building dev tools)
- **Platform arbitrage**: Integration gaps between major platforms
  (Shopify + X, Notion + Y)
- **Temporal arbitrage**: 6-month window before major platforms ship a
  feature (build the bridge tool, get acquired)
- **Information arbitrage**: Niche data sets that aren't widely accessible

### Lens 04 (Leverage) — Tech/SaaS specific leverage
- **Code leverage is the default**. If you're not using code leverage,
  you're in the wrong domain.
- **Media leverage** works well for developer tools (technical blog,
  YouTube tutorials, conference talks)
- **Network leverage** is hard for SaaS (cold-start problem) but powerful
  if achieved (marketplace, community)
- **Avoid labor leverage** unless you're explicitly building an agency/
  services business

### Lens 05 (Network Path) — Tech/SaaS specific distribution
- **GitHub organic** (open-source distribution) — strongest for dev tools
- **HN/Reddit launch** — initial spike, not sustained
- **SEO for high-intent queries** ("how to do X", "alternative to Y")
- **Developer community presence** (Discord, Slack, niche forums)
- **Newsletter/podcast partnerships** — sustained, warm
- **Avoid paid acquisition early** — CAC is too high for solo devs

### Lens 07 (Exponential Potential) — Tech/SaaS tier expectations
- **Tier 1 (Moonshot)**: Rare for solo devs. Requires network effects or
  platform play. Examples: Notion (network effects via sharing), Stripe
  (platform play)
- **Tier 2 (Scalable Linear)**: The realistic target. Code leverage,
  zero marginal cost, but no network effects. Most successful indie
  SaaS are Tier 2.
- **Tier 3 (Linear)**: Service businesses disguised as SaaS (heavy
  onboarding, custom work). Avoid unless intentionally building services.

## Industry-Specific Bias Patterns

### Bias 1: "I'll build it and they'll come"
The most common SaaS bias. Building is the easy part; distribution is
the hard part. Every dev-tool founder overestimates build quality
importance and underestimates distribution.

**Counter**: Force Lens 05 (Network Path) to run BEFORE Lens 04
(Leverage). If you can't answer "how do I reach 100 users?" don't build.

### Bias 2: "Feature parity with incumbent"
Trying to match every feature of an established competitor. You will
lose — they have more engineers and existing users.

**Counter**: Force a "wedge" — one specific use case the incumbent does
badly. Win there, expand later.

### Bias 3: "Open-source will distribution-solve itself"
Open-sourcing is not a distribution strategy. It's a leverage choice.
You still need Lens 05.

**Counter**: Open-source + explicit distribution plan (launch post,
community presence, partnerships).

### Bias 4: "VC funding = validation"
VC funding validates a market hypothesis, not a business. Many funded
SaaS companies fail.

**Counter**: In anti-bias audit, treat VC funding as a Saturation signal
(many competitors with capital) AND a Validation signal (market is real).
Both are true. Weigh accordingly.

## Regulatory Considerations

Most SaaS is lightly regulated. Exceptions:

- **Fintech**: KYC/AML, money transmission licenses, PCI-DSS. Don't
  touch without legal counsel.
- **Healthtech**: HIPAA (US), GDPR health data (EU). Don't touch
  without compliance review.
- **Edtech with student data**: FERPA (US), COPPA (under-13). Moderate
  complexity.
- **AI tools**: EU AI Act (2026 enforcement), various state laws (US).
  Watch for category-specific rules.
- **Data processing**: GDPR (EU), CCPA (California). Applies to almost
  all SaaS. Plan for it.

## Case Study Examples

### Success: Plausible Analytics
- **Opportunity**: Privacy-focused Google Analytics alternative
- **Wedge**: GDPR made cookie-based analytics risky; Plausible is
  cookieless by design
- **Leverage**: Open-source + paid hosted tier (code leverage + capital
  leverage at scale)
- **Distribution**: GitHub stars + indie hacker community + SEO for
  "Google Analytics alternative"
- **Tier**: 2 (Scalable Linear) — no network effects, but strong
  structural edge (regulatory tailwind)
- **Lesson**: Regulatory change + open-source + clear wedge = durable
  Tier 2 business

### Failure: Various "Notion for X" clones
- **Opportunity**: Apply Notion's model to a specific vertical
- **Why they failed**: No wedge beyond "Notion but for [industry]".
  Notion itself eventually serves most verticals. No distribution
  advantage. No network effects.
- **Lesson**: "X for Y" is not a strategy. You need a wedge Notion
  structurally can't serve.

### Mixed: Many dev-tool SaaS
- **Pattern**: Solo dev ships useful tool, gets to $5-20K MRR, plateaus
- **Why plateau**: No network effects, no distribution beyond initial
  launch spike, incumbent copies the feature
- **Lesson**: Tier 2 is a fine outcome. $20K MRR is a great business
  for one person. Don't feel like a failure for not being Tier 1.

## Lens Modifications for Tech/SaaS

| Lens | Modification |
|------|--------------|
| 01 Signal | Add GitHub star velocity as primary signal type |
| 02 Demand | GitHub issues + Stack Overflow as primary gap sources |
| 03 Arbitrage | Skill arbitrage and platform arbitrage most common |
| 04 Leverage | Default to code leverage; media as secondary |
| 05 Network | GitHub organic + SEO + community are primary channels |
| 06 Anti-Bias | Watch for "build it they will come" bias |
| 07 Exponential | Set realistic expectation: Tier 2 is the target, not Tier 1 |
| 08 Risk of Ruin | Time-at-risk is the main exposure (build time); financial is low |

## Common Anti-Patterns in Tech/SaaS

1. **Building before validating** — most common SaaS failure
2. **Chasing Tier 1 when Tier 2 is the right target** — burns years
   chasing network effects that won't materialize
3. **Ignoring distribution until post-launch** — too late by then
4. **Over-engineering the MVP** — the first version should be embarrassing
5. **Pricing too low** — devs underprice consistently; $9/mo is often
   the wrong answer for B2B SaaS (should be $50-200)
