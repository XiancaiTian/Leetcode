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
        p.next.next = cur # dummy = [0, 1]+?+[5]; combine part A+C
        p.next = pre      # dummy = [0, 1, 4, 3, 3, 5]; combine part A+B+C
        return dummy.next
