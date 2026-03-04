# Havel-Hakimi-Theorem Proof and Implementation

This repository contains two complementary artefacts:

1. A **Lean 4 formalisation** of the Havel–Hakimi theorem (see
   `src/HavelHakimi.lean`).  The core lemma shows that a
   nonincreasing sequence is `hh_graphic` precisely when the
   sequence obtained by performing one Havel–Hakimi reduction is.
   This is the combinatorial heart of the classical proof.

2. A **Python implementation** of the Havel–Hakimi algorithm
   that decides whether a finite list of non‑negative integers
   is the degree sequence of a simple undirected graph.  The
   code is in `havel_hakimi.py` and can be run directly from the
   command line.


## Lean 4 proof

The Lean formalisation lives in a small mathlib project.  To
build and check the proof you need to have the Lean toolchain
installed; the usual `lake` commands work in the devcontainer:

```sh
lake env         # cd into the project root first
lake build       # compile the library and check the proofs
``` 

The main theorem of interest is the lemma `HavelHakimi.havel_hakimi`.


## Python usage

The algorithm can be invoked as a script or imported as a
module::

```python
>>> from havel_hakimi import is_graphic
>>> is_graphic([3,3,2,2,2,1,1,1,1])
True
>>> is_graphic([4,4,3,1])
False
```

On the command line:

```sh
$ python havel_hakimi.py 3 3 2 2 2 1 1 1 1
[3, 3, 2, 2, 2, 1, 1, 1, 1] -> True
```

You can also run the bundled unit tests:

```sh
python -m unittest test_havel_hakimi.py
```

## Havel–Hakimi theorem

To state the theorem precisely we fix some terminology.  A finite
sequence of non‑negative integers
$$d = (d_1, d_2, \\, \dots, d_n)$$ is called **graphical** if there
exists a simple (no loops or multiple edges) undirected graph on
vertices $v_1,\dots,v_n$ such that $	ext{deg}(v_i)=d_i$ for each
$i$.  Such a sequence is also known as a *degree sequence* of a
simple graph.

The **Havel–Hakimi procedure** is the following reduction step:

1. Sort the sequence in nonincreasing order; write it as
   $(d_1, d_2,\dots,d_n)$ with $d_1\ge d_2\ge \cdots\ge d_n$.
2. Remove the first term $d_1$ and subtract $1$ from each of the
   next $d_1$ entries.
3. If at any point a negative number occurs or there are fewer than
   $d_1$ remaining terms, the process stops and the sequence is
   declared non‑graphical.
4. Otherwise, repeat with the new sequence (after resorting).

The **Havel–Hakimi theorem** states that a sequence is graphical if
and only if this process eventually terminates in the all‑zero
sequence.  In other words, the greedy reduction preserves
graphicality and reduces the length of the sequence.

A convenient formulation (the one proved in the Lean file) is:

> Let $s = (d_1,\dots,d_n)$ be a nonincreasing list of naturals.  If
> $d_1\le n-1$ then $s$ is graphical iff the list obtained by
> deleting $d_1$ and subtracting $1$ from each of the next $d_1$
> elements (followed by resorting) is graphical.

### Proof sketch

The proof proceeds by a simple combinatorial argument.  Suppose
$s$ corresponds to a graph $G$ with vertices labelled so that
$	ext{deg}(v_i)=d_i$ and $d_1$ is the largest degree.  In
$G$, vertex $v_1$ is adjacent to exactly $d_1$ other vertices.
Remove $v_1$ and all incident edges; the remaining graph has
$n-1$ vertices whose degree sequence is exactly the list obtained by
subtracting $1$ from the $d_1$ neighbours of $v_1$ and leaving the
others unchanged.  Sorting does not affect the multiset of degrees,
so the reduced sequence satisfies the same condition.  Conversely,
given a graph realising the reduced sequence we can reconstruct a
graph for $s$ by adding a new vertex connected to the appropriate
$d_1$ vertices of highest degree.

The Lean formalisation abstracts away the graph argument and works
entirely with lists: the inductive predicate `hh_graphic` captures
"reducible to zero by repeated Havel–Hakimi steps" and the lemma
`HavelHakimi.havel_hakimi` proves the equivalence mentioned above.
The proof uses only simple list manipulations and `simp`.

### Königsberg seven‑bridges example

The historic Königsberg bridges problem can be phrased in terms of
graph degree sequences.  Four landmasses are connected by seven
bridges, giving the sequence `[5,3,3,3]`.  The Havel–Hakimi
algorithm quickly shows that this sequence is **not** graphical –
there is no simple graph with those degrees.  In the original
puzzle this shows that no Eulerian route crossing each bridge once
exists.

You can run the example script in `examples/konigsberg.py`:

```sh
python examples/konigsberg.py
```

It will print the degree sequence and the result of the test.
