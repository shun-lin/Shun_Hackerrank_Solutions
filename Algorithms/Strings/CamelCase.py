#!/bin/python3

import sys

s = input().strip()
total = 1;
for char in s:
    if (char.isupper()):
        total += 1;
print(total);
