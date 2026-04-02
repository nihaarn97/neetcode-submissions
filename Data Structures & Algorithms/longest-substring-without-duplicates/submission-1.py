class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        maxLen = 0
        i, j = 0, 0
        while j<len(s):
            if s[j] not in hashmap:
                hashmap[s[j]] = j
                maxLen = max(len(hashmap), maxLen)
                j = j+1
            else:
                end = hashmap[s[j]]
                while i<=end:
                    del hashmap[s[i]]
                    i = i+1
                hashmap[s[j]] = j
                j = j+1

        return maxLen
        