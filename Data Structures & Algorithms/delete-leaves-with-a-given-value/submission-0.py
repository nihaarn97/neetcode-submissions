# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #postorder traversal
        def postorder(root):
            if not root:
                return 0
            else:
                left_check = postorder(root.left)
                right_check = postorder(root.right)
                if left_check == 1 and root.left.left == None and root.left.right == None:
                    root.left = None
                if right_check == 1 and root.right.left == None and root.right.right == None:
                    root.right = None
                if root.val == target:
                    return 1
                return 0

        root_check = postorder(root)
        if root_check == 1:
            return None
        return root
        