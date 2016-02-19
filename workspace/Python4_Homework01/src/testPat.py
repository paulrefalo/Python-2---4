'''
Created on Sep 11, 2012

'''

import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing"
    return s[::-1]

def square(x):
    "Multiplies a number by itself"
    return x*x

def add(x):
    "Adds a number to itself"
    return x+x

class ComposableTes1t(unittest.TestCase):

    def test_pow(self):
        adder = Composable(add)
        add1 = adder**1
        for v,r in ((1,2),(2,4),(3,6)):
            self.assertEquals(add1(v),r)
    
    def test_pow2(self):
        adder = Composable(add)
        add1 = adder**2
        for v,r in ((1,4),(2,8),(3,12)):
            self.assertEquals(add1(v),r)

    def test_pow3(self):
        adder = Composable(add)
        add1 = adder**3
        for v,r in ((1,8),(2,16),(3,24)):
            self.assertEquals(add1(v),r)
    
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = fc ** square
        with self.assertRaises(ValueError):
            fc = fc ** 0
        with self.assertRaises(ValueError):
            fc = fc ** -1
            

if __name__ == "__main__":
    unittest.main()
