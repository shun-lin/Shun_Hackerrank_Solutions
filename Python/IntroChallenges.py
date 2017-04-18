V = int(input());
n = int(input());
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')];
result = 0;
while (arr[result] != V):
    result += 1;
print(result);
