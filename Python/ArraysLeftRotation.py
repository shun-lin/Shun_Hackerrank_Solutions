def array_left_rotation(a, n, k):
    answer = [0 for x in range(n)];
    for i in range(n):
        index = i - k;
        if (index < 0):
            index += n;
        answer[index] = a[i];
    return answer;

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
