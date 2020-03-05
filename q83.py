# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = []
        dummy = ListNode(0)
        dummy.next = head
        head_ptr = dummy
        while head_ptr.next:
            if head_ptr.next.val not in seen:
                seen.append(head_ptr.next.val)
                head_ptr = head_ptr.next
            else:
                hold = head_ptr.next.next
                head_ptr.next = hold
        return dummy.next
