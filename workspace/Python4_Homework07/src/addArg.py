'''
Created on Nov 12, 2015

@author: prefalo
'''
def addArg(first):
    def decorator(f):
        def argAdded(*args, **kw):
            return f(first, *args, **kw)
        return argAdded
    return decorator

@addArg(1)
def prargs(*args):
    return args

print(prargs(2, 3))
print(prargs("child"))

if __name__ == '__main__':
    pass
