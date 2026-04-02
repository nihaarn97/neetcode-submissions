class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hmap = {}
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l<r:
                if nums[i]+nums[l]+nums[r] == 0:
                    hmap[(nums[i],nums[l],nums[r])] = 1
                    l = l+1
                    r = r-1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r = r-1
                else:
                    l = l+1

        return [list(x) for x in hmap.keys()]
        