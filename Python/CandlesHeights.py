#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
highest = max(height);
total = 0;
for i in height:
    if (i == highest):
        total += 1;
print(total);
