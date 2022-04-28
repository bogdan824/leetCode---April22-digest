"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        keep = set()
        
        for i in nums2:
            if i in nums1:
                keep.add(i)
        return keep
        
nums1 = [1,2,2,1]
nums2 = [2,2]