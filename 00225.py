class MyStack:

    def __init__(self):
        self.inQueue = []
        self.outQueue = []
        self.front = 0
        

    def push(self, x: int) -> None:
        self.inQueue.append(x)
        self.front = x
        

    def pop(self) -> int:
        size = len(self.inQueue)
        while size > 1:
            self.front = self.inQueue.pop(0)
            self.outQueue.append(self.front)
            size -= 1
        ret = self.inQueue.pop(0)
        assert(self.inQueue == [])
        self.inQueue, self.outQueue = self.outQueue, self.inQueue
        return ret
        

    def top(self) -> int:
        return self.front

    def empty(self) -> bool:
        return len(self.inQueue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



def main():
    s = MyStack()
    s.push(0)
    s.push(1)
    s.push(2)
    s.pop()
    s.top()
    return



if __name__ == '__main__':
    main()
