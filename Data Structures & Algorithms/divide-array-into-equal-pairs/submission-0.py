class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hmap = {}
        for val in nums:
            hmap[val] = 1 + hmap.get(val, 0)

        pairs = 0
        for val in hmap.values():
            pairs += val//2

        if pairs == len(nums)/2:
            return True
        return False
        