"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #convert array to num
        num = 0
        result = []
        for i in range(len(digits)):
            num*=10
            num+=digits[i]
        #add 1
        num = num+1
        #convert num to array
        while num != 0:
            result.insert(0,num%10)
            num//=10
        return result
digits = [1,2,3]       