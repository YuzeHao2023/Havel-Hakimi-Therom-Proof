"""Example using the Havel--Hakimi algorithm to analyse the
Königsberg seven-bridges problem.

The historic puzzle can be modelled as a graph with four "land"
vertices joined by seven bridges.  The degree sequence of this
graph is

    [5, 3, 3, 3]

(the landmass corresponding to the two islands has five bridges
attached; the three riverbanks each have three).  Because the
maximum degree exceeds the number of other vertices and, more
fundamentally, because all four degrees are odd, the sequence is
not graphical: there is no simple graph with those degrees.
Using the Havel–Hakimi test below confirms this, which in the
original argument shows there cannot be an Eulerian tour that
traverses each bridge exactly once.
"""

from havel_hakimi import is_graphic


def main() -> None:
    sequence = [5, 3, 3, 3]
    print("Königsberg degree sequence:", sequence)
    print("Graphic?", is_graphic(sequence))


if __name__ == "__main__":
    main()
