class MyQueue:

    def __init__(self):
        self.q = []
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        temp = []
        while self.q:
            temp.append(self.q.pop())
        val = temp.pop()
        while temp:
            self.q.append(temp.pop())
        return val

    def peek(self) -> int:
        temp = []
        while self.q:
            temp.append(self.q.pop())
        val = temp[-1]
        while temp:
            self.q.append(temp.pop())
        return val

    def empty(self) -> bool:
        return False if self.q else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()