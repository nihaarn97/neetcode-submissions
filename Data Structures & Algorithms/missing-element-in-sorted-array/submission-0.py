import random

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(1, n):
            missed = nums[i] - nums[i-1] - 1
            if missed>=k:
                return nums[i-1]+k
            k = k - missed

        return nums[-1] + k