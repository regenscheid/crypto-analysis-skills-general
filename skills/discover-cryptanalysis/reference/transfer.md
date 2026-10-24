# Transfer results from adjacent fields

Use this reference after normalizing the cryptographic target into mathematical
objects. Search by object, invariant, and mechanism; do not search only by the
scheme name or the word “attack.”

## Build a transfer map

For each source result, fill this map before treating it as a candidate:

| Obligation | Question |
|---|---|
| source object | What exact category of object does the result act on? |
| source operation | Which operation, oracle, or representation does it use? |
| target object | What concrete part of the scheme is proposed as that object? |
| morphism | Which map carries the source object and operation to the target? |
| preserved property | Which rank, product, metric, distribution, or invariant survives the map? |
| source assumptions | Which algebraic, probabilistic, asymptotic, or oracle hypotheses are required? |
| target evidence | Where is each hypothesis established for the real parameter set? |
| consequence | Which named security objective changes if the transfer works? |
| falsifier | What is the smallest observation that would disprove applicability? |

Reject an analogy that cannot name the morphism and preserved operation. Shared
terminology, equal dimension, or similar-looking equations do not establish a
transfer.

## Route structural handles

Use the table to seed searches, then follow citations in both directions. Treat
these as search neighborhoods, not claims of applicability.

| Structural handle | Search neighboring fields and mechanisms |
|---|---|
| low rank, hidden subspace, bilinear map | matrix/tensor recovery, tensor decomposition, MinRank, algebraic statistics, incidence geometry |
| sparse or biased secret/error | compressed sensing, sparse recovery, hypothesis testing, learning theory, statistical-query lower bounds |
| polynomial system or rational map | computational algebraic geometry, elimination, invariant theory, resultants, tensor rank, constraint solving |
| code or noisy linear relation | decoding, list decoding, locally testable codes, coding bounds, planted inference |
| lattice or module relation | geometry of numbers, integer programming, module algorithms, random matrix theory |
| group action, orbit, or symmetry | representation theory, invariant theory, orbit algorithms, harmonic analysis, hidden-subgroup methods |
| ring, ideal, or field extension | commutative algebra, module theory, restriction of scalars, CRT decompositions, norm and trace methods |
| noncommutative multiplication | matrix algebras, representation theory, module and ideal structure; exclude commutative-field results unless embedded |
| iterative rounds or local constraints | coding theory, graph expansion, MILP/SAT/SMT, combinatorial optimization, automated reasoning |
| differential, linear, or correlation bias | probability, Fourier/harmonic analysis, additive combinatorics, statistical distinguishers |
| collision or multicollision structure | random graphs, occupancy, subset algorithms, time-memory-data tradeoffs |
| planted versus random distribution | average-case complexity, contiguity, spectral methods, low-degree methods, statistical physics |

Search the source mechanism in three forms:

1. its field's native name
2. the target object's mathematical name
3. the predicted cryptanalytic consequence

Then search the proposed application directly with scheme aliases, problem
variants, and structural synonyms. Record exact queries and channels even when
they return nothing.

## Check structural mismatches

Fail a transfer immediately when its load-bearing structure is absent.

### Field extension versus matrix ring

Do not transfer a field-extension result to a full matrix ring merely because
both have the same dimension as vector spaces over the base field.

For an extension field `F_(q^d)`:

- multiplication is commutative
- every nonzero element is invertible
- there are no nonzero zero divisors
- Frobenius, trace, and norm obey field identities
- subfields exist only under their divisibility conditions

For `M_l(F_q)` with `l > 1`:

- multiplication is generally noncommutative
- nonzero singular matrices are not invertible and are zero divisors
- one-sided ideals and invariant subspaces affect algorithms
- the determinant is not a field norm for arbitrary algebra transfers

Accept the transfer only after constructing an actual embedded commutative
field or subalgebra, proving that every operation used by the source result
stays inside it, and mapping the target distribution into that image. Otherwise
mark the multiplicative-structure obligation `unchecked` unless a concrete
counterexample proves that it fails. Failure to establish closure is not proof
that closure is absent.

### Other recurring mismatches

Check each pair explicitly:

- worst-case theorem versus average-case or planted target
- existential theorem versus constructive algorithm
- reduction from A to B versus the direction needed to attack A
- uniform random input versus structured keys or correlated samples
- independent samples versus reuse, compression, or conditioning
- asymptotic improvement versus the concrete parameter range
- classical access versus quantum, chosen-input, related-key, or leakage access
- scalar field arithmetic versus module, quotient-ring, or noncommutative
  arithmetic
- exact invariant versus approximate, noisy, or truncated observation
- reduced-round or weakened instance versus the full primitive

Treat an unchecked mismatch as an unchecked assumption, not as evidence for the
candidate.

## Choose cheap falsifiers

Use the least expensive decisive test:

- **Type test:** construct the objects and test closure, commutativity,
  invertibility, dimensions, rank, or ideal membership.
- **Direction test:** draw the reduction arrows and verify that an algorithm for
  the source problem yields the desired target algorithm.
- **Parameter test:** substitute real parameters into every inequality,
  probability bound, and sample requirement.
- **Distribution test:** compare the assumed and actual support, independence,
  bias, and conditioning; use a null model when computation helps.
- **Tiny positive case:** plant the required structure and confirm the mechanism
  detects or exploits it.
- **Negative control:** use a comparison with a justified prediction. Removing
  a sufficient assumption does not necessarily force failure.
- **Known-answer test:** reproduce a published result before trusting a new
  model or implementation.
- **Concrete-cost test:** include constants, memory, data, and success
  probability; find the crossover rather than quoting asymptotics.

Preserve stdout, stderr, parameters, versions, seeds, and failure messages for
computational tests. Diagnose what a failure establishes: the mathematical
claim, its mapping, and the implementation can have different failure modes.

## Separate established correspondence from an open question

An established transferred result needs the required object/operation mapping,
assumptions, and implication. State a missing correspondence as unresolved;
state a contradiction as defeating the particular argument that depends on it.
Neither belongs in an unconditional established conclusion.

These are requirements for a result, not a gate on which mathematical questions
may appear in a research proposal. A supporting lemma or conditional formulation
may be the next useful product before a decisive test exists. Use
[the research workflow](../../crypto-investigate/reference/mathematical-research-workflow.md)
for proposal breadth, research horizons, and meaningful intermediate progress.

## Record transfer provenance

Distinguish evidence:

- `paper`, `spec`, or other source: what the external result actually says
- `computation`: what was run and observed
- `derivation`: original mapping or consequence, marked `[DERIVATION]`
- `independent-check`: a separate re-derivation, proof audit, computation, or
  human review

Do not cite the source paper as evidence for the new mapping unless the paper
itself makes that mapping. Keep the source result and the original transfer as
separate provenance entries.
