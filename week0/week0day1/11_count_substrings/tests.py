import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 11 - Counting substrings module"""
    def test_count_substrings(self):
        self.assertEqual(2, solution.count_substrings("This is a test string", "is"))
        self.assertEqual(2, solution.count_substrings("babababa", "baba"))
        self.assertEqual(4, solution.count_substrings("Python is an awesome language to program in!", "o"))
        self.assertEqual(0, solution.count_substrings("We have nothing in common!", "really?"))
        self.assertEqual(2, solution.count_substrings("This is this and that is this", "this"))


if __name__ == '__main__':
    unittest.main()