import unittest, time
from database import login_info
import mysql.connector as msc
from JOTD import sqlJOTD
from settings import RECIPIENTS, DAYCOUNT
import pprint
#import numpy as np
#from matplotlib import pyplot

class testJOTD(unittest.TestCase):
    
    def testDaycounts(self):
        """
        Tests for all DAYCOUNTs 1, 10, 50, 100, 500
        """
        results = {}
        for x in range(0, 5):
            self.count = DAYCOUNT[x]
            self.startTime = time.time()
            sqlJOTD(self.count)
            interval = time.time() - self.startTime
            results[self.count] = interval
            #print ("Daycount %s took %.3f seconds" %(self.count, interval))
            
            conn = msc.Connect(**login_info)
            curs = conn.cursor()
            curs.execute("SELECT COUNT(*) FROM messages")
            
            self.expected=curs.fetchone()[0]
            self.assertEqual(self.expected, self.count*len(RECIPIENTS))
            conn.close()
            
        #pprint.pprint(results)
        for k, v in sorted(results.items()):
            print("Daycount %s took %.3f" % (k, v))
        
        #plt.bar(myDictionary.keys(), myDictionary.values(), width, color='g')
        
if __name__=="__main__":
    unittest.main()