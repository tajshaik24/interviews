'''
LeetCode 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        output = [1 for num in nums]
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        rightProduct = 1
        for i in range(len(nums) - 2, -1 , -1):
            rightProduct = rightProduct * nums[i + 1]
            output[i] = output[i] * rightProduct
        return output
