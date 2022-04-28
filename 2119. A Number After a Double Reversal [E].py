"""
Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.
"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        result = 0
        neg = 0
        x=num
        
        if x<0:
            neg = 1
            x = x * -1
        
        while x > 0:
            result = result * 10 + x%10
            x = x // 10
            
        while result > 0:
            x = x * 10 + result%10
            result = result // 10
      
        if x==num:
            return True
        return False

 num = 526