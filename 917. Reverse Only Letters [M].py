"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        letters = [ch for ch in s if ch.isalpha()]
        keep = []
        
        for i in s:
            if i.isalpha():
                keep.append(letters.pop())
            else:
                keep.append(i)
        return "".join(keep)
        
s = "ab-cd"