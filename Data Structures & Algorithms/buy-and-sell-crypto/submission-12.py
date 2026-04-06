class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0
        while i<len(prices)-1:
            if prices[i+1]>prices[i]:
                j = i+1
                while j<len(prices) and prices[j]>prices[i]:
                    maxProfit = max(maxProfit, prices[j]-prices[i])
                    j = j+1
                i = j
            else:
                i = i+1

        return maxProfit