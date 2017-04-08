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
    m = 88
    if extra_long_factorials(m) == 185482642257398439114796845645546284380220968949399346684421580986889562184028199319100141244804501828416633516851200000000000000000000:
        print(True)
    else:
        print(False)
        
test_extra_long_factorials()
#print(extra_long_factorials(n))
