import random

class Solution:

    def __init__(self, w: List[int]):
        self.nums = w
        self.probs = []
        weightSum = sum(w)
        for val in self.nums:
            self.probs.append(round(val/weightSum,2))
        for i in range(1,len(self.probs)):
            self.probs[i] += self.probs[i-1]

    def pickIndex(self) -> int:
        pick = random.uniform(0.0, 1.0)
        l = 0
        r = len(self.probs)-1
        idx = 0
        while l<=r:
            mid = (l+r)//2
            if round(pick, 2) == self.probs[mid]:
                return mid
            elif round(pick, 2) > self.probs[mid]:
                l = mid+1
            else:
                idx = mid
                r = mid-1

        return idx




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()