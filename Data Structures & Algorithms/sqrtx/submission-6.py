class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        if x == 1:
            return 1
        ans = 0

        while l<=r:
            mid = (l+r)//2
            res = mid*mid 
            if res==x:
                return mid
            elif res>x:
                r = mid-1
            else:
                ans = mid
                l = mid+1
        
        return ans