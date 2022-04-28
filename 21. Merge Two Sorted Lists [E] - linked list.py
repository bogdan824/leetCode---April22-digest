"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create empty node list
        dummy = ListNode()
        tail = dummy
        
        #as long we have values to compare...
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        #if there is no value for one list but another...
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

list1 = [1,2,4]
list2 = [1,3,4]