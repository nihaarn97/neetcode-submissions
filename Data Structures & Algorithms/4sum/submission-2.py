class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        hmap = {}
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l = j+1
                r = len(nums)-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r]==target:
                        hmap[(nums[i],nums[j],nums[l],nums[r])] = 1
                        l = l+1
                        r = r-1
                    elif nums[i]+nums[j]+nums[l]+nums[r]<target:
                        l = l+1
                    else:
                        r = r-1

        return [list(x) for x in hmap.keys()]