class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hmap = OrderedDict()
        for val in arr:
            hmap[val] = 1 + hmap.get(val, 0)

        print(hmap)
        tgt = k
        for key,val in hmap.items():
            if val == 1 and tgt == 1:
                return key
            elif val == 1:
                tgt = tgt-1
            
        return ""
        