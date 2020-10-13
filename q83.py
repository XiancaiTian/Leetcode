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

# More elegant solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head
