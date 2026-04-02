class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif flag == 0 and nums[i] >= nums[i-1]:
                flag = 1
            elif flag == 0 and nums[i] <= nums[i-1]:
                flag = 2
            elif flag == 1 and nums[i] <= nums[i-1]:
                return False
            elif flag == 2 and nums[i] >= nums[i-1]:
                return False

        return True