# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative solution (Template)

# iteration 1: prev = 1-> None
# iteration 2: prev = 2->1-> None
# iteration 3: prev = 3->2->1->None
# etc...
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head is not None:
            holder = head.next
            head.next = prev
            prev = head
            head = holder
        return prev

# recursive solution
class Solution(object):
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
