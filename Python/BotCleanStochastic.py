# A deterministic environment is one where the next state is completely determined by the current state of the environment and the task executed by the agent.
# If there is any randomness involved in determining the next state, the environment is stochastic.

# The game Bot Clean took place in a deterministic environment.
# In this version, the bot is given 200 moves to clean as many dirty cells as possible.
# The grid initially has 1 dirty cell. When the bot cleans this cell, a new cell in the grid is made dirty.
# The new cell can be anywhere in the grid.

# The bot here is positioned at the top left corner of a 5*5 grid.
# Your task is to move the bot to appropriate dirty cell and clean it.

# Complete the function nextMove that takes in 3 parameters posr, posc being the co-ordinates of the bot’s current position and board which indicates the board state, and print the bot’s next move.

#!/bin/python3
def nextMove(posr, posc, board):
    if (board[posr][posc] == 'd'):
        print("CLEAN");
        return;
    n = len(board);
    found = False;
    closest_position = [0, 0];
    for i in range(0, n):
        if (found == True):
            break;
        for j in range(0, n):
            if (found == True):
                break;
            if (board[i][j] == 'd'):
                closest_position[0] = i;
                closest_position[1] = j;
                found = True;
                break;
    y_difference = closest_position[0] - posr;
    x_difference = closest_position[1] - posc;
    if (y_difference > 0):
        print("DOWN");
        return;
    elif (y_difference < 0):
        print("UP");
        return;
    if (x_difference > 0):
        print("RIGHT");
        return;
    elif (x_difference < 0):
        print("LEFT");
        return;


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
