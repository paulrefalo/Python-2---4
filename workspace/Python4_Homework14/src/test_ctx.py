'''
Created on Nov 16, 2015

@author: prefalo
'''
import unittest
from ctx import controlledExecution


class Test(unittest.TestCase):


    def testSupress(self):
        with controlledExecution():
            raise ValueError()
        
    def testOtherException(self):
        with controlledExecution():
            self.assertRaises("Python string")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()