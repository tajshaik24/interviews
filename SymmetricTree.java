/** Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
   
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root == null || root.left == null && root.right == null){
            return true;
        }
        else if(root.left != null && root.right == null || root.left == null && root.right != null){
            return false;
        }
        else if(root.left.val != root.right.val){
            return false;
        }
        return isSymmetricHelper(root.left, root.right);
    }
    boolean isSymmetricHelper(TreeNode left, TreeNode right){
        if(left != null && right == null || left == null && right != null){
            return false;
        }
        else if(left == null && right == null){
            return true;
        }
        else if(left.left == null && right.right == null && right.left == null && left.right == null){
            if(left.val != right.val){
                return false;
            }
            return true;
        }
        return left.val == right.val && isSymmetricHelper(left.right, right.left) && isSymmetricHelper(left.left, right.right);
        
    }
}