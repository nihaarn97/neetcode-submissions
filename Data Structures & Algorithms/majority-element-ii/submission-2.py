from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        target = len(nums)//3 + 1
        res = []
        for key, val in c.items():
            if val >= target:
                res.append(key)

        return res