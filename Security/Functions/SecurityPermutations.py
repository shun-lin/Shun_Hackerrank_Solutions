n = int(input());
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')];
for i in range(0, n):
    f_i = arr[i];
    print(arr[f_i - 1]);
