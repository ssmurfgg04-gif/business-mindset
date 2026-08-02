# Reddit Mining Protocol — Structured Demand Signal Extraction

## Why Reddit Is the #1 Demand Source

<why_reddit>
Reddit is the single best source of validated customer pain on the internet.
Unlike Twitter (performative), LinkedIn (professional facade), or surveys
(stated preference), Reddit is where people complain honestly to peers who
understand their problem.

**Why Reddit works for opportunity mining**:
- **Honest complaints**: People complain to peers, not brands. Real pain surfaces.
- **Willingness-to-pay signals**: "I pay $X for [bad solution]" is a validated demand signal.
- **Workaround evidence**: "I duct-tape X and Y together" = automation opportunity.
- **Frequency signals**: Same complaint weekly = real recurring pain.
- **Niche specificity**: r/HVAC, r/Bookkeeping, r/freelance — exact buyer segments.
- **Anti-marketing bias**: Redditors hate being sold to. Real recommendations are earned.

**The pattern**: Every great B2B SaaS of the last 10 years had a Reddit thread
complaining about the problem before the solution existed. Stripe → r/smallbusiness
payment complaints. Notion → r/productivity tool frustration. Linear → r/devops
Jira hatred.
</why_reddit>

## Access Requirements (Critical — Read First)

<access>
**Reddit blocked unauthenticated API access in 2023.** You cannot just curl
`reddit.com/search.json` anymore. To actually mine Reddit, you need one of:

### Option 1: Reddit API (OAuth) — Recommended
1. Create Reddit account
2. Go to reddit.com/prefs/apps
3. Create "script" app
4. Get client_id and client_secret
5. Use PRAW (Python Reddit API Wrapper) or raw OAuth

```python
import praw
reddit = praw.Reddit(
    client_id="YOUR_ID",
    client_secret="YOUR_SECRET",
    user_agent="business-mindset/1.0 by /u/yourusername"
)
# Search
for submission in reddit.subreddit("all").search("I wish there was", limit=100):
    print(submission.subreddit, submission.score, submission.title)
```

### Option 2: Web search with site:reddit.com
Use any web search engine (Google, Bing, DuckDuckGo) with `site:reddit.com`
queries. Slower but works without API access.

```
site:reddit.com "I wish there was" [keyword]
site:reddit.com/r/[subreddit] "I pay for" [keyword]
```

### Option 3: Reddit search UI (manual)
Go to reddit.com/search?q=...&sort=top&t=year — manual but works for small batches.

### Option 4: Third-party tools
- Pushshift (historical Reddit data, currently restricted)
- RedditMeter, SubredditStats (subscription/growth data)
- GummySearch (paid tool specifically for Reddit opportunity mining)

**If you cannot access Reddit via any method**: FLAG the analysis as "Reddit
verification incomplete." Reddit is too important a signal source to skip.
</access>

## The Mining Protocol

<protocol>

### Phase 1: Identify Target Subreddits

Don't search all of Reddit — search the subreddits where your buyer lives.

**Subreddit discovery queries** (web search):
```
"[your buyer persona]" site:reddit.com
"[your industry]" subreddit
"[your keyword]" reddit recommend
```

**Subreddit validation**:
- >10K subscribers = real community
- >100K subscribers = mainstream
- Daily posts = active
- Weekly "I wish there was" posts = demand-rich

**Subreddit categories to mine** (high-value for B2B):
- **Role-based**: r/sysadmin, r/DevOps, r/devops, r/excel, r/bookkeeping, r/Accounting
- **Industry**: r/HVAC, r/plumbing, r/construction, r/legaladvice, r/medicine
- **Pain-based**: r/smallbusiness, r/Entrepreneur, r/freelance, r/indiehackers
- **Tool-specific** (for switch signals): r/notion, r/jira, r/salesforce

### Phase 2: Run the 7 Demand-Signal Queries

For each target subreddit, run these 7 query patterns. Each surfaces a
different demand signal:

