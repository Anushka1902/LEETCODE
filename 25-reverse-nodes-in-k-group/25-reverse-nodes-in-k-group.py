# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev,curr,new=dummy,dummy,dummy
        c=0
        while curr.next!=None:
            c+=1
            curr=curr.next
        while c>=k:
            curr=prev.next
            new=curr.next
            for i in range(1,k):
                curr.next=new.next
                new.next=prev.next
                prev.next=new
                new=curr.next
            prev=curr
            c-=k
        return dummy.next
        