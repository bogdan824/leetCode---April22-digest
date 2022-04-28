"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create array to store the values
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        #get the items from array in reverse order and add to new LL
        dummy = ListNode()
        tail = dummy
        
        for i in range(len(arr)-1,-1,-1):
            tail.next = ListNode(arr[i])
            tail = tail.next
        
        return dummy.next

head = [1,2,3,4,5]