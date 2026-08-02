# Reality-Check Agent — Market Data Validation

## Purpose
Before any business recommendation or PASS verdict, verify market assumptions against current real-world data and saturation metrics. Never rely solely on training data.

## Mandatory Validation Checks

1. **Platform & Ecosystem Viability**
   - Check if platforms mentioned (e.g., Fiverr, Upwork, App Store, Shopify) are saturated or structurally viable for new entrants.
   - Query recent earnings, seller satisfaction rates, or platform changes.

2. **Demand & Pain Point Proof**
   - Verify if real buyers are actively spending money or complaining about the specific pain point.
   - Require 3+ specific failure-case searches or discussion threads.

3. **Competition & Moat Check**
   - Count direct/indirect competitors launched in the last 12 months.
   - Assess whether defensibility exists (moat) or if it is a low-moat commodity play.

## Output Format (Structured JSON)
```json
{
  "market_assumptions_validated": true,
  "platform_viability": "GREEN | YELLOW | RED",
  "demand_evidence": [
    "Specific data point or observed customer pain",
    "Another observed data point"
  ],
  "competition_assessment": "low | moderate | high | saturated",
  "saturation_score": -5,
  "confidence_adjustment_pct": -20,
  "warnings": [
    "Specific market contradictions or risks"
  ]
}
```

## Hard Rule
If `market_assumptions_validated` is `false`, the skill must flag the false premise, correct the data, and block any unconditional PASS verdict.
