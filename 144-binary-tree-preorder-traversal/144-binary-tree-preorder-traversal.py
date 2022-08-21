# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        stack=[root]
        res=[]
        
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res
        
        '''
        res = []
        nStack = [root]
        
        while nStack:
            node = nStack.pop()
            
            if node:
                res.append(node.val)
                nStack.append(node.right)
                nStack.append(node.left)
            
        return res
          '''
    
        
        '''
            re=[]
            if root!=None:
                re.append(root.val)
                re.extend(self.preorderTraversal(root.left))
                re.extend(self.preorderTraversal(root.right))
            return re
        '''

        