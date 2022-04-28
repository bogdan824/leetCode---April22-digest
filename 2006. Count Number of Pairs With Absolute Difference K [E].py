"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
"""


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        counter = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] - nums[j] == k:
                    counter+=1
                    
        return counter


  nums = [1,3]
   k = 3