# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    Requires a pointer, and a output linkedlist
    Should not change the oirginal input
    '''
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        output = ListNode(-1)
        output.next = head
        pointer_output = output
        
        # head is the pointer
        while head and head.next:
            # load new
            one = head
            two = head.next
            
            # 2-> 1, 1->3
            three = two.next
            two.next = one
            one.next = three
            # -1> 2
            pointer_output.next = two
            
            # move pointer to end of two
            pointer_output = one
            # move pointer to three
            head = three
            
        return output.next
            
            
