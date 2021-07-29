'''
LeetCode 253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        for interval in sorted_intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)
