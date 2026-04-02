# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return True
        if not root or not subRoot:
            return False

        res2 = []

        def preorder(root, arr):
            if root:
                arr.append(root.val)
                preorder(root.left, arr)
                preorder(root.right, arr)
            else:
                arr.append(None)
        
        preorder(subRoot, res2)
        nodes = deque()
        nodes.append(root)
        while nodes:
            for i in range(len(nodes)):
                curr = nodes.popleft()
                if curr.val == subRoot.val:
                    res1 = []
                    preorder(curr, res1)
                    if res1 == res2:
                        return True
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)

        return False
        