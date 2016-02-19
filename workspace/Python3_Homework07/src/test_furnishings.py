'''
Created on Oct 18, 2015

@author: prefalo
'''
import unittest
from furnishings import *


class Test(unittest.TestCase):


    def setUp(self):
        self.home = []
        self.home.append(Bed("Bedroom"))
        self.home.append(Bed("Guest Room"))
        self.home.append(Sofa("Living Room"))
        self.home.append(Table("Dining Room"))
        self.home.append(Table("Office"))
        self.home.append(Bookshelf("Den"))

    def testMap(self):
        '''
        Get the chart dict back and check the class for each item
        '''
        chart = map_the_home(self.home)
        for item in chart['Bedroom']:
            self.assertIsInstance(item, Bed)
        for item in chart['Guest Room']:
            self.assertIsInstance(item, Bed)
        for item in chart['Living Room']:
            self.assertIsInstance(item, Sofa)
        for item in chart['Dining Room']:
            self.assertIsInstance(item, Table)
        for item in chart['Office']:
            self.assertIsInstance(item, Table)
        for item in chart['Den']:
            self.assertIsInstance(item, Bookshelf)

        
    def testCounter(self):
        '''
        Get the count dict back from counter and check the values are right
        '''
        count = counter(self.home)
        self.assertEqual(count['Bed'], 2)
        self.assertEqual(count['Sofa'], 1)
        self.assertEqual(count['Table'], 2)
        self.assertEqual(count['Bookshelf'], 1)  

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()