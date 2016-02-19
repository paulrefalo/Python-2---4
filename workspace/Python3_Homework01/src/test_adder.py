'''
Created on Oct 6, 2015

@author: prefalo
'''
import unittest
from adder import add_errors


class Test(unittest.TestCase):


    def testAddErrors(self):
        "Tests ensuring errors in data cause validation failures."
        self.assertRaises(TypeError, add_errors, "one", 2)  # one string one int
        self.assertRaises(TypeError, add_errors, 2)         # one argument
        self.assertRaises(TypeError, add_errors, 2, 5.5)    # one float
        self.assertRaises(TypeError, add_errors, "one", "two") # two strings
  
    def testAddSuccesses(self):
        "Test ensuring that valid data passes."
        self.assertEqual(9, add_errors(3, 6), "Can't add it up")
        self.assertEqual(5, add_errors(-1, 6), "Can't add it up")
        self.assertEqual(-99, add_errors(0, -99), "Can't add it up")

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()