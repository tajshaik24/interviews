'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = {0 : -1}
        s, maxLen = 0, 0
        for i, num in enumerate(nums):
            addend = -1 if num == 0 else num
            s += addend
            if s in counter:
                maxLen = max(maxLen, i - counter[s])
            if s not in counter:
                counter[s] = i
        return maxLen
