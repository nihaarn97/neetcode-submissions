class Solution:
    def maxDifference(self, s: str) -> int:
        countmap = {}
        for val in s:
            countmap[val] = 1 + countmap.get(val, 0)
        
        a1 = 0
        a2 = len(s)
        for val in countmap.values():
            if val%2 == 1:
                a1 = max(a1, val)
            else:
                a2 = min(a2, val)
            
        return a1-a2