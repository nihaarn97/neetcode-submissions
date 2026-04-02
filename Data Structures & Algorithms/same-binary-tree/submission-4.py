# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qbfs = deque([q])
        pbfs = deque([p])

        while qbfs and pbfs:
            curr_p = pbfs.popleft()
            curr_q = qbfs.popleft()

            if curr_p is None and curr_q is None:
                continue

            elif curr_p is None or curr_q is None or curr_p.val != curr_q.val:
                return False

            pbfs.append(curr_p.left)
            pbfs.append(curr_p.right)
            qbfs.append(curr_q.left)
            qbfs.append(curr_q.right)

        return True
            
        