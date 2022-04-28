"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create empty array to get the middle
        arr = []
        #create copy of LL 
        ptr = head
        #enumerate throught the LL
        while ptr:
            arr.append(ptr.val)
            ptr=ptr.next
        mid = len(arr)//2
        
        dummy = ListNode()
        tail = dummy
        #create new LL without the middle element
        for i,x in enumerate(arr):
            if i != mid:
                tail.next = ListNode(x)
                tail = tail.next
        
        return dummy.next

head = [1,3,4,7,1,2,6]
        