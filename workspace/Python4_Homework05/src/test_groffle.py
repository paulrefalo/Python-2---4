'''
Created on Nov 11, 2015

@author: prefalo
'''
import unittest
from groffle import groffle_fast
from groffle import groffle_slow

from math import log, fsum
from timeit import Timer 
import pstats
import array

import cProfile as profile

class Test(unittest.TestCase):


    def setUp(self):       
        mass = 2.5
        density = 12
        self.slow_answer = groffle_slow(mass, density)
        self.fast_answer = groffle_fast(mass, density)
        
        sTimer = Timer("total = groffle_slow(mass, density)", 
        "from groffle import groffle_slow, mass, density") 
        self.slow = sTimer.timeit(number=1000)
        
        fTimer = Timer("total = groffle_fast(mass, density)", 
        "from groffle import groffle_fast, mass, density") 
        self.fast = fTimer.timeit(number=1000)
        
    def testGroffle(self):
        self.assertEqual(self.slow_answer, self.fast_answer)
        print("Slow is:", self.slow, "\nFast is:", self.fast)
        print("The fraction is:", self.fast/self.slow)
        self.assertTrue(self.slow * 0.50 > self.fast)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()