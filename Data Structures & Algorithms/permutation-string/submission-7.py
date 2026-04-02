class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        map_s1 = [0]*26
        map_s2 = [0]*26

        for val in s1:
            map_s1[ord(val)-ord('a')] += 1

        for i in range(len(s1)):
            map_s2[ord(s2[i])-ord('a')] += 1

        l = 0
        r = len(s1)
        while r<len(s2):
            if tuple(map_s1) == tuple(map_s2):
                return True
            map_s2[ord(s2[l])-ord('a')] -= 1
            map_s2[ord(s2[r])-ord('a')] += 1
            l = l+1
            r = r+1

        if tuple(map_s1) == tuple(map_s2):
            return True
        return False



