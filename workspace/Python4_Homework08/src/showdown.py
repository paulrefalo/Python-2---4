'''
Created on Nov 12, 2015

@author: prefalo
'''

from random import random
from timeit import timeit

def aList():
    lst = []
    for _ in range(1000000):
        lst.append(random())
    return lst

def aGen():
    for _ in range(1000000):
        yield random()

print("List Comprehension from List")
print(timeit("[x for x in aList()]", "from __main__ import aList", number = 1))

print("List Comprehension from Generator")
print(timeit("[x for x in aGen()]", "from __main__ import aGen", number = 1))

print("list() from List")
print(timeit("list(aList())", "from __main__ import aList", number = 1))

print("list() from Generator")
print(timeit("list(aGen())", "from __main__ import aGen", number = 1))


if __name__ == '__main__':
    pass

"""
list(x*x for x in sequence == [x*x for x in sequence]

# Generator expression
(x*2 for x in range(256))

# List comprehension
[x*2 for x in range(256)]

>>> for i in (10000, 100000, 1000000, 10000000, 20000000, 50000000):
...     lst = [random() for j in range(i)]
...     print("Length", i)
...     print(timeit("sum(x+1 for x in lst)", "from __main__ import lst", number=1))
...     print(timeit("sum([x+1 for x in lst])", "from __main__ import lst", number=1))
"""