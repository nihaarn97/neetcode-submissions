class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = set(["+", "D", "C"])
        for val in operations:
            if val in ops:
                if val == "+":
                    stack.append(stack[-1] + stack[-2])
                
                elif val == "D":
                    stack.append(stack[-1]*2)

                else:
                    stack.pop()
            
            else:
                stack.append(int(val))

        return sum(stack)

        
        