"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] >= target:
                return i
            keep = i
        return keep+1
nums = [1,3,5,6]
target = 5