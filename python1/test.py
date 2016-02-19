#!/usr/local/bin/python3
"""Python testing test.py"""


def lower_case(s):
    s = 'This is now lowercase: ' + s.lower()
    return s

print(lower_case('ABCDEFGHIJKLMNOP'))