# Lens 04: Leverage Map — What Force Multiplier Fits This Opportunity?

## Core Question
How can output be scaled without linearly scaling effort or cost?

## When to Use
- User asks "how do I scale this"
- User wants to compare business models
- User has an idea and needs to evaluate its scalability
- User wants to know what kind of business to build

## The Leverage Spectrum

### 1. Code Leverage (Permissionless)
Software that runs automatically. Best for: repeatable operations, data
processing, automation.

**Signal**: "Is there a repetitive manual process here?"

**Moat**: Ongoing maintenance + data accumulation + switching costs.

**Zero-capital start**: Build a CLI tool, open-source for distribution,
charge for hosted version or support.

**Exponential potential (Lens 07)**: HIGH. Pure permissionless leverage.
Marginal cost ~0. If distribution wedge exists, can be Tier 1.

### 2. Media Leverage (Permissionless)
Content that distributes at zero marginal cost. Best for: attention capture,
trust building, audience ownership.

**Signal**: "Is there information asymmetry or expertise here?"

**Moat**: Audience relationship + accumulated trust + brand.

**Zero-capital start**: Niche newsletter, technical blog, YouTube tutorials.

**Exponential potential (Lens 07)**: MEDIUM-HIGH. Permissionless, but
distribution is slow. Often Tier 2 because reflexive loop is weak.

### 3. Network Leverage (Permissioned)
Communities that create value through members. Best for: matching, curation,
trust-based transactions.

**Signal**: "Would this get better with more participants?"

**Moat**: Critical mass + switching costs + content/connections.

**Zero-capital start**: Niche community (Discord, Slack, subreddit),
focused on a specific industry pain point.

**Exponential potential (Lens 07)**: HIGH if network effect type is strong.
But cold-start problem caps early Tier. Often Tier 1 if pre-tipping-point.

### 4. Labor Leverage (Permissioned)
Other people's time. Best for: services that can't be fully automated.

**Signal**: "Is there a high-touch service people need?"

**Moat**: Training + quality control + relationships.

**Zero-capital start**: Subcontracting (find clients, hire freelancers,
take margin).

**Exponential potential (Lens 07)**: LOW. Permissioned leverage scales
linearly with headcount. Almost always Tier 2/3.

### 5. Capital Leverage (Permissioned)
Money deployed to earn more money. Best for: buying assets, scaling proven
models.

**Signal**: "Is there a proven model that needs capital to scale?"

**Moat**: Exclusive deals + scale advantages.

**Zero-capital start**: Not applicable. Requires existing capital.

**Exponential potential (Lens 07)**: VARIABLE. Capital itself is linear
leverage. The asset it's deployed into determines Tier.

## Leverage Decision Tree

```
Can this be pure software?
  YES -> Code leverage (highest margin, but competitive)
   NO  -> Can this be content?
          YES -> Media leverage (slow build, durable moat)
           NO  -> Can this be a marketplace/community?
                  YES -> Network leverage (hardest to start, strongest moat)
                   NO  -> Does it require humans?
                          YES -> Can you hire/subcontract?
                                 YES -> Labor leverage (manageable margin)
                                  NO -> Capital leverage (skip if zero capital)
```

## What to Extract

| Leverage Type | Fit | Estimated Margin | Time to First $ | Switch Cost | Exponential Tier |
|---------------|-----|-----------------|----------------|-------------|------------------|
| Code | yes/no | 80-95% | 2-12 weeks | Medium | Often Tier 1-2 |
| Media | yes/no | 70-90% | 12-24 weeks | High | Often Tier 2 |
| Network | yes/no | 50-80% | 4-16 weeks | Highest | Often Tier 1 if pre-tipping |
| Labor | yes/no | 20-50% | 1-4 weeks | Medium | Almost always Tier 3 |
| Capital | yes/no | 5-20% | Immediate | Low | Variable |

## Bias Warnings
- Code leverage is the most natural default for technical founders. But code
  alone with no distribution advantage is just a feature, not a business.
- Media leverage works but takes months. Don't suggest it as a quick path.
- Network leverage has the strongest moat but hardest cold-start problem.
- Labor leverage is sustainable but low-margin. Use it to fund other plays.
- Never suggest capital leverage to someone with zero starting capital.

