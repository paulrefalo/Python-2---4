#!/usr/local/bin/python3
"""Obj 15 - Handling Exceptions - divider.py"""

while True:
    """ Get integer from the user and divde 10 by that integer -
        similar to handling from exceptions.py
    """
    i = input("Provide an integer: ")		# get user input
    if i == "":					# give them a way out
        break
    try:
        i = int(i)				# try to see if i is an integer and if 10 / i is okay
        print(10 / i)
    except ValueError:				# catch a ValueError if i is not an int
        print("Your input must be an integer")
    except ZeroDivisionError:			# catch divide by zero
        print("Your input must not be zero (0)")
    except Exception as msg:			# catch if something else when wrong
        print("Something unexpected occurred: {0}".format(msg))