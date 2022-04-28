"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashm = {}
        
        for num in nums:
            if num in hashm:
                hashm[num]+=1
            else:
                hashm[num]=1
        
        suma = 0
        
        for key,value in hashm.items():
            if value == 1:
                suma+=key
        return suma
nums = [1,2,3,2]