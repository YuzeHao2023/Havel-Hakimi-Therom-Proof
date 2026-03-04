import unittest
from havel_hakimi import is_graphic

class TestHavelHakimi(unittest.TestCase):
    def test_trivial(self):
        self.assertTrue(is_graphic([]))
        self.assertTrue(is_graphic([0, 0, 0]))

    def test_graphic(self):
        self.assertTrue(is_graphic([3,3,2,2,2,1,1,1,1]))
        self.assertTrue(is_graphic([1,1,1,1]))

    def test_non_graphic(self):
        self.assertFalse(is_graphic([4,4,3,1]))
        self.assertFalse(is_graphic([3,3,3]))
        self.assertFalse(is_graphic([2,2,2,1]))
        # Königsberg seven-bridges problem
        self.assertFalse(is_graphic([5,3,3,3]))

if __name__ == '__main__':
    unittest.main()
