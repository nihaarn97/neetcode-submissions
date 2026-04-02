class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {}
        lcs = 0
        for num in nums:
            if num not in hmap:
                hmap[num] = ''

        for key in hmap.keys():
            if key-1 not in hmap:
                i = key
                maxlen = 0
                while i in hmap:
                    maxlen += 1
                    i = i+1
                lcs = max(lcs, maxlen)

        return lcs
        