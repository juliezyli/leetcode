def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def preOrder(x):
            if not x:
                return
            answer.append(x.val)
            preOrder(x.left)
            preOrder(x.right)
        preOrder(root)
        return answer