## ECR Phase Discipline

### Expansion Phase Output (generate 15-20+)
For a given opportunity, generate 15-20+ possible leverage configurations
(combinations of leverage types, distribution channels, monetization models).
No filtering.

### Contraction Phase Output (reduce to 3-5)
Apply weak-link elimination. Reduce to 3-5 viable leverage plays with
explicit kill reasons.

## Weak Link: What Kills This Leverage Play?

```
Can you actually execute this leverage type?
  Code: Can you build it? If not, can you afford to hire?
    NO to both -> Eliminate. Code leverage is inaccessible.
  Media: Do you have expertise worth sharing and time for 6+ months?
    NO -> Eliminate unless you can shortcut via acquisition/partnership.
  Network: Can you solve the cold-start problem?
    NO -> Eliminate. Empty networks have no value.
  Labor: Can you hire and manage people?
    NO -> Eliminate labor leverage. It's harder than it looks.
  Capital: Do you have $50K+?
    NO -> Eliminate capital leverage immediately.

Does the leverage type match the opportunity?
  High-touch service -> Code won't fully replace it. Hybrid model needed.
  Repeatable operation -> If you're using labor, you're leaving margin on the table.
  Information product -> Media or code. If you suggested labor, reconsider.

What's the time-to-money?
  Over 6 months without alternative revenue -> Flag. Can user survive?
  Over 12 months -> Eliminate unless user explicitly says they have runway.

Does the leverage compound or plateau?
  Compounds (code, media, network) -> Prefer. Value grows over time.
  Plateaus (labor, some capital) -> Acceptable if cash flow positive immediately.

Does this leverage support exponential potential (Lens 07)?
  Permissionless (code/media) + reflexive loop + network effects -> Tier 1 candidate
  Permissioned (labor/capital) -> Tier 2/3 regardless of other factors
```

## Time Horizon Tagging

| Leverage Type | Time to First $ | Time to Compounding |
|---|---|---|
| Code | 2-12 weeks | 6-18 months |
| Media | 12-24 weeks | 12-36 months |
| Network | 4-16 weeks | 12-36 months (if cold-start solved) |
| Labor | 1-4 weeks | Never truly compounds |
| Capital | Immediate | Continuous |

## Output

### Expansion Phase
List 15-20+ leverage configurations.

### Contraction Phase
List 3-5 viable leverage plays, each with:
- Leverage type
- Fit assessment
- Estimated margin
- Time to first $
- Switch cost
- Exponential Tier indication
- Kill reason for the 10-15 eliminated (one sentence each)

---

## Decision Protocol

### Exact Question This Lens Answers
"What force multiplier fits this opportunity — and can I actually
execute that leverage type?"

### Data Required
- Identified leverage type (code/media/network/labor/capital)
- User's execution capability for that type (from intake or autonomous default)
- Time-to-first-dollar estimate
- Margin estimate at scale
- Failure-case search: have others tried this leverage type and failed?

### Confidence Threshold
- **Deploy (use this leverage)**: ≥70% confidence, user can execute, time-to-$ <6 months
- **Flag (hybrid or secondary leverage)**: 50-70% confidence, or time-to-$ 6-12 months
- **Discard**: <50% confidence, or user cannot execute, or time-to-$ >12 months without runway

### Conflict Resolution Rules
- When Lens 04 (Leverage) disagrees with Lens 02 (Demand):
  - Demand present + no viable leverage → **service business (Tier 3)**. Accept or wait.
  - No demand + leverage available → **solution looking for a problem**. Discard.
- When Lens 04 disagrees with Lens 05 (Network):
  - Leverage available + no distribution → **build but can't reach users**. Discard until distribution solved.
  - Distribution available + no leverage → **audience without product**. Build leverage first.
- When Lens 04 disagrees with Lens 07 (Exponential):
  - Permissionless leverage (code/media) + reflexive loop → **Tier 1 candidate**.
  - Permissioned leverage (labor/capital) → **Tier 3 regardless of other factors**. Accept.
- When user cannot execute the optimal leverage type:
  - Downgrade to next-best leverage type the user CAN execute. Don't recommend code leverage to a non-coder.
