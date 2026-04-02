class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t)<len(s):
            return False
        if len(s)==0:
            return True
        i = 0
        j = 0
        while j<len(t) and i<len(s):
            if s[i] == t[j]:
                i = i+1
            j = j+1
        
        if i == len(s):
            return True
        return False
        