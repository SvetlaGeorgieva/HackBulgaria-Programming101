import solution
import unittest


class SolutionTest(unittest.TestCase):
    """Testing Bonus Round 2 - Magic String module"""
    def test_magic_string(self):
        self.assertEqual(2, solution.magic_string(">><<><"))
        self.assertEqual(0, solution.magic_string(">>>><<<<"))
        self.assertEqual(4, solution.magic_string("<<>>"))
        self.assertEqual(20, solution.magic_string("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))


if __name__ == '__main__':
    unittest.main()