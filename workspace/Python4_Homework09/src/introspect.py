'''
Created on Nov 13, 2015

@author: prefalo
'''

import inspect

def intro(m):
    funcs = inspect.getmembers(m, inspect.isfunction)
    #print(funcs)
    for k, f in funcs:
        args = inspect.formatargspec(*inspect.getfullargspec(f))
        print("def {0}{1}".format(k, args))

if __name__ == '__main__':
    intro(inspect)