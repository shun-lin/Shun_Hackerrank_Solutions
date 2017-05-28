#!/bin/python3

import sys

def make_change(coins, n):
    if n < 0 or len(coins) == 0:
        return 0;
    elif n == 0:
        return 1;
    else:
        return make_change(coins, n - coins[len(coins) - 1]) + make_change(coins[0:len(coins) - 1], n)



n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
coins.sort();
print(make_change(coins, n))
