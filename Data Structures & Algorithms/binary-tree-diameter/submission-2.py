# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs_depth(root):
            if not root:
                return 0
            return 1 + max(dfs_depth(root.left), dfs_depth(root.right))

        if not root:
            return 0
        
        diameter = 0
        nodes = deque()
        nodes.append(root)
        while nodes:
            for i in range(len(nodes)):
                curr = nodes.popleft()
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
                diameter = max(diameter, dfs_depth(curr.left) + dfs_depth(curr.right))

        return diameter