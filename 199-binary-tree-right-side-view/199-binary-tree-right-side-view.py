# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,level,res):
            if root==None:
                return
            if level==len(res):
                res.append(root.val)
            dfs(root.right,level+1,res)
            dfs(root.left,level+1,res)
        res=[]
        dfs(root,0,res)
        return res