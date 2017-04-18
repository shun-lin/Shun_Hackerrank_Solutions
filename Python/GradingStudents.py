#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    result = [None] * len(grades);
    for i in range(0, len(grades)):
        grade = grades[i];
        reminder = grade % 5;
        if (grade < 38 or (grade > 38 and reminder < 3)):
            result[i] = grades[i];
        else:
            result[i] = grade + 5 - reminder;
    return result;

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
for j in range(0, len(result)):
    print(result[j]);
