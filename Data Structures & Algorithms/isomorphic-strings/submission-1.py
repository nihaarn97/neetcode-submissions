class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = {}
        visited = set()
        for v1, v2 in zip(s, t):
            if v1 in hmap:
                if hmap[v1]!=v2:
                    return False
            else:
                if v2 not in visited:
                    hmap[v1] = v2
                    visited.add(v2)
                else:
                    return False

        return True
        