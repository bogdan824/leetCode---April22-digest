"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        no = 0
        result = []
        for i in range(len(num)):
            no*=10
            no+=num[i]
        
        no += k
        while no != 0:
            result.insert(0,no%10)
            no//=10
        return result
num = [1,2,0,0]
k = 34