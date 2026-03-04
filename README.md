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
