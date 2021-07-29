'''
LeetCode 92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if(head == None):
            return ListNode()
        prev, node = None, head
        while(m > 1):
            prev, node = node, node.next
            m -= 1
            n -= 1
        prevNodeM, tailReverse = prev, node
        while(n > 0):
            nextNode = node.next
            node.next = prev
            prev, node = node, nextNode
            n -= 1
        if(prevNodeM):
            prevNodeM.next = prev
        else:
            head = prev
        tailReverse.next = node
        return head
