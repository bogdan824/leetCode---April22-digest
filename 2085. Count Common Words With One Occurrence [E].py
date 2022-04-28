"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
"""

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1=Counter(words1)
        c2=Counter(words2)
        counter= 0
        for i in words1:
            if i in words2 and c1[i]==c2[i]==1:
                counter+=1
        return counter

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]