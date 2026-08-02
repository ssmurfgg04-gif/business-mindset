# SCHEMA.md — Business Mindset Skill v2.0 State & Architecture

## Typed State Schema (`BusinessOpportunityState`)

```python
from typing import TypedDict, Literal, List, Optional
from pydantic import BaseModel, Field

class MarketAssumption(BaseModel):
    assumption: str
    validated: bool
    source: str
    data_point: str
    confidence: int = Field(ge=0, le=100)

class LensOutput(BaseModel):
    lens_name: str
    score: int = Field(ge=0, le=32)
    reasoning: str
    signals: List[str]
    warnings: List[str]

class PersonaOutput(BaseModel):
    persona: Literal["Operator", "Steward", "Adversary"]
    verdict: Literal["PASS", "FLAG", "REJECT", "KILLED"]
    confidence: int = Field(ge=0, le=100)
    reasoning: str
    specific_evidence: List[str]

class RiskAssessment(BaseModel):
    post_loss_runway_months: float
    kelly_fraction: float
    max_position_size_dollars: float
    max_time_hours_per_week: int
    survival_probability: float
    veto_override: bool = False
    veto_reason: Optional[str] = None

class ValidationStep(BaseModel):
    day: int
    action: str
    tool: str
    success_criteria: str
    kill_criteria: str

class BusinessOpportunityState(TypedDict):
    user_query: str
    user_context: dict
    mode: Literal["quick", "standard", "deep"]
    market_assumptions: List[MarketAssumption]
    platform_viability: Literal["GREEN", "YELLOW", "RED"]
    lens_outputs: List[LensOutput]
    persona_outputs: List[PersonaOutput]
    risk_assessment: Optional[RiskAssessment]
    validation_playbook: Optional[List[ValidationStep]]
    final_verdict: Optional[Literal["PASS", "FLAG", "REJECT"]]
    final_confidence: Optional[int]
    final_output: Optional[str]
    execution_log: List[str]
    search_count: int
    errors: List[str]
```

## File Tree

```
business-mindset/
│
├── SKILL.md                          ← Entry point (Router, <500 tokens).
├── SCHEMA.md                         ← THIS FILE. State schema & file map.
├── README.md
├── LICENSE                           ← MIT.
├── CONTRIBUTING.md
│
    ├── references/
    │   ├── agents/
    │   │   ├── reality-check.md          ← Market data validation agent
    │   │   ├── adversary-prompt.md       ← Enforced adversary agent
    │   │   └── risk-manager.md           ← Kelly criterion & survival math veto gate
    │   ├── playbooks/
    │   │   └── validation-saas.md        ← 7-day SaaS validation sprint
    │   ├── validation/
    │   │   └── case-studies.md           ← Historical scored examples & base rates
    │   ├── frameworks/
    │   │   ├── lookback-validation.md    ← Base-rate checking protocol
    │   │   ├── asymmetric-execution.md
    │   │   ├── sell-before-mvp.md        ← Pre-sale & deposit validation protocol
    │   │   └── vc-wisdom-playbook.md     ← YC, Sequoia, a16z startup principles
    │   ├── business-classics-compendium.md ← 12 business & growth book summaries
    │   └── lens-index.md                 ← Progressive loading map
```
