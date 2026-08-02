# Lookback Validation Protocol

## Purpose
Check historical success/failure base rates for similar venture categories before issuing a PASS verdict.

## Protocol Steps
1. Identify 3–5 real-world historical analogs or comparable startups/side projects in the last 24 months.
2. Determine their outcome (Success / Struggling / Failed).
3. Compute the empirical base rate of success.
4. Apply base-rate penalty to confidence if empirical success rate is <15%.

## Output Schema
```json
{
  "analogs_reviewed": 4,
  "empirical_success_rate": "15%",
  "primary_failure_cause": "High customer acquisition cost relative to lifetime value",
  "base_rate_adjusted_confidence": 35
}
```
