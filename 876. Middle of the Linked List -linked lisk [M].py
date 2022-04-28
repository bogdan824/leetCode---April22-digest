"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Create copy of LL
        ptr = head
        #empty array to store elements and find middle
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr=ptr.next
        mid = len(arr)//2 
        #append from mid onwards
        dummy = ListNode()
        tail = dummy
        
        for i,x in enumerate(arr):
            if i>=mid:
                tail.next=ListNode(x)
                tail=tail.next
        return dummy.next

head = [1,2,3,4,5,6]