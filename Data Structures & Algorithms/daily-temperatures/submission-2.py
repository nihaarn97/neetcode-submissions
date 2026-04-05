class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx,val in enumerate(temperatures):
            if not stack:
                stack.append((val, idx))
            else:
                while stack and stack[-1][0] < val:
                    temp, pos = stack.pop()
                    res[pos] = idx-pos
                stack.append((val, idx))

        return res