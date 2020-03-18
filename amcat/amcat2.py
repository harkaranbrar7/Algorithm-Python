from fractions import gcd
from functools import reduce
def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    x = reduce(gcd, arr)
    return x