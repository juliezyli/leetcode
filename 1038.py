def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inorder_traversal = []
        self.InOrder(root)
        self.inorder_traversal.reverse()
        self.replace_values(root)
        return root

    def InOrder(self, x):
        if x is None:
            return
        self.InOrder(x.left)
        self.inorder_traversal.append(x.val)
        self.InOrder(x.right)

    def replace_values(self, x): 
        if x is None:
            return 
        self.replace_values(x.left)
        self.replace_values(x.right)
        
        sum = 0
        for i in self.inorder_traversal:
            if i > x.val:
                sum += i
            else: 
                break
        x.val += sum