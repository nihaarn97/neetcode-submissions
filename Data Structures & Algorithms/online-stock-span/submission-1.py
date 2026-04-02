class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        temp = []
        span = 0
        while self.stack:
            if self.stack[-1]<=price:
                temp.append(self.stack.pop())
                span += 1
            else:
                break
        while temp:
            self.stack.append(temp.pop())

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)