# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def treeTraversal(root):
            answer=0
            if root:
                if root.val>=low and root.val<=high:
                    answer+=root.val
                answer+=treeTraversal(root.left)+treeTraversal(root.right)               
            return answer
        return treeTraversal(root)