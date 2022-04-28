"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #create empty array
        arr = []
        #store all numbers in array
        while head:
            arr.append(head.val)
            head=head.next
        #ass the array is even, we sum up the twins and we get the maximum value
        start = 0
        end = len(arr)-1
        suma = 0
        while start<end:
            suma = max(suma, arr[start]+arr[end])
            start+=1
            end-=1
        return suma

head = [5,4,2,1]