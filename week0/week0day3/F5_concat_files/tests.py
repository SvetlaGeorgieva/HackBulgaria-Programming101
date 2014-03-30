import solution
import unittest
import os


class SolutionTest(unittest.TestCase):
    """Testing Problem F5 - Concatenate files into one - module"""
    def setUp(self):
        self.filename1 = "test1.txt"
        file = open(self.filename1, "w")
        content1 = "HELLO, First file, one row"
        file.write(content1)
        file.close()

        self.filename2 = "test2.txt"
        file = open(self.filename2, "w")
        content2 = "Second file,\ntwo rows"
        file.write(content2)
        file.close()

    def test_concatenate(self):
        filenames = [self.filename1, self.filename2]
        self.assertEqual("HELLO, First file, one row\n\nSecond file,\ntwo rows\n\n", solution.concatenate(filenames, "test_concatenate.txt"))
        self.assertEqual("HELLO, First file, one row\n\nSecond file,\ntwo rows\n\nHELLO, First file, one row\n\nSecond file,\ntwo rows\n\n", solution.concatenate(filenames, "test_concatenate.txt"))

    def tearDown(self):
        os.remove(self.filename1)
        os.remove(self.filename2)
        os.remove("test_concatenate.txt")


if __name__ == '__main__':
    unittest.main()
