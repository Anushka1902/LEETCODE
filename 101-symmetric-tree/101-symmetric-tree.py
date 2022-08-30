# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val==q.val and check(p.right,q.left) and check(p.left,q.right)
        if root==None:
            return True
        return check(root.left,root.right)
        