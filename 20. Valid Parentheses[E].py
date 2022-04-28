"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = { "(" : ")", "[" : "]", "{" : "}"}
        
        for par in s:
            if par in pairs:
                print(par)
                stack.append(pairs[par])
            else:
                if len(stack) == 0 or stack.pop() != par:
                    return False
        return len(stack)==0

s = "()"