def superDigit(number):
    if len(number) < 2:
        return number;
    sum = 0;
    for char in number:
        sum += int(char);
    return superDigit(str(sum));


nAndk = list(map(int, input().strip().split(' ')))
n = nAndk[0];
k = nAndk[1];
n_string = str(n);
n_superDigit = superDigit(n_string);
print(superDigit(n_superDigit * k));
