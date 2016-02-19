#!/usr/local/bin/python3
"""Obj 13 - More Python Functions - caser.py
   
   This script allows a user to input a string and
   have the string modified in typical ways...upper case,
   lower case, etc.

"""

import sys
    
if __name__ == "__main__":    
    
    switch = {						# set up switch to give proper str output
        'capitalize': str.capitalize,
        'title': str.title,
        'upper': str.upper,
        'lower': str.lower,
        'exit': sys.exit
    }

    options = switch.keys()
    prompt = 'Pick an option from the list({0}): '.format(', '.join(options))
    while True:
        s = ''						# user input string
        f = input(prompt)				# user function choice
        if not f in switch:             		# validate function choice
            print('Please select a valid option!')
            continue
        elif ( f == 'exit' ):				# if exit no string input is needed so exit
            print('Goodbye for now')
            sys.exit()
        else:						# if function ok get switch
            s = input('Enter a string: ')
            print(switch[f](s))