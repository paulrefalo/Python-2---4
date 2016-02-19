'''
Created on Nov 9, 2015

@author: prefalo
'''
import unittest
from tree import Tree


class Test(unittest.TestCase):


    def setUp(self):
        self.test = Tree("D", ord("D"))
        for c in "BJQKFAC":
            self.test.insert(c, ord(c)) 


    def testTree(self):
        self.assertEqual(self.test.answer(70), 'F')
        self.assertEqual(self.test.answer(81), 'Q')
        
    def testExceptions(self):
        self.assertRaises(KeyError, self.test.find(99))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()