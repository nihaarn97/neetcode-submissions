class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brac in s:
            if brac in set(['(', '[', '{']):
                stack.append(brac)
            else:
                if not stack:
                    return False
                tos = stack.pop()
                if (brac == ')' and tos != '(') or (brac == ']' and tos != '[') or (brac == '}' and tos != '{'):
                    return False
        if stack:
            return False
        
        return True
        