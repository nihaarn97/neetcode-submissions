from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for val in nums:
            freqmap[val] = freqmap.get(val, 0) + 1

        freq_buckets = [[] for i in range(len(nums)+1)]

        for key, val in freqmap.items():
            freq_buckets[val].append(key)

        result = []

        for i in range(len(freq_buckets)-1, -1, -1):
            if freq_buckets[i]:
                result.extend(freq_buckets[i])
                if len(result) >= k:
                    return result