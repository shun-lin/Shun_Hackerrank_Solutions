#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if (x1 == x2):
    print("YES");
elif ((x2 > x1 and v2 >= v1) or (x1 > x2 and v1 >= v2)):
        print("NO");
elif (abs(x2 - x1) % abs(v1 - v2) == 0):
    print("YES");
else:
    print("NO");
