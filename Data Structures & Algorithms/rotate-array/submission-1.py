class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        pivot = k%len(nums)
        if pivot == 0:
            return nums
        l = 0
        r = len(nums)-pivot
        i = 0
        while r<len(temp):
            nums[i] = temp[r]
            i += 1
            r += 1
        while l < len(nums)-pivot:
            nums[i] = temp[l]
            i += 1
            l += 1