# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        seen = []
        counter = 1
        seen.append(head.val)
        while head.next:
            seen.append(head.next.val)
            counter += 1
            head = head.next
        for i in range(int(counter/2)):
            if seen[0] == seen [-1]:
                seen = seen[1:-1]
            else:
                return False
        return True
                