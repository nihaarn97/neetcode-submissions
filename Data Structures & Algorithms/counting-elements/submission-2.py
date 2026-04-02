class Solution:
    def countElements(self, arr: List[int]) -> int:
        hmap = {}
        for val in arr:
            hmap[val] = 1 #+ hmap.get(val, 0)

        count = 0
        for val in arr:
            count += hmap.get(val+1, 0)

        return count

        