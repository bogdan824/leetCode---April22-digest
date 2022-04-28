"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #store all numbers in dict to see their frew
        hashm = {}
        while head:
            if head.val in hashm:
                hashm[head.val]+=1
            else:
                hashm[head.val]=1
            head=head.next
            
        dummy = ListNode()
        tail = dummy   
        #create and return a node with the items that appears once
        for key, value in hashm.items():
            if value == 1:
                tail.next=ListNode(key)
                tail = tail.next
        
        return dummy.next
head = [1,2,3,3,4,4,5]