# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return root
        res = []
        
        def dfs(rt, p, r):
            if not rt:
                return
            if rt and not rt.left and not rt.right:
                p+=[rt.val]
                r+=["->".join(str(x) for x in p)]
                return
            dfs(rt.left, p+[rt.val], r)
            dfs(rt.right, p+[rt.val], r)
        
        dfs(root, [], res)
        return res