import string_utils
import unittest


class StringUtilsTest(unittest.TestCase):
    """Testing the string utils module"""
    def test_lines(self):
        self.assertEqual(["Takes ", "a ", "String ", "argument"], string_utils.lines("Takes \na \nString \nargument"))
        self.assertEqual(["Takes"], string_utils.lines("Takes"))

    def test_unlines(self):
        self.assertEqual("Takes \na \nString \nargument", string_utils.unlines(["Takes ", "a ", "String ", "argument"]))
        self.assertEqual("Takes", string_utils.unlines(["Takes"]))
        self.assertEqual("Takes \na \nString \nargument", string_utils.unlines(string_utils.lines("Takes \na \nString \nargument")))


    def test_words(self):
        self.assertEqual(["Takes", "a", "String", "argument"], string_utils.words("Takes \na \nString \nargument"))
        self.assertEqual(["Takes", "a", "String", "argument"], string_utils.words("Takes a String argument"))
        self.assertEqual(["Takes"], string_utils.words("Takes"))
        self.assertEqual(["Takes"], string_utils.words("Takes "))


    def test_unwords(self):
        self.assertEqual("Takes a String argument", string_utils.unwords(["Takes", "a", "String", "argument"]))
        self.assertEqual("Takes", string_utils.unwords(["Takes"]))


    def test_tabs_to_spaces(self):
        self.assertEqual("Takes a    Tab", string_utils.tabs_to_spaces("Takes a\tTab", 4))
        self.assertEqual("Takes a  Tab", string_utils.tabs_to_spaces("Takes a\tTab", 2))


if __name__ == '__main__':
    unittest.main()