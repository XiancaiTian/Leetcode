# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # define dummy
        dummy = ListNode(0)
        ptr_d = dummy
        
        # define carry digits
        carry = 0
        
        # no need to define a new ptr for l1 or l2
        # because we only append to dummy
        # l1 may be shorter or longer than l2
        while l1 or l2:
            if l1:
                carry = carry + l1.val
                l1 = l1.next
            
            if l2:
                carry = carry + l2.val
                l2 = l2.next
                
            carry, remainder = divmod(carry, 10)
            
            # add a new node to dummy
            new = ListNode(remainder)
            ptr_d.next = new
            ptr_d = ptr_d.next
        
        if carry:
            new = ListNode(carry)
            ptr_d.next = new
            ptr_d = ptr_d.next
            
        return dummy.next 
