# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
LeetCode 1382. Balance a Binary Search Tree

Given a binary search tree, return a balanced binary search tree with the same node values. A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them.
'''
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        data = []

        def inOrder(curNode):
            if (curNode == None):
                return
            inOrder(curNode.left)
            data.append(curNode.val)
            inOrder(curNode.right)

        def buildTree(arr):
            n = len(arr)
            if (n == 0):
                return None
            elif (n == 1):
                return TreeNode(arr[0])
            elif (n == 2):
                root = TreeNode(arr[1])
                root.left = TreeNode(arr[0])
                return root
            else:
                mid = n // 2
                root = TreeNode(arr[mid])
                root.left = buildTree(arr[:mid])
                root.right = buildTree(arr[mid+1:])
                return root

        inOrder(root)
        return buildTree(data)
