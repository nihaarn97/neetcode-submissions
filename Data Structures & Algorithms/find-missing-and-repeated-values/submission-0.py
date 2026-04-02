class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hmap = {}
        res = deque()
        for i in range(len(grid)):
            for j in range(len(grid)):
                hmap[grid[i][j]] = 1 + hmap.get(grid[i][j], 0)

        for i in range(1, len(grid)*len(grid)+1):
            if i not in hmap:
                res.append(i)
            else:
                if hmap[i] == 2:
                    res.appendleft(i)

        return list(res)