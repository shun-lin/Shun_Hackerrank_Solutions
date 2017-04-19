n = input();
result = "";
for char in n:
    if (char == "9"):
        result += "0";
    else:
        result += str(int(char) + 1);
print(result)
