"""
Simple program to dump the cmd line arguments
"""

import sys
for n, arg in enumerate(sys.argv):
    print(n, ":", arg)