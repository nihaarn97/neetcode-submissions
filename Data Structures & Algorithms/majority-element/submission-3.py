class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        maj = len(nums)
        for val in nums:
            hmap[val] = 1 + hmap.get(val, 0)
            if hmap[val] > maj//2:
                return val
        