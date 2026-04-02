class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, val in enumerate(nums):
            idx_diff = hashmap.get(target - val, -1)
            if idx_diff != -1:
                return [idx_diff, idx]
            hashmap[val] = idx
        