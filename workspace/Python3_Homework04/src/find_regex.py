'''
Created on Oct 13, 2015

@author: prefalo
'''
import re

def matchMaker(pat, text):
    '''
    Takes a regex pattern and text
    Searches for the pattern in the text and
    Returns the start and end if found, AttributeError caught otherwise
    '''
    m = re.search(pat, text)

    try:
        return (m.start(), m.end())
    except AttributeError:
        return (m, m)
   
if __name__ == "__main__":
    matchMaker("text")