class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if r == 0:
            return 0
        while l<=r:
            mid = (l+r)//2
            if mid == 0 and nums[mid]>nums[mid+1]:
                return mid
            elif mid == len(nums)-1 and nums[mid]>nums[mid]-1:
                return mid
            elif nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                l = mid+1
            else:
                r = mid-1
        