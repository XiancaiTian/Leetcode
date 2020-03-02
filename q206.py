# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            hold = head.next
            head.next = prev
            prev = head
            head = hold
            # iteration 1: prev = 1-> None
            # iteration 2: prev = 2->1-> None
            # iteration 3: prev = 3->2->1->None
            # etc...
        return prev # return five
