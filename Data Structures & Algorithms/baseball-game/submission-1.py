class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if val == "+":
                stack.append(stack[-1] + stack[-2])
            elif val == "C":
                stack.pop()
            elif val == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(val))

        return sum(stack) 
        