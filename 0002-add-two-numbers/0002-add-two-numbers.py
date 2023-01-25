# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = head = ListNode()
        rem = 0
        while(l1 or l2):
            if l1:
                val_1 = l1.val
                l1 = l1.next
            else:
                val_1 = 0
            if l2:
                val_2 = l2.val
                l2 = l2.next
            else:
                val_2 = 0
            tail.next = ListNode()
            tail = tail.next
            val = val_1 + val_2 + rem
            if val > 9:
                rem = 1
                val %= 10
            else:
                rem = 0
            tail.val = val
        if rem:
            tail.next = ListNode(val=rem)
        return head.next