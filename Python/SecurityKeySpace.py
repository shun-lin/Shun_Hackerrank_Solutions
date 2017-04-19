x = input();
n = int(input());
result = "";
for char in x:
    shift = int(char) + n;
    shift = shift % 10;
    result += str(shift);
print(result);
