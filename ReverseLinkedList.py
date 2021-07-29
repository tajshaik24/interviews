'''
LeetCode 206. Reverse Linked List

Reverse a singly linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head == None):
            return None
        prev, node = None, head
        while(node != None):
            newNode = node.next
            node.next = prev
            prev, node = node, newNode
        return prev
