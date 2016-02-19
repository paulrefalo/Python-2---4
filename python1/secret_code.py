#!/usr/local/bin/python3
"""Obj 10 - Python operators, secret_code.py"""

# globals
output = ""

while True:
    alpha = input("Enter text: ")	# user input alpha
    if alpha == "":			# give them a way out
        break 
        
    for letter in alpha:		# loop over letters
        t = chr( ord(letter) + 1 )	# get the ord of the letter, add one, then get the chr of that number
        output += t			# build the output string
        
    print(output[::-1])			# display in reverse order
    output = ""				# clear output for next iteration