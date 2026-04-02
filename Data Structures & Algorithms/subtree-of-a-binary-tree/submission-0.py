# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        mainq = deque([root])
        def isSameTree(p, q) -> bool:
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

        while mainq:
            curr = mainq.popleft()
            if not curr:
                continue
            if curr.val == subRoot.val:
                if isSameTree(curr, subRoot):
                    return True
            if curr.left:
                mainq.append(curr.left)
            if curr.right:
                mainq.append(curr.right)
        
        return False

        