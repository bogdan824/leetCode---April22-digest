"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #initiate a start and end variable
        start = 0 
        end = len(height)-1
        result = 0
        length = len(height)-1
        keep = 0
        
        #go through the container and get the maximum value possible
        while(start<end):
            result = max(result, length*min(height[start],height[end]))
            if height[start] > height[end]:
                end-=1
            else:
                start+=1
            length-=1
            
        return result
        
height = [1,8,6,2,5,4,8,3,7]

