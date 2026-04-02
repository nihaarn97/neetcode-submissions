class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = set(['(', '{', '[']) #Constant time lookup
        for val in s:
            if val in open_brackets:
                stack.append(val)
            else:
                if not stack:
                    return False
                tos = stack.pop()
                if (val == ')' and tos != '(') or (val == '}' and tos != '{') or (val == ']' and tos != '['):
                    return False
                
        return len(stack) == 0
        