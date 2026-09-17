#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    exp = -b if b < 0 else b
    res = 1
    for _ in range(exp):
        res *= a
    if b < 0:
        return 1 / res
    return res
