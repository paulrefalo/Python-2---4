#!/usr/local/bin/python3
"""Objective 7 - multuple.py; formatting strings."""

## Define some globals ##
tup = ((1,1),(2,2),(12,13),(4,4),(99,98))
product, int1, int2 = 0, 0, 0

for entry in tup:
    int1, int2 = entry		## do some math
    product = int1 * int2

    print("{0:>5} = {1:>2} x {2:>2}".format(product, int1, int2))  ## format the output