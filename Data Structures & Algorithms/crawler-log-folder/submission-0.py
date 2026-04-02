class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for val in logs:
            if val == "../":
                if stack:
                    stack.pop()
                continue
            elif val =="./":
                continue
            else:
                stack.append(val)

        return len(stack)
        