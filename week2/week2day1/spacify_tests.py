from subprocess import call
import unittest
import os

class SpacifyTests(unittest.TestCase):
    """Testing the spacify module"""
    def setUp(self):
        self.file_name = "test"
        self.file_handle = open(self.file_name, "w")

    def test_sapcify(self):
        self.file_handle.write("    Python!")
        self.file_handle.close()
        
        call("py spacify.py test", shell = True)

        f = open(self.file_name, "r")
        contents = f.read()
        f.close()

        self.assertEqual("    Python!", contents)

    def tearDown(self):
        os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
