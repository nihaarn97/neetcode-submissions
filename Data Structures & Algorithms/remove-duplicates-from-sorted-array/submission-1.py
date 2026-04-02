from collections import OrderedDict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # counts = OrderedDict()
        # for val in nums:
        #     counts[val] = 1 + counts.get(val, 0)

        # for idx, val in enumerate(counts.keys()):
        #     nums[idx] = val

        # return len(counts)

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l = l+1

        return l