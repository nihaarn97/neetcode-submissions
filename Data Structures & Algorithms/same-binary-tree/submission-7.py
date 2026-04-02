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

        def inorder1(root):
            if root:
                inorder1(root.left)
                inorder1(root.right)
                res1.append(root.val)
                
            else:
                res1.append(None)
                
        def inorder2(root):
            if root:
                inorder2(root.left)
                inorder2(root.right)
                res2.append(root.val)
                
            else:
                res2.append(None)

        inorder1(p)
        inorder2(q)

        print(res1)
        print(res2)

        return res1 == res2
        