"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            last = merged[-1]
            if last.end > intervals[i].start:
                return False
            merged.append(intervals[i])
        return True