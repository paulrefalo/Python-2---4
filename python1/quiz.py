#!/usr/local/bin/python3
"""General Quiz Testing Ground\n"""

list = [1,2,3]

list[2] = [1,2,3]
list[2:] = [1,2,3]

print("The array is", list)

wordlist = ['abc-123', 'defox-456', 'ghi-789', 'abc-456']
if any("fox" in s for s in wordlist):
    print("Got it.")
else:
    print("Don't got it.")