# Enter your code here. Read input from STDIN. Print output to STDOUT

# working backward
def maxS(N, B):

    class helperSolution:
        def __init__(self, maxSWithMax, maxLastDigit, maxSWithMin, minLastDigit):
            self.maxSWithMax = maxSWithMax
            self.maxLastDigit = maxLastDigit
            self.maxSWithMin = maxSWithMin
            self.minLastDigit = minLastDigit

    def calculate(Bi, lastSolution):
        maxThisDigit = Bi;
        maxSWithMax = lastSolution.maxSWithMax + abs(Bi - lastSolution.maxLastDigit);
        if (maxSWithMax < lastSolution.maxSWithMin + abs(Bi - lastSolution.minLastDigit)):
            maxSWithMax = lastSolution.maxSWithMin + abs(Bi - lastSolution.minLastDigit);
        minThisDigit = 1;
        maxSWithMin = lastSolution.maxSWithMax + abs(1 - lastSolution.maxLastDigit);
        if (maxSWithMin < lastSolution.maxSWithMin + abs(1 - lastSolution.minLastDigit)):
            maxSWithMin = lastSolution.maxSWithMin + abs(1 - lastSolution.minLastDigit);
        return helperSolution(maxSWithMax, maxThisDigit, maxSWithMin, minThisDigit);

    def highestMaxS(helperSolution):
        if (helperSolution.maxSWithMax > helperSolution.maxSWithMin):
            return helperSolution.maxSWithMax;
        return helperSolution.maxSWithMin;

    # return maxS and the first element
    def helper(index, B, lastSolution):
        if (index < 0):
            return lastSolution;
        if (index == len(B) - 1):
            thisSolution = helperSolution(0, B[index], 0, 1);
        else:
            thisSolution = calculate(B[index], lastSolution)
        return helper(index-1, B, thisSolution);

    Solution = helper(N-1, B, None);
    return highestMaxS(Solution);


T = int(input().strip())
for i in range(0, T):
    N = int(input().strip());
    B = list(map(int, input().strip().split(' ')));
    print(maxS(N, B))
