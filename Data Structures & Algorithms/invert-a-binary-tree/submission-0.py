# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertLeftRight(self, node: Optionl[TreeNode]) -> Optional[TreeNode]:
        node.left, node.right = node.right, node.left
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        else:
            if root.left != None:
                self.invertTree(root.left)
            if root.right != None:
                self.invertTree(root.right)
            self.invertLeftRight(root)
        return root
