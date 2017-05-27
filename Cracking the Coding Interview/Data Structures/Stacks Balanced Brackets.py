def is_matched(expression):
    if not expression:
        return True;
    storage = [];
    for ele in expression:
        if ele == '(' or ele == '[' or ele == '{':
            storage.append(ele);
        elif ele == ')':
            if not storage or storage[len(storage) - 1] != '(':
                return False;
            else:
                storage.pop();
        elif ele == ']':
            if not storage or storage[len(storage) - 1] != '[':
                return False;
            else:
                storage.pop();
        elif ele == '}':
            if not storage or storage[len(storage) - 1] != '{':
                return False;
            else:
                storage.pop();
    if len(storage) == 0:
        return True;
    else:
        return False;

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
