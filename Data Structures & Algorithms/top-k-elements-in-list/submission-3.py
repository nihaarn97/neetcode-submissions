class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        for val in nums:
            countmap[val] = 1 + countmap.get(val, 0)

        buckets = [[] for i in range(max(countmap.values()))]

        for key,val in countmap.items():
            buckets[val-1].append(key)

        i = len(buckets)-1
        res = []
        while len(res)<k:
            res.extend(buckets[i])
            i = i-1

        return res
                