"""
Given the head of a sorted linked list, delete all duplicates such 
that each element appears only once. Return the linked list sorted as well.
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = head
        
        while ptr:
            while ptr.next and ptr.next.val == ptr.val:
                ptr.next = ptr.next.next     # skip duplicated node
            ptr = ptr.next     # not duplicate of current node, move to next node
            
        return head

head = [1,1,2]
