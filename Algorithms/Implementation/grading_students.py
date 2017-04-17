#!/bin/python3
# https://www.hackerrank.com/challenges/grading

import sys

def test_grading():
    samples = [73, 67, 38, 33]
    expected = [75, 67, 40, 33]
    result = solve(samples)
    for grade in expected:
        if grade in result:
            print(True)
        else:
            print("False:", grade)
                        
def solve(grades):
    return list(custom_rounding_to_multiple_of_five2(x) for x in grades)

def custom_rounding_to_multiple_of_five2(grade):
    if grade < 38:
        return grade
    elif grade % 5 in (3, 4):
        grade += 5 - (grade % 5)
    return grade

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)

#test_grading()
answers = solve(grades)
for answer in answers:
    print(answer)
