class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cmap = Counter(arr)
        res = -1
        for k,v in cmap.items():
            if k==v:
                res = max(res, k)

        return res
        