#!/bin/python3

import sys


def minimumAbsoluteDifference(n, arr):
    # Complete this function

    def helper(minSoFar, arr, startingIndex):
        if (startingIndex == len(arr) - 1):
            return minSoFar;
        for i in range(startingIndex, len(arr) - 2):
            minSoFar = min(abs(startingIndex - arr[i]), minSoFar);
        return helper(minSoFar, arr, startingIndex + 1);
    return helper(999999, arr, 0);

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
