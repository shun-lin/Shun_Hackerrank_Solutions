#!/bin/python3

import sys

def makingAnagrams(s1, s2):
    # Complete this function

    # error checking
    if (s1 == None or s2 == None):
        return 0
    difference_storage = dict()
    for char in s1:
        if (not char in difference_storage):
            difference_storage[char] = 1
        else:
            difference_storage[char] += 1

    for char in s2:
        if (not char in difference_storage):
            difference_storage[char] = -1
        else:
            difference_storage[char] -= 1

    result = 0

    for key in difference_storage:
        value = difference_storage[key]
        if (value != 0):
            result += abs(value)

    return result


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
