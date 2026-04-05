class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = set()
        lcs = 0
        for val in nums:
            hmap.add(val)

        for val in nums:
            if val-1 not in hmap:
                num = val
                count = 0
                while num in hmap:
                    count = count+1
                    num = num+1
                lcs = max(lcs, count)
        
        return lcs