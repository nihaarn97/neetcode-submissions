class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expect = sorted(heights)
        count = 0
        for a,b in zip(expect, heights):
            if a!=b:
                count = count+1
        return count