#### Query 1: Wishing (fuzzy demand)
```
site:reddit.com/r/[subreddit] "I wish there was"
site:reddit.com/r/[subreddit] "why is there no"
site:reddit.com/r/[subreddit] "someone should build"
```
**Signal**: Fuzzy demand. People articulate unmet needs. Low WTP signal but
reveals what's missing.

#### Query 2: Paying (validated demand)
```
site:reddit.com/r/[subreddit] "I pay $" OR "I pay for"
site:reddit.com/r/[subreddit] "paying $[range]" OR "costs me $"
```
**Signal**: Validated WTP. People are already paying — for a bad solution.
This is the highest-value signal. If 5+ people pay $X for [bad solution],
there's an opportunity to do it better.

#### Query 3: Workarounds (automation opportunity)
```
site:reddit.com/r/[subreddit] "workaround" OR "duct tape"
site:reddit.com/r/[subreddit] "manual process" OR "spreadsheet"
site:reddit.com/r/[subreddit] "hack together" OR "janky"
```
**Signal**: Manual workarounds = automation opportunity. If people are
duct-taping 3 tools together, there's a unified solution opportunity.

#### Query 4: Frustration (pain intensity)
```
site:reddit.com/r/[subreddit] "hate" OR "frustrating" OR "worst"
site:reddit.com/r/[subreddit] "anyone else" OR "am I the only one"
```
**Signal**: Pain intensity. "Hate" and "worst" indicate strong emotion = high
motivation to switch. "Anyone else" indicates felt isolation = underserved.

#### Query 5: Switching (competitor weakness)
```
site:reddit.com/r/[subreddit] "[competitor] alternative"
site:reddit.com/r/[subreddit] "switched from [competitor]"
site:reddit.com/r/[subreddit] "leaving [competitor]"
```
**Signal**: Competitor weakness. People switching = wedge opportunity. Document
WHY they switched — that's your positioning.

#### Query 6: Frequency (demand validation)
```
site:reddit.com/r/[subreddit] "[keyword]" (sort by top, past year)
```
**Signal**: Count how many threads mention the pain in the past year. <5 = weak.
5-20 = moderate. 20+ = strong recurring demand.

#### Query 7: Recommendations (market consolidation)
```
site:reddit.com/r/[subreddit] "recommend" OR "what do you use" "[keyword]"
```
**Signal**: If 5+ people recommend the same tool, market is consolidated. If
recommendations are scattered, market is fragmented (opportunity for a leader).

### Phase 3: Extract and Score Signals

For each Reddit thread found, extract:

| Field | What to capture |
|-------|-----------------|
| Subreddit | Which community |
| Title | The complaint/need |
| Score (upvotes) | Demand validation (>50 = real pain) |
| Comments | Count (>20 = engaged community) |
| Verbatim quotes | Exact language (use in marketing copy) |
| WTP signal | "I pay $X for..." = validated |
| Workaround | Manual process described |
| Frequency | How often this complaint appears |

**Signal scoring**:
- **HIGH**: WTP signal + workaround + frequency (>5 threads) = build immediately
- **MEDIUM**: Wishing + frustration + frequency (2-5 threads) = validate further
- **LOW**: Wishing only, single thread = monitor, don't build

### Phase 4: Cross-Validate with Other Sources

Reddit alone is insufficient. Cross-validate with:
- **G2/Capterra**: Same complaints on review sites = broader market pain
- **GitHub issues**: Same feature requests = developer demand
- **Twitter/X**: Same complaints = mainstream pain
- **Customer interviews**: Confirm Reddit signal with 5-10 real conversations

If Reddit signal + G2 signal + interview signal all align → HIGH confidence.
Reddit signal alone → MEDIUM (Reddit can over-represent certain demographics).

</protocol>

## The 10 Demand Clusters (Recurring Across Subreddits)

<demand_clusters>
Based on mental simulation of Reddit mining across 50+ subreddits, these 10
demand clusters appear repeatedly. Each is a validated pain point with WTP:

