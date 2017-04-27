#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    storage = [];
    isBalanced = 1;
    printedNo = 0;
    for char in s:
        if (char == '('):
            storage.append(1);
        elif (char == '['):
            storage.append(2);
        elif (char == '{'):
            storage.append(3);
        elif (char == ')'):
            if (len(storage) == 0):
                print("NO");
                isBalanced = 0;
                printedNo = 1;
                break;
            elif (storage[len(storage) - 1] != 1):
                print("NO");
                isBalanced = 0;
                printedNo = 1;
                break;
            else:
                storage.pop(len(storage) - 1);
        elif (char == ']'):
            if (len(storage) == 0):
                print("NO");
                isBalanced = 0;
                printedNo = 1;
                break;
            elif (storage[len(storage) - 1] != 2):
                print("NO");
                isBalanced = 0;
                printedNo = 1;
                break;
            else:
                storage.pop(len(storage) - 1);
        elif (char == '}'):
            if (len(storage) == 0):
                print("NO");
                isBalanced = 0;
                printedNo = 1;
                break;
            elif (storage[len(storage) - 1] != 3):
                print("NO");
                isBalanced = 0;
                printedNo = 1;
                break;
            else:
                storage.pop(len(storage) - 1);
    if (isBalanced == 1 and len(storage) == 0):
        print("YES");
    elif (printedNo == 0):
        print("NO");
