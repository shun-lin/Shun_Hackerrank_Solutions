# given input of N towers and M heights and curr player (player 1 = curr = 1), returns the winner.
def TowerBreakers(N, M, curr):
    if (M == 1):
        return 3 - curr;
    elif (N == 1):
        return curr;
    else:
        if (N % 2 == 0):
            return 3 - curr;
        else:
            return curr;

#main
num_test = input();
for i in range(0, int(num_test)):
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    N = arr[0];
    M = arr[1];
    winner = TowerBreakers(N, M, 1);
    print(winner);
