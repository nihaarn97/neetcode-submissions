class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valmap = {}
        for i in range(len(nums)):
            if target - nums[i] in valmap:
                return [valmap[target - nums[i]], i]
            valmap[nums[i]] = i

        