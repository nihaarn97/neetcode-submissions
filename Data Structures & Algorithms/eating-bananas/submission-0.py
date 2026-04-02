import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        global_min = high
        while low<=high:
            mid = (low+high)//2
            time_taken = sum([math.ceil(x/mid) for x in piles])
            if time_taken <= h:
                high = mid - 1 #eat slower
                global_min = min(mid, global_min)
            else:
                low = mid + 1 #eat faster
        return global_min
        