# Position & P&L Ledger

A JSONL-based ledger at `~/.local/state/opencode/business-mindset-ledger.jsonl`
for tracking positions opened and closed through the business-mindset skill.

The schema is **generalized** to support any opportunity type: trades, SaaS,
services, content, partnerships, products, and other plays. One JSON object
per line. Append-only. Read with `jq`.

## Entry Format

### Open a position

```json
{
  "type": "open",
  "id": "pos-001",
  "category": "trade|saas|service|content|partnership|product|other",
  "name": "AI dev tools newsletter",
  "entry_date": "2026-07-30",
  "entry_cost": 0,
  "entry_cost_currency": "USD",
  "time_investment_hrs_week": 4,
  "expected_validation_days": 14,
  "hypothesis": "100 subscribers in 30 days → sponsorship viable",
  "kill_criteria": "<30 subscribers by day 30 → close",
  "exponential_tier": "2",
  "systemic_edge_score": 12,
  "status": "open"
}
```

For trades specifically, add trade-specific fields:

```json
{
  "type": "open",
  "id": "pos-002",
  "category": "trade",
  "name": "ETH spot",
  "asset": "ETH",
  "platform": "Uniswap",
  "amount": 0.5,
  "entry_price": 1850,
  "entry_date": "2026-07-30",
  "fees": 12.50,
  "reason": "Structural arb",
  "kill_criteria": "price < 1700 → close",
  "status": "open"
}
```

### Close a position

```json
{
  "type": "close",
  "id": "pos-001",
  "exit_date": "2026-08-15",
  "outcome": "success|failure|abandoned|ongoing",
  "revenue_to_date": 1200,
  "costs_to_date": 80,
  "time_total_hours": 60,
  "lessons_learned": "Sponsorship rate too low at <1K subs; need 5K+ for $2K/mo",
  "would_do_again": true,
  "notes": "Pivoted to paid newsletter model"
}
```

For trades:

```json
{
  "type": "close",
  "id": "pos-002",
  "exit_price": 2100,
  "exit_date": "2026-08-15",
  "fees": 15.00,
  "pnl": 112.50,
  "notes": "Target hit"
}
```

### Record a dividend / interest / recurring revenue / extra

```json
{"type":"dividend","id":"pos-001","date":"2026-08-01","amount":5.20,"source":"sponsorship payment"}
{"type":"dividend","id":"pos-001","date":"2026-09-01","amount":5.20,"source":"subscription revenue"}
```

## Field Reference

| Field | Required | Description |
|---|---|---|
| `type` | yes | `open`, `close`, `dividend` |
| `id` | yes | Unique position ID (e.g., `pos-001`) |
| `category` | open | `trade`, `saas`, `service`, `content`, `partnership`, `product`, `other` |
| `name` | open | Human-readable name |
| `entry_date` | open | ISO date |
| `entry_cost` | open | Total upfront cost in `entry_cost_currency` |
| `time_investment_hrs_week` | open | Expected weekly hours |
| `expected_validation_days` | open | Days until hypothesis is testable |
| `hypothesis` | open | What you're testing |
| `kill_criteria` | open | Written kill rule (mandatory) |
| `exponential_tier` | open | 1/2/3 from Lens 07 (optional but recommended) |
| `systemic_edge_score` | open | 0-32 from 6 Pillars (optional) |
| `exit_date` | close | ISO date |
| `outcome` | close | `success`/`failure`/`abandoned`/`ongoing` |
| `revenue_to_date` | close | Total revenue generated |
| `costs_to_date` | close | Total ongoing costs (excluding entry) |
| `time_total_hours` | close | Total hours invested |
| `lessons_learned` | close | What worked / what didn't |
| `would_do_again` | close | Boolean |

## Shell Commands

```bash
# File location
LEDGER="$HOME/.local/state/opencode/business-mindset-ledger.jsonl"
mkdir -p "$(dirname "$LEDGER")"
touch "$LEDGER"

# Add an open entry (content opportunity example)
cat >> "$LEDGER" <<'EOF'
{"type":"open","id":"pos-003","category":"content","name":"AI dev tools newsletter","entry_date":"2026-07-30","entry_cost":0,"time_investment_hrs_week":4,"expected_validation_days":14,"hypothesis":"100 subscribers in 30 days","kill_criteria":"<30 subscribers by day 30","exponential_tier":"2","status":"open"}
EOF

# List all open positions (opened but not closed)
jq -s '[.[] | select(.type=="open")]' "$LEDGER" | jq -c '.[]' | while read line; do
  id=$(echo "$line" | jq -r '.id')
  closed=$(jq -s --arg id "$id" '[.[] | select(.type=="close" and .id==$id)] | length' "$LEDGER")
  if [ "$closed" -eq 0 ]; then echo "$line"; fi
done

# Show all positions by category
jq -s 'group_by(.category) | map({category: .[0].category, count: length})' "$LEDGER"

# Show total realized revenue (across all closes)
jq -s '[.[] | select(.type=="close") | .revenue_to_date // .pnl // 0] | add' "$LEDGER"

# Show positions that hit their kill criteria (manual check)
jq -s '[.[] | select(.type=="open") | {id, name, kill_criteria, entry_date}]' "$LEDGER"

# Show outcome distribution
jq -s 'group_by(.outcome) | map({outcome: .[0].outcome, count: length})' "$LEDGER"

# Show all entries in chronological order
jq -s 'sort_by(.entry_date // .date // .exit_date)' "$LEDGER"

# Count total entries
wc -l "$LEDGER"
```

## Usage in Skill

After recommending or executing a position, write the open entry to the
ledger immediately. The `kill_criteria` field is **mandatory** — without it,
the position can drift indefinitely without exit discipline.

Monitor weekly. When closed, write the close entry with `lessons_learned`
and `would_do_again` filled in honestly. These fields feed the Outcomes
Feedback Loop in SKILL.md for cross-session calibration.

The agent reads this file at the start of any session to know what positions
are active and adjust recommendations accordingly. If the user has an open
ETH position at $1,850 and the price drops to $1,200, the agent should
prioritize risk management over new opportunity hunting. If the user has an
open content position past its `expected_validation_days` with no `close`
entry, the agent should prompt: "Position pos-003 was due for validation
on [date]. Status?"
