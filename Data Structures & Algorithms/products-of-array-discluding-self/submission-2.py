class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [1] * len(nums)
        rprod = [1] * len(nums)

        for i in range(1, len(lprod)):
            lprod[i] = lprod[i-1]*nums[i-1]

        for i in range(len(rprod)-2, -1, -1):
            rprod[i] = rprod[i+1]*nums[i+1]

        return [x*y for x,y in zip(lprod,rprod)]