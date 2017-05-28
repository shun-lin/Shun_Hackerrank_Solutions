n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

total_numberOfSwaps = 0
for i in range(0, n):
    numberOfSwaps = 0;
    for j in range(0, n-1):
        if (a[j] > a[j + 1]):
            temp = a[j];
            a[j] = a[j+1];
            a[j+1] = temp;
            numberOfSwaps += 1;
            total_numberOfSwaps += 1;
    if numberOfSwaps == 0:
        break;
print("Array is sorted in " + str(total_numberOfSwaps) + " swaps.");
print("First Element: " + str(a[0]));
print("Last Element: " + str(a[len(a) - 1]));
