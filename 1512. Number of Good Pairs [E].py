"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                #print("i,j :", i, j, "nums i:",nums[i]," j",nums[j])
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count



nums = [1,2,3,1,1,3]