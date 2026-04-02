class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftmin = [0]*len(prices)
        leftmin[0] = prices[0]
        for i in range(1,len(prices)):
            leftmin[i] = min(leftmin[i-1], prices[i])
        
        res = [x-y for x,y in zip(prices, leftmin)]
        return max(res)
        