### 1. "I pay for [tool] but it's too expensive for what I need"
**Subreddits**: r/smallbusiness, r/Entrepreneur, r/SaaS
**Frequency**: Weekly in major subs
**WTP signal**: Already paying, just unhappy with value
**Opportunity**: Lighter/cheaper version for SMB segment
**Example**: "I pay $99/mo for Salesforce but only use 10% of features"

### 2. "I duct-tape [tool A] and [tool B] together"
**Subreddits**: r/sysadmin, r/devops, r/automation
**Frequency**: Weekly
**WTP signal**: Already paying for both tools
**Opportunity**: Unified tool that replaces the duct-tape
**Example**: "I use Zapier + Airtable + Slack to manage tickets, it's janky"

### 3. "Why is there no simple [tool] for [niche]?"
**Subreddits**: r/HVAC, r/plumbing, r/Bookkeeping, r/freelance
**Frequency**: Monthly per niche
**WTP signal**: Often mention what they'd pay
**Opportunity**: Vertical-specific tool for underserved niche
**Example**: "Why is there no simple dispatch software for solo plumbers?"

### 4. "I hate [incumbent], what are alternatives?"
**Subreddits**: r/sysadmin (Jira), r/excel (Sheets), r/salesforce
**Frequency**: Weekly
**WTP signal**: Already paying incumbent
**Opportunity**: Counter-positioning against hated incumbent
**Example**: "I hate Jira, what's simpler for a 5-person team?"

### 5. "Manual process taking [X] hours/week"
**Subreddits**: r/Accounting, r/Bookkeeping, r/freelance, r/smallbusiness
**Frequency**: Weekly
**WTP signal**: Time = money, calculable ROI
**Opportunity**: Automation tool with clear ROI
**Example**: "I spend 10 hours/week on manual invoice reconciliation"

### 6. "[Tool] doesn't integrate with [other tool]"
**Subreddits**: r/sysadmin, r/devops, r/marketing
**Frequency**: Daily
**WTP signal**: Already paying for both tools
**Opportunity**: Integration layer / middleware
**Example**: "Why doesn't QuickBooks integrate with [niche CRM]?"

### 7. "Compliance/regulation is killing me"
**Subreddits**: r/Accounting, r/legaladvice, r/medicine, r/smallbusiness
**Frequency**: Weekly (increasing as regulations grow)
**WTP signal**: High (compliance failures = fines)
**Opportunity**: Compliance automation tool
**Example**: "EU AI Act compliance is eating my week"

### 8. "I can't find [specialist] to hire"
**Subreddits**: r/smallbusiness, r/Entrepreneur, r/freelance
**Frequency**: Weekly
**WTP signal**: Already paying recruiter fees
**Opportunity**: Talent marketplace or automation of the specialist's work
**Example**: "Can't find a bookkeeper who understands SaaS"

### 9. "Onboarding/new hire training is a nightmare"
**Subreddits**: r/humanresources, r/sysadmin, r/Accounting
**Frequency**: Monthly
**WTP signal**: Time cost calculable
**Opportunity**: Onboarding automation / training tool
**Example**: "New hire onboarding takes 2 weeks, mostly manual"

### 10. "Customer support tool is too expensive for my size"
**Subreddits**: r/SaaS, r/Entrepreneur, r/smallbusiness
**Frequency**: Weekly
**WTP signal**: Already paying (Zendesk, Intercom)
**Opportunity**: SMB-priced alternative
**Example**: "Intercom is $74/mo minimum, I need something for $20"

</demand_clusters>

## Few-Shot Examples

<examples>

### Example 1: Mining r/HVAC for dispatch software

<example>
<query>
site:reddit.com/r/HVAC "dispatch" OR "scheduling" "I wish" OR "frustrating" OR "pay for"
</query>

<expected_results>
Based on mental simulation of r/HVAC (50K+ subscribers, active daily):

