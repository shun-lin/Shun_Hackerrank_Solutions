class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item);
         self.items.sort();

     def pop(self):
         self.items.pop(len(self.items) - 1)

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s = Stack();

n = int(input());
for i in range(0, n):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    if (arr_t[0] == 1):
        s.push(arr_t[1]);
    elif (arr_t[0] == 2):
        s.pop();
    else:
        if (not s.isEmpty()):
            print(s.peek());
