length = int(input());
arr = [int(c_temp) for c_temp in input().strip().split(' ')];
dictionary = dict();
arr_set = set(arr);
for ele in arr_set:
    dictionary[ele] = 0;
for ele in arr:
    dictionary[ele] += 1;
most_occurance = 0;
for ele in dictionary:
    if (dictionary[ele] > most_occurance):
        most_occurance = dictionary[ele];
print(len(arr) - most_occurance)
