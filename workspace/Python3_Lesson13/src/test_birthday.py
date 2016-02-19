from datetime import datetime
import unittest

from birthday import *

class TestBirthday(unittest.TestCase):

    
    def test_birthday_counter(self):
        # will fail on Oct 31
        self.assertTrue(birthday_counter("10-31-1948") > 0)
        
        # will fail on Feb 1
        self.assertTrue(birthday_counter("02-01-1999") > 0)
        
    def test_string_to_date(self):
        self.assertRaises(InvalidDateFormat, string_to_date, "10-32-1948")
        # create new datetime object
        datetime_obj = datetime(2012, 10, 31)
        self.assertEqual(datetime_obj, string_to_date("10-31-2012"))
        

if __name__ == "__main__":
    unittest.main()
 