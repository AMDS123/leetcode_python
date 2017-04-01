# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def V(val):
            return val is not None
        result = None
        pre = None
        tag = 0
        while V(l1) or V(l2):
            l1_val = V(l1) and l1.val or 0
            l2_val = V(l2) and l2.val or 0
            val = l1_val + l2_val + tag
            tag = val / 10
            node = ListNode(val % 10)
            if result is None:
                result = node
                pre = node
            else:
                pre.next = node
                pre = node
            if V(l1):
                l1 = l1.next
            if V(l2):
                l2 = l2.next

        if tag == 1:
            pre.next = ListNode(1)

        return result
