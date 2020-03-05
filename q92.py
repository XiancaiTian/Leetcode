# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''Note: we want a reverse, not an exchange
I plan to get three parts: (1, 234, 5)
then reverse (234) then join them back
'''

class Solution(object):
    def reverseBetween(self, head, m, n):
        
        if m == n:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        # dummy = [0, 1] ; part A
        
        cur = p.next
        pre = None
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next
        
        p.next.next = cur # dummy = [0, 1, 2, 5]; combine part A+C
        p.next = pre      # dummy = [0, 1, 2, 3, 4, 5]; combine part A+B+C
        return dummy.next
