class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1_map = [0]*26
        s2_map = [0]*26

        for val in s1:
            s1_map[ord(val)-ord('a')] += 1

        for i in range(0, len(s1)):
            s2_map[ord(s2[i])-ord('a')] += 1

        l = 0
        r = len(s1)

        while r<len(s2):
            if tuple(s1_map) == tuple(s2_map):
                return True
            s2_map[ord(s2[r])-ord('a')] += 1
            s2_map[ord(s2[l])-ord('a')] -= 1
            r = r+1
            l = l+1

        if tuple(s1_map) == tuple(s2_map):
            return True
        return False

        


