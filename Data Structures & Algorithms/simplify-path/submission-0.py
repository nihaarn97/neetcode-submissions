import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r'/+', '/', path)
        folders = [p for p in path.split('/') if p]
        
        stack1 = []
        stack2 = []
        res = "/"
        actions = set(['.', '..'])
        for val in folders:
            if val in actions:
                if val == ".":
                    continue
                if stack1:
                    stack1.pop()
            else:
                stack1.append(val)

        if stack1:
            while stack1:
                stack2.append(stack1.pop())
            while stack2:
                res += stack2.pop() + "/"

        return res[0:-1] if len(res)>1 else res

        