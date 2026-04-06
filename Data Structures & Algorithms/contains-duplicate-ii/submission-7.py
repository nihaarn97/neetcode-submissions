class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for idx, val in enumerate(nums):
            if val in hashmap and abs(hashmap[val]-idx)<=k:
                return True
            else:
                hashmap[val] = idx
        return False

        