'''
composable.py: defines a composable function class.
Created on Nov 7, 2015

@author: prefalo
'''

import types
class Composable:
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    def __mul__(self, other):
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    def __rper__(self):
        return "<Composable function {0} at 0x[1:X]>".format(self.func.__name__, id(self))
    
    def __pow__(self, exp):
        if isinstance( exp, int ):
            if exp <= 0:
                raise ValueError("Object cannot be negative")
            elif exp == 1:
                return self
            else:
                val = self
                for num in range(exp - 1):
                    val *= self
                return val
        else:
            raise TypeError("The Object must be a non-negative integer")

if __name__ == '__main__':
    pass