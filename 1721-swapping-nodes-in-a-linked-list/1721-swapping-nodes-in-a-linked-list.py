# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        kn=head
        for i in range(k-1):
            temp=temp.next
        keth=temp
        while(temp.next!=None):
            kn=kn.next
            temp=temp.next
        keth.val,kn.val=kn.val,keth.val
        return head