'''
Created on Oct 13, 2015

@author: prefalo
'''
import unittest
from find_regex import matchMaker

text = """In the 1950s, mathematician Stephen Cole Kleene described automata theory
and formal language theory in a set of models using a notation called "regular sets"
as a method to do pattern matching. Active usage of this system, called
Regular Expressions, started in the 1960s and continued under such pioneers
as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer."""

class regexTest(unittest.TestCase):

    def testBogusPattern(self):
        '''
        Shouldn't be able to find Waldo in this one
        '''
        self.pat = "Waldo"
        self.text = text
        observedStart, observedEnd = matchMaker(self.pat, self.text)
        self.assertEqual(observedStart, None)
        self.assertEqual(observedEnd, None)
        
    def testWrongAddress(self):
        '''
        Shoudn't get the right 231, 250 values
        '''
        self.pat = "Thompson"
        self.text = text
        observedStart, observedEnd = matchMaker(self.pat, self.text)
        self.assertNotEqual(observedStart, 231)
        self.assertNotEqual(observedEnd, 250)

    def testRegex(self):
        '''
        Okay, this should work out
        '''
        self.pat = "Regular Expressions"
        self.text = text
        observedStart, observedEnd = matchMaker(self.pat, self.text)
        self.assertEqual(observedStart, 231)
        self.assertEqual(observedEnd, 250)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()