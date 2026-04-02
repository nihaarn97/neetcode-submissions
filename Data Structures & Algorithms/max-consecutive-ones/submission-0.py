class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for val in nums:
            if val == 1:
                count = count+1
            else:
                maxcount = max(maxcount, count)
                count = 0

        return max(maxcount, count)
        