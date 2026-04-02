class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # visited = set()
        # for val in nums:
        #     if val in visited:
        #         return val
        #     visited.add(val)

        for val in nums:
            idx = abs(val)-1
            if nums[idx]<0:
                return abs(val)

            nums[idx] *= -1

        return -1