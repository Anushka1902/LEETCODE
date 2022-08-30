# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 and t2 or not t2 and t1 or t1.val != t2.val: 
                return False
            return check(t1.left,t2.left) and check(t1.right,t2.right)
        if subRoot==None:
            return True
        if root==None:
            return False
        return check(root,subRoot) or self.isSubtree(root.left,subRoot)or self.isSubtree(root.right,subRoot)
        