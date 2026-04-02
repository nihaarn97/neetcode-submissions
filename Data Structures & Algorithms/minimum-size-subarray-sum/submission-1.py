class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        minLen = len(nums)+1
        currSum = 0
        while j<len(nums):
            currSum += nums[j]
            if currSum>=target:
                minLen = min(minLen, j-i+1)
                while i<j:
                    currSum -= nums[i]
                    i = i+1
                    if currSum>=target:
                        minLen = min(minLen, j-i+1)
                    else:
                        break
            j = j+1

        if minLen == len(nums)+1:
            return 0
        return minLen