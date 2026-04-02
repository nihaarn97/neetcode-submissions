class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_i, low_j = 0,0
        high_i, high_j = len(matrix)-1, len(matrix[0])-1

        while low_i!=high_i:
            mid_i, mid_j = (low_i+high_i)//2, (low_j+high_j)//2
            if matrix[mid_i][mid_j] == target:
                return True
            elif matrix[mid_i][-1] >= target:
                high_i = mid_i
            else:
                low_i = mid_i+1
        print(low_i, high_i)
        l = 0
        r = len(matrix[low_i])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[low_i][mid] == target:
                return True
            elif matrix[low_i][mid] > target:
                r = mid-1
            else:
                l = mid+1

        return False