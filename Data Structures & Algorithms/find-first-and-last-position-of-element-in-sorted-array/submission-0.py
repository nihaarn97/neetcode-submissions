class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        if r==0 and nums[0]!=target:
            return [-1,-1]

        low_pt = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                low_pt = mid
                r = mid-1
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1

        l = low_pt+1
        r = len(nums)-1
        high_pt = low_pt
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                high_pt = mid
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1

        return[low_pt, high_pt]
        