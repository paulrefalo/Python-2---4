#!/usr/local/bin/python3
"""Obj 12 - Python Standard Library - guessing_game.py"""

import random, sys

n = random.randint(1, 99)
result = ''

def test(n, inp):
    """Takes 2 params the are ints and compares them.  Exits if they are equal"""
    if ( n > inp ):			# compare the values
        result = 'Too low'
    elif ( n < inp ):
        result = 'Too high'
    else:
        print('You guessed it!')
        sys.exit()			# print and exit if they guess the value
    return result

while True:
    inp = input('Guess a integer (1 - 99): ')	# get input
    if inp == "":			# give them a way out
        break 
    if not ( inp.isdigit() ):		# check to be sure we have a valid input
        print("That's not a number")
        continue
    inp = int(inp)			# convert inp to int
    if ( inp < 1 or inp > 99):		# check input range
        print("That's out of range")
        continue
    print(test(n, inp))			# in case you want to see the values
