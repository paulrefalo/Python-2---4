#!/usr/local/bin/python3
"""Obj 10 - Python operators, secret_code.py"""


f = open('Q.txt', 'w')
f.write('my text')
f.close()

z = open('Q.txt', 'r')
#z.read()
print(z.read())
z.close()