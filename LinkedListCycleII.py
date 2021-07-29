'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tortoise = intersect(head)
        if tortoise is None:
            return None
        ptr1 = head
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

def intersect(head):
    tortoise = head
    hare = head
    while (hare != None and hare.next != None):
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return tortoise
    return None