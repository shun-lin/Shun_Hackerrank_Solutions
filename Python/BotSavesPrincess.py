#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    bot_position = [0, 0];
    princess_position = [0, 0];
    bot_found = False;
    princess_found = False;
    for i in range(0, n):
        if (bot_found and princess_found):
            break;
        for j in range(0, n):
            if (bot_found and princess_found):
                break;
            if (grid[i][j] == 'm'):
                bot_position[0] = i;
                bot_position[1] = j;
                bot_found = True;
            elif (grid[i][j] == 'p'):
                princess_position[0] = i;
                princess_position[1] = j;
                princess_found = True;
    y_difference = princess_position[0] - bot_position[0];
    x_difference = princess_position[1] - bot_position[1];
    if (y_difference > 0):
        for y_moves in range(0, y_difference):
            print("DOWN");
    elif (y_difference < 0):
        for y_moves in range(0, -y_difference):
            print("UP");
    if (x_difference > 0):
        for x_moves in range(0, x_difference):
            print("RIGHT");
    elif (x_difference < 0):
        for x_moves in range(0, -x_difference):
            print("LEFT");

#print all the moves here
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
