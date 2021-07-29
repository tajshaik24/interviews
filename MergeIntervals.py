'''
LeetCode 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        insert_interval = intervals_sorted[0]
        res = []
        for curr_interval in intervals_sorted[1:]:
            if curr_interval[0] <= insert_interval[1]:
                insert_interval[1] = max(insert_interval[1], curr_interval[1])
            else:
                res.append(insert_interval)
                insert_interval = curr_interval
        res.append(insert_interval)
        return res
