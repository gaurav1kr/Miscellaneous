# GitHub math rendering audit

- All 301 problem pages inspected programmatically.
- Removed 280 potentially misleading generic formula sections.
- Converted 2 remaining display-math blocks in problem pages to literal fenced text, so GitHub cannot report KaTeX brace parsing errors from them.
- Replaced Problem 1218's unrelated LIS recurrence with the correct value-indexed recurrence and a numerical trace.
- This is a **rendering-safety pass**, not a mathematical verification of all 301 algorithms.
- Original C++ source blocks are retained.
