# Symmetric cryptanalysis: specialist skills

Generated from `config/skill-registry.json` by `tools/family_tables.py`;
do not edit by hand. 28 skills. Read a skill before claiming to
use its procedure; a skill not installed is unavailable, not inapplicable.

| Skill | For |
|---|---|
| `algebraic-sat-smt-cp-and-cube-analysis` | Model a symmetric primitive as equations or exact constraints and evaluate SAT/SMT/CP, algebraic and cube attacks. |
| `arx-differential-rotational-rx-analysis` | Analyze addition-rotation-XOR (ARX) designs with carry-aware differential models, rotational and RX properties, constants and key schedules. |
| `automated-search-model-builder` | Build, validate and audit exact or relaxed solver models for symmetric-cryptanalysis searches (trails, division properties, impossible transitions, MITM cuts). |
| `boomerang-and-rectangle-analysis` | Build boomerang, amplified-boomerang and rectangle attacks on symmetric primitives with dependence-aware middle transitions and quartet-level data accounting. |
| `differential-family-analysis` | Find, evaluate, cluster and extend XOR, modular, truncated, higher-order and mixed differential properties of symmetric primitives. |
| `differential-linear-analysis` | Construct and validate differential-linear distinguishers and key recovery on symmetric primitives without assuming unjustified independence at the middle connection. |
| `distinguisher-to-key-recovery-extension` | Extend a symmetric distinguisher or structural property into key or state recovery with explicit round boundaries, filtering, ranking, false positives and verification. |
| `generic-baseline-calculator` | Compute exact generic and exhaustive-attack baselines for a symmetric security model so attacks are compared against the right target. |
| `hash-and-permutation-analysis` | Evaluate hash functions, XOFs, compression functions, sponges and public permutations for collision, preimage, distinguishing, multicollision, herding and sponge-specific attacks. |
| `impossible-differential-and-zero-correlation-analysis` | Construct exact impossible differentials and zero-correlation linear properties of symmetric primitives and evaluate elimination and statistical key-recovery attacks. |
| `integral-and-division-property-analysis` | Find and verify integral properties of symmetric primitives with structured sets, algebraic degree and division properties, and extend them to key recovery. |
| `linear-family-analysis` | Analyze linear approximations, trails, hulls and multiple or multidimensional linear attacks on symmetric primitives with sign and dependency accounting. |
| `mitm-dissection-and-biclique-analysis` | Design and audit meet-in-the-middle attacks on symmetric primitives: cuts, partial matching, splice-and-cut, initial structures, dissection and bicliques. |
| `mode-mac-and-aead-analysis` | Analyze symmetric modes, MACs, key wrap and AEAD for privacy, authenticity, nonce behavior, tag bounds, domain separation, multi-user effects and misuse. |
| `primitive-structure-and-assumption-mapper` | Map the exact structure and assumptions of a symmetric primitive or construction to expose attack-relevant dependencies before choosing techniques or encoding a search. |
| `quantum-symmetric-attack-analysis` | Formalize Q1/Q2 quantum access and evaluate Grover, collision, period-finding and hybrid quantum attacks on symmetric constructions with concrete oracle, depth, qubit and verification costs. |
| `rebound-analysis` | Construct inbound-outbound (rebound) attacks on wide permutations and hash-like designs with explicit degrees of freedom, nonlinear matching and outbound probabilities. |
| `related-key-and-tweakey-analysis` | Formalize realistic key and tweak relations, propagate them through schedules, and evaluate related-key and tweakey differentials, symmetries and key recovery. |
| `security-model-and-claim-formalizer` | Turn informal symmetric-cryptography security statements into explicit games, adversary powers, success events, resources and non-goals. |
| `security-proof-and-bound-auditor` | Audit symmetric constructions' security games, reductions, bad-event bounds, concrete constants, idealized models and instantiation. |
| `slide-invariant-subspace-and-symmetry-analysis` | Find exploitable self-similarity in symmetric primitives: slid pairs, invariant subspaces and partitions, fixed structures and weak-key symmetries, checking constants and schedules. |
| `stream-cipher-analysis` | Analyze stream-cipher initialization and keystream generation with correlation, algebraic and cube, guess-and-determine, state-recovery, resynchronization and time-memory-data attacks. |
| `symmetric-attack-complexity-and-success-auditor` | Recompute a symmetric attack end to end, normalize resource units, check success probability and false positives, and compare it with the right generic baseline and claim. |
| `symmetric-attack-hypothesis-generator-and-triage` | Generate falsifiable symmetric attack hypotheses from claims, design features, literature and reduced-round findings, then rank them by claim impact and information gain. |
| `symmetric-attack-transfer-and-adaptation` | Decompose a symmetric attack from the literature or prior work, map each indispensable requirement to a new target, and develop minimal falsifiable adaptations. |
| `symmetric-evidence-synthesis-and-research-backlog` | Turn symmetric attack records, proofs, reproductions, failures and disagreements into claim-level judgments and a ranked, falsifiable research agenda. |
| `symmetric-literature-attack-extractor` | Extract a published or discovered symmetric-cryptanalysis result into a normalized, source-grounded attack record for reproduction and transfer. |
| `symmetric-reproduction-and-falsification-planner` | Design decisive, controlled, reproducible tests of symmetric-cryptanalysis claims, from exhaustive toy checks to full experiments and solver certificates. |
