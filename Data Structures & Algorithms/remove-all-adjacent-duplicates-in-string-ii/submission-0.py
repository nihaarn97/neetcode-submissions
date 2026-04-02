class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for val in s:
            if not stack:
                stack.append((val,1))
            elif val == stack[-1][0]:
                if stack[-1][1]+1==k:
                    stack.pop()
                else:
                    tos = stack.pop()
                    stack.append((val, tos[1]+1))
            else:
                stack.append((val, 1))

        res = ""
        for item in stack:
            res += item[0]*item[1]

        return res
        