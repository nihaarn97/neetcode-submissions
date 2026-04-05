class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l<r:
            currArr = (r-l)*min(heights[r],heights[l])
            maxArea = max(maxArea, currArr)
            if heights[r] > heights[l]:
                l = l+1
            else:
                r = r-1

        return maxArea

        