n = int(input());
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_set = set(arr);
if (len(arr) == len(arr_set)):
    print("YES");
else:
    print("NO");
