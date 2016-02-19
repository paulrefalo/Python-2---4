"""
Testing coconuts.py for add and total_weight functionality
"""

import unittest
from coconuts import Coconut
from coconuts import Inventory

class TestCoconuts(unittest.TestCase):

    def setUp(self):
        """
        Instantiate each of the 3 coconut species
        """
        self.southAsian = Coconut('South Asian')
        self.middleEastern = Coconut('Middle Eastern')
        self.american = Coconut('American')
        
    def testCoconutsExist(self):
        """
        Just check that all coconuts are instances of Coconut
        Check the taking the lime and the coconut and shake it all up
        gives a KeyError because it is not allowed by class Coconut
        """
        self.assertTrue(self.southAsian.weight)
        self.assertTrue(self.middleEastern.weight)
        self.assertTrue(self.american.weight)
        self.assertRaises(KeyError, Coconut, 'lime')
        
    def testDifferentWeights(self):
        """
        Test to be sure each coconut type has a different weight by
        adding each weight to a set so length of the set == 3
        This also verifies that all weights are correct
        """
        cw = set()
        cw.add(self.southAsian.weight)
        cw.add(self.middleEastern.weight)
        cw.add(self.american.weight)
        self.assertEqual(len(cw), 3)
        knownSet = set([3, 2.5, 3.5])
        self.assertEqual(cw, knownSet)
        
    def testInventoryWeight(self):
        """
        Gimme 2 South Asian, 1 Middle Eastern, and 3 American coconuts weighing 19 units
        Also check that adding invalid instance of Coconut raises an error
        """
        inv = Inventory()
        inv.addCoconut(self.southAsian)
        inv.addCoconut(self.southAsian)
        inv.addCoconut(self.middleEastern)
        inv.addCoconut(self.american)
        inv.addCoconut(self.american)
        inv.addCoconut(self.american)

        observed = inv.totalWeight()
        self.assertEqual(observed, 19.0)
        
        self.assertRaises(TypeError, inv.addCoconut, 'Dodecelsulfate')

     
if __name__ == "__main__":
    unittest.main()   