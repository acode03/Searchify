import unittest
import subprocess
from ProductionCode.helperFunctions import *

if __name__ == '__main__':
    unittest.main()

# class Test_loaddata(unittest.TestCase):
#     def test_loaddata_edge(self):
#         """tests if loaddata returns error message for dataset that doesn't exist"""
#         self.assertEqual(load_data("hello.csv"), "Not a valid dataset")

class Test_maxormin(unittest.TestCase):
    
    def test_maxormin_standard(self):
        """seeing if maxormin works for standard values"""
        data = load_data("mini.csv")
        self.assertEqual(max_or_min("energy", 1, "max", data), ["Taste - Sabrina Carpenter: 0.91"])

    def test_maxormin_invalidDataset(self):
        """making sure maxormin returns error message when given an invalid dataset"""
        self.assertEqual(max_or_min("energy", 1, "max", "hello"), "Invalid dataset inputted.")

    def test_maxormin_invalidMax(self):
        """checks that it handles an invalid value for max or min"""
        data = load_data("mini.csv")
        self.assertEqual(max_or_min("energy", 1, "hello", data), "receives only 'max' or 'min'")

    def test_maxormin_invalidVariable(self):
        """checks that an invalid variable is handled"""
        data = load_data("mini.csv")
        self.assertEqual(max_or_min("hello", 1, "max", data), "Error: statistic not found")

    def test_maxormin_invalidNum_tooBig(self):
        """checks to see if a number larger than the size of the dataset is handled"""
        data = load_data("mini.csv")
        self.assertEqual(max_or_min("hello", 11, "max", data), "invalid number")

    def test_maxormin_invalidNum_negative(self):
        """checks to see if a negative number is handled"""
        data = load_data("mini.csv")
        self.assertEqual(max_or_min("hello", -1, "max", data), "invalid number")

    def test_maxormin_invalidNum_zero(self):
        """checks to see if zero is handled"""
        data = load_data("mini.csv")
        self.assertEqual(max_or_min("hello", 0, "max", data), "invalid number")

class Test_command_line(unittest.TestCase):
    def test_commandline_standard(self):
        '''Check if command_line.py works for valid command line arguments'''
        code = subprocess.Popen(['python3', 'command_line.py', '--var', 'tempo', '--sort', 'max', '--n', '1'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertIn(output, "('Hell N Back', 'Bakar', 209.688)\n")
        code.terminate()
