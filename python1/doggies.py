#!/usr/local/bin/python3
"""Obj 14 - Classes - doggies.py"""

import sys

dogs = list()						# define a global list dogs

class Dog(object):
    """Dog class takes two arguments, name and breed
       Returns the formatted string with of name:breed
    """
    def __init__(self, name, breed):			# __init__ to define name and breed
        self.name = name
        self.breed = breed
        
    def __str__(self):					# __str__ to return formatted string
        return "{0}:{1}".format(self.name, self.breed)
        
        
if __name__ == '__main__':
       
    while True:
        name = input('Name: ')				# get input
        if not name:					# a way out
            break
        breed = input('Breed: ')			
        a_dog = Dog(name, breed)			# get an instance of Dog
        dogs.append(a_dog)				# add that instance to the list dogs
        print("DOGS")
        for i, dog in enumerate(dogs):			# print and enumerate elements of the list
            print("{0}. {1}".format(i, dog))
        print('*'*30)