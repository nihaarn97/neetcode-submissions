# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # if i had robbed
        # if i had not robbed
        # return max of both scenarios
        def postorder(root):
            if not root:
                return [0,0]
            
            left = postorder(root.left)
            right = postorder(root.right)
            
            root_picked = root.val + left[1] + right[1]
            root_not_picked = max(left) + max(right)
            
            return [root_picked, root_not_picked]

        return max(postorder(root))

        