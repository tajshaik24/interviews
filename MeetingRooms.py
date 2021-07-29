'''
LeetCode 252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sortedListMeetings = sorted(intervals, key = lambda i:i[1])
        for i in range(1, len(sortedListMeetings)):
            if sortedListMeetings[i-1][1] > sortedListMeetings[i][0]:
                return False
        return True
