class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.max_ele = k
        self.left = 0
        self.right = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.right = (self.right+1)%self.max_ele
        self.q[self.right] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.left] = 0
        self.left = (self.left+1)%self.max_ele
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.right]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.max_ele:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()