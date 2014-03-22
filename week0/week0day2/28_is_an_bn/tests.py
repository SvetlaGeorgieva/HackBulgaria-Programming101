import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 28 - Word from a^nb^n module"""
    def test_is_an_bn(self):
        self.assertEqual(True, solution.is_an_bn(""))
        self.assertEqual(False, solution.is_an_bn("rado"))
        self.assertEqual(False, solution.is_an_bn("aaabb"))
        self.assertEqual(True, solution.is_an_bn("aaabbb"))
        self.assertEqual(False, solution.is_an_bn("aabbaabb"))
        self.assertEqual(False, solution.is_an_bn("bbbaaa"))
        self.assertEqual(True, solution.is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
    unittest.main()