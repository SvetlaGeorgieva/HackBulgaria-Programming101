import solution
import unittest
import os


class SolutionTest(unittest.TestCase):
    """Testing Problem F6 - Count characters, words or lines module"""
    def setUp(self):
        self.filename1 = "test1.txt"
        file = open(self.filename1, "w")
        content1 = "Hello, one row"
        file.write(content1)
        file.close()

        self.filename2 = "test2.txt"
        file = open(self.filename2, "w")
        content2 = "Hello there\ntwo rows"
        file.write(content2)
        file.close()

        self.filename3 = "test3.txt"
        file = open(self.filename3, "w")
        content3 = ""
        file.write(content3)
        file.close()

    def test_wc_lines(self):
        self.assertEqual(1, solution.wc("lines", self.filename1))
        self.assertEqual(2, solution.wc("lines", self.filename2))
        self.assertEqual(1, solution.wc("lines", self.filename3))

    def test_wc_words(self):
        self.assertEqual(3, solution.wc("words", self.filename1))
        self.assertEqual(4, solution.wc("words", self.filename2))
        self.assertEqual(0, solution.wc("words", self.filename3))

    def test_wc_chars(self):
        self.assertEqual(12, solution.wc("chars", self.filename1))
        self.assertEqual(17, solution.wc("chars", self.filename2))
        self.assertEqual(0, solution.wc("chars", self.filename3))

    def tearDown(self):
        os.remove(self.filename1)
        os.remove(self.filename2)
        os.remove(self.filename3)


if __name__ == '__main__':
    unittest.main()
