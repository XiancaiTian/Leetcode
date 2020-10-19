class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        
        # part A, let dummy be 0 -> 1
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        
        # part B 
        curr = p.next # 2
        prev = None
        for _ in range(n - m + 1):
            holder = curr.next
            curr.next = prev
            prev = curr
            curr = holder
            
        # combine part A+C
        p.next.next = curr # let dummy be 0 -> 1 -> ? -> 5
        # combine part A+B+C
        p.next = prev
        
        return dummy.next
