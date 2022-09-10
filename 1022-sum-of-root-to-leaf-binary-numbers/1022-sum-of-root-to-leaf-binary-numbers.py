# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total=0
        Q=[]
        stack=[]
        def DFS(r):
            if r:
                stack.append(str(r.val))
                if r.left:
                    DFS(r.left)
                    
                    if stack: 
                        stack.pop()
                if r.right:
                    DFS(r.right)
                    
                    if stack: 
                        stack.pop()
                if not (r.left or r.right):
                    Q.append(int(''.join(stack),2))
                    
        DFS(root)
        return sum(Q)