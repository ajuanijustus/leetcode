# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tail = dummy = ListNode()
        c = 0
        c_head = head
        while c_head:
            c_head = c_head.next
            c += 1
        for x in range(c-1, -1, -1):
            temp_head = head
            for y in range(x):
                temp_head = temp_head.next
            dummy.val = temp_head.val
            if x:
                dummy.next = ListNode()
                dummy = dummy.next
        return tail