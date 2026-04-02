class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_count = 0
        countmap = {}
        for val in nums:
            countmap[val] = 1 + countmap.get(val, 0)
            max_count = max(max_count, countmap[val])

        bucket = [[] for _ in range(max_count+1)]

        for key, val in countmap.items():
            bucket[val].append(key)
        
        res = []
        k_count = 0
        i = -1
        while k_count < k:
            res.extend(bucket[i])
            k_count += len(bucket[i])
            i = i-1
        
        return res
                