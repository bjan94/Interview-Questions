"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
import heapq


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def min_meeting_rooms(intervals):
    if intervals is None or len(intervals) == 0:
        return 0

    intervals.sort(key=lambda i: i.start)

    pq = []
    res = 0

    for interval in intervals:
        if not pq or interval.start < pq[0]:
            res += 1
        else:
            heapq.heappop(pq)
        heapq.heappush(pq, interval.end)

    return len(pq)


def main():
    i0 = Interval(0, 30)
    i1 = Interval(5, 10)
    i2 = Interval(15, 20)
    print(min_meeting_rooms([i2, i0, i1]))

    i4 = Interval(7, 10)
    i5 = Interval(2, 4)
    print(min_meeting_rooms([i4, i5]))

    i4 = Interval(5, 10)
    i5 = Interval(6, 10)
    print(min_meeting_rooms([i4, i5]))


if __name__ == "__main__":
    main()
