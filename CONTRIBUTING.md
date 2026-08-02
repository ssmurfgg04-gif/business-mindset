# Contributing to business-mindset

Thanks for your interest in improving this skill. This document explains
how to extend it correctly.

## Skill Design Principles

Before contributing, understand the design philosophy:

1. **Lenses are checkable, not platitudinous.** Every signal, check, or
   weak-link test must be concretely answerable from public information.
   "Is the market large?" is bad. "Is the TAM > $1B per [specific source]?"
   is good.

2. **Frameworks have citations or are explicitly labeled as synthesis.**
   The ECR model and Effectuation are peer-reviewed academic frameworks.
   The Fang Yuan Mindset is the author's synthesis of Stoicism, Sun Tzu,
   Machiavelli, Soros, and Taleb — labeled as such. Don't present opinion
   as cited research.

3. **Anti-bias is enforced, not suggested.** The 06-anti-bias-audit.md lens
   is a hard gate. Every output passes through it. Don't add lenses or
   frameworks that bypass this gate.

4. **Expansion before contraction.** The ECR model requires 15-20+ candidates
   per lens before any contraction. Don't add shortcuts that collapse to
   "top 3" prematurely.

5. **Pre-mortem is mandatory for PASS.** Don't add PASS conditions that
   skip the pre-mortem step.

6. **Safety floor is non-negotiable.** The Fang Yuan Mindset's cold
   rationality is for analysis, not predation. Don't add axioms, lenses,
   or anti-patterns that violate the Floor (fraud, exploitation of
   vulnerable parties, ToS violation, KYC bypass).

## How to Add a New Lens

1. **Check if it's already covered.** Read all 7 existing lenses. Many
   "new lens" ideas are actually sub-cases of existing lenses.

2. **If genuinely new**, create `references/lenses/NN-name.md` where NN is
   the next number (08, 09, etc.). Use the established format:
   - Core Question
   - When to Use / When NOT to Use
   - Search Strategies
   - What to Extract (table format)
   - Bias Warnings
   - ECR Phase Discipline (expansion 15-20+, contraction 3-5)
   - Weak Link: What Kills This?
   - Time Horizon Tagging
   - Output (expansion + contraction formats)

3. **Update SKILL.md** routing table with the new lens.

4. **Update SCHEMA.md** file tree.

5. **Add a worked example** in `examples/` showing the lens applied to a
   real opportunity.

6. **Submit a PR** with all 5 changes (lens file, SKILL.md, SCHEMA.md,
   example, PR description explaining why this lens is needed and not
   covered by existing ones).

## How to Add a New Framework

1. **Verify it has academic grounding OR is explicitly the author's synthesis.**
   Don't add frameworks that are "just an idea."

2. **If academic**, include full citation (authors, year, journal, DOI).
   Verify the citation is real — don't fabricate.

3. **Create `references/frameworks/name.md`** with:
   - Source citation
   - Core insight
   - Key principles
   - Application to this skill (which lenses it informs, how)
   - Key warnings / anti-patterns

4. **Update SKILL.md** to reference the framework in the appropriate places.

5. **Update SCHEMA.md**.

## How to Add an Anti-Pattern

Anti-patterns go in `references/lenses/07-exponential-potential.md` under
the "Anti-Patterns: Fake Exponentials" section, OR in
`references/lenses/06-anti-bias-audit.md` under "Familiarity Trap
Counter-Patterns."

Each anti-pattern must include:
- **Name** (memorable)
- **What it looks like** (concrete description)
- **Why it fails** (the structural reason)
- **Real example** (named company or known case)

## How to Improve an Existing Lens

1. **Open an issue first** describing the proposed change and why. Don't
   submit a PR for a major lens rewrite without discussion.

2. **Small improvements** (new search query patterns, new weak-link test,
   new bias warning) can be PR'd directly.

3. **Keep the format consistent.** Don't restructure a lens file to a
   different format than the others.

## How to Report a Bug

Use the bug-report issue template. Bugs include:
- Lens gives obviously wrong output on a specific input
- Formula computes incorrectly
- Routing table sends user to wrong lens
- Anti-bias gate fails to catch an obvious anti-pattern
- Sub-agent prompt is ambiguous or broken

## How to Request a New Lens or Feature

Use the lens-request issue template. Include:
- The question the new lens would answer
- Why existing lenses don't cover it
- 2-3 concrete examples of opportunities where this lens would add value
- Whether you'd be willing to write the lens yourself

## Style Guide

- **Voice**: Direct, technical, slightly cold. The Fang Yuan Mindset
  governs tone — no marketing language.
- **Headers**: ATX (#, ##, ###). No setext.
- **Tables**: GitHub-flavored markdown.
- **Code blocks**: Always specify language for syntax highlighting.
- **Emphasis**: Use **bold** for defined terms on first use. Use *italics*
  sparingly, for emphasis.
- **Emojis**: Avoid in skill files. OK in README and issue templates.
- **Citations**: Full academic format (Authors, Year, *Journal*, Volume(Issue),
  pages. DOI).
- **Cross-references**: Use full relative paths on first reference in each
  file (e.g., `references/frameworks/asymmetric-execution.md`), short name
  thereafter.

## Testing

There's no automated test suite (yet). Before submitting a PR:

1. **Manually trace** your change through the pipeline. Pick a sample
   query ("find me an opportunity in [X]") and walk through which lenses
   load, what they output, how the anti-bias gate handles it.

2. **Check the formulas**. If you change the Systemic Edge formula or
   Lens 07 scoring, verify the math still works on the golden-output
   example.

3. **Check cross-references**. If you rename a file, update all
   references to it across the skill.

## License

By contributing, you agree that your contributions will be licensed under
the MIT license (see LICENSE file).
