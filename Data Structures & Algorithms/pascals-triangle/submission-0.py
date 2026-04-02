class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fact(num):
            if num == 0 or num == 1:
                return 1
            else:
                return num * fact(num-1)
        
        res = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(fact(i)//(fact(j)*fact(i-j)))

            res.append(temp)

        return res
        