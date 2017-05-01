#!/bin/python3

import sys

def getRecord(s):
    if (len(s) ==0):
        return;
    highest = s[0];
    lowest = s[0];
    high_changes = 0;
    low_changes = 0;
    for i in range(1, len(s)):
        if (s[i] > highest):
            highest = s[i];
            high_changes += 1;
        if (s[i] < lowest):
            lowest = s[i];
            low_changes += 1;
    return high_changes, low_changes;

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
