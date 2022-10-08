# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() #set of nodes we have already seen
        while head:
            if head in seen: #if we already saw this node then there is a cycle
                return True
            seen.add(head) #add node to our list of seen nodes
            head = head.next #visit next node
        return False #we reached the end of the list -- no cycle!
        '''
        if head is None:
            return False
        slow = head 
        fast = head.next
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next 
            fast = fast.next.next
                
        return True
        '''