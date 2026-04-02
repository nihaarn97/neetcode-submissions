class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hmap = {}
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k] == 0 and ((nums[i], nums[j], nums[k])) not in hmap:
                    hmap[(nums[i], nums[j], nums[k])] = 1
                    j += 1
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j = j+1
                else:
                    k = k- 1

        return [list(x) for x in hmap.keys()]
        