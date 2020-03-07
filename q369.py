# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# adapt the concept mention here...
# https://leetcode.com/problems/plus-one-linked-list/solution/
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        digit = dummy
        while ptr and ptr.next:
            if not ptr.next.next:
                
                # if last digit is nine
                if ptr.next.val != 9:
                    ptr.next.val +=1
                    ptr = ptr.next
                else:
                    digit.val += 1
                    digit = digit.next
                    while digit:
                        digit.val = 0
                        digit = digit.next
                    ptr = digit
            else:
                if ptr.next.val != 9:
                    digit = ptr.next
                ptr = ptr.next
                
        # in case of 99->100
        if dummy.val:
            return dummy
        # most cases
        else:
            return dummy.next
                
           
                
