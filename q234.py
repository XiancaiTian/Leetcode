# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        part2 = self.reverseLinkedList(self.middleNode(head))
        p1 = head
        p2 = part2
        while (p2 is not None):
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
        
        
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow.next

    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        while (head is not None):
            holder = head.next
            head.next = prev
            prev = head
            head = holder
        return prev
        
