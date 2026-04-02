class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.maxsize = size
        self.size = 0
        self.add = 0

    def next(self, val: int) -> float:
        if self.size < self.maxsize:
            self.q.append(val)
            self.add += val
            self.size += 1
            return self.add/self.size
        else:
            self.add -= self.q.popleft()
            self.q.append(val)
            self.add += val
            return self.add/self.maxsize
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
