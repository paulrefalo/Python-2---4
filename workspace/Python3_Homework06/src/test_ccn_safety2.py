'''
Created on Oct 16, 2015

@author: prefalo
'''

import unittest
from ccn_safety2 import CCNsafety

text = ("Have you ever noticed, in television and movies, that phone numbers and credit cards "
"are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number "
"that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and "
"security experts.")

enchilada = ("Have you ever noticed, in television and movies, that phone numbers and credit cards "
"are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number "
"that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and "
"security experts.")

class Test(unittest.TestCase):


    def testCCNsafety(self):
        '''
        Test the hiding of the CCN for security
        '''
        response = CCNsafety(text)
        self.assertTrue("555-123-4567" in response)
        self.assertTrue("CCN REMOVED FOR YOUR SAFETY" in response)

        self.assertFalse("5555-5555-5555-5555" in response)
        self.assertFalse("1234-5678-1234-5678" in response)
        self.assertEqual(response, enchilada) # This tests a comparison to the whole enchilada
        print(response)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()