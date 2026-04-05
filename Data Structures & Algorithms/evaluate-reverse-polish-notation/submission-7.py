class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1+op2)
            elif val == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2-op1)
            elif val == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2*op1)
            elif val == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2/op1))
            else:
                stack.append(int(val))
        
        return stack[-1]
        