#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
i = len(arr) - 1;
while (i >= 0):
    print(arr[i], end= " ")
    i -= 1;
