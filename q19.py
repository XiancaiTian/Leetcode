# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Maintain two pointers and update one with a delay of n steps.
Remember to use dummy
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        head_fast = dummy
        head_slow = dummy 
        for _ in range(n+1):
            head_fast = head_fast.next
        while head_fast:
            head_fast = head_fast.next
            head_slow = head_slow.next
        hold = head_slow.next.next
        head_slow.next = hold
        return dummy.next
