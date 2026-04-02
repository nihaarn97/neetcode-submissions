class Solution:
    def parseTernary(self, expression: str) -> str:
        exp = expression[::-1]
        stack = []
        for val in exp:
            if not stack:
                stack.append(val)
                continue
            if val.isdigit() or val == "?":
                stack.append(val)
            elif val == "T":
                if stack[-1]=="?":
                    stack.pop()
                    true_res = stack.pop()
                    stack.pop()
                    stack.append(true_res)
                else:
                    stack.append(val)
            elif val == "F":
                if stack[-1]=="?":
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(val)
        
        return stack[-1]