'''
Created on Nov 12, 2015

@author: prefalo
'''
import unittest
import addArg


class Test(unittest.TestCase):

    def testName(self):
        self.assertEqual(addArg.prargs(2, 3), (1, 2, 3))
        self.assertEqual(addArg.prargs("child"), (1, "child"))
        self.assertEqual(addArg.prargs("is the", "loneliest number"), 
                         (1, "is the", "loneliest number"))
        self.assertNotEqual(addArg.prargs(2), (2))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()