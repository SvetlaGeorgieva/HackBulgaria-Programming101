import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Bonus Round 3 - One Dimensional Robot module"""
    def test_oned_robot(self):
        self.assertEqual(2, solution.oned_robot("RRLRRLLR", 10, 10))
        self.assertEqual(4, solution.oned_robot("RRRRR", 3, 4))
        self.assertEqual(-1, solution.oned_robot("LLLLLLLLLLR", 2, 6))
        self.assertEqual(20, solution.oned_robot("RRRRRRRLRRLRRRRRRRRRRRRLRLRRRRRRRRLRRRRRLRRRRRRRRR", 5, 20))
        self.assertEqual(-30, solution.oned_robot("RLRLLLLLLLRLLLRLLLLLLLLRLLLLLRLLLRRLLLLLRLLLLLRLLL", 34, 15))


if __name__ == '__main__':
    unittest.main()