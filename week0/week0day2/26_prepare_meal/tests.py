import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 26 - Spam and Eggs module"""
    def test_unique_prepare_meal(self):
        self.assertEqual("eggs", solution.prepare_meal(5))
        self.assertEqual("spam", solution.prepare_meal(3))
        self.assertEqual("spam spam spam", solution.prepare_meal(27))
        self.assertEqual("spam and eggs", solution.prepare_meal(15))
        self.assertEqual("spam spam and eggs", solution.prepare_meal(45))
        self.assertEqual("", solution.prepare_meal(7))


if __name__ == '__main__':
    unittest.main()