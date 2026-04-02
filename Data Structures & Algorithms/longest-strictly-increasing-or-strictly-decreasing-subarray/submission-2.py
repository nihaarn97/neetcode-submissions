class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxsub = 1
        i = 0
        while i<len(nums)-1:
            if nums[i+1]>nums[i]:
                count = 1
                j = i+1
                while j<len(nums) and nums[j]>nums[j-1]:
                    count = count+1
                    j = j+1
                maxsub = max(maxsub, count)
                i = j-1
            elif nums[i+1]<nums[i]:
                count = 1
                j = i+1
                while j<len(nums) and nums[j]<nums[j-1]:
                    count = count+1
                    j = j+1
                maxsub = max(maxsub, count)
                i = j-1
            else:
                i = i+1

        return maxsub