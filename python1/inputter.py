#!/usr/local/bin/python3
"""Obj 9 - reading and writing to files"""

fn = 'obj9.txt'		# set up file name

while True:
    f = open(fn, 'a+')	# open to read
    f.seek(0)		# move pointer to the start
    print(f.read())	# print out all the lines like the quiz
    x = input("Enter text: ")	# user input x
    if not x:			# give them a way out
        break 

    f.write(x)			# write x to f and close
    f.close()			# close the file

    
