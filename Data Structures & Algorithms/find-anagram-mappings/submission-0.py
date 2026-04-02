class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        for idx, val in enumerate(nums2):
            hmap[val] = idx

        res = []

        for val in nums1:
            res.append(hmap[val])

        return res
        