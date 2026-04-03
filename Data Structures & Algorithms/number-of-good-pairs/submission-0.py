class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap = {}
        for val in nums:
            hmap[val] = 1 + hmap.get(val, 0)
        
        pairs = 0
        for val in hmap.values():
            pairs += (val*(val-1))//2
        
        return pairs