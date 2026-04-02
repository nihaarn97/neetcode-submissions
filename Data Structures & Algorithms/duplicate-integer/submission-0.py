class Solution:
    def hasDuplicate(self, nums) -> bool:
        numset = set(nums)
        return not len(numset)==len(nums)