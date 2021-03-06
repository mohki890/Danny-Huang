# -*- coding: utf-8 -*-
# @Time    : 13/01/2018 5:56 PM
# @Author  : Huang_xk
# @FileName: Medium 24. Swap Nodes in Pairs.py


'''
    Given a linked list, swap every two adjacent nodes and return its head.

    For example,
    Given 1->2->3->4, you should return the list as 2->1->4->3.

    Your algorithm should use only constant space.
    You may not modify the values in the list, only nodes itself can be changed.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(-1)
        dummy.next = head
        while cur.next and cur.next.next:
            p0, p1 = cur.next, cur.next.next
            cur.next = p1
            p0.next = p1.next
            p1.next = p0
            cur = cur.next.next
        return dummy.next