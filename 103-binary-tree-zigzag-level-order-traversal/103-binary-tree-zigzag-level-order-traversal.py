# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        ans = []  # store the traversal in the ans array
        queue = [root] # use list as queue
        flag = False
        while len(queue) != 0:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue[0]
                queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag = not flag
            if flag == False:
                level = level[::-1]
            ans.append(level)
        return ans
 
        