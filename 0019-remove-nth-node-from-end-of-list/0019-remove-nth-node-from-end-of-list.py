# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = d = head
        l = 0
        while(t):
            t = t.next
            l += 1
        if l < 2:
            return None
        elif l == 2 and n == 1:
            head.next = None
        elif l == n:
            return head.next
        else:
            for i in range(l - n - 1):
                d = d.next
            d.next = d.next.next
        return head