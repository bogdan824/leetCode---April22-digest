"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #create an array and store all the numbers
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        #sort the array
        arr.sort()
        #create new LL and append the items from the array
        dummy = ListNode()
        tail = dummy
        
        for i,a in enumerate(arr):
            tail.next = ListNode(a)
            tail = tail.next
        
        return dummy.next
lists = [[1,4,5],[1,3,4],[2,6]]