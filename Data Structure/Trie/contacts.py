# return the numbers of ones in deep array "arr"
def findones(arr):
    total = 0;
    for element in arr:
        if (type(element) is int):
            total += element;
        else:
            total += findones(element);
    return total;

class Trie:
     def __init__(self):
         self.words = [0] * 27;

     # add word into our words bank
     def add(self, word):
            temp_arr = self.words;
            for i in range(0, len(word)):
                index = ord(word[i]) - ord('a');
                if (temp_arr[index] == 0):
                    temp_arr[index] = [0] * 27;
                temp_arr = temp_arr[index];
            temp_arr[26] = 1;

     # find the number of words that has the word "word" in it
     def find(self, word):
            temp_arr = self.words;
            for i in range(0, len(word)):
                index = ord(word[i]) - ord('a');
                if (temp_arr[index] == 0):
                    return 0;
                else:
                    temp_arr = temp_arr[index];
            total = 0;
            for j in temp_arr:
                if (type(j) is int):
                    total += j;
                else:
                    total += findones(j);
            return total;

# main function
t = Trie();

n = int(input());
for i in range(0, n):
    arr_t = [arr_temp for arr_temp in input().strip().split(' ')];
    if (arr_t[0] == "add"):
        t.add(arr_t[1]);
    else:
        print(t.find(arr_t[1]));
