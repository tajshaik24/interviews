/**
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
 */
 
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxPathSum(TreeNode root) {
        int[] maxSum = {root.val};
        maxPathSum(root, maxSum);
        return maxSum[0];
    }

    private int maxPathSum(TreeNode root, int[] maxSum) {
        if (root == null)
            return 0;
        int left = maxPathSum(root.left, maxSum);
        int right = maxPathSum(root.right, maxSum);
        maxSum[0] = Math.max(maxSum[0], root.val);
        maxSum[0] = Math.max(maxSum[0], root.val + left);  
        maxSum[0] = Math.max(maxSum[0], root.val + right); 
        maxSum[0] = Math.max(maxSum[0], root.val + left + right); 
        return root.val + Math.max(0, Math.max(left, right));
    }
}

