def count_inversions(a):
    if (a == None or len(a) <= 1):
        return 0;
    total_inversions = 0;
    def swap(a, i, j):
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
        return;
    n = len(a);
    i = 0;
    j = 1;
    prev_i = 0;
    prev_j = 0;
    has_prev = 0;
    while (i < n - 1):
        if (a[i] > a[j]):
            swap(a, i, j);
            total_inversions += 1;
            has_prev = 1;
            prev_i = i;
            prev_j = j;
            if (i != 0):
                i -= 1;
                j -= 1;
            else:
                i += 1;
                j += 1;
        elif (has_prev):
            i = prev_i;
            j = prev_j;
            has_prev = 0;
        else:
            i += 1;
            j += 1;
    return total_inversions;



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))
