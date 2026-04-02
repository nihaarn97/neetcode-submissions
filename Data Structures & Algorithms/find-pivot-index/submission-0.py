class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = {0:0}
        suffixSum = {len(nums)-1:0}

        preSum = 0
        sufSum = 0
        for i in range(1, len(nums)):
            preSum += nums[i-1]
            prefixSum[i] = preSum

        for i in range(len(nums)-2, -1, -1):
            sufSum += nums[i+1]
            suffixSum[i] = sufSum

        for i in range(len(nums)):
            if prefixSum[i] == suffixSum[i]:
                return i

        return -1