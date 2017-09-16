#!/bin/python3

import sys


def minimumAbsoluteDifference(n, arr):

    arr.sort();
    minimum = 999999999999;
    for i in range(0, len(arr) - 1):
        minimum = min(minimum, abs(arr[i] - arr[i + 1]));
    return minimum;


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
