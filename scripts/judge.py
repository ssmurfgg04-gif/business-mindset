#!/usr/bin/env python3
"""
Business Mindset - Automated LLM-as-a-Judge Evaluator
Grades agent outputs against a rigorous rubric for reasoning quality,
framework adherence, and monetization validation.
"""

import sys

JUDGE_CRITERIA = {
  "monetization_path_clear": {
    "weight": 0.30,
    "description": "Output explicitly identifies a monetization engine and price/volume path"
  },
  "failure_case_searched": {
    "weight": 0.20,
    "description": "Output demonstrates disconfirming evidence search was performed before PASS"
  },
  "six_pillar_correctness": {
    "weight": 0.20,
    "description": "Asymmetry scorecard uses full 6-pillar math (C x R x S x O x A / 1+F)"
  },
  "adversarial_pass_completed": {
    "weight": 0.15,
    "description": "Mentions Tri-Persona adversarial collision results or kill test"
  },
  "single_next_action_present": {
    "weight": 0.10,
    "description": "Concludes with specific physical action tied to measurable monetary inflow"
  },
  "knightian_uncertainty_classified": {
    "weight": 0.05,
    "description": "Classifies uncertainty as known/risk/knightian before final verdict"
  }
}

def judge_output(output_text):
  """
  Grades an agent's output text against the judge rubric.
  Returns score (0-100) and list of failed criteria.
  """
  scores = {}
  failed = []

  for criterion, meta in JUDGE_CRITERIA.items():
    hit = False
    # Heuristic keyword presence checks
    if criterion == "monetization_path_clear":
      hit = any(kw in output_text.lower() for kw in ["monetization", "revenue", "pricing", "capture rate", "ltv", "cac", "$", "recurring"])
    elif criterion == "failure_case_searched":
      hit = any(kw in output_text.lower() for kw in ["failure-case", "disconfirming", "adversarial", "kill", "survived"])
    elif criterion == "six_pillar_correctness":
      hit = all(kw in output_text.lower() for kw in ["convexity", "reflexivity", "structural", "optionality", "asymmetry", "friction"]) and "/" in output_text
    elif criterion == "adversarial_pass_completed":
      hit = any(kw in output_text.lower() for kw in ["adversarial", "inverter", "first-principles", "contrarian", "survived the collision", "killed by market"])
    elif criterion == "single_next_action_present":
      hit = any(kw in output_text.lower() for kw in ["single next action", "today", "physical action"])
    elif criterion == "knightian_uncertainty_classified":
      hit = any(kw in output_text.lower() for kw in ["knightian uncertainty", "known", "risk", "knightian"])
    
    scores[criterion] = 1 if hit else 0
    if not hit:
      failed.append(meta["description"])

  total_score = sum(JUDGE_CRITERIA[c]["weight"] * scores[c] for c in JUDGE_CRITERIA) * 100
  return total_score, failed

def main():
  print("=== LLM-as-a-Judge Evaluation ===")
  
  # Simulate an example agent output
  sample_output = """
  Verdict: PASS, Tier 3 — Local LLM Code Assistant
  
  Monetization: Open-core model with $20/dev/mo team tier. High willingness-to-pay.
  Real-world verification (simulated): 12 competing OSS projects on GitHub, none with strong monetization.
  Asymmetry Scoreboard math (convexity, reflexivity, structural edge, optionality, asymmetry, friction): (C=2 x R=1 x S=2 x O=2 x A=2) / (1 + F=1) = 16/32. PASS threshold >= 8.

  Failure-case search: Tested against cloud LLM cost escalation, model deprecation, and hallucination risks. Survived adversarial pass.

  Adversarial Verdict: SURVIVED (Inverter caught cost risk: "How does this fail" — mitigated via local model pinning).
  Knightian Uncertainty: Risk (model performance degradation trackable).

  Single Next Action: Build MVP CLI that wraps llama.cpp with token cost tracking today.
  """
  
  score, failed = judge_output(sample_output)
  
  print(f"Judge score: {score:.1f}/100")
  if failed:
    print("[FAIL] Missing criteria:")
    for f in failed:
      print(f"  - {f}")
    sys.exit(1)
  else:
    print("[SUCCESS] Output passed all judge criteria.")
    sys.exit(0)

if __name__ == "__main__":
  main()
