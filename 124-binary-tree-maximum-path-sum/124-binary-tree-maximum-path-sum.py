# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum=float('-inf')
        def height(node):
            if node==None:
                return 0
            leftsum=max(0,height(node.left))
            rightsum=max(0,height(node.right))
            self.maximum=max(self.maximum,leftsum+rightsum+node.val)
            return node.val+max(leftsum,rightsum)
        height(root)
        return self.maximum
        