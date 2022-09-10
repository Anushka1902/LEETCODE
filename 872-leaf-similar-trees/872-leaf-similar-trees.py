# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        q =[root1]
        
        
        while q:
            poped = q.pop()
            if not poped.left and not poped.right:
                l1.append(poped.val)
            if poped.left:
                q.append(poped.left)
            if poped.right:
                q.append(poped.right)
        q = [root2]
        while q:
            poped = q.pop()
            if not poped.left and not poped.right:
                l2.append(poped.val)
            if poped.left:
                q.append(poped.left)
            if poped.right:
                q.append(poped.right)
                
        return l1==l2