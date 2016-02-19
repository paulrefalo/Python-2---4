'''
Created on Nov 10, 2015

@author: prefalo
'''

""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log, fsum
from timeit import Timer 
import pstats
import array

import cProfile as profile



def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

def groffle_medium(mass, density):
    masslog = log(mass * density)
    results = sum([masslog / i for i in range(1, 10001)])
    return results

def groffle_map(mass, density):
    masslog = log(mass * density)
    my_list = list(range(1, 10001))
    values = map(lambda x: masslog/x, my_list)
    return sum(values)

def groffle_fast(mass, density):
    masslog = log(mass * density)
    return sum([masslog/x for x in range(1, 10001)])



mass = 2.5 
density = 12.0 
"""
timer = Timer("total = groffle_slow(mass, density)", 
 "from __main__ import groffle_slow, mass, density") 
print("Slow time:", timer.timeit(number=1000)) 

timer = Timer("total = groffle_fast(mass, density)", 
 "from __main__ import groffle_fast, mass, density") 
print("Fast time:", timer.timeit(number=1000)) 

print("Slow result:", groffle_slow(2.5, 12.0))
print("Fast result:", groffle_fast(2.5, 12.0))
"""
if __name__ == '__main__':
    pass
    """
    profile.run("groffle_slow(2.5, 12.0)", "slowdata")
    s = pstats.Stats("V:\\workspace\\Python4_Homework05\\src\\slowdata") 
    s.strip_dirs().sort_stats('calls', 'time').print_stats()
    
    profile.run("groffle_fast(2.5, 12.0)", "fastdata")
    s = pstats.Stats("V:\\workspace\\Python4_Homework05\\src\\fastdata") 
    s.strip_dirs().sort_stats('calls', 'time').print_stats()
    
        #masslog = log(mass * density)
    #total = sum([masslog / i for i in range(1, 10001)])
        #def ans(x): return masslog/x
    #my_list = list(range(1, 10001))
    #values = map(lambda x: masslog/x, my_list)
    
    
    masslog = log(mass * density)
    results = 0.0
    for x in range(1, 10001):
        results += masslog/x 
    return results
    """
