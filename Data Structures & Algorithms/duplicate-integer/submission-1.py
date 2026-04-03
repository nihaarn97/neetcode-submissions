class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for val in nums:
            if val in visited:
                return True
            visited.add(val)

        return False
        