class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if r==0:
            return nums[0]
        while l<=r:
            mid = (l+r)//2
            if mid == 0:
                if nums[mid+1] != nums[mid]:
                    return nums[mid]
                else:
                    l = mid+1
            elif mid == len(nums)-1:
                if nums[mid-1] != nums[mid]:
                    return nums[mid]
                else:
                    r = mid-1
            elif nums[mid] != nums[mid-1] and nums[mid]!=nums[mid+1]:
                print(mid)
                return nums[mid]
            elif nums[mid-1] == nums[mid]:
                if (mid+1)%2 == 1:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if (len(nums)-mid)%2 == 1:
                    l = mid+1
                else:
                    r = mid-1