# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# refers to two pointers solution
# https://leetcode.com/problems/intersection-of-two-linked-lists/solution/
# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        pa, pb = headA, headB
        while pa is not pb:          
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
    
        return pa
