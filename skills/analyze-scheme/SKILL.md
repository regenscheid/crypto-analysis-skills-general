---
name: analyze-scheme
description: Map the complete attack surface of a cryptographic scheme by fixing its claims and parameters, identifying underlying problems and added structure, checking every applicable attack family and its preconditions, recomputing costs in named models, and locating thin margins or promising deviations. Use for new or modified schemes, parameter-security claims, NIST-category checks, construction reviews, attack prioritization, or the baseline phase of an active search for weaknesses. Covers public-key, lattice, multivariate, symmetric, and hash targets.
---

# Analyze a cryptographic scheme

Use [the environment guide](../investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text. Tool names
and Python record-keeping examples below apply only when those capabilities are
available. Without them, analyze the inspected evidence and keep a text record;
label missing source retrieval, computation, or independent checks explicitly.


Produce an attack-surface map, not an unqualified verdict. Use `investigate` as
the outer workflow when the task also includes discovery, validation, or formal
proof.

## Mathematical research assignment

For a research proposal or a stated mathematical question, use
[the research workflow](../investigate/reference/mathematical-research-workflow.md).
The full evaluation procedure below applies when that evaluation is requested;
a proposal or lemma does not require completing every assessment artifact.
Use supplied assumptions and prior results at their stated evidence strength.
A catalog link or published ingredient does not itself assign a paper audit;
see [paper use and verification](../investigate/reference/paper-use-and-verification.md).

## Fix scope and mode

Identify every evaluated layer:

- **primitive or hard problem** — mathematical object or permutation;
- **construction** — composition and claimed security notion;
- **parameter set** — concrete dimensions, distributions, rounds, and work
  factor;
- **implementation interface** — parsing, validation, failures, leakage, or
  faults, only when requested;
- **deployment** — protocol composition, nonce lifecycle, multi-user behavior,
  or operational assumptions, only when requested.

Infer `ASSESS` for a general scheme assessment and `DISCOVER` for mathematical
research and proposals. Select from the intended product, not isolated words
such as “new.” A bounded mathematical question may use only the relevant part
of this map; state its scope without claiming complete scheme coverage.

## Route by domain

Load the relevant domain orchestrator before selecting technique skills:

- `symmetric-cryptanalysis-orchestrator` for block/stream ciphers, hashes,
  permutations, modes, MACs, and AEAD;
- `public-key-cryptanalysis-orchestrator` for PKE, KEMs, signatures, key
  agreement, and mathematical assumptions;
- both for hybrid or mixed constructions;
- `formal-methods-router` only for a justified machine-checked obligation.

Use the detailed local checklists only for their domains:

- [`reference/lattice.md`](reference/lattice.md)
- [`reference/multivariate.md`](reference/multivariate.md)
- [`reference/symmetric.md`](reference/symmetric.md)

The imported orchestrators and technique skills cover additional public-key,
protocol, implementation-interface, and formal-method families. Do not force an
unlisted target into the nearest legacy checklist.

## Build the map

### 1. Freeze artifacts and claims

Record exact specification and implementation revisions, parameters, test
vectors, proofs, errata, encodings, and claimed categories or bit levels. Hash
or otherwise identify artifacts when possible.

Turn prose claims into explicit rows containing the security notion, attacker
powers, oracle/session model, success event, resources, and exclusions.

### 2. Normalize structure

Describe algorithms, algebraic objects, maps, distributions, encodings, state
transitions, validation rules, and assumption chains. Diff the construction
against its canonical or standardized relative and rank each added structure,
special distribution, symmetry, failure behavior, and interface seam.

### 3. Establish baselines

Search standards, primary specifications, papers, code, issue discussions, and
competition records for the exact version and its aliases. Extract attack
preconditions and full costs from source bodies, not abstracts or headlines.

Establish generic and family-specific baselines before judging specialized
attacks. Reuse checked baselines when the inputs, versions, and models match;
recompute affected quantities for changed dependencies or an explicit fresh
validation assignment. Name estimator versions, cost models, units, memory assumptions,
quantum access model, and uncertainty. Run arithmetic and estimators with actual
tools; do not rely on mental calculation for load-bearing numbers.

### 4. Cover every applicable family

Use the selected orchestrator to populate the `investigate` coverage ledger.
For each family:

1. state why it applies or which precondition fails;
2. bind the attack model to the actual target;
3. compute or source its best relevant cost;
4. compare it with generic and claimed baselines;
5. record missing models, artifacts, or computations as blocked or unchecked.

A tool exception, timeout, unsupported estimator model, or search miss is a
scoped result about the attempt—not evidence of security.

### 5. Locate the margins

Report:

- the cheapest known attacks under each defensible cost model;
- concrete margin against every claim;
- sensitivity to parameters, estimator choices, and implementation assumptions;
- deviations most likely to enable an improvement;
- the precise step where an attack would have to improve;
- missing evidence whose resolution could change the ranking.

For a mathematical research assignment, pass the relevant definitions, source
ingredients, and open questions to `discover-cryptanalysis`. Do not require a
complete assessment ledger before developing a selected mathematical question.
A requested proposal and a requested derivation have different completion rules.

## Computation discipline

Use `scripts/sweep.py` when its supported estimator model matches the target.
Before a sweep, run and time one representative instance, bound runtime, pin
versions, emit progress, and retain the exact input and output. If required
software is absent or the target is inadmissible, mark the row `NOT CHECKED` and
name the missing capability.

Never report a bare security exponent. Include time, data, memory, success,
preprocessing, verification, amortization, and the cost convention.

## Output contract

Return:

1. frozen target and claims;
2. skill trace and domain routing;
3. structure and assumption map;
4. known-result and generic-baseline table;
5. complete attack-family coverage ledger;
6. parameter and cost comparison;
7. ranked deviations and thin margins;
8. unchecked areas and next decisive work.

Use “no applicable attack found under these families, models, sources, and
budgets,” never “secure.” A reduced-round, weak-key, malformed-input,
related-key, multi-target, leakage, fault, or quantum result keeps that qualifier
in every conclusion.
