"""
Here we are trying to merge the array elements with overlaps 
each other in start and end index

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Intution
1) First we sort the array so its easier to iterate though and check overlaps
2) We check last elements end if bigger than next elements start
3) If so we overlap array elements and end becames max of 2 ends
4) Other elements are just appended normally to the array
[[1, 6]]
[[1, 6], [8, 10]]
[[1, 6], [8, 10], [15, 18]]
"""

class Solution:
    def merge(self, intervals):         

        intervals.sort()
        res = [intervals[0]]

        for start,end in intervals[1:]:
            lastEnd = res[-1][1]
            if lastEnd >= start:
                res[-1][1] = max(lastEnd ,end)
            else:
                res.append([start,end])

        return res