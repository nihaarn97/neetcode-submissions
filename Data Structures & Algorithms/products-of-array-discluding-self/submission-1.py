class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [1] * len(nums)
        rprod = [1] * len(nums)
        res = []
        for i in range(1, len(nums)):
            lprod[i] = nums[i-1] * lprod[i-1]

        for i in range(len(nums)-2, -1, -1):
            rprod[i] = nums[i+1] * rprod[i+1]

        for i in range(len(nums)):
            res.append(rprod[i] * lprod[i])

        return res
        