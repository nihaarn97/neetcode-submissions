class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            if not stack:
                stack.append((val, idx))
            else:
                while stack:
                    if val > stack[-1][0]:
                        tos = stack.pop()
                        result[tos[1]] = idx - tos[1] 
                    else:
                        break
                stack.append((val, idx))

        return result
            
        