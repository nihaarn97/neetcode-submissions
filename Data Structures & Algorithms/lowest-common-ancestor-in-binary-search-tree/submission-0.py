# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        curr = root
        lca = None
        
        while True:
            if not curr:
                return lca
            lca = curr
            if min_val < curr.val and max_val > curr.val: 
                return lca
            elif min_val > curr.val:
                curr = curr.right
            elif max_val < curr.val:
                curr = curr.left
            elif min_val == curr.val or max_val == curr.val:
                return lca
        
        