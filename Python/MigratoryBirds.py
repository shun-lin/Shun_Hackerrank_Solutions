#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
freq = [0, 0, 0, 0, 0];
for ele in types:
    freq[ele - 1] += 1;
highest = freq[0];
index = 0;
for i in range(1, len(freq)):
    if (freq[i] > highest):
        highest = freq[i];
        index = i;
print(index + 1);
