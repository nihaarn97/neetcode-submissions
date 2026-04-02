class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        minLen = len(nums)+1
        currSum = 0
        while r<len(nums):
            currSum = currSum + nums[r]
            if currSum>=target:
                minLen = min(minLen, r-l+1)
                while l<r:
                    currSum = currSum - nums[l]
                    l = l+1
                    if currSum >= target:
                        minLen = min(minLen, r-l+1)
                    else:
                        break
                r = r+1

            else:
                r = r+1

        if minLen == len(nums)+1:
            return 0
        else:
            return minLen