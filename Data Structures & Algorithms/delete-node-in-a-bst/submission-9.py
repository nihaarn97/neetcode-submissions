# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val==key and not root.right and not root.left:
            return None

        parent = None
        
        def search(curr):
            nonlocal parent
            if not curr:
                return None
            elif curr.val == key:
                return curr
            parent = curr
            if curr.val>key:
                pos = search(curr.left)
            else:
                pos = search(curr.right)
            
            return pos

        pos = search(root)
        if not pos:
            return root

        #When it is a leaf
        if not pos.left and not pos.right:
            if parent.left == pos:
                parent.left = None
            else:
                parent.right = None
        elif pos.left and not pos.right:
            if parent:
                if parent.left == pos:
                    parent.left = pos.left
                else:
                    parent.right = pos.left
            else:
                return pos.left
            pos.left = None
        elif pos.right and not pos.left:
            if parent:
                if parent.left == pos:
                    parent.left = pos.right
                else:
                    parent.right = pos.right
            else:
                return pos.right
            pos.right = None
        else:
            curr = pos.right
            par = None
            while True:
                if not curr.left:
                    break
                par = curr
                curr = curr.left
            if not par:
                if parent and parent.left == pos:
                    parent.left = curr
                    curr.left = pos.left
                    pos.left, pos.right = None, None
                elif parent and parent.right == pos:
                    parent.right = curr
                    curr.left = pos.left
                    pos.left, pos.right = None, None
                else:
                    curr.left = pos.left
                    root.left, root.right = None, None
                    return curr
            else:
                pos.val = curr.val
                par.left = curr.right
                curr.right = None
        
        return root