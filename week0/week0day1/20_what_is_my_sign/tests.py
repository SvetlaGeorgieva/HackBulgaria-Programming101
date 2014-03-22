import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 20 - What is the sign? module"""
    def test_what_is_my_sign(self):
        self.assertEqual("Leo", solution.what_is_my_sign(5, 8))
        self.assertEqual("Aquarius", solution.what_is_my_sign(29, 1))
        self.assertEqual("Cancer", solution.what_is_my_sign(30, 6))
        self.assertEqual("Gemini", solution.what_is_my_sign(31, 5))
        self.assertEqual("Aquarius", solution.what_is_my_sign(2, 2))
        self.assertEqual("Taurus", solution.what_is_my_sign(8, 5))
        self.assertEqual("Capricorn", solution.what_is_my_sign(9, 1))


if __name__ == '__main__':
    unittest.main()