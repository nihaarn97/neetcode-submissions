class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        low = 0
        high = len(nums) - 1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<nums[mid-1]:
                start = mid
                break
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        
        if target >= nums[start] and target <= nums[-1]:
            low = start
            high = len(nums) - 1
        else:
            low = 0
            high = start - 1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1     