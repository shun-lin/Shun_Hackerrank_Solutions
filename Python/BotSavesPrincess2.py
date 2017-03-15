# Complete the function nextMove which takes in 4 parameters
# an integer N, integers r and c indicating the row & column position of the bot and the character array grid
# and outputs the next move the bot makes to rescue the princess.
def nextMove(n,r,c,grid):
    princess_position = [0, 0];
    princess_found = False;
    for i in range(0, n):
        if (princess_found):
            break;
        for j in range(0, n):
            if (princess_found):
                break;
            if (grid[i][j] == 'p'):
                princess_position[0] = i;
                princess_position[1] = j;
                princess_found = True;
    y_difference = princess_position[0] - r;
    x_difference = princess_position[1] - c;
    if (y_difference > 0):
        return "DOWN";
    elif (y_difference < 0):
        return "UP";
    if (x_difference > 0):
        return "RIGHT";
    elif (x_difference < 0):
        return "LEFT";


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
