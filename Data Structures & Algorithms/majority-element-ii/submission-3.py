class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        target = len(nums)//3
        countmap = {}
        for val in nums:
            if val in res:
                continue
            countmap[val] = 1 + countmap.get(val, 0)
            if countmap[val] > target:
                res.add(val)
        
        return list(res)