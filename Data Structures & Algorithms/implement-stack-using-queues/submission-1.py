from collections import deque

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        left = 0
        while left<len(self.stack)-1:
            temp.append(self.stack[left])
            left = left+1
        val = self.stack[left]
        self.stack = temp
        return val

    def top(self) -> int:
        temp = []
        left = 0
        while left<len(self.stack)-1:
            temp.append(self.stack[left])
            left = left+1
        val = self.stack[left]
        self.stack = temp
        self.stack.append(val)
        return val

    def empty(self) -> bool:
        return False if self.stack else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()