class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mindiff = nums[k-1] - nums[0]
        l = 1
        r = k
        while r<len(nums): 
            mindiff = min(mindiff, nums[r]-nums[l])
            l = l+1
            r = r+1

        return mindiff
        