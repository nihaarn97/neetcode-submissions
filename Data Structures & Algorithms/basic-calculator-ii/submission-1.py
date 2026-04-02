import re

class Solution:
    def calculate(self, s: str) -> int:
        s = re.sub(r'\s+', '', s)
        stack = []
        num = 0
        op = '+'
        for idx, val in enumerate(s):
            if val.isdigit():
                num = num*10 + int(val)
            if (not val.isdigit()) or idx == len(s)-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == "*":
                    operand = stack.pop()
                    stack.append(num*operand)
                else:
                    operand = stack.pop()
                    stack.append(int(operand/num))

                op = val
                num = 0

        return sum(stack) 