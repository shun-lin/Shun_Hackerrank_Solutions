n = int(input().strip())
names = dict();
def add(name, names):
    for i in range(1, len(name) + 1):
        sub = name[0:i];
        if sub in names:
            names[sub] += 1;
        else:
            names[sub] = 1;
def find(partial, names):
    if partial in names:
        return names[partial];
    return 0;
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        add(contact, names);
    else:
        print(find(contact, names));
        
