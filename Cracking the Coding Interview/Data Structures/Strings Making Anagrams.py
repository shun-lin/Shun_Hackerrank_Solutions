def number_needed(a, b):
    if not a:
        if not b:
            return 0;
        else:
            return len(b);
    else:
        a_list = list(a);
        b_list = list(b);
        repeat = 0;
        a_length = len(a);
        b_length = len(b);
        for ele in a_list:
            if ele in b_list:
                b_list.remove(ele);
                repeat += 1;
        return a_length + b_length - 2 * repeat;

a = input().strip()
b = input().strip()

print(number_needed(a, b))
