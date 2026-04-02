# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = deque()
        res = []
        nodes.append(root)
        while nodes:
            temp = []
            for i in range(len(nodes)):
                curr = nodes.popleft()
                temp.append(curr.val)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
            res.append(temp)

        return res
        