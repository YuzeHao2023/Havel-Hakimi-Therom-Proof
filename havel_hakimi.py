"""Havel-Hakimi algorithm implementation.

Provides a routine to decide whether a finite sequence of
nonnegative integers is the degree sequence of a simple
undirected graph.

The implementation follows the standard greedy reduction: sort
in nonincreasing order, remove the first element `d`, subtract
1 from the next `d` entries, and repeat.  If at any point an
invalid operation is required (too large `d` or negative
values appear) the sequence is not graphical.  The sequence is
graphic iff the process terminates with all zeros.
"""
from __future__ import annotations

from typing import List


def is_graphic(sequence: List[int]) -> bool:
    """Return ``True`` if ``sequence`` is graphical.

    The list is not required to be sorted; the algorithm sorts
    internally.  Negative numbers are immediately rejected.  ``None``
    (or empty) sequences are considered graphical.
    """
    seq = list(sequence)  # work on a copy
    for x in seq:
        if x < 0:
            return False
    while True:
        # remove zeros and sort
        seq = [x for x in seq if x > 0]
        seq.sort(reverse=True)
        if not seq:
            return True
        d = seq.pop(0)
        if d > len(seq):
            return False
        for i in range(d):
            seq[i] -= 1
            if seq[i] < 0:
                return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Usage: python havel_hakimi.py 3 3 2 2 2 1 1 1 1")
        sys.exit(1)

    try:
        seq = [int(x) for x in sys.argv[1:]]
    except ValueError:
        print("All arguments must be integers.")
        sys.exit(1)
    print(seq, "->", is_graphic(seq))
