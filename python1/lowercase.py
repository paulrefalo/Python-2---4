#!/usr/local/bin/python3
"""Check for lower case."""

s = input("Enter any string: ")

for case in s:
    if case.islower():
      print("Case is ", case, "and is a lower case letter.")
    else:
      print("Case is ", case, "and is not a lower case letter.")