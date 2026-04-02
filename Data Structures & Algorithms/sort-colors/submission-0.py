class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0, 0, 0]
        for val in nums:
            res[val] += 1

        j = 0
        for idx, val in enumerate(res):
            while val>0:
                nums[j] = idx
                j = j+1
                val = val-1