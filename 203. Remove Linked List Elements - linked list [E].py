"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #[SOLUTION 1]
        dummy = ListNode()
        tail = dummy
        
        while head:
            if head.val != val:
                tail.next = ListNode(head.val)
                tail=tail.next
            head=head.next
        return dummy.next
        
        
        """
        [SOLUTION 2]
        #create empty array and store all values
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        dummy = ListNode()
        tail = dummy
        #if the values to new list
        for i,x in enumerate(arr):
            if x != val:
                tail.next = ListNode(x)
                tail=tail.next
        return dummy.next
        """