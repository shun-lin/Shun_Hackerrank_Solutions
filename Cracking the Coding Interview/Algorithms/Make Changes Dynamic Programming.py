#!/bin/python3

import sys

def make_change(coins, n):
    if n < 0 or len(coins) == 0:
        return 0;
    elif n == 0:
        return 1;
    coins_tuple = tuple(coins);
    coins_hash = hash(coins_tuple);
    total_tuple = (coins_hash, n);
    hash_val = hash(total_tuple);
    if hash_val in storage:
        return storage[hash_val];
    else:
        answer = make_change(coins, n - coins[len(coins) - 1]) + make_change(coins[0:len(coins) - 1], n);
        storage[hash_val] = answer;
        return answer;



n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
storage = dict();
coins.sort();
print(make_change(coins, n))
