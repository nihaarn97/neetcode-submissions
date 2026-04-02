class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for val in s.lower():
            if val.isalnum():
                new_str += val

        i = 0
        j = len(new_str)-1
        while(i<j):
            if new_str[i] == new_str[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        