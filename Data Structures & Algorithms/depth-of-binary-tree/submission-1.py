# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodes = deque()
        nodes.append(root)
        depth = 0
        while nodes:
            depth = depth + 1
            for i in range(len(nodes)):
                curr = nodes.popleft()
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)

        return depth


        