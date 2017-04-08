#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials

import sys


n = int(input().strip())

def extra_long_factorials(number):
    total = 1
    while number > 0:
        total = total * number
        number = number - 1
    return total
    
def test_extra_long_factorials():
    n = 25
    if extra_long_factorials(n) == 15511210043330985984000000:
        print(True)
    else:
        print("False %s" % extra_long_factorials(n))
    
#test_extra_long_factorials()
print(extra_long_factorials(n))
