#!/usr/local/bin/python3
"""This script creates two lists.
One for words with CAPITALS and one for words without."""

s = input("Enter your string: ")
words = s.strip().split()

caps = []
no_caps = []
results = []

for word in words:
    if any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in word):
     caps.append(word)
    else:
     no_caps.append(word)
            
results = caps + no_caps

for r in results:
    print(r)
        