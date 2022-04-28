"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        if len(strs) == 0:
            return result
        
        for i in range(len(strs[0])):
            for ch in strs:
                if i == len(ch) or ch[i] != strs[0][i]:
                    return result
            result += ch[i]
        return result

strs = ["flower","flow","flight"]