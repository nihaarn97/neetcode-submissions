class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, low, mid, high):
            res = []
            left = low
            right = mid+1
            while left<=mid and right<=high:
                if arr[left] <= arr[right]:
                    res.append(arr[left])
                    left = left + 1
                else:
                    res.append(arr[right])
                    right = right + 1
            while left<=mid:
                res.append(arr[left])
                left = left+1
            while right<=high:
                res.append(arr[right])
                right = right+1
            
            for i in range(low, high+1):
                arr[i] = res[i-low]

            return arr
        
        def mergesort(arr, low, high):
            mid = (low+high)//2
            if mid<high:
                mergesort(arr, low, mid)
                mergesort(arr, mid+1, high)
                return merge(arr, low, mid, high)
            return arr

        return mergesort(nums, 0, len(nums)-1)
        