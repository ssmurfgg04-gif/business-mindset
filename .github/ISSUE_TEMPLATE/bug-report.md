---
name: Bug Report
about: Report a lens giving wrong output, broken formula, routing error, or anti-bias failure
title: "[BUG] "
labels: bug
assignees: []
---

## Summary

<!-- One-sentence description of the bug -->

## What Happened

<!-- What did the agent output that was wrong? -->

## What I Expected

<!-- What should have happened instead? -->

## How to Reproduce

1. <!-- Step 1 — exact user message -->
2. <!-- Step 2 — mode selected (Quick/Standard/Deep Dive) -->
3. <!-- Step 3 — which lenses were loaded -->
4. <!-- Step 4 — where the output went wrong -->

## Input

```
<!-- Exact user message that triggered the bug -->
```

## Output (or relevant excerpt)

```
<!-- Paste the output that demonstrated the bug -->
```

## Lens / Framework Affected

- [ ] 01-signal-scan
- [ ] 02-demand-gap
- [ ] 03-arbitrage-pattern
- [ ] 04-leverage-map
- [ ] 05-network-path
- [ ] 06-anti-bias-audit
- [ ] 07-exponential-potential
- [ ] fang-yuan-mindset
- [ ] ecr-model
- [ ] effectuation
- [ ] asymmetric-execution
- [ ] SKILL.md (routing / output format)
- [ ] subagent-prompts
- [ ] ledger
- [ ] research-protocols
- [ ] intake
- [ ] other: _________

## Severity

- [ ] **Critical** — skill produces harmful or fraudulent output
- [ ] **High** — skill produces obviously wrong analysis
- [ ] **Medium** — skill produces misleading-but-not-wrong analysis
- [ ] **Low** — cosmetic / formatting / documentation issue

## Suggested Fix (optional)

<!-- If you have an idea how to fix it, describe here. PRs welcome. -->

## Environment

- Skill version: <!-- commit hash or tag -->
- Agent runtime: <!-- opencode / Cursor / other -->
- Model: <!-- if relevant -->

## Safety Floor Check (if relevant)

- [ ] This bug caused the skill to recommend something that violates the Safety Floor
      (fraud, exploitation of vulnerable parties, ToS violation, KYC bypass)
