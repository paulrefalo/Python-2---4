'''
Created on Nov 16, 2015

@author: prefalo
'''

class controlledExecution:

    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called")
        return isinstance(exc_val, ValueError)

if __name__ == '__main__':
    pass