import solution
import unittest
import os


class SolutionTest(unittest.TestCase):
    """Testing Problem F1 - Implement the cat command -
    Print file contents module"""
    def test_cat1(self):
        self.filename = "v1.txt"
        file = open(self.filename, "w")
        content = "Hello, I am a test file"
        file.write(content)
        file.close()
        self.assertEqual("Hello, I am a test file", solution.cat(self.filename))
        os.remove(self.filename)

    # testing an empty file
    def test_cat2(self):
        self.filename = "v2.txt"
        file = open(self.filename, "w")
        content = ""
        file.write(content)
        file.close()
        self.assertEqual("", solution.cat(self.filename))
        os.remove(self.filename)

    # testing a file with new lines in it
    def test_cat3(self):
        self.filename = "v3.txt"
        file = open(self.filename, "w")
        content = "Hello, I am a test file\nWoow, a new line"
        file.write(content)
        file.close()
        self.assertEqual("Hello, I am a test file\nWoow, a new line", solution.cat(self.filename))
        os.remove(self.filename)

"""
    def setUp(self):
        self.filename = "v1.txt"
        file = open(self.filename, "w")
        content = "Hello, I am a test file"
        file.write(content)
        file.close()

    def test_cat(self):
        self.assertEqual("Hello, I am a test file", solution.cat(self.filename))

    def tearDown(self):
        os.remove(self.filename)
"""

if __name__ == '__main__':
    unittest.main()
