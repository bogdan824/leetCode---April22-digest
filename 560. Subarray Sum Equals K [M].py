"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter=0
        hashm={0:1}
        suma = 0
        
        for num in nums:
            suma+=num
            if suma-k in hashm:
                counter+=hashm[suma-k]
            
            if suma in hashm:
                hashm[suma]+=1
            else:
                hashm[suma]=1
        
        return counter

nums = [1,1,1], k = 2         