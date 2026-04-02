class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # expect = sorted(heights)
        # count = 0
        # for a,b in zip(expect, heights):
        #     if a!=b:
        #         count = count+1
        # return count


        count_arr = [0]*101
        for val in heights:
            count_arr[val] += 1
        res = []
        for idx, val in enumerate(count_arr):
            if val!=0:
                for i in range(val):
                    res.append(idx)
        count = 0
        for a,b in zip(res, heights):
            if a!=b:
                count = count+1
        return count