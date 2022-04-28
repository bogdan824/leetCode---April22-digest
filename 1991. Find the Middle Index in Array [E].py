"""
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
"""

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        #sliding window sum
        start = 0
        end = sum(nums)
        
        for i in range(len(nums)):
        #check if is the middle index    
            if start == end - nums[i]:
                return i
            
            start += nums[i]
            end -= nums[i]
            
        return -1
nums = [2,3,-1,8,4]
