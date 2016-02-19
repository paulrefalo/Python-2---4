'''
Created on Oct 14, 2015

@author: prefalo
'''

import re

def CCNsafety(text):
    '''
    Hide the first 12 digits of a CNN for security
    '''
    return re.subn(r"\d{4}-\d{4}-\d{4}-", "XXXX-XXXX-XXXX-", text)

if __name__ == '__main__':
    pass