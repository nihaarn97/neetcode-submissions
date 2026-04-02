class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for val in details:
            if int(val[11:13])>60:
                count = count+1
        return count