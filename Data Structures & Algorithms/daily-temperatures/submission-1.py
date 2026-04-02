class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            if stack:
                while stack:
                    if stack[-1][0] < val:
                        temp = stack.pop()
                        res[temp[1]] = idx - temp[1]
                    else:
                        break
                stack.append((val,idx))
            else:
                stack.append((val,idx))

        return res