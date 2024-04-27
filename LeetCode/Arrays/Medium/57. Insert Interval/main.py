"""
here we have to insert a touple with start and end values into an arr
such that it combines with ovelapping tupple in the list

for eg - 
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

PREREQUISITES: 56. Merge Intervals

Intution:
1) Here we iterate through



"""


class Solution:
    def insert(self, intervals, newInterval):

        res = []

        for i in range(len(intervals)):

            # IF NEW ELEMENT IS NOT OVERLAPPING
            # if new element last less than ith iterations first
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # IF NEW ELEMENT IS NOT OVERLAPPING
            # if new element firt more than ith iterations last
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # IF NEW ELEMENT IS OVERLAPPING
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])

        # appening new element if its at last 
        res.append(newInterval)
        return res