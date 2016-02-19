'''
Created on Oct 16, 2015

@author: prefalo
'''

import re

def CCNsafety(text):
    '''
    Hide CNN for security
    '''
    warning = 'CCN REMOVED FOR YOUR SAFETY'
    regex = re.compile(r"""        ## Compile the pattern into regex
                        \d{4}-    # first set
                        \d{4}-    # second set
                        \d{4}-    # third set
                        \d{4}     # final set
                        """, re.VERBOSE)
    
    return regex.sub(warning, text)   # replace the matches in text with the warning

if __name__ == '__main__':
    pass