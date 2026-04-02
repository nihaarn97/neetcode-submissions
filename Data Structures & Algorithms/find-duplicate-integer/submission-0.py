class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for val in nums:
            if val in visited:
                return val
            visited.add(val)
        