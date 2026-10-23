# Select computational tools by capability

> Part of `investigate`. Apply this policy across public-key, symmetric,
> implementation, and formal-method work. Select tools according to the required
> computation, evidence standard, and capabilities visible from the host.

## Decide what the investigation needs

Before the first load-bearing computation, and again when a new hypothesis
changes the method, identify the required capabilities. Examples include:

- exact finite-field, polynomial, group, lattice, or number-theoretic algebra;
- numerical simulation, statistics, inference, optimization, or visualization;
- SAT, SMT, CP, MILP, Gröbner-basis, or exhaustive search;
- compilation, profiling, tracing, fuzzing, or implementation measurement;
- proof checking, certificate replay, or symbolic protocol analysis.

Use computation when it can establish a value, falsify a hypothesis, validate a
model, or produce replayable evidence. Do not run a tool merely because it is
available, and do not silently replace a required exact computation with a
floating-point approximation or an informal estimate.

## Discover before installing

Resolve each required capability in this order:

1. Inspect the tools, execution environments, and approved compute resources
   visible from the current platform.
2. Check for suitable executables on `PATH` **inside the actual analysis
   execution context**. A program visible in the user's terminal may be absent
   from a sandbox or managed kernel.
3. Check existing platform-managed environments and project environments.
4. If supported and justified, create an isolated managed environment with a
   pinned, recorded specification. Prefer a separate environment for large or
   tightly coupled systems such as SageMath rather than expanding a general
   scientific environment.
5. Use an already configured, permission-controlled remote compute or SSH
   resource when the local options are absent, licensed only on the remote host,
   or materially unsuitable for the workload.
6. If no suitable route exists, mark the computation `BLOCKED` or `NOT CHECKED`
   and name the missing capability and the claims it affects.

Do not install over a suitable existing tool. Do not mutate an environment while
another computation is using it. Wait for environment creation or package
operations to finish, then run a minimal version and functionality check before
the real workload.

## Choose the implementation on its merits

The following implementations are illustrative; consider other available tools
when they provide a better fit:

| Capability | Possible implementations |
|---|---|
| exact algebra and number theory | SageMath, Magma, PARI/GP, GAP, Singular, FLINT/NTL-based programs |
| statistics and data analysis | R, Python with appropriate scientific libraries, Julia |
| symbolic and numerical mathematics | SageMath, SymPy, Mathematica, Maple, Julia, domain-specific programs |
| constraint and optimization search | CryptoMiniSat, CaDiCaL, Z3, cvc5, OR-Tools, SCIP, Gurobi, MiniZinc |
| lattice and cryptographic costing | maintained estimator packages, fplll/fpylll, G6K, scheme-specific tools |
| implementation experiments | the target's native compiler, build system, profiler, tracer, and test tools |
| formal or certified evidence | Lean, Rocq, Isabelle, EasyCrypt, ProVerif, Verus, or certificate checkers |

Select among available implementations using:

- semantic fit and exactness requirements;
- independent validation and certificate support;
- known version compatibility with the model or script;
- performance and resource limits at the required scale;
- reproducibility and availability to the intended reviewer;
- licensing, permissions, and execution isolation.

Choose the language and program according to the computation. For example, R may
fit a statistical symmetric-cryptanalysis experiment, SageMath or Magma may fit
exact algebra, and a standalone solver may fit a constraint problem. Use
proprietary software such as Magma only through an existing licensed local or
remote installation. Never automatically install, copy, or redistribute it.

## Preserve the platform's security model

Use the platform's managed execution, environment, permission, and remote-compute
interfaces. Do not bypass them with embedded credentials, ad hoc SSH command
construction, or unapproved host execution. Supply scripts and data through the
platform's supported staging mechanism, request any required access through its
normal approval flow, and apply bounded runtimes and resource limits.

Use the host's supported sandboxing, credential storage, environment management,
and job control. Retain an execution manifest yourself when none is supplied.
If execution is absent, return a derivation or clearly labeled unexecuted code
with the computational obligation still open.

## Make every material run reproducible

For a load-bearing computation, retain:

- the capability requested and why the selected implementation fits;
- executable or service name, resolved execution route, and version;
- managed environment name or remote resource label, without credentials;
- package, model, solver, and database versions that affect the result;
- exact script or command, inputs and their identifiers or hashes, parameters,
  random seeds, resource limits, and relevant environment variables;
- raw output, parsed result, runtime, exit status, warnings, and produced
  certificates or witnesses;
- at least one semantic sanity check or independent cross-check when the result
  is load-bearing.

Treat a missing executable, failed environment build, solver timeout, remote-job
failure, or unsupported model as a scoped tool result. Try a materially distinct
available route when appropriate, but do not repeat the same failing call in a
loop and do not turn tool failure into evidence for or against a cryptographic
claim.
