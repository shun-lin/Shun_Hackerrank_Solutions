n = int(input());
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')];
for i in range(1, n + 1):
    print(arr.index(i) + 1)
