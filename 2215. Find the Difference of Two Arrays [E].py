"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        keep = [[],[]]
        
        for i in nums1:
            if i not in nums2 and i not in keep[0]:
                keep[0].append(i)
        
        for i in nums2:
            if i not in nums1 and i not in keep[1]:
                keep[1].append(i)
        
        return keep

nums1 = [1,2,3]
nums2 = [2,4,6]