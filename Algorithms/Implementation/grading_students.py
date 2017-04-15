#!/bin/python3
# https://www.hackerrank.com/challenges/grading

import sys

def test_grading():
    samples = [73, 67, 38, 33]
    expected = [75, 67, 40, 33]
    result = list(solve(x) for x in samples)
    for grade in expected:
        if grade in result:
            print(True)
        else:
            print("False:", grade)
                        
def solve(grade):
    if grade < 38:
        return grade
    return custom_rounding_to_multiple_of_five(grade)

def custom_rounding_to_multiple_of_five(grade):
    if grade % 5 == 3:
        grade += 2
    elif grade % 5 == 4:
        grade += 1
    return grade

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)

# test_grading()
answers = list(solve(x) for x in grades)
for answer in answers:
    print(answer)
