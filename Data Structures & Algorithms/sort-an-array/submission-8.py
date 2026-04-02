class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, low, mid, high):
            temp = []
            i = low
            j = mid+1
            while i<=mid and j<=high:
                if arr[i]<=arr[j]:
                    temp.append(arr[i])
                    i = i+1
                else:
                    temp.append(arr[j])
                    j = j+1
            
            while i<=mid:
                temp.append(arr[i])
                i = i+1
            while j<=high:
                temp.append(arr[j])
                j = j+1

            for i in range(len(temp)):
                arr[low+i] = temp[i]

            return arr
        
        def mergesort(low, high, nums):
            if low>=high:
                return nums
            mid = (low+high)//2
            mergesort(low, mid, nums)
            mergesort(mid+1, high, nums)
            return merge(nums, low, mid, high)

        return mergesort(0, len(nums)-1, nums)
        