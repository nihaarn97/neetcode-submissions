class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        l = 0
        r = len(nums)-1
        for val in nums:
            if val%2==0:
                res[l]=val
                l = l+1
            else:
                res[r]=val
                r = r-1

        return res

        