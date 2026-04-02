class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for val in nums:
            nums[abs(val)-1] = -1*abs(nums[abs(val)-1])

        res = []
        for idx, val in enumerate(nums):
            if val>0:
                res.append(idx+1)

        return res
        