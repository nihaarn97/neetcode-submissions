class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cursum = 0
        for val in nums:
            cursum += val
            self.prefix.append(cursum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]    
        return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)