"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1 = l1.next
            if l2: 
                carry+=l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry//=10
        return dummy.next
 l1 = [2,4,3]
 l2 = [5,6,4]           