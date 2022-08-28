# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node):
            if not node:
                return 0
            
            left = self.getHeight(node.left)
            right = self.getHeight(node.right)
            
            return max(left, right) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        difference = abs(leftHeight - rightHeight) 
        return difference < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        