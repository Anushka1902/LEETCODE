# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        t1_val = root1.val if root1 else 0
        t2_val = root2.val if root2 else 0
        next_node = TreeNode(t1_val + t2_val)
        next_node.left = self.mergeTrees(root1.left, root2.left)
        next_node.right = self.mergeTrees(root1.right, root2.right)
        return next_node