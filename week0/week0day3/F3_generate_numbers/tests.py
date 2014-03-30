import solution
import unittest
import os


class SolutionTest(unittest.TestCase):
    """Testing Problem F3 - Generate file with random integers module"""
    def setUp(self):
        self.filename1 = "num1.txt"
        file = open(self.filename1, "w")
        content = ""
        file.write(content)
        file.close()

    def test_generate_numbers(self):
        num_string = solution.generate_numbers(self.filename1, 10)
        result = num_string.split()
        self.assertEqual(10, len(result))

    def tearDown(self):
        os.remove(self.filename1)


if __name__ == '__main__':
    unittest.main()
