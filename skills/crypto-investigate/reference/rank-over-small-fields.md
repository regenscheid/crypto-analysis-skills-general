# Large rank computations over small fields

> Part of `crypto-investigate`. Read from [computation](computation.md) before
> estimating the time or memory of a rank, kernel or echelon form of a large
> matrix over a small finite field (a Macaulay, XL or linearisation matrix, for
> example), and before deciding that no method fits. The figures are examples
> measured in one library, not constants; measure the library you use.

## Estimate memory from the library's actual storage

Dense matrices over small fields are rarely stored at one byte per entry. In
Sage 10.9 (its reference manual, and measured):

| Field | Sage class (library) | Bits per entry |
|---|---|---|
| GF(2) | `Matrix_mod2_dense` (M4RI) | 1 |
| GF(2^e), 2 ≤ e ≤ 16 | `Matrix_gf2e_dense` (M4RIE) | e rounded up to a power of two: 2 for GF(4), 4 for GF(8) and GF(16), 8 up to GF(256), 16 up to GF(2^16) |
| GF(p), p < 2^8 | `Matrix_modn_dense_float` (LinBox) | 32, a float |
| GF(p), 2^8 ≤ p < 94,906,266 | `Matrix_modn_dense_double` (LinBox) | 64, a double |
| other fields, such as GF(9) or GF(2^17) | a generic dense matrix | an object reference per entry (about 16 bytes for GF(9)), and far slower |

Sparse storage keeps only the nonzero entries and their positions, but
elimination creates new nonzeros, so measure a sparse elimination's memory as it
runs, not from the starting count.

## Elimination needs more than the stored matrix

Elimination needs room for a working copy, a change of representation and
temporaries: about twice the stored matrix, often more. In Sage 10.9, on dense
square matrices, an in-place `echelonize()` peaked at 1.4 to 2.4 times the
stored matrix (2.3 to 2.4 for GF(16)), and `rank()` and `echelon_form()`, which
work on a copy, at 2.4 to 4 times (3.3 to 3.5 for GF(16)). M4RIE's
documentation says its PLE elimination converts the matrix to a bitsliced form
and back, and so uses more memory than its table-based elimination. Budget for
the call you will use.

## A subset of rows gives a lower bound

A subset of the rows has at most the rank of the whole matrix, so its rank is a
lower bound. It settles the question only when it reaches the value needed (the
number of columns, a proved upper bound, or the least value a claim needs); a
shortfall says nothing about the full matrix. A random subset with exactly as
many rows as the rank sought often falls short: on Macaulay matrices of random
quadratic systems, 28 of 40 such subsets did over GF(2) and 2 to 10 of 40 over
GF(16) (for uniformly random rows, about 71% and 7%). Take some extra rows
(with ten extra, at most 1 of 40 fell short) and try a fresh subset before
reading anything into a shortfall.

## Reuse the lower degrees

Systems built degree by degree often let a later degree start from the
elimination already done at a lower one. For homogeneous equations of degree δ,
the rows at degree d + 1 are spanned by the variables times a basis of the rows
at degree d, for d ≥ δ; the matrix form of the F5 algorithm uses the lower
degrees' echelon forms to drop rows that are combinations of others (Bardet,
Faugère and Salvy, doi:10.1016/j.jsc.2014.09.025, Proposition 8). Check that
the reuse holds for the system at hand (equations that are not homogeneous need
care) and start from the saved echelon form rather than rebuilding it.

## Measure with a pilot

A pilot at smaller sizes of the same structure tells time and memory better
than a formula. Run the method you will use at two or three sizes, record wall
time and peak memory, fit the growth, and check the fit at one more size before
extrapolating. For example, Sage 10.9's `rank()` over GF(16) took 1.1 s at
8,000 × 8,000 and 6.3 s at 16,000 × 16,000 on one machine: growth of about
n^2.5 at these sizes, not the n^3 of the textbook count.

Checked on 2026-11-28 against Sage 10.9's reference manual and source
(`matrix_gf2e_dense`, `matrix_mod2_dense`, `matrix_modn_dense_float`,
`matrix_modn_dense_double`) and M4RIE's headers (`gf2e.h`, `echelonform.h`),
with the measurements above made in Sage 10.9; the statement on reuse was
checked by derivation, a small Sage computation and the cited paper.
