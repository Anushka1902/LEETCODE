# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        A=root
        stack=[]
        ans=[]
        while(True):
            if A!=None:
                stack.append(A)
                A=A.left
            else:
                if len(stack)==0:
                    break
                A=stack.pop()
                ans.append(A.val)
                A=A.right
        return ans
        '''
        #recursive
        re=[]
        if root!=None:
            re.extend(self.inorderTraversal(root.left))
            re.append(root.val)
            re.extend(self.inorderTraversal(root.right))
        return re
        '''
        '''
        #iterative
        A=root
        stack=[]
        ans=[]
        while(True):
            if A is not None:
                stack.append(A)
                A=A.left
            else:
                if len(stack)==0:
                    break
                A=stack.pop()
                ans.append(A.val)
                A=A.right
        return ans
        '''