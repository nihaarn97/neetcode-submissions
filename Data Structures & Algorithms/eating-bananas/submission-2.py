import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = max(piles)
        l = 1
        r = minSpeed
        while l<=r:
            mid = (l+r)//2
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile/mid)

            if timeTaken <= h:
                minSpeed = mid
                r = mid-1

            else:
                l = mid+1



        return minSpeed