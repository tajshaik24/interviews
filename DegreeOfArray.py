'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        firstOccur, lastOccur, count = {}, {}, {}
        for i, n in enumerate(nums):
            if n not in firstOccur:
                firstOccur[n] = i
            lastOccur[n] = i
            count[n] = count.get(n, 0) + 1
        minLen, degree = len(nums), max(count.values())
        for elem in count:
            if count[elem] == degree:
                minLen = min(minLen, lastOccur[elem] - firstOccur[elem] + 1)
        return minLen
