import solution
import unittest
import os


class SolutionTest(unittest.TestCase):
    """Testing Problem F4 - Sum integers from file module"""
    def setUp(self):
        self.filename1 = "num2.txt"
        file = open(self.filename1, "w")
        content = "10 20 30 40 50 60 70 80 90"
        file.write(content)
        file.close()

    def test_sum_numbers(self):
        self.assertEqual(450, solution.sum_numbers(self.filename1))

    def tearDown(self):
        os.remove(self.filename1)


if __name__ == '__main__':
    unittest.main()
