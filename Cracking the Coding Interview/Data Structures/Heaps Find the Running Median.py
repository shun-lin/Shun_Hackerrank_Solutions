#!/bin/python3

import sys
import bisect


n = int(input().strip())
a_i = 0
a = []
for a_i in range(n):
    a_t = int(input().strip())
    index = bisect.bisect(a, a_t);
    a.insert(index, a_t);
    if len(a) % 2 == 1:
        print(float(a[int(len(a) / 2)]));
    else:
        print((a[int(len(a) / 2 - 1)] + a[int(len(a)/2)]) /2);
