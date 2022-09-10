# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Brute Force : Time -> O(n) , Space O(n) due to recursiom could be O(h) where h = height of the tree.
        self.minn = float(inf)
        self.prev = None
        self.inorder(root)
        return self.minn
    
    def inorder(self,node):
        
        if node.left:
            self.inorder(node.left)
        if self.prev:
            if (node.val - self.prev.val) < self.minn:
                self.minn = node.val - self.prev.val
        self.prev = node
        
        if node.right:
            self.inorder(node.right)