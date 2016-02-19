'''
Created on Nov 8, 2015

@author: prefalo
'''
import unittest
import arr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for h in range(N):
                        self.assertEqual(a[i, j, h], 0)
                    
    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for h in range(N):
                        self.assertEqual(a[i, j, h], i == j == h)
                    
    def _index(self, a, r, c, d):
        return a[r, c, d]

    def test_key_validity(self):
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a ,-1, 1, 1)
        self.assertRaises(KeyError, self._index, a ,10, 1, -1)
        self.assertRaises(KeyError, self._index, a ,1, -1, 10)
        self.assertRaises(KeyError, self._index, a ,1, 10, -1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()