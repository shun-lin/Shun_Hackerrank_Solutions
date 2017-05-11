#!/bin/python3

import sys

def getWays(squares, d, m):
    result = 0;
    i = 0;
    while (i + m - 1 < len(squares)):
        sum = 0;
        for j in range(i, i + m):
            sum += squares[j];
        if (sum == d):
            result += 1;
        i += 1;
    return result;
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)
