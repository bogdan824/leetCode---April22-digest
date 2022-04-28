"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashm={}
        count = 0
        for i in arr:
            if i in hashm:
                hashm[i]+=1
            else:
                hashm[i]=1
        keep = [-1]        
        for k,v in hashm.items():
            if v==k:
                keep.append(v)
        return max(keep)
        
arr = [2,2,3,4]