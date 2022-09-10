class Solution:
    def __init__(self):
        self.inOrder = []
        
    def traversal(self,root):
        if root is None:
            return []
        if root:
            self.traversal(root.left)
            self.inOrder.append(root.val)
            self.traversal(root.right)
        return self.inOrder
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = self.traversal(root)
        tree = TreeNode(val=arr[0])
        node = tree
        for i in range(1,len(arr)):
            node.right = TreeNode(val=arr[i])
            node = node.right
        return tree