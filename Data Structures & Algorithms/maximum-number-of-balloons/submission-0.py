class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = set(['b','a','l','o','n'])
        bmap = {'b':1, 'a':1 , 'l':2, 'o':2, 'n':1}
        hmap = {}
        for val in text:
            if val in chars:
                hmap[val] = 1 + hmap.get(val, 0)

        count = 5000000
        for b_key, b_val in bmap.items():
            h_val = hmap.get(b_key, 0)
            contri = h_val//b_val
            count = min(count, contri)

        return 0 if count == 5000000 else count