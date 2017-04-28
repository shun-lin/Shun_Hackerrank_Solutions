# return the numbers of ones in deep array "arr"
def findones(dic):
    total = 0;
    for key in list(dic.keys()):
        if (type(dic[key]) is int):
            total += 1;
        else:
            total += findones(dic[key]);
    return total;

class Trie:
     def __init__(self):
         self.words = dict();

     # add word into our words bank
     def add(self, word):
            temp_dic = self.words;
            for i in range(0, len(word)):
                char = word[i];
                if (char not in temp_dic):
                    temp_dic[char] = dict();
                temp_dic = temp_dic[char];
            if ("_end" not in temp_dic):
                temp_dic["_end"] = 0;

     # find the number of words that has the word "word" in it
     def find(self, word):
            temp_dic = self.words;
            for i in range(0, len(word)):
                char = word[i];
                if (char not in temp_dic):
                    return 0;
                temp_dic = temp_dic[char];
            return findones(temp_dic);

# main function
t = Trie();

n = int(input());
for i in range(0, n):
    arr_t = [arr_temp for arr_temp in input().strip().split(' ')];
    if (arr_t[0] == "add"):
        t.add(arr_t[1]);
    else:
        print(t.find(arr_t[1]));
