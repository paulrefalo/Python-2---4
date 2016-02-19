#!/usr/local/bin/python3
"""Obj 11 - Building methods three_param.py"""

# Function with three parameters
def my_func(a, b = 'b was not entered', c = 'c was not entered'):
    print(a)
    print(b)
    print(c)

my_func('test')					# call with one param
my_func('test', 'test')				# call with two params
my_func('test', 'test', 'test') 		# call with all three params
   
print(my_func)					# print the func (memory address thereof)