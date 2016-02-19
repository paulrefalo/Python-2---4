'''
Created on Oct 12, 2015

@author: prefalo
'''
from string import ascii_uppercase

def alphabator(molecule):
    """
    Yield either the iterator or letter equivalent if integer 1 to 26 inclusive
    """
    try:
        test_iterable = iter(molecule)
    except TypeError:
        print(molecule, 'is not iterable')
    
    for atom in molecule:
        if isinstance(atom, int) and atom in range(27):
            yield ascii_uppercase[atom - 1]
        else:
            yield atom 
        