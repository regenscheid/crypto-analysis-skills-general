# Read historical cases for mathematical insight

Use a case to clarify a concept, compare assumptions, or explain a boundary.
Do not require reproducing the historical result to record the idea it illustrates.
For a substantive mathematical dependency, inspect the relevant source statement
or supply the needed derivation. Follow [paper use](paper-use-and-verification.md).

If an optional catalog is connected, its `get_catalog_info` may list editorial
reading guides. Without it, use inspected primary sources for the same comparisons.
Selected records from `get_attack` include their applicable `reading_guides` with
source IDs, locators, and the scope of the editorial review. Older servers may
omit these fields; ordinary record/source reads still work. Cite the returned
snapshot and canonical IDs. Missing guides indicate incomplete reference curation.

| Mathematical reading question | What the comparison should expose |
|---|---|
| Which distribution is required? | Distinguish marginals, joint distributions, conditioning, and implementation observations. Uniform marginals do not imply independence. |
| What work or information is shared? | Name the population and the event whose probability or cost is being discussed. A per-instance quantity and an amortized quantity answer different questions. |
| Which representation preserves the claim? | State the map and properties it preserves. Shared vocabulary across families is not a mathematical correspondence. |
| What follows about the construction? | Keep a component, reduced version, changed access model, and full-construction claim separate; identify the missing implication. |
| What changed between versions? | Distinguish an improved bound, a corrected claim, a changed construction, and a new observation model. Supersession alone does not make the old theorem false. |
| What is the proposed additional contribution? | Separate applying the same result, evaluating a new case, extending its assumptions, and introducing a new method. |

Choose the question that matters to the current mathematical work. This is a
reading guide, not a checklist to run in full or a procedure for generating
attacks. Changing examples and citation details belong in the catalog; these
interpretive distinctions remain in the skills.

When recording what was learned, separate the source's actual claim from the
editor's explanatory analogy and the current investigation's conjecture. An
editorial note may have only metadata-level support; its presence is not an
independent paper verification. A missing locator should remain missing until
the passage has actually been inspected.
