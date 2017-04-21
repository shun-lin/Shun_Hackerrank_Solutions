player = int(input());
game_board = [[0] * 8 for element in range(0, 8)];
for i in range(0, 8):
    raw_input = input();
    for j in range(0, 8):
        piece = int(raw_input[j]);
        if (piece == 0):
            game_board[i][j] = -1;
        else:
            game_board[i][j] = 1;
fire_score = [[0] * 8 for element in range(0, 8)];
for i in range(0, 8):
    for j in range(0, 8):
        if (game_board[i][j] == -1):
                fire_score[i][j] = -99999;
        elif (j != 7 and i != 7):
            fire_score[i][j] = game_board[i][j] + game_board[i+1][j] + game_board[i][j+1];
        elif (j == 7 and i != 7):
            fire_score[i][j] = game_board[i][j] + game_board[i+1][j];
        elif(j != 7 and i == 7):
            fire_score[i][j] = game_board[i][j] + game_board[i][j+1];
        else:
            fire_score[i][j] = 1;
max_score = fire_score[0][0];
max_i = 0;
max_j = 0;
for i in range(0, 8):
    for j in range(0, 8):
        if (max_score == 3):
            break;
        if (fire_score[i][j] > max_score):
            max_score = fire_score[i][j];
            max_i = i;
            max_j = j;
print(str(max_i) + " " + str(max_j));
