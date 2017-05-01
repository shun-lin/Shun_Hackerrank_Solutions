#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
highest = max(height);
if (k >= highest):
    print(0);
else:
    print(highest - k);
