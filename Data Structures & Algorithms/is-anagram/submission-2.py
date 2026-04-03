class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = [0]*26
        t_map = [0]*26

        for val in s:
            s_map[ord(val)-ord('a')] += 1
        for val in t:
            t_map[ord(val)-ord('a')] += 1

        return s_map == t_map


        