# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def traverse(root, _set):
            if root:
                # key step - check if the difference is in set
                if k - root.val in _set:
                    return True
                _set.add(root.val)
                return traverse(root.left, _set) or traverse(root.right, _set)
            return False
        return traverse(root, set())