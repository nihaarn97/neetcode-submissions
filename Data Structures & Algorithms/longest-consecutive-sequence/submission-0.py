class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for val in nums:
            if val not in hashmap:
                hashmap[val] = 1

        maxlen = 0
        for key, val in hashmap.items():
            if key-1 in hashmap:
                continue
            else:
                currkey = key
                currlen = 1
                while currkey+1 in hashmap:
                    currlen += 1
                    currkey += 1
                maxlen = max(maxlen, currlen)

        return maxlen
        