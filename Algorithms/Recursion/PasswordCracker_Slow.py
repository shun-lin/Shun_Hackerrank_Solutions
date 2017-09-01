# Enter your code here. Read input from STDIN. Print output to STDOUT

def isCorrect(attempt, passwords):
    failures = dict();

    def matchFront(attempt, start, password):
        if (len(password) > len(attempt) - start):
            return False;
        return password == attempt[start:start + len(password)];

    def helper(attempt, start, passwords, soFar, failures):
        if (start in failures):
            return None;
        restAttempt = attempt[start:];
        if (attempt == None or start >= len(attempt)):
            return None;
        if (restAttempt in passwords):
            soFar.append(restAttempt);
            return soFar;
        for password in passwords:
            if (matchFront(attempt, start, password)):
                potentialSolution = list(soFar);
                potentialSolution.append(password);
                newStart = start + len(password);
                result = helper(attempt, newStart, passwords, potentialSolution, failures);
                if (result != None):
                    return result;
                failures[newStart] = result;
        return None;

    result = helper(attempt, 0, passwords, [], failures);
    if (result == None):
        return "WRONG PASSWORD";
    return " ".join(result);



T = int(input().strip())
for i in range(0, T):
    n = int(input().strip())
    passwords_lst = list(input().strip().split(' '));
    passwords = dict();
    for password in passwords_lst:
        passwords[password] = True;
    attempt = input().strip();
    print(isCorrect(attempt, passwords))
