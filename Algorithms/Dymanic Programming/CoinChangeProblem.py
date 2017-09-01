# Enter your code here. Read input from STDIN. Print output to STDOUT

def waysForChange(n, m, C):
    storage = dict();

    def hashcode(n, m):
        return n + m * 2000;

    def helper(n, m, C, storage):
        key = hashcode(n, m);
        if (key in storage):
            return storage[key];
        if (n == 0):
            return 1;
        if (n < 0 or m <= 0):
            return 0;
        result = helper(n, m - 1, C, storage) + helper(n - C[m-1], m, C, storage);
        storage[key] = result;
        return result;

    return helper(n, m, C, storage);


nAndm = list(map(int, input().strip().split(' ')))
n = nAndm[0];
m = nAndm[1];
C = list(map(int, input().strip().split(' ')))
C.sort();
print(waysForChange(n, m, C))
