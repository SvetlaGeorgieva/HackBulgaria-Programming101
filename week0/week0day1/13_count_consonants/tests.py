import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 13 - Consonants in a string module"""
    def test_count_consonants(self):
        self.assertEqual(4, solution.count_consonants("Python"))
        self.assertEqual(11, solution.count_consonants("Theistareykjarbunga"))
        self.assertEqual(7, solution.count_consonants("grrrrgh!"))
        self.assertEqual(44, solution.count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
        self.assertEqual(6, solution.count_consonants("A nice day to code!"))


if __name__ == '__main__':
    unittest.main()