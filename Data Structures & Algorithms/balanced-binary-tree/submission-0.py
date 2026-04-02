# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def depth(root):
            if not root:
                return 0
            
            leftDepth = depth(root.left)
            rightDepth = depth(root.right)

            return 1 + max(leftDepth, rightDepth)

        q = deque()
        q.append(root)
        
        while q:
            current = q.popleft()
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

            if abs(depth(current.left) - depth(current.right)) > 1:
                return False

        return True
