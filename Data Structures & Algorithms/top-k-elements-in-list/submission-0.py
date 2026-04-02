from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1 = Counter(nums)
        return [x[0] for x in c1.most_common(k)]