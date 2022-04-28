"""
Write a program to count the number of days between two dates
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
"""

from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")
        
        return abs((date2 - date1).days)
        
date1 = "2019-06-29"
date2 = "2019-06-30"