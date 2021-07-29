'''
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
'''
class Solution:
	def findMinDifference(self, timePoints: List[str]) -> int:
		for i in range(len(timePoints)):
			tem = timePoints[i].split(':')
			timePoints[i] = int(tem[0]) * 60 + int(tem[1])
		diff = float('inf')
		timePoints = sorted(timePoints)
		for i in range(1,len(timePoints)):
			temp = timePoints[i] - timePoints[i-1]
			diff = min(diff,temp)
		diff = min(diff, 24*60 - timePoints[-1] + timePoints[0])
		return diff
