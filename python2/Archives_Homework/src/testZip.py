import unittest
import os
import shutil
import myZip

HOME = os.getcwd()

class TestZip(unittest.TestCase):
     
    def setUp(self):
        """Create a directory and some files
        Then write those files to that directory"""
        
        self.path = r"v:\workspace\Archives_Homework\src\tmp"
        # be sure file path is clear
        if os.path.exists(self.path):
            try:
                shutil.rmtree(self.path, ignore_errors=True)
            except IOError:
                pass


        self.zip_filename = os.path.join(self.path, "planets.zip")
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.file_names = ["mercury", "venus", "earth"]  
              
        for fn in self.file_names:
            f = open(os.path.join(self.path, fn), "w")
            f.close()

    def testArchives(self):
        expected = ["tmp/mercury", "tmp/venus", "tmp/earth"]
        observed = myZip.zipDir(self.path)
        self.assertEqual(set(expected), set(observed), "There is a mismatch in the directory vs ZipFile.")
        
    def testNotTransported(self):
        os.chdir(HOME)  # go home!
        self.assertEqual(HOME, os.getcwd(), "undocumented side effect:  transported!")          
        
    def tearDown(self):
        """Rmove the test directory"""
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass

        
if __name__ == "__main__":     
    unittest.main()