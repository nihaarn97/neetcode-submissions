class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = len(nums) - k%len(nums)

        left = 0
        right = mid-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left+1
            right = right - 1

        left = mid
        right = len(nums)-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left+1
            right = right - 1

        left = 0
        right = len(nums)-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left+1
            right = right - 1