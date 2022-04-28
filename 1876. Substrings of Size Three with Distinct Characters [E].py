"""
A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.
"""

def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i]!=s[i+2]:
                count+=1
                #print(s[i:i+3])
        return count

 s = "xyzzaz"