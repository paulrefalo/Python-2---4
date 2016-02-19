#!/usr/local/bin/python3

print("{0} {1} {2}".format("Python", "is", "fun"))

print("{a} {b} {c}".format(a='Python', b='is', c='fun'))

## Define some globals ##
tup = ((1,1),(2,2),(12,13),(4,4),(99,98))
product, int1, int2 = 0, 0, 0

for entry in tup:
    int1, int2 = entry		## do some math
    product = int1 * int2

    print("{0:^5} = {1:^5} x {2:^5}".format(product, int1, int2))  ## format the output

#print(keys(dct))
#print("{a}".format(0))
#print({a}{b}{c}.format(a,b,c))

#fms = "{"+fmt+"}"
#print("Format:", a, "output:", a.format(a))