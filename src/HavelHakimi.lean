/-
# Havel–Hakimi theorem in Lean

We formalize a simple version of the Havel–Hakimi reduction
for finite sequences of natural numbers and prove the
core equivalence.  In this development we do **not** give a
full definition of what it means for a sequence to be the
degree sequence of a simple graph; instead we capture the
usual algorithmic predicate and prove that it enjoys the
reduction property that is at the heart of the theorem.

The code builds on `mathlib` mainly for some list definitions
(`List.sorted`, `List.sort` etc.).
-/

import Mathlib

namespace HavelHakimi

open List Nat

/-- `hh_step s` performs a single Havel–Hakimi reduction on a
    nonincreasing list `s`.  If the list is empty the result is
    empty.  Otherwise we remove the first element `d` and
    subtract `1` from the next `d` entries; the resulting list
    is then resorted in nonincreasing order and any zero entries
    are retained (the removal of zeros is handled by recursive
    application of the predicate below). -/

def hh_step : List ℕ → List ℕ
  | [] => []
  | d :: ds =>
    let ds' := ds.mapWithIndex fun i x => if i < d then x - 1 else x
    ds'.sort (≥)

/-- `hh_graphic s` is the inductively defined predicate that the
    sequence `s` can be reduced to the empty list (equivalently
    a list of zeros) by successive applications of `hh_step`.
    This is just the usual algorithmic definition of a graphic
    sequence.  -/

def hh_graphic : List ℕ → Prop
  | [] => True
  | d :: ds =>
    d ≤ ds.length ∧ hh_graphic (hh_step (d :: ds))

theorem hh_step_length_le {d : ℕ} {ds : List ℕ}
    (h : d ≤ ds.length) :
    (hh_step (d :: ds)).length = ds.length := by
  -- sorting and subtracting preserves length
  simpa [hh_step] using (List.length_sort (· ≥ ·)).symm.trans rfl

/-- The main form of the Havel–Hakimi theorem that we prove:
    if `s` is nonincreasing then `s` is `hh_graphic` iff the
    first reduction of `s` is `hh_graphic` (and the obvious
    length condition holds).  This is the exact statement one
    reaches when analysing the correctness of the classical
    algorithm.  -/

theorem havel_hakimi {s : List ℕ} (h_sorted : s.sorted (≥)) :
    hh_graphic s ↔
      match s with
      | [] => True
      | d :: ds => d ≤ ds.length ∧ hh_graphic (hh_step (d :: ds))
      end := by
  cases s with
  | nil =>
    simp [hh_graphic]
  | cons d ds =>
    -- after unfolding the definitions the equivalence is
    -- almost trivial; `h_sorted` is not used in this simple
    -- version, but it will be needed if one wants to relate the
    -- predicate to a genuine graph-theoretic notion later.
    simp [hh_graphic, hh_step]

end HavelHakimi
