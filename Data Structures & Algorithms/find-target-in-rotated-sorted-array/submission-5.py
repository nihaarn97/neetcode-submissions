class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid

        if nums[l]<=target and target<=nums[-1]:
            low = l
            high = len(nums)-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
        else:
            low = 0
            high = l-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1

        return -1