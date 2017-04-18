# returns 0 is first player wins and 1 is second player wins, n stones starts
def GameOfStone(n):
    result = n % 7;
    if (result < 2):
        return 1;
    else:
        return 0;


# main
num_lines = input();
for i in range(0, int(num_lines)):
    n_str = input();
    n = int(n_str);
    who_wins = GameOfStone(n);
    if (who_wins == 0):
        print("First");
    else:
        print("Second");
