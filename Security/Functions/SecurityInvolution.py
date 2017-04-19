def check(n, arr):
    inverse_array = [None] * n;
    arr_set = set(arr);
    if (len(arr) != len(arr_set)):
        print("NO");
        return;
    for i in range(1, n + 1):
        inverse_array[i - 1] = arr.index(i) + 1
    involution = True;
    for j in range(0, n):
        if (inverse_array[j] != arr[j]):
            involution = False;
            print("NO");
            break;
    if (involution):
        print("YES");

# main
n = int(input());
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')];
check(n, arr);
