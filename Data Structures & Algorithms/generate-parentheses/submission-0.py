class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_bracks, closed_bracks):
            if open_bracks == closed_bracks == n:
                result.append("".join(stack))
                return
            if open_bracks<n:
                stack.append("(")
                backtrack(open_bracks+1, closed_bracks)
                stack.pop()
            if closed_bracks<open_bracks:
                stack.append(")")
                backtrack(open_bracks, closed_bracks+1)
                stack.pop()

        backtrack(0,0)
        return result
        