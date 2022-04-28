"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_arr = list(jewels)
        stones_arr = list(stones)
        counter = 0
        
        for stone in stones_arr:
            if stone in jewels_arr:
                counter += 1


jewels = "aA"
stones = "aAAbbbb"
                
        return counter