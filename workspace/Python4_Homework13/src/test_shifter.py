'''
Created on Nov 16, 2015

@author: prefalo
'''
import unittest
from shifter import sstr


class TestSSTR(unittest.TestCase):
    def setUp(self):
        self.test = sstr("abcde")

    def testLeft(self):
        self.assertEqual(self.test << 0, 'abcde')
        self.assertEqual(self.test << 1, 'bcdea')
        self.assertEqual(self.test << 2, 'cdeab')
        self.assertEqual(self.test << 3, 'deabc')
        self.assertEqual(self.test << 4, 'eabcd')
        self.assertEqual(self.test << 5, 'abcde')
        self.assertNotEqual(self.test << 1, 'abcde')
        
    def testRight(self):
        self.assertEqual(self.test >> 0, 'abcde')
        self.assertEqual(self.test >> 1, 'eabcd')
        self.assertEqual(self.test >> 2, 'deabc')
        self.assertEqual(self.test >> 3, 'cdeab')
        self.assertEqual(self.test >> 4, 'bcdea')
        self.assertEqual(self.test >> 5, 'abcde')
        self.assertNotEqual(self.test >> 1, 'abcde')
        
    def testAroundTheWorld(self):
        self.assertEqual( (self.test >> 5) << 5, 'abcde')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()