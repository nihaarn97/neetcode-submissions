class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        difference = (arr[-1]-arr[0])//n

        expected = arr[0]
        for val in arr:
            if val!=expected:
                return expected
            
            expected = expected + difference

        return expected
        