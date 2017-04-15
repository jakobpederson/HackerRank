#!/bin/python3
# https://www.hackerrank.com/challenges/grading

import sys

def test_grading():
    samples = [73, 67, 38, 33]
    expected = [75, 67, 40, 33]
    result = list(custom_rounding_to_multiple_of_five(x) for x in samples)
    for grade in expected:
        if grade in result:
            print(True)
        else:
            print("False:", grade)
                        
def solve(grade):
    if grade < 38 or grade % 5 == 0:
        return grade
    return custom_rounding_to_multiple_of_five(grade)

def custom_rounding_to_multiple_of_five(grade):
    goal = grade
    count = 0
    while(goal % 5 != 0):
        goal += 1
        count += 1
        if count > 2:
            return grade
    return goal

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
