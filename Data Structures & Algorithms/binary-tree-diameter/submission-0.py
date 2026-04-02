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
        
        def maxDepth(root):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        q = deque()
        q.append(root)
        diameter = 0

        while q:
            current = q.popleft()
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            diameter = max(diameter, maxDepth(current.left) + maxDepth(current.right))

        return diameter
        