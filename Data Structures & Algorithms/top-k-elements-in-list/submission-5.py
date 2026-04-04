class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cmap = {}
        for val in nums:
            cmap[val] = 1 + cmap.get(val, 0)

        buckets = [[] for i in range(max(cmap.values())+1)]

        for key,v in cmap.items():
            buckets[v].append(key)

        i = len(buckets)-1
        res = []
        while len(res)<k:
            res.extend(buckets[i])
            i = i-1
            
        return res