# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res=[]
        def inorder(rootpa):
            if not rootpa:
                return
            inorder(rootpa.left)
            res.append(rootpa.val)
            inorder(rootpa.right)
            
        inorder(root)
        # print(res)
        res.sort()
        ii=0
        def inordercrct(rootka,i):
            if not rootka:
                return
            inordercrct(rootka.left,i)
            rootka.val=res[0]
            res.pop(0)
            inordercrct(rootka.right,i)
            
        inordercrct(root,ii)
        return root
        