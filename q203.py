# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head_ptr = dummy
        while head_ptr.next:
            if head_ptr.next.val == val:
                hold = head_ptr.next.next
                head_ptr.next = hold              
            else:
                head_ptr = head_ptr.next
        return dummy.next
