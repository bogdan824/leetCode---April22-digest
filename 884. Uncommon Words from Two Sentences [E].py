"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        x = s1 + " " + s2
        x = x.split(" ")
        
        hashm = {}
        for i in x:
            if i in hashm:
                hashm[i]+=1
            else: 
                hashm[i]=1
        keep = []
        
        for k,v in hashm.items():
            if v==1:
                keep.append(k)
        
        return keep