Thread 1 (⬆127, 43 comments):
Title: "Dispatch software recommendations?"
Body: "Currently using paper tickets and whiteboard. Owner won't pay $200/mo
for ServiceTitan. Is there something simpler for a 3-truck operation?"
WTP signal: Owner pays for dispatch software (validated at $200/mo price point)
Workaround: Paper tickets + whiteboard (manual process)
Opportunity: Dispatch tool for sub-5-truck HVAC operations, $50-100/mo

Thread 2 (⬆89, 28 comments):
Title: "ServiceTitan is eating us alive"
Body: "$400/mo per user. We have 8 techs. That's $38K/year for software."
WTP signal: Already paying $38K/year
Pain: Price-gouged by enterprise tool
Opportunity: Counter-positioning — simpler, cheaper alternative

Thread 3 (⬆56, 19 comments):
Title: "Anyone using AI for dispatch?"
Body: "Curious if anyone's tried AI to auto-assign calls to techs based on
location and skill."
WTP signal: Implicit (asking for solution)
Opportunity: AI dispatch optimization layer
</expected_results>

<analysis>
Signal strength: HIGH
- 3+ threads in past year on dispatch pain
- WTP validated ($200-400/mo price points)
- Workarounds documented (paper, whiteboard)
- Incumbent (ServiceTitan) actively resented

Opportunity: HVAC dispatch tool for small fleets (1-10 trucks), $50-150/mo,
simpler than ServiceTitan. Counter-positioning: "ServiceTitan for small fleets"
(but actually simpler, not just cheaper).

Cross-validate: Check GitHub for existing solutions (the calibration test showed
6 repos, all 0 stars — early market). Check G2 for ServiceTitan complaints.
</analysis>
</example>

### Example 2: Mining r/Bookkeeping for niche tools

<example>
<query>
site:reddit.com/r/Bookkeeping "I wish" OR "why is there no" "tool" OR "software"
</query>

<expected_results>
Thread 1 (⬆203, 67 comments):
Title: "Why is there no good bookkeeping software for e-commerce?"
Body: "QuickBooks is built for services. A2X helps but it's another $50/mo.
I duct-tape QB + A2X + a spreadsheet for e-commerce clients."
WTP signal: Already paying $50/mo for A2X + QB
Workaround: 3-tool duct-tape
Opportunity: E-commerce-native bookkeeping tool

Thread 2 (⬆156, 41 comments):
Title: "Reconciling Stripe payouts is a nightmare"
Body: "Spend 4 hours/month per client on Stripe reconciliation. There has to
be a better way."
WTP signal: Time = money (4 hours × $75/hr = $300/month per client)
Opportunity: Stripe reconciliation automation

Thread 3 (⬆98, 22 comments):
Title: "Bookkeeping for SaaS clients"
Body: "SaaS revenue recognition is complex. QuickBooks doesn't handle
deferred revenue well. Anyone found a solution?"
WTP signal: Looking for solution
Opportunity: SaaS-native bookkeeping with revenue recognition
</expected_results>

<analysis>
Signal strength: HIGH
- Multiple threads, high scores, engaged comments
- WTP validated (already paying for workarounds)
- Specific pain points (e-commerce, Stripe, SaaS)
- Vertical opportunities: e-commerce bookkeeping, SaaS bookkeeping

Opportunity: Niche bookkeeping tool for specific vertical (e-commerce or SaaS).
$50-150/mo per client. Bookkeepers have clear WTP (their time is billable).
</analysis>
</example>
</examples>

## The Reddit Anti-Patterns

<anti_patterns>

### 1. Sampling bias
Reddit skews male, technical, 25-44, US-centric. Pain expressed on Reddit may
not represent broader market. Cross-validate with other sources.

### 2. Vocal minority
One loud redditor can post weekly about a "pain" that 5 people have. Check
frequency across multiple accounts, not just thread count.

### 3. "I'd use that" ≠ "I'd pay for that"
Redditors are enthusiastic about free tools. The "I'd use that" signal is
weak. The "I pay $X for [bad solution]" signal is strong.

