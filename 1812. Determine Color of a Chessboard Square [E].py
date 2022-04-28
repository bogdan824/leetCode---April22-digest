"""
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        evens = ["b","d","f","h"]
        #
        if coordinates[0] in evens:
            return int(coordinates[1])%2!=0
        
        if coordinates[0] not in evens:
            return int(coordinates[1])%2==0
