"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = fast = slow = ListNode(0,next=head)
        
        #move fast n steps
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
head = [1,2,3,4,5], n = 2        