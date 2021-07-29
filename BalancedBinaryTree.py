'''
LeetCode 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if(not root):
            return True
        leftHeight = self.height(root.left, 0)
        rightHeight = self.height(root.right, 0)
        if(abs(leftHeight - rightHeight) > 1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node, height):
        if(not node):
            return height
        return max(self.height(node.left, height+1), self.height(node.right, height+1))
