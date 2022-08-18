# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or head is None or head.next is None:
            return head
        cnt=1
        dummy=head
        while dummy.next :
            cnt+=1
            dummy=dummy.next
        dummy.next=head
        k=cnt-k%cnt
        while k>0:
            dummy=dummy.next
            k=k-1
        head=dummy.next
        dummy.next=None
        return head
            