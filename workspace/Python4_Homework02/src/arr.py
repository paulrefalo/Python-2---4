'''
Created on Nov 8, 2015

@author: prefalo

Class-based dict allowing tuple subscripting and sparse data.

'''


class array:
    
    def __init__(self, A, B, C):
        "Create an M-element list of N-element row lists."
        self._data = {}
        self._alpha = A
        self._beta = B
        self._gamma = C
                  
    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple"
        alpha, beta, gamma = self._validate_key(key)
        try:
            return self._data[alpha, beta, gamma]
        except KeyError:
            return 0
    
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        alpha, beta, gamma = self._validate_key(key)
        self._data[alpha, beta, gamma] = value
        
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        alpha, beta, gamma = key
        if (0 <= alpha < self._alpha and 
                0 <= beta < self._beta and
                0 <= gamma < self._gamma):
            return key
        raise KeyError("Subscript out of range")
        



if __name__ == '__main__':
    pass