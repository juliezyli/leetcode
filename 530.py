class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minimum = float('inf')
        self.prev = None 

        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev is not None:
                    self.minimum = min(self.minimum, node.val - self.prev)
                self.prev = node.val 
                dfs(node.right)
        dfs(root)
        return self.minimum