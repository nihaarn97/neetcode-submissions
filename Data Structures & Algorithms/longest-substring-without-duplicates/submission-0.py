class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = 1
        hashmap = set()
        maxLen = 0

        hashmap.add(s[l])

        while r<len(s):
            if s[r] not in hashmap:
                hashmap.add(s[r])
                r = r+1
            else:
                while s[r] in hashmap:
                    hashmap.remove(s[l])
                    l = l+1
                hashmap.add(s[r])
                r = r+1
            maxLen = max(maxLen, len(hashmap))

        return maxLen