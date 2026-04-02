# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        hmap_inorder = {}
        hmap_preorder = {}

        for idx, val in enumerate(inorder):
            hmap_inorder[val] = idx

        for idx, val in enumerate(preorder):
            hmap_preorder[val] = idx

        def build_tree(children):
            if len(children) == 0:
                return None
            if len(children) == 1:
                return TreeNode(children[0])

            parent_idx = -1
            parent_val = -1001
            for idx, val in enumerate(preorder):
                if val in children:
                    parent_idx = idx
                    parent_val = val
                    break

            hmap_children = {}
            for idx, val in enumerate(children):
                hmap_children[val] = idx
            
            left_children = children[:hmap_children[parent_val]]
            right_children = children[hmap_children[parent_val]+1:]

            print(parent_val)
            print(left_children)
            print(right_children)

            parent = TreeNode(parent_val)
            parent.left = build_tree(left_children)
            parent.right = build_tree(right_children)
            return parent

        root = TreeNode(preorder[0])
        print(inorder[:hmap_inorder[root.val]])
        print(inorder[hmap_inorder[root.val]+1:])
        root.left = build_tree(inorder[:hmap_inorder[root.val]])
        root.right = build_tree(inorder[hmap_inorder[root.val]+1:])

        return root