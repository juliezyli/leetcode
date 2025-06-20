def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def postOrder(x):
            if not x:
                return
            postOrder(x.left)
            postOrder(x.right)
            answer.append(x.val)
        postOrder(root)
        return answer