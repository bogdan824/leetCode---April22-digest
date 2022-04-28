"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        suma = 0
        
        for i in range(len(nums)):
            suma+=nums[i]
            result.append(suma)
            
        
        return result
nums = [1,2,3,4]            
