# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        nodes = deque()
        nodes.append(root)
        res = []
        while nodes:
            res.append(nodes[-1].val)
            for i in range(len(nodes)):
                curr = nodes.popleft()
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)

        return res
                
        