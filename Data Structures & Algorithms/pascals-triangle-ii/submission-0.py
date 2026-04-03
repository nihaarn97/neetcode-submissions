class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(num):
            if num == 1 or num == 0:
                return 1
            return num*fact(num-1)

        res = []
        for i in range(rowIndex+1):
            res.append(fact(rowIndex)//(fact(i)*fact(rowIndex-i)))

        return res

        
        