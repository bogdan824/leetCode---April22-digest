"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        keep = x
        result = 0
        
        if x<0:
            return False
        
        while keep > 0:
            result = result * 10 
            result+=keep%10
            keep//=10
        
        
        return result == x

x = 121