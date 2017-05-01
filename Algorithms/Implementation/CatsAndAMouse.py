#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    dis_a = abs(x - z);
    dis_b = abs(y - z);
    if (dis_a < dis_b):
        print("Cat A");
    elif (dis_a > dis_b):
        print("Cat B");
    elif (dis_a == dis_b):
        print("Mouse C");
