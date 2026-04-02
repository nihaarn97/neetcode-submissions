# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def search(root):
            if val <= root.val:
                if root.left:
                    pos = search(root.left)
                else:
                    pos = root
            else:
                if root.right:
                    pos = search(root.right)
                else:
                    pos = root

            return pos

        pos = search(root)
        if val<=pos.val:
            pos.left = TreeNode(val)
        else:
            pos.right = TreeNode(val)

        return root
        