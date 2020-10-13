# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def find_cycle_length(slow):
            ptr = slow
            count = 0
            while ptr.next:
                ptr = ptr.next
                count += 1
                if ptr == slow:
                    return count
        
        # stop in the loop
        slow = head
        fast = head
        
        if not head:
            return None
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # find_cycle_length
                cycle_length = find_cycle_length(slow)
                
                # let fast be "cycle_length" faster
                fast = head
                for i in range(cycle_length):
                    fast = fast.next

                # equal speed until meet again
                slow = head
                while fast.next:
                    if fast == slow:
                        return slow
                    fast = fast.next
                    slow = slow.next

        return None
