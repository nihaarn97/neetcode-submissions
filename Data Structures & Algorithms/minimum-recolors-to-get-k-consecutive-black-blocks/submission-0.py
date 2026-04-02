class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countmap = {}
        for i in range(k):
            countmap[blocks[i]] = 1 + countmap.get(blocks[i], 0)

        mincount = countmap.get('W', 0)
        l = 0
        r = k
        while r<len(blocks):
            countmap[blocks[r]] = 1 + countmap.get(blocks[r], 0)
            countmap[blocks[l]] = countmap.get(blocks[l]) - 1
            mincount = min(mincount, countmap.get('W', 0))
            r = r+1
            l = l+1

        return mincount