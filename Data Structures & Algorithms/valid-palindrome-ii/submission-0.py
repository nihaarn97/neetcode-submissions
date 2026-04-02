class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                skippedLeft = s[left+1:right+1]
                skippedRight = s[left:right]

                if skippedLeft == skippedLeft[::-1] or skippedRight == skippedRight[::-1]:
                    return True
                else:
                    return False

            left = left + 1
            right = right - 1

        return True