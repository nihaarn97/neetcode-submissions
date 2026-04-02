class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rev = ""
        for val in num:
            if val in set(['2','3','4','5','7']):
                return False
            elif val == "6":
                rev = rev + "9"
            elif val == "9":
                rev = rev + "6"
            else:
                rev = rev + val
                
        return rev[::-1] == num
        