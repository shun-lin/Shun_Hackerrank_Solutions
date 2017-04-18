# returns 0 is first player wins and 1 is second player wins, n stones starts
def GameOfStone(n):
    # n = number of stones, curr = current player (0 = first, 1 = second)
    def GameOfStoneHelper(n, curr):
        # base case, if having less than 2 stones the other player wins
        if (n < 2):
            return 1 - curr;
        # recursion
        if (curr == 1):
            return GameOfStoneHelper(n - 2, 1 - curr) or GameOfStoneHelper(n - 3, 1 - curr) or GameOfStoneHelper(n - 5, 1 - curr);
        else:
            return GameOfStoneHelper(n - 2, 1 - curr) and GameOfStoneHelper(n - 3, 1 - curr) and GameOfStoneHelper(n - 5, 1 - curr);
    return GameOfStoneHelper(n, 0);


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
