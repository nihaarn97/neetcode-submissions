class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxSum = max(nums)
        i=0
        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                currSum = nums[i]
                j = i+1
                while j<len(nums):
                    if nums[j]>nums[j-1]:
                        currSum += nums[j]
                        j = j+1
                    else:
                        break
                maxSum = max(maxSum, currSum)
                i = j
            else:
                i = i+1

        return maxSum

        