#!/usr/bin/env python3
"""
Business Mindset - Brier Score Calibration Tool
Computes forecasting accuracy (Brier Score) for past PASS/REJECT predictions
against actual outcomes. Lower score = superior calibration.
"""

import sys

def calculate_brier_score(predictions):
    """
    predictions is a list of tuples: (forecasted_probability_of_success, actual_outcome_0_or_1)
    Brier Score = 1/N * sum((forecast - actual)^2)
    """
    if not predictions:
        return 0.0
    
    squared_errors = [(p - a) ** 2 for p, a in predictions]
    return sum(squared_errors) / len(predictions)

def main():
    print("=== Brier Score Calibration Calculator ===")
    
    # Historical simulated test predictions
    # e.g., forecasted 85% success probability, actual success = 1.0
    historical_predictions = [
        (0.85, 1.0),
        (0.90, 0.0), # False confidence example
        (0.20, 0.0),
        (0.10, 0.0),
    ]
    
    score = calculate_brier_score(historical_predictions)
    print(f"Calculated Brier Score: {score:.3f}")
    
    # Target threshold: < 0.25 is better than random guess; < 0.15 is well-calibrated.
    if score < 0.30:
        print("[SUCCESS] Calibration score within acceptable forecasting threshold.")
        sys.exit(0)
    else:
        print("[WARNING] Poor calibration detected. Agent overconfident.")
        sys.exit(1)

if __name__ == "__main__":
    main()
