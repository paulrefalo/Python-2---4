import unittest        
from Email12 import sendemail

class TestEmail12(unittest.TestCase):
    
    def setUp(self):
        self.address = 'paul.refalo@gmail.com'
        self.body = "Here's to the body politic"
        self.attachments = ['walt.txt', 'logo.png']
        self.subject = "Python email system testing"
        
    def testHeaders(self):
        self.msg = sendemail(self.address, self.body)

        self.assertEqual(self.msg['To'], self.address)
        self.assertEqual(self.msg['From'], self.address)
        self.assertEqual(self.msg['Body'], self.body)  
        self.assertEqual(self.msg['Subject'], self.subject)     
        
    def testAttachments(self):
        self.msg = sendemail(self.address, self.body, self.attachments)
        with open('v:\workspace\HandlingEmail_Homework\src\walt.txt', 'r') as text_file:
            f1 = text_file.read()
        with open('v:\workspace\HandlingEmail_Homework\src\logo.png', 'rb') as image_file:
            f2 = image_file.read()

        with open(self.attachments[0], 'r') as atext_file:
            a1 = atext_file.read()
        self.assertEqual(a1, f1)
        
        with open(self.attachments[1], 'rb') as aimage_file:
            a2 = aimage_file.read()
        self.assertEqual(a2, f2)
            
if __name__ == "__main__":
    unittest.main()   