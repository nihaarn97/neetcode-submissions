class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - k%len(nums)
        if pivot == 0:
            return nums
        l = 0
        r = pivot - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l+1
            r = r-1

        l = pivot
        r = len(nums) - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l+1
            r = r-1

        l = 0
        r = len(nums) - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l+1
            r = r-1
