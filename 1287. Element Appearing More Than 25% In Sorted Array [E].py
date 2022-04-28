"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
"""

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        hashm = {}
        #put the elements and their occurence in a dictionary
        for num in arr:
            if num in hashm:
                hashm[num]+=1
            else:
                hashm[num]=1
        maxi = 0
        keep = 0
        #get the maximum and store its value
        for key,value in hashm.items():
            if value > maxi:
                maxi = value
                keep = key
        return keep

arr = [1,2,2,6,6,6,6,7,10]