# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        carry=0
        temp=dummy
        while l1 is not None or l2 is not None or carry:
            sum=0
            if l1 is not None:
                sum+=l1.val
                l1=l1.next
            if l2 is not None:
                sum+=l2.val
                l2=l2.next
            sum+=carry
            carry=sum//10
            new=ListNode(sum%10)
            temp.next=new
            temp=temp.next
        return dummy.next
        '''
        dummy=ListNode()
        temp=dummy
        carry=0
        while l1 is not None or l2 is not None or carry:
            sum=0
            if l1 is not None:
                sum+=l1.val
                l1=l1.next
            if l2 is not None:
                sum+=l2.val
                l2=l2.next
            sum+=carry
            carry=sum//10
            temp1=ListNode(sum%10)
            temp.next=temp1
            temp=temp.next
        return dummy.next
        '''
        '''
        head = sm = ListNode()                            
        carry = 0                                         
        while l1 or l2:                                   
            if l1: carry, l1 = carry + l1.val, l1.next   
            if l2: carry, l2 = carry + l2.val, l2.next    
            sm.next = sm = ListNode(val = carry % 10)    
            carry //= 10                                 
        if carry: sm.next = ListNode(val = carry)         
        return head.next            
        '''