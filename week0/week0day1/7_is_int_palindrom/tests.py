import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 7 - Integer Palindromes module"""
    def test_is_int_palindrom(self):
        self.assertEqual(True, solution.is_int_palindrom(1))
        self.assertEqual(False, solution.is_int_palindrom(42))
        self.assertEqual(True, solution.is_int_palindrom(100001))
        self.assertEqual(True, solution.is_int_palindrom(999))
        self.assertEqual(False, solution.is_int_palindrom(123))


if __name__ == '__main__':
    unittest.main()