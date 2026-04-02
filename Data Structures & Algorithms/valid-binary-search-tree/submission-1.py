# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.inorder.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(len(self.inorder)-1):
            if self.inorder[i] >= self.inorder[i+1]:
                return False

        return True
        