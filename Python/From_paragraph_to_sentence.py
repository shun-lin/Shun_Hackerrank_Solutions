raw_input = input();
in_quotation = False;
for i in raw_input:
    if (i == '"'):
        in_quotation = not in_quotation;
    if ((i == '.') or (i =='?') or (i == '!')):
        if (in_quotation):
            print(i, end='');
        else:
            print(i);
    else:
        print(i, end='');
