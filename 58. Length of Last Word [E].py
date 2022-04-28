"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        #remove all white spaces
        s = s.strip()
        #convert string
        ans = s.split()
        #remove last element
        return len(ans[-1])

s = "Hello World"
#s = "   fly me   to   the moon  "