# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def minToEqual(N, lst):
    storage = dict();

    def helper(N, lst, storage):

        def give(N, lst, numCho, index):
            for i in range(0, N):
                if (i != index):
                    lst[i] += numCho;

        def differences(lst, N):
            result = 0;
            maximum = max(lst);
            for i in range(0, N):
                result += maximum - lst[i];
                return result;

        if (differences(lst, N) == 0):
            return 0;

        for i in range(0, N):
            giveOne = give(N, )


    return helper(N, lst, storage);

T = int(input().strip());
for i in range(0, T):
    N = int(input().strip());
    lst = list(map(int, input().strip().split(' ')));
    print(minToEqual(N, lst));
