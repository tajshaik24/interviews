'''
LeetCode 15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        result = []
        for index, num in enumerate(nums):
            if(num not in seen):
                left = index + 1
                right = len(nums) - 1
                seen.add(num)
                while left < right:
                    left_num = nums[left]
                    right_num = nums[right]
                    if(num + left_num + right_num == 0):
                        result.append([num, left_num, right_num])
                        while(left < len(nums) - 1 and nums[left] == left_num):
                            left += 1
                        while(right < 0 and nums[right] == right_num):
                            right -= 1
                    elif(num + left_num + right_num < 0):
                        left += 1
                    else:
                        right -= 1
        return result

