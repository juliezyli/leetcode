class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        final = []
        if not root:
            return final
        stack = [(root, str(root.val))] # store as a tuple 
        while stack:
            node, path = stack.pop() 
            if not node.left and not node.right: 
                final.append(path)
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        return final