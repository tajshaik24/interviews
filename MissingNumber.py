'''
LeetCode 268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        expected_sum = n*(n-1) // 2
        actual_sum = sum(nums)
        return expected_sum-actual_sum
