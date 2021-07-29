'''
LeetCode 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setNums = dict()
        for index in range(len(nums)):
            setNums[nums[index]] = index
        for index in range(len(nums)):
            secondNum = target - nums[index]
            if secondNum in setNums.keys() and index != setNums[secondNum]:
                return [index, setNums[secondNum]]
        return []
