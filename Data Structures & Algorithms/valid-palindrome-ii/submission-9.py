class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                if s[l+1] == s[r] or s[r-1] == s[l]:
                    l1 = l+1
                    r1 = r
                    flag = 0
                    while l1<r1:
                        if s[l1]!=s[r1]:
                            flag = 1
                            break
                        l1 = l1+1
                        r1 = r1-1

                    if flag==0:
                        return True
                        
                    l1 = l
                    r1 = r-1
                    while l1<r1:
                        if s[l1]!=s[r1]:
                            return False
                        l1 = l1+1
                        r1 = r1-1
                    return True
                else:
                    return False
            else:
                l += 1
                r -= 1

        return True
        