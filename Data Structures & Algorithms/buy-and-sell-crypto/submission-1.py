class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0
        while i<=len(prices)-2:
            if prices[i+1]<=prices[i]:
                i = i+1
            else:
                j = i+1
                while j<len(prices):
                    if prices[j]>prices[i]:
                        profit = prices[j] - prices[i]
                        maxProfit = max(maxProfit, profit)
                        j = j+1
                    else:
                        break
                i = j

        return maxProfit
        