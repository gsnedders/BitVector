#!/usr/bin/env python3

adict = {'a':1, 'size':2}

print(adict)

if 'size' in adict: s = adict.pop('size')

if s >= 0:
    print("s is greater than 0")

print(s)
