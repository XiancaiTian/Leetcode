# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        odds = ListNode(0)
        evens = ListNode(0)
        oddsHead = odds
        evensHead = evens
        isOdd = True
        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd = not isOdd
            head = head.next
        evens.next = None
        odds.next = evensHead.next
        return oddsHead.next
