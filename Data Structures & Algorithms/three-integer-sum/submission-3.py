class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hmap = set()

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            target = 0 - nums[i]
            while j<k:
                if nums[j] + nums[k] == target:
                    hmap.add((nums[i], nums[j], nums[k]))
                    j = j+1
                    k = k-1
                elif nums[j] + nums[k]>target:
                    k = k-1
                else:
                    j = j+1

        return [list(x) for x in hmap]


        