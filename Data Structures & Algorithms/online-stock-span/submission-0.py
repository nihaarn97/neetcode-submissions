class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        temp = []
        while self.stack and self.stack[-1]<=price:
            temp.append(self.stack.pop())
            span = span+1
        
        while temp:
            self.stack.append(temp.pop())
        
        self.stack.append(price)
        
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)