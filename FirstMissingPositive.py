'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        base = 1
        while True:
            low = None
            for i in nums:
                if i >= base and (not low or i < low):
                    low = i
            if not low: 
                return base
            if low != base: 
                return min(low - 1, base)
            base += 1