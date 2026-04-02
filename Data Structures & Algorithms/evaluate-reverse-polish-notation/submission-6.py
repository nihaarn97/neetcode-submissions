class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val in set(['+', '-', '*', '/']):
                op2 = stack.pop()
                op1 = stack.pop()
                if val == "+":
                    stack.append(op1+op2)
                elif val == "-":
                    stack.append(op1-op2)
                elif val == "*":
                    stack.append(op1*op2)
                else:
                    stack.append(int(op1/op2))
            else:
                stack.append(int(val))

        return stack.pop()
        