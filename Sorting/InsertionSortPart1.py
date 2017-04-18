n = input();
n = int(n);
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_len = len(arr);
unordered_element = arr[arr_len - 1];
i = arr_len - 2;
while (arr[i] > unordered_element):
    arr[i + 1] = arr[i];
    for j in range(0, arr_len - 1):
        print(str(arr[j]) + " ", end="");
    print(str(arr[arr_len - 1]) + " ");
    i -= 1;
    if (i == -1):
        break;
arr[i + 1] = unordered_element;
for j in range(0, arr_len):
    print(str(arr[j]) + " ", end="");
