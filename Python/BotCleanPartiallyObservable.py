# The game Bot Clean took place in a fully observable environment, i.e., the state of every cell was visible to the bot at all times.
# Let us consider a variation of it where the environment is partially observable.
# The bot has the same actuators and sensors. But the sensors visibility is confined to its 8 adjacent cells.

# Complete the function next_move that takes in 3 parameters: posr and posc denote the co-ordinates of the bot’s current position, and board denotes the board state, and print the bot’s next move.

#!/usr/bin/python3
def next_move(posx, posy, board):
    if (board[posx][posy] == 'd'):
        print("CLEAN");
        return;
    n = len(board);
    closest_distance = 2 * len(board); # initalize closest distance to max possible distance
    closest_position = [0, 0];
    for i in range(0, n):
        if (closest_distance == 1):
            break;
        for j in range(0, n):
            if (closest_distance == 1):
                break;
            if (board[i][j] == 'd'):
                distance = abs(posx - i) + abs(posy - j);
                if (distance <= closest_distance):
                    closest_distance = distance;
                    closest_position[0] = i;
                    closest_position[1] = j;
    if (closest_distance == 2 * len(board)):
        if (posx == 0):
            print("DOWN");
            return;
        elif (posx == 4):
            print("UP");
            return;
        elif (posy == 0):
            print("RIGHT");
            return;
        elif (posy == 4):
            print("LEFT");
            return;
        else:
            if (posx == 1 and (posy == 1 or posy == 2)):
                print("RIGHT");
                return;
            elif ((posx == 1 or posx == 2) and posy == 3):
                print("DOWN");
                return;
            elif (posx == 3 and (posy == 3 or posy == 2)):
                print("LEFT");
                return;
            elif ((posx == 3 or posx == 2) and posy == 1):
                print("UP");
                return;
            else:
                print("RIGHT");
                return;
    y_difference = closest_position[0] - posx;
    x_difference = closest_position[1] - posy;
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
    next_move(pos[0], pos[1], board)
