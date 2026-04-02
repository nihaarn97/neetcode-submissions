# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        res1 = []
        res2 = []

        def preorder(root, arr):
            if root:
                preorder(root.left, arr)
                preorder(root.right, arr)
                arr.append(root.val)
                
            else:
                arr.append(None)

        preorder(p, res1)
        preorder(q, res2)

        return res1 == res2
        