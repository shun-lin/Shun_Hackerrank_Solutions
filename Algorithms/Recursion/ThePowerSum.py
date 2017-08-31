# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def powerSums(X, N):

    def powerSumsHelper(X, N, minimum):
        if (X < 0):
            return 0;
        min_pow_n = minimum ** N;
        if (min_pow_n > X):
            return 0;
        if (min_pow_n == X):
            return 1;
        return powerSumsHelper(X, N, minimum + 1) + powerSumsHelper(X-min_pow_n, N, minimum + 1);

    return powerSumsHelper(X, N, 1);

X = int(input().strip())
N = int(input().strip())

print(powerSums(X, N));
