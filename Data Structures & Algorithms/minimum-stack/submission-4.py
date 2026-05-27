class MinStack:
    stack = list()

    def __init__(self):
        self.stack = list()
        self.minStack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else: 
            if self.minStack[-1] >= val: self.minStack.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]: self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
