# The goal of Artificial Intelligence is to create a rational agent (Artificial Intelligence 1.1.4).
# An agent gets input from the environment through sensors and acts on the environment with actuators.
# In this challenge, you will program a simple bot to perform the correct actions based on environmental input.

# Meet the bot MarkZoid.
# It's a cleaning bot whose sensor is a head mounted camera and whose actuators are the wheels beneath it.
# It's used to clean the floor.

# The bot here is positioned at the top left corner of a 5*5 grid.
# Your task is to move the bot to clean all the dirty cells.

# Complete the function next_move that takes in 3 parameters posr, posc being the co-ordinates of the bot's current position and board which indicates the board state to print the bot's next move.
# The codechecker will keep calling the function next_move till the game is over or you make an invalid move.

#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
    if (board[posr][posc] == 'd'):
        print("CLEAN");
        return;
    n = len(board);
    closest_distance = 2 * n + 1; # initalize closest distance to max possible distance
    closest_position = [0, 0];
    for i in range(0, n):
        if (closest_distance == 1):
            break;
        for j in range(0, n):
            if (closest_distance == 1):
                break;
            if (board[i][j] == 'd'):
                distance = abs(posr - i) + abs(posc - j);
                if (distance < closest_distance):
                    closest_distance = distance;
                    closest_position[0] = i;
                    closest_position[1] = j;
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

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
