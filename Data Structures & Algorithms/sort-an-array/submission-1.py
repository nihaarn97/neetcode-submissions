class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:  
        def merge(arr, low, mid, high):
            result = []
            left = low
            right = mid+1

            while left<=mid and right<=high:
                if arr[left]<arr[right]:
                    result.append(arr[left])
                    left += 1
                else:
                    result.append(arr[right])
                    right += 1
    
            while left<=mid:
                result.append(arr[left])
                left += 1

            while right<=high:
                result.append(arr[right])
                right += 1

            for i in range(low, high+1):
                arr[i] = result[i-low]

            return arr
            

        def mergesort(arr, low, high):
            if low<high:
                mid = (low+high)//2
                mergesort(arr, low, mid)
                mergesort(arr, mid+1, high)
                return merge(arr, low, mid, high)
            return arr

        return mergesort(nums, 0, len(nums)-1)
            
