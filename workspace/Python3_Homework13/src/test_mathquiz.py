'''
Created on Oct 27, 2015

@author: prefalo
'''
import unittest
import random
from mathquiz import addNumbers
from unittest.mock import patch


class Test(unittest.TestCase):
    
    def setUp(self):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)
        assert isinstance(self.a, int)
        assert isinstance(self.b, int)
    

    def testRightAnswer(self):
        self.c = self.a + self.b

        ( answer, time ) = addNumbers(self.a, self.b, self.c)
        self.assertEqual(answer, self.c)
        assert time >= 0
        
    def testWrongAnswer(self):
        self.c = self.a + self.b

        ( answer, time ) = addNumbers(self.a, self.b, self.c)
        self.assertNotEqual(answer + 1, self.c)
        assert time >= 0
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMathquiz']
    unittest.main()