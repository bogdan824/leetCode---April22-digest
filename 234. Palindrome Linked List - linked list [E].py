"""
Given the head of a singly linked list, return true if it is a palindrome.
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #create array and store all the values
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        #check if palindrome
        start = 0
        end = len(arr)-1
        
        while start < end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True