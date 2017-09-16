#!/bin/python3

import sys

# return the maximum profit of the array
def maximumProfit(n, arr):

    # return the maximum profit of the array from arr[start] to arr[end]
    def helper(arr):

        def buyAllSellLast(arr):
            priceToBuy = 0;
            for price in arr[0:len(arr) - 1]:
                priceToBuy += price;
            numStockBought = len(arr) - 1;
            result = arr[len(arr) - 1] * numStockBought - priceToBuy;
            return result;
        if (arr == None or len(arr) <= 1):
            return 0;
        maximum_price = max(arr);
        maximum_index = arr.index(maximum_price);
        if (maximum_index == 0):
            return helper(arr[1:]);
        elif (maximum_index == len(arr) - 1):
            return buyAllSellLast(arr);
        else:
            return helper(arr[0:maximum_index + 1]) + helper(arr[maximum_index+1:len(arr)]);

    return helper(arr);
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = maximumProfit(n, arr);
        print(result);
