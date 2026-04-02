class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > greatest:
                temp = arr[i]
                arr[i] = greatest
                greatest = temp
            else:
                arr[i] = greatest
        arr[-1] = -1
        return arr

        