class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        maxlen = 0
        l, r = 0, 0
        while r<len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = r
                maxlen = max(maxlen, r-l+1)
                r = r+1
            else:
                end = hashmap[s[r]]
                while l<=end:
                    del hashmap[s[l]]
                    l = l+1
                hashmap[s[r]] = r
                r = r+1

        return maxlen