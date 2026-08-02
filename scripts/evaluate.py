#!/usr/bin/env python3
"""
Business Mindset - Calibration & Asymmetry Scorecard Evaluator
Tests opportunity evaluation metrics against the 6-pillar framework:
Systemic Edge = (C * R * S * O * A) / (1 + F)
"""

import json
import sys

def calculate_edge(convexity, reflexivity, structural_edge, optionality, asymmetry, friction):
    """
    Computes systemic edge score.
    Each parameter scored 0, 1, or 2.
    Threshold: >= 8, A >= 1, F <= 1
    """
    numerator = convexity * reflexivity * structural_edge * optionality * asymmetry
    denominator = 1 + friction
    score = numerator / denominator
    passed = (score >= 8.0) and (asymmetry >= 1) and (friction <= 1)
    return score, passed

def main():
    print("=== Business Mindset Calibration Test Runner ===")
    
    # Test sample simulation cases
    test_cases = [
        {"name": "High-Arb SaaS Play", "C": 2, "R": 2, "S": 2, "O": 2, "A": 2, "F": 0},
        {"name": "Saturated E-Commerce Drop", "C": 0, "R": 0, "S": 0, "O": 1, "A": 0, "F": 2},
        {"name": "Asymmetric API Aggregator", "C": 2, "R": 1, "S": 2, "O": 2, "A": 2, "F": 1},
    ]

    all_passed = True
    for case in test_cases:
        score, passed = calculate_edge(
            case["C"], case["R"], case["S"], case["O"], case["A"], case["F"]
        )
        print(f"Case: {case['name']} | Score: {score:.2f} | Result: {'PASS' if passed else 'FAIL'}")
        if case["name"] == "High-Arb SaaS Play" and not passed:
            all_passed = False
        if case["name"] == "Saturated E-Commerce Drop" and passed:
            all_passed = False

    if all_passed:
        print("\n[SUCCESS] Calibration evaluation runner passed all simulation tests.")
        sys.exit(0)
    else:
        print("\n[FAILURE] Calibration test expectations violated.")
        sys.exit(1)

if __name__ == "__main__":
    main()
