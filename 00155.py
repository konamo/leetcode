class MinStack:
    def __init__(self):
        self.A = []
        self.M = []
    def push(self, x):
        self.A.append(x)
        M = self.M
        M.append( x if not M else min(x,M[-1]) )
    def pop(self):
        self.A.pop()
        self.M.pop()
    def top(self):
        return self.A[-1]
    def getMin(self):
        return self.M[-1]


class MinStack2:

    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));

    # @return nothing
    def pop(self):
        self.q.pop()


    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]


    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]


def main():
    s = MinStack()
    s.push(0)
    s.push(-2)
    s.push(-3)

    print(s.pop())
    print(s.pop())
    print(s.getMin())
    return



if __name__ == '__main__':
    main()
