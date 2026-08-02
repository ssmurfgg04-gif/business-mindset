# Optional: User Intake Protocol

**Default mode is autonomous.** The skill operates without requiring any
user-specific information. This is the correct default for an autonomous AI
business execution engine — most people give generic answers to intake
questions, and most users are "average" (no specific advantages).

**When to invoke intake:**
- User explicitly asks for personalized analysis ("given my skills, what should I do?")
- User wants recommendations matched to their specific situation
- User has provided partial context and wants the agent to fill in the rest
- User is making a multi-year commitment decision (e.g., "should I quit my job
  to do this?") where generic defaults are inadequate

**When NOT to invoke intake:**
- User asks for market analysis ("analyze the AI dev tools market") — autonomous
- User asks for opportunity scan ("find me opportunities in X") — autonomous
- User is exploring, not committing — autonomous defaults are fine
- User has already provided context in their message — use that, don't re-ask

## Intake Questions

If invoked, ask these 6 questions in a single batched message (not one-by-one):

### 1. Skills
What can you do that 95% of people can't? This isn't "I'm a fast learner" —
it's specific capabilities: technical (e.g., "I can ship a React app in a
weekend"), domain (e.g., "I've spent 5 years in healthcare billing"), social
(e.g., "I have a network of 200 CFOs").

If you can't think of anything specific, that's fine — answer "average" and
the agent will default to opportunities that don't require specialized skills.

### 2. Network
Name 5 specific people or groups you can reach in less than 1 week with a
warm intro (not cold outreach). If you can't name 5, that's also fine —
answer "limited" and the agent will plan around cold channels.

### 3. Capital
How much money can you lose without lifestyle impact?
- $0 (no capital to risk)
- <$500 (small experiments only)
- <$5K (can fund MVP or 1-month validation)
- <$50K (can fund serious build)
- >$50K (significant capital available)

### 4. Time
- Hours per week available for this work: <5 / 5-10 / 10-20 / 20-40 / 40+
- Runway (months you can sustain without income from this): 0 / <3 / 3-6 /
  6-12 / 12+ / indefinite

### 5. Domain
Where have you spent 100+ hours? Work, hobby, obsession, community. Domains
where you have implicit knowledge that outsiders lack. If nowhere specific,
answer "generalist."

### 6. Taboos
Anything you won't do? Examples: no crypto, no adult content, no B2B enterprise
sales, no physical products, no regulated industries, no hire-managing-businesses.
Being explicit saves wasted analysis.

## Caching

Cache intake answers at:
```
~/.local/state/opencode/business-mindset-intake.json
```

Schema:
```json
{
  "intake_date": "2026-07-30",
  "skills": ["React/TypeScript weekend-shipping", "5y healthcare billing"],
  "network": ["3 CFOs from previous job", "Healthcare admin LinkedIn group"],
  "capital": "<$500",
  "time_hrs_week": "10-20",
  "runway_months": "6-12",
  "domain": "healthcare billing",
  "taboos": ["no crypto", "no enterprise sales"],
  "version": "1.0"
}
```

## Cache Validity

- Cache is valid for **30 days** from `intake_date`.
- After 30 days, prompt user: "Your intake is from [date]. Has anything
  changed? [Update / Keep as-is]"
- If user explicitly states new context in a message, update the cache.

## How Intake Affects Analysis

| Lens | How intake changes the analysis |
|---|---|
| 02 Demand Gap | Filter to gaps the user has domain knowledge in |
| 03 Arbitrage | Filter to arbitrage types matching user's access (information, geographic, skill) |
| 04 Leverage | Filter to leverage types user can execute (code if technical, media if writer, etc.) |
| 05 Network Path | Filter to channels reachable via user's network |
| 06 Anti-Bias (Asymmetry Check) | Use stated skills/network/capital as the asymmetry input |
| 07 Exponential Potential | Asymmetric Bet Structure scored against user's actual loss tolerance |

## Autonomous Mode Defaults (when no intake provided)

If no intake file exists OR intake is stale, the agent operates in autonomous
mode with these defaults:

- Skills: average (no specialized advantage assumed)
- Network: limited (cold channels primarily)
- Capital: $0 (zero-capital plays only)
- Time: 10-15 hrs/week
- Runway: 0-3 months (validate fast or die)
- Domain: generalist (no domain filter applied)
- Taboos: standard (no fraud, no ToS violation — per Floor in fang-yuan-mindset.md)

In autonomous mode, the Anti-Bias Audit's Asymmetry Check is run with the
note: "Autonomous mode — user-specific asymmetry not assessed. Only Structural
Edge (rule-based) or Timing advantage qualifies. Flag for explicit user
review."

Output is still actionable. Intake is **not** a blocker.
