#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort();
total = 0;
prev = c[0];
counter = 1;
for i in range(1, len(c)):
    if (c[i] == prev):
        if (counter == 1):
            total += 1;
            counter += 1;
        else:
            counter = 1;
    else:
        prev = c[i];
        counter = 1;
print(total)
