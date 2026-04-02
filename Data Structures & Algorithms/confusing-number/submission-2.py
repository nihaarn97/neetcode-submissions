class Solution:
    def confusingNumber(self, n: int) -> bool:
        new_num = ""
        for val in str(n):
            if val in ('2','3','4','5','7'):
                return False
            elif val == '6':
                new_num +='9'
            elif val == '9':
                new_num += '6'
            else:
                new_num += val

        if int(new_num[::-1]) == n:
            return False
        return True
    