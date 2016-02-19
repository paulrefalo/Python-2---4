'''
Created on Nov 11, 2015

@author: prefalo
'''
import unittest
import string
from pyDict import SubDct

class Test(unittest.TestCase):
    def setUp(self):
        self.d = dict.fromkeys(string.ascii_lowercase, 0)
        for x in self.d:
            self.d[x] = ord(x)
        self.d.__init__(self.d)
        print(self.d)
        self.test = SubDct(self.d)
        self.test.__init__('Monkey')

    def testGetItem(self):
        self.assertEqual(self.d.__getitem__('a'), 97)
        self.assertRaises(KeyError, self.d.__getitem__, 'A')
        self.assertEqual(self.d.__getitem__('b'), 98)
        self.assertEqual(self.test.__missing__('Z'), 'Monkey')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()