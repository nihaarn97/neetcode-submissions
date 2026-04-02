class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        res = 0
        countmap = {}
        for r in range(len(s)):
            countmap[s[r]] = 1 + countmap.get(s[r], 0)
            windowlen = r-l+1
            while windowlen-max(countmap.values())>k:
                countmap[s[l]] -= 1
                l = l+1
                windowlen -= 1

            res = max(windowlen, res)

        return res