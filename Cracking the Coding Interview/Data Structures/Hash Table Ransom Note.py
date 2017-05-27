def ransom_note(magazine, ransom):
    if not ransom:
        return True;
    elif not magazine and ransom:
        return False;
    words = dict();
    for word in magazine:
        if word in words:
            words[word] += 1;
        else:
            words[word] = 1;
    for ran in ransom:
        if ran in words:
            if words[ran] == 0:
                return False;
            else:
                words[ran] -= 1;
                continue;
        return False;
    return True;


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
