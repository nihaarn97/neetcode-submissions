# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = 0
        def dfs(root):
            nonlocal flag
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right)>1:
                flag = 1

            return 1 + max(left, right)

        dfs(root)

        if flag == 0:
            return True
        return False
        