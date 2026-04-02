class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mindiff = nums[k-1]-nums[0]
        l = 0
        r = k-1
        while r<len(nums):
            mindiff = min(mindiff, nums[r]-nums[l])
            r = r+1
            l = l+1

        return mindiff
        