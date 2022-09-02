# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        for _ in range(n):
            right = right.next
        
        while right and right.next:
            right = right.next
            left = left.next
        
        if right:
            left.next = left.next.next
        else:
            head = left.next
        return head
        