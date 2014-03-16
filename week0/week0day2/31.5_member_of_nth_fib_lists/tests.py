import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Problem 31.5 - Is member of nth fibonacci lists module"""
    def test_member_of_nth_fib_lists(self):
        self.assertEqual(False, solution.member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
        self.assertEqual(True, solution.member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
        self.assertEqual(True, solution.member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))
        self.assertEqual(False, solution.member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))


if __name__ == '__main__':
    unittest.main()