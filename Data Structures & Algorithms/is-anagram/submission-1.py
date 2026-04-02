class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charmap = [0] * 26

        for i in range(len(s)):
            charmap[ord(s[i]) - 97] += 1
            charmap[ord(t[i]) - 97] -= 1

        for val in charmap:
            if val != 0:
                return False

        return True


        