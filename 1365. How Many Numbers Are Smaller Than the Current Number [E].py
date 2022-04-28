"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 """

 class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        hashm = {}
        keep = sorted(nums)
        result = []
      
        for i in range(len(keep)):
            if keep[i] not in hashm:
                hashm[keep[i]]=i
        
        for i in range(len(nums)):
            result.append(hashm[nums[i]])
        return result

nums = [8,1,2,2,3]


