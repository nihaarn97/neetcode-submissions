class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMatrix = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for i in range(1, len(self.sumMatrix)):
            for j in range(1, len(self.sumMatrix[0])):
                self.sumMatrix[i][j] = self.sumMatrix[i][j-1] + self.sumMatrix[i-1][j] + matrix[i-1][j-1] - self.sumMatrix[i-1][j-1]
        print(self.sumMatrix)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMatrix[row2+1][col2+1] - self.sumMatrix[row1][col2+1] - self.sumMatrix[row2+1][col1] + self.sumMatrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)