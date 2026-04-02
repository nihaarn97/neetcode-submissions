class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x//2
        if x == 1:
            return 1
        while True:
            mid = (l+r)//2
            res = mid*mid 
            if res==x:
                return mid
            elif res>x:
                r = mid-1
            else:
                if (mid+1)*(mid+1)>x:
                    return mid
                l = mid+1
        