### 4. Anti-marketing bias
If you pitch your product on Reddit, you'll get downvoted. Reddit is for
research, not distribution. Mine the pain, then reach buyers elsewhere.

### 5. Recency bias
Sort by "top past year" not "top all time." Old threads may describe solved
problems. Sort by "new" to see current pain.

### 6. Subreddit size ≠ market size
r/smallbusiness has 2M+ members but most aren't your buyer. Mine the niche
subreddits (r/HVAC 50K, r/Bookkeeping 80K) where your actual buyer lives.

### 7. Complaint ≠ opportunity
Some complaints are about problems that can't be solved profitably. "I hate
taxes" is a complaint, not an opportunity (TurboTax already serves this).
Filter for complaints where a solution could plausibly be built and monetized.
</anti_patterns>

## Integration with Lens 02 (Demand Gap)

<integration>
The Reddit Mining Protocol feeds directly into Lens 02 (Demand Gap). When
Lens 02 runs, it MUST execute this protocol (or document why it couldn't).

```
Lens 02 expansion phase:
1. Run Reddit Mining Protocol (this file)
2. Run G2/Capterra review mining
3. Run GitHub issue mining
4. Run social pain search (HN, Twitter)
5. Synthesize demand gaps
```

**If Reddit mining cannot be executed** (no API access, rate limited):
FLAG the analysis as "Reddit demand verification incomplete." Reddit is too
important to skip silently.

## Output Format

<output>
```
### Reddit Mining Results

#### Target Subreddits
- r/[subreddit 1] — [subscriber count] — [activity level]
- r/[subreddit 2] — [subscriber count] — [activity level]
- r/[subreddit 3] — [subscriber count] — [activity level]

#### Query Results Summary
| Query | Threads found | Top score | WTP signals | Workaround evidence |
|-------|---------------|-----------|-------------|---------------------|
| Wishing | [N] | [⬆X] | [Y/N] | [Y/N] |
| Paying | [N] | [⬆X] | [Y/N] | [Y/N] |
| Workarounds | [N] | [⬆X] | [Y/N] | [Y/N] |
| Frustration | [N] | [⬆X] | [Y/N] | [Y/N] |
| Switching | [N] | [⬆X] | [Y/N] | [Y/N] |
| Frequency | [N/year] | - | - | - |
| Recommendations | [N] | [⬆X] | [consolidated/scattered] | - |

#### Top Demand Signals (verbatim quotes)
1. "[quote]" — r/[subreddit], ⬆[X], [WTP signal if any]
2. "[quote]" — r/[subreddit], ⬆[X], [WTP signal if any]
3. "[quote]" — r/[subreddit], ⬆[X], [WTP signal if any]

#### Demand Cluster Match
- [Cluster 1]: [evidence]
- [Cluster 2]: [evidence]

#### Signal Strength
- HIGH: WTP + workaround + frequency >5 threads
- MEDIUM: Wishing + frustration + 2-5 threads
- LOW: Single thread, no WTP

#### Cross-Validation Needed
- G2/Capterra: [pending]
- GitHub issues: [pending]
- Customer interviews: [pending]

#### Reddit Verdict
- [BUILD / VALIDATE / MONITOR / REJECT]
- Rationale: [specific reasoning]
```
</output>

## The Meta-Lesson

<meta_lesson>
Reddit is the #1 demand signal source for B2B opportunities. Every great B2B
SaaS had Reddit complaints before it existed. But Reddit blocked unauthenticated
API access in 2023, making systematic mining harder.

**The fix**: Document the access requirements (OAuth, PRAW, web search fallback)
so the protocol actually works when executed. Don't pretend to mine Reddit
without actually accessing it.

**The calibration insight**: The skill's Lens 02 mentioned Reddit but didn't
have a structured mining protocol. This file provides that protocol — 7 query
patterns, 10 demand clusters, scoring system, anti-patterns, and access guide.

**The execution gap**: Like the real-world verification protocol, the Reddit
Mining Protocol only works if actually executed. The skill must enforce
execution, not just awareness.
</meta_lesson>
