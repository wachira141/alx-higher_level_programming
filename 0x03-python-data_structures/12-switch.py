#!/usr/bin/python3
a = 89
b = 10
a, b = copy(b), copy(a)
print("a={:d} - b={:d}".format(a, b))
