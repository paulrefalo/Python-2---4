import unittest
from database import login_info
import mysql.connector
from classFactory import build_row

class DBTest(unittest.TestCase):
    # mysql -h sql -u <username> -p <username>

    def setUp(self):       
        S = build_row("animal", "id name family weight")
        self.a = S([8, "Dennis", "Dragon", 10000])
        
        self.e = S([1, "Ellie", "Elephant", 2350])

        
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()
                 
        
    def test_attributes(self):
        self.assertEqual(self.a.id, 8)
        self.assertEqual(self.a.name, "Dennis")
        self.assertEqual(self.a.family, "Dragon")
        self.assertEqual(self.a.weight, 10000)
        
    def test_repr(self):
        self.assertEqual(repr(self.a), 
                         "animal_record(8, 'Dennis', 'Dragon', 10000)")
        
    def testRetrieveConditional(self):   
        #print(self.a)          
        for row in self.a.retrieve(self.cursor, "weight>5000"): 
            self.assertEqual(repr(row), self.a)
            
    def testRetrieve(self):   
        #print(self.e)          
        self.assertEqual(repr(self.e), "{0}".format(self.e))
    
        
if __name__ == "__main__":
    unittest.main(warnings='ignore')
    

