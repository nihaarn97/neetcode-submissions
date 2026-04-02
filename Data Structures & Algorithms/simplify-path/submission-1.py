import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r'/+', '/', path)
        folders = [p for p in path.split('/') if p]
        res = "/"
        actions = set(['..', '.'])
        stack = []
        for val in folders:
            if val in actions:
                if val == "..":
                    if stack:
                        stack.pop()
                continue
            else:
                stack.append(val)

        if stack:
            for val in stack:
                res+= val + "/"

        return res[:-1] if len(res)>1 else res
        
                
        