class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_i, low_j = 0, 0
        high_i, high_j = len(matrix)-1,  len(matrix[0])-1
        while low_i != high_i:
            mid_i, mid_j = (low_i+high_i)//2, (low_j+high_j)//2
            if matrix[mid_i][mid_j] == target:
                return True
            elif target > matrix[mid_i][-1]:
                low_i = low_i + 1
            else:
                high_i = high_i - 1

        low = 0
        high = len(matrix[0])-1
        
        while low<=high:
            mid = (low+high)//2
            if target == matrix[low_i][mid]:
                return True
            elif target<matrix[low_i][mid]:
                high = mid - 1
            else:
                low = mid+1

        return False