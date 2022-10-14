# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return 
        
        fast=head
        slow=head
        previous=slow
        while fast and fast.next:
            previous=slow
            slow=slow.next
            fast=fast.next.next
        print(previous.val)
        previous.next=previous.next.next
        return head