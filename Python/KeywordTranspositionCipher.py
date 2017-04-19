import math

n = int(input());
for test_case in range(0, n):
    keyword = input();
    keyword = [j for i,j in enumerate(keyword) if j not in keyword[:i]];
    coll = len(keyword);
    roww = math.ceil(26 / coll);
    alpha_matrix = [[0 for x in range(coll)] for y in range(roww)];
    alpha_matrix[0] = keyword;
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0;
    for alphabet in alphabets:
        if alphabet in keyword:
            continue;
        else:
            row = 1 + math.floor(index / coll);
            col = index % coll;
            alpha_matrix[row][col] = alphabet;
            index += 1;
    keyword = sorted(keyword);
    new_alpha = [];
    for character in keyword:
        index = alpha_matrix[0].index(character);
        for j in range(0, roww):
            if (alpha_matrix[j][index] != 0):
                new_alpha.append(alpha_matrix[j][index]);
    arr = input();
    for en_char in arr:
        if (en_char == " "):
            print(en_char, end="");
        else:
            original_offset = new_alpha.index(en_char);
            new_char = str(chr(original_offset + ord("A")));
            print(new_char, end="");
    print();
