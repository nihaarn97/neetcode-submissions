class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.preCompute = [[0] * (COLS+1) for i in range(ROWS+1)]
        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                self.preCompute[i][j] = self.preCompute[i-1][j] + self.preCompute[i][j-1] + matrix[i-1][j-1] - self.preCompute[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preCompute[row2+1][col2+1] - self.preCompute[row2+1][col1-1+1] - self.preCompute[row1-1+1][col2+1] + self.preCompute[row1-1+1][col1-1+1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)