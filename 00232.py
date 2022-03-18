class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []
        

    def push(self, x: int) -> None:
        self.inStack.append(x)
        

    def pop(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()
        

    def peek(self) -> int:
        if self.outStack:
            return self.outStack[-1]
        else:
            return self.inStack[0]
        

    def empty(self) -> bool:
        return len(self.inStack) == 0 and len(self.outStack) == 0




