class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        target = len(nums)//2 + 1
        for idx, val in enumerate(nums):
            c = hashmap.get(val, 0)
            if c+1 == target:
                return val
            hashmap[val] = c+1