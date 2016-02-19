#!/usr/local/bin/python3
#
# check_string.py
#
"""Detect is string is all caps and end with a period."""

uin = input("Please enter a string: ")
if uin.isupper() and uin.endswith('.'):
    print(uin, "-->", "is all caps and ends with a period")
elif uin.isupper():
    print(uin, "-->", "is all caps but does NOT end with a period")
elif uin.endswith('.'):
    print(uin, "-->", "is NOT all caps but does end with a period")
else:
    print("Neither case is true.")