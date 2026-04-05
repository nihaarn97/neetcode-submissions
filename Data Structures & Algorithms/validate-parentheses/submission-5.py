class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val in ['[', '(', '{']:
                stack.append(val)
            else:
                if not stack:
                    return False
                elif (val == '}' and stack[-1]!='{') or (val == ')' and stack[-1]!='(') or (val == ']' and stack[-1]!='['):
                    return False
                else:
                    stack.pop()

        return not stack
