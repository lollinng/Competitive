class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        '''

            [[1,3],[2,6],[8,10],[15,18]]

        res = [[1,3]]

        if last<start    append normal
        elif last>start  update thier last with max(both last)

            


        '''
        if not intervals:
            return []

        intervals = sorted(intervals)
        intervals_len = len(intervals)
        res = [intervals[0]]
        for index in range(1,intervals_len):
            
            arr_last = res[-1][1]
            curr_start = intervals[index][0]
            curr_last = intervals[index][1]


            if arr_last>=curr_start:
                res[-1][1] = max(arr_last,curr_last)
            else:
                res.append(intervals[index])
        
        return res

            