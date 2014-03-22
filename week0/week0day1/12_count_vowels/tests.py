import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 12 - Vowels in a string module"""
    def test_count_vowels(self):
        self.assertEqual(2, solution.count_vowels("Python"))
        self.assertEqual(8, solution.count_vowels("Theistareykjarbunga"))
        self.assertEqual(0, solution.count_vowels("grrrrgh!"))
        self.assertEqual(22, solution.count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
        self.assertEqual(8, solution.count_vowels("A nice day to code!"))


if __name__ == '__main__':
    unittest.main()