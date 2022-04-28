"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        neg = 0
        if x<0:
            neg = 1
            x = x * -1
        
        while x > 0:
            result = result * 10 + x%10
            x = x // 10
        if result > pow(2,31):
            return 0
    
        if neg == 1:
            result=int("-" + str(result))
            return  result
        return result

Input: x = 123