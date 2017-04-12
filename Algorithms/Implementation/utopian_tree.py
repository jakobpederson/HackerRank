#!/bin/python3
# https://www.hackerrank.com/challenges/utopian-tree

import sys

def utopian_tree_height(cycles):
    heights = []
    for cycle in cycles:
        heights.append(height_calculator(cycle))
    return heights
            
def height_calculator(cycle):
    height = 0
    for i in range(cycle + 1):
        if i == 0 or i % 2 == 0:
            height = height + 1
        else:
            height = height * 2
    return height
       
def test_utopian_tree_height():
    if [1, 2] != utopian_tree_height([0, 1]):
        print(False)
        print(utopian_tree_height([0, 1]))
    else:
        print(True)
    if [7, 6] != utopian_tree_height([4, 3]):
        print(False)
        print(utopian_tree_height([4, 3]))
    else:
        print(True)
        
t = int(input().strip())
cycles = []
for a0 in range(t):
    cycles.append(int(input().strip()))

#test_utopian_tree_height()
for height in utopian_tree_height(cycles):
    print(height)
