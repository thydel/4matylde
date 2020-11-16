#!/usr/bin/python

import sys

def f(b, k, s = []):
    if k == 0:
        print("".join(s))
    else:
        for i in b:
            f(b, k - 1, s + [i])

f(list(str(sys.argv[1])), int(sys.argv[2]))
