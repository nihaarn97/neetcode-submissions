class Solution:
    def check(self, nums: List[int]) -> bool:
        small = min(nums)
        start = nums.index(small)
        pos = start
        next_pos = (pos+1)%len(nums)
        while next_pos!=start:
            if nums[next_pos]>=nums[pos]:
                pos = next_pos
                next_pos = (next_pos+1)%len(nums)
            else:
                return False

        return True

        