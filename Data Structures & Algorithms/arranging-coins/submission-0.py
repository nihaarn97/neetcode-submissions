class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        l = 1
        r = n
        while l<=r:
            mid = (l+r)//2
            if mid*(mid+1)//2 > n:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        
        return res
            
        