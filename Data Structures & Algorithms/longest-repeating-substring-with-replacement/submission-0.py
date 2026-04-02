class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        countmap = {}

        for r in range(len(s)):
            countmap[s[r]] = countmap.get(s[r], 0) + 1

            windowLen = r-l+1
            while windowLen - max(countmap.values()) > k:
                countmap[s[l]] -= 1
                l = l + 1
                windowLen -= 1

            res = max(res, windowLen)

        return res