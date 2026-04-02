class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([val for val in s if val.isalnum()]).lower()
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l +=1
            r -= 1
        return True