class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for val in s:
            if val.isnumeric():
                if stack and str(stack[-1]).isnumeric():
                    stack.append(stack.pop()*10+int(val))
                else:
                    stack.append(int(val))
            elif val.isalpha() or val == '[':
                stack.append(val)
            else:
                charstr = ""
                while stack:
                    tos = stack.pop()
                    if tos == '[':
                        break
                    else:
                        charstr = tos + charstr
                
                stack.append(charstr*stack.pop())


        return "".join(stack)

            

        