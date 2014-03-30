import solution
import unittest
import os


class SolutionTest(unittest.TestCase):
    """Testing Problem F2 - Cat multiple file module"""
    def setUp(self):
        self.filename1 = "v1.txt"
        file = open(self.filename1, "w")
        content = "Hello, I am a test file"
        file.write(content)
        file.close()

        self.filename2 = "v2.txt"
        file = open(self.filename2, "w")
        content = ""
        file.write(content)
        file.close()

        self.filename3 = "v3.txt"
        file = open(self.filename3, "w")
        content = "Hello, I am a test file\nWoow, a new line"
        file.write(content)
        file.close()

    def test_cat2(self):
        filenames = [self.filename1, self.filename2, self.filename3]
        self.assertEqual("Hello, I am a test file\n\n\n\nHello, I am a test file\nWoow, a new line", solution.cat2(filenames))

    def tearDown(self):
        os.remove(self.filename1)
        os.remove(self.filename2)
        os.remove(self.filename3)


if __name__ == '__main__':
    unittest.main()
