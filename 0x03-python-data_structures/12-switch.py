#!/usr/bin/python3
a = 89
b = 10
x, a = a, b
b = x
print("a={id} - b={:d}".format(a, b))
