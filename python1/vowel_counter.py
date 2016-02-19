#!/usr/local/bin/python3
"""Counts the vowels in a user input string."""

s = input("Enter a string: ")
vcount = 0
for c in s:
    if c in "aeiouAEIOU":
        vcount += 1
print("Vowel count:", vcount)