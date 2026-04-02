from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0
        
        def maxDepth(root):
            if not root:
                return 0

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)

            self.diameter = max(self.diameter, leftDepth + rightDepth) 

            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        maxDepth(root)

        return self.diameter
        