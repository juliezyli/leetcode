import javax.swing.tree.TreeNode;

public class problem404{
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left != null && (root.left.right == null && root.left.left == null)) {
            if (root.right != null) {
                return root.left.val + sumOfLeftLeaves(root.right);
            }
            return root.left.val;
        }
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
}
