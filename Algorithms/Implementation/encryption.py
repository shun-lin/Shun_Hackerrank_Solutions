#!/bin/python3

import sys, math


s = input().strip()
lower_bound = math.floor(len(s) ** (1/2));
upper_bound = math.ceil(len(s) ** (1/2));
row = upper_bound;
col = upper_bound;
for i in range(0, col):
    for j in range(0, row):
        if (j * col + i < len(s)):
            print(s[j * col + i], end="");
    print(" ", end="");
