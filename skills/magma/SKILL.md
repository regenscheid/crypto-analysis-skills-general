---
name: magma
description: Use an available licensed Magma installation for exact finite-field, polynomial, group, elliptic-curve, or linear-algebra computations supporting cryptanalysis. Check capability and provenance first; if Magma is unavailable, use a suitable available alternative or report the computation as blocked.
license: Apache-2.0
---

# Exact computation with Magma

Use Magma only when the session has access to a licensed local installation or
an already configured remote resource. Follow
[computation guidance](../investigate/reference/computation.md). No remote host,
SSH configuration, scheduler, wrapper API, thread count, or hardware is assumed.
Do not automatically install or redistribute proprietary software.

Identify the executable or service, version, input files, working directory,
resource limits, and output route. Use the host's actual execution interface.
If a local shell and `magma` are available, a batch invocation can be:

```sh
magma -b job.m < /dev/null
```

This is an example for a Unix-like shell, not an interface every session has.
Use equivalent supported input and job-control mechanisms elsewhere. Apply a
bounded runtime and inspect cancellation behavior for the actual runner.

## Confirm completion rather than trusting an exit code

Magma diagnostics and runner exit behavior can differ by version and wrapper.
Retain stdout, stderr, and exit status; inspect for error diagnostics and require
an explicit final completion marker. Results printed before a failure are partial.
For example:

```magma
SetQuitOnError(true);
P<x> := PolynomialRing(GF(2));
assert IsIrreducible(x^8 + x^4 + x^3 + x + 1);
printf "CRYPTO_JOB_COMPLETE\n";
```

Test the error path on a tiny job before trusting automated result collection.
A successful submission or cancellation receipt alone does not establish that
the computation completed or stopped. Use the configured runner's status and
process controls; do not infer remote termination from a local client timeout.

## Validate the mathematical model

Start with an instance whose answer is known. For polynomial solving, plant a
solution and confirm that the encoding and returned witness recover it. A basis
containing `1` may expose an inconsistent encoding rather than a broken scheme.

State the coefficient field, characteristic, extension representation, polynomial
ordering, and conventions. A polynomial irreducible over a base field can be
reducible over an extension. Compare exact returned objects rather than trusting
printed coercions. Measure thread count and resource usage instead of assuming
machine defaults. Do not extrapolate a toy timing to a security level without a
named cost model and applicable scaling evidence.

## Retain evidence

Keep the exact script, input hashes, seed, Magma version, resource configuration,
raw output, completion check, and mathematical sanity checks with each material
result. State what the computation establishes and its limits. With persistent
storage, optionally use `workbench-knowledge`; otherwise return the evidence and
unsaved research handoff in the conversation. If Magma is unavailable, identify
a suitable alternative or leave the exact obligation `BLOCKED`; an unexecuted
script is not a computational result.
