# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # two pointers: fast and slow
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                return True
        return False

# Template (for unknown reason slow==fast comaprison is faster)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:  # Alternative: if slow.val == fast.val:
                return True
            
        return False
