class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        maxLen = 100001

        for right in range(len(nums)):
            total += nums[right]
            while total>=target:
                maxLen = min(maxLen, right-left+1)
                total = total - nums[left]
                left = left + 1

        return 0 if maxLen == 100001 else maxLen
            

            
        