import hashlib

# helper function
def most_common(lst):
    return max(set(lst), key=lst.count)

def hashing(str):
    result = 0;
    for i in range(0, len(str)):
        result += ord(str[i]) * 31 ^ i;
    return result;

raw_input = input();
raw_input_array = [i for i in raw_input.split()];
while(True):
    try:
        raw_input = input();
        raw_input_array += [i for i in raw_input.split()];
    except EOFError:
        break;

pun = "!.?";
for i in range(0, len(raw_input_array)):
    word = raw_input_array[i];
    for char in pun:
        word = word.replace(char, "");
    word = word.lower();
    raw_input_array[i] = word;
trigrams = [None] * (len(raw_input_array) - 2);
for i in range(0, len(raw_input_array) - 2):
    trigrams[i] = [raw_input_array[i], raw_input_array[i + 1], raw_input_array[i + 2]];
hash_trigrams = [None] * len(trigrams);
for i in range(0, len(trigrams)):
    hash_trigrams[i] = hashing(trigrams[i][0]) * hashing(trigrams[i][1]) * hashing(trigrams[i][2]);
most_frequent_trigram_hash = most_common(hash_trigrams);
index = 0;
while (hash_trigrams[index] != most_frequent_trigram_hash):
    index += 1;
most_frequent_trigram = trigrams[index];
print(most_frequent_trigram[0] + " " + most_frequent_trigram[1] + " " + most_frequent_trigram[2]);
