class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hmap = {}
        for val in nums:
            hmap[val] = 1 + hmap.get(val, 0)

        res = -1
        for key, val in hmap.items():
            if val == 1:
                res = max(res, key)

        return res
        