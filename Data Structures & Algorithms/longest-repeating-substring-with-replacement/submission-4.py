class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        maxf = 0
        countmap = {}
        for r in range(len(s)):
            countmap[s[r]] = 1 + countmap.get(s[r], 0)
            maxf = max(maxf, countmap[s[r]])
            windowlen = r-l+1
            while windowlen - maxf > k:
                countmap[s[l]] = countmap[s[l]] - 1
                l = l+1
                windowlen = windowlen - 1

            res = max(windowlen, res)

        return res