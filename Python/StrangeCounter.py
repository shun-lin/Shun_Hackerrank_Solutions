#!/bin/python3

import sys


t = int(input().strip())
# find the ones
value_base = 3;
time = 0;
while (time + value_base < t):
    time += value_base;
    value_base *= 2;
difference = t - time - 1;
print(value_base - difference)
