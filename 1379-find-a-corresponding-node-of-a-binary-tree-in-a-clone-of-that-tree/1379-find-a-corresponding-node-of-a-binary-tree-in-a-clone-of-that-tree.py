# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(root2):
            if root2==None:
                return root2
            if root2.val == target.val:
                return root2
            return helper(root2.left) or helper(root2.right)
        return helper(cloned)
        