def add_word(word, bank):
    for i in range(1, len(word)+1):
        if word[:i] in bank:
            bank[word[:i]] += 1
        else:
            bank[word[:i]] = 1

def find_partial(word, bank):
    return bank.get(word) or 0

# main
bank = {};
n = int(input());
for i in range(0, n):
    arr_t = [arr_temp for arr_temp in input().strip().split(' ')];
    word = arr_t[1];
    if (arr_t[0] == "add"):
        add_word(word, bank);
    else:
        print(find_partial(word, bank));
