'''
adder.py: validation function for adding two integers
'''

def add_errors(a, b):
    """
    Validate a and b are integers then return the sum
    """
    # print("A is", a, "B is", b)
    try: a
    except TypeError("a is undefined"): a = None
    try: b
    except TypeError("b is undefined"): b = None

    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError("Both parameters must be integers")

 
