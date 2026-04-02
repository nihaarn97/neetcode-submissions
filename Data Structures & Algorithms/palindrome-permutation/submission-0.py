class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hmap = {}
        for val in s:
            hmap[val] = 1 + hmap.get(val, 0)

        flag = 0
        for key, val in hmap.items():
            if val%2 == 1 and flag == 1:
                return False
            elif val%2 == 1 and flag == 0:
                flag = 1
            
        return True
        