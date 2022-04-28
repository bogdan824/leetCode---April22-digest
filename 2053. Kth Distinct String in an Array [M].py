"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        hashm = {}
        
        for i in arr:
            if i in hashm:
                hashm[i] += 1
            else:
                hashm[i] = 1

        for key,value in hashm.items():
            if value==1 and k==1:
                return key
            elif value==1:
                k-=1
        
        return ""

arr = ["d","b","c","b","c","a"]
k = 2