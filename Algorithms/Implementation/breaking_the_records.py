#!/bin/python3
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

import sys

def test_get_record():
    SCORES = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    SCORES_1 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    result = getRecord(SCORES)
    result_1 = getRecord(SCORES_1)
    if result == (2, 4) and result_1 == (4, 0):
        pass
    else:
        if result_1 != (4, 0):
            print("Fail %s", result_1)
        elif result != (2, 4):
            print("Fail %s", result)

def getRecord(scores):
    max_score = scores[0]
    min_score = scores[0]
    count_max = 0
    count_min = 0
    for score in scores:
        if score > max_score:
            count_max += 1
            max_score = score
        elif score < min_score:
            count_min += 1    
            min_score = score
    return count_max, count_min

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result_max, result_min = getRecord(s)
test_get_record()
print (result_max, result_min)
