# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left,right):
            if left ==None and right==None:
                return True
            if left==None or right==None:
                return False
            return left.val==right.val and check(left.left,right.right) and check(left.right,right.left)
        if root is None:
            return True
        return check(root.left,root.right)
        '''
        def check(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val==q.val and check(p.right,q.left) and check(p.left,q.right)
        if root==None:
            return True
        return check(root.left,root.right)
        '''