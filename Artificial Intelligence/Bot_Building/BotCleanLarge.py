def next_move(posx, posy, dimx, dimy, board):
    if (board[posx][posy] == 'd'):
        print("CLEAN");
        return;
    closest_distance = dimx + dimy; # initalize closest distance to max possible distance
    closest_position = [0, 0];
    for i in range(0, dimx):
        if (closest_distance == 1):
            break;
        for j in range(0, dimy):
            if (closest_distance == 1):
                break;
            if (board[i][j] == 'd'):
                distance = abs(posx - i) + abs(posy - j);
                if (distance < closest_distance):
                    closest_distance = distance;
                    closest_position[0] = i;
                    closest_position[1] = j;
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
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
