# 301-problem study expansion: coverage and verification

**All 301 pages have an additional walkthrough section.** The original 26 have concrete worked numerical examples; 2 more (#403 and #4023) have independently constructed examples and trace tables. The other 273 have source-grounded code-landmark tables, a symbolic dry-run worksheet, and a control-flow diagram, **not yet validated problem-specific numerical dry runs**. Do not confuse this structural coverage with 301 fully verified mathematical proofs.

| Coverage | Count |
|---|---:|
| Original C++ solution pages preserved | 301 |
| Worked numerical examples | 28 |
| Code-grounded symbolic walkthroughs newly added | 275 |
| Remaining without verified numerical dry runs | 273 |

## How to use

Open [the problem master index](Problem-Master-Index.md), select a problem, and use its **Source-grounded algorithm walkthrough** to match the original C++ to state/transition/termination. For fully numerical examples, see the existing 26 problem pages from the previous edition and [Frog Jump](Problems/403.md) or [Elevator Requests II](Problems/4023.md).

## Why verification matters

Many of the 301 accepted solutions do not use the same algorithm as their broad concept-family template. A numerical example, state table, or proof should only be labeled verified when it has been derived against the actual problem and solution. This edition explicitly distinguishes verified examples from code-based study scaffolding.
