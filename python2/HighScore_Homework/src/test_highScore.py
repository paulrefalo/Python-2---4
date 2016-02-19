import unittest
import highScore
import shelve
import glob
import os

class TestHighScore(unittest.TestCase):
        
    def testScores(self):
        """Test out some scores -
        expected vs observed (shelf previous best) """

        self.assertEqual(99, highScore.playerHighScore('Dr Teeth', 99))
        self.assertEqual(99, highScore.playerHighScore('Dr Teeth', 91))
        self.assertEqual(108, highScore.playerHighScore('Dr Teeth', 108))
        self.assertEqual(0, highScore.playerHighScore('Animal', 0))
        self.assertEqual(0, highScore.playerHighScore('Animal', -2))
        self.assertEqual(49, highScore.playerHighScore('Animal', 49))
        self.assertEqual(5000, highScore.playerHighScore('Pinball Wizard', 5000))
        self.assertEqual(5000, highScore.playerHighScore('Pinball Wizard', 4999))
        self.assertEqual(10000, highScore.playerHighScore('Pinball Wizard', 10000))
          
    def tearDown(self):
        """Remove the .shelve.* files"""
        shelve_files = glob.glob('scores.shelve.*')
        for fn in shelve_files:
            os.remove(fn)

if __name__ == "__main__":
    f = shelve.open('v:\workspace\HighScore_Homework\src\scores.shelve')
    f.close()
    unittest.main()