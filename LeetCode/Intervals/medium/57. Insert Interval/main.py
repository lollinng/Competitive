class Solution:
    
    def insert(self, intervals,newInterval):
       
        '''
        Basic logic is to not insert if overlapping 
        and insert if not overlapping

        in case of first if overlapping get min and max of start and ends
        and skip curretn elemetn from intervals and not add to res
        since it overalapped and hence
        and wait for case of not overlapping over loop 
        '''

        res = []
        interval_len = len(intervals)
        for index in range(interval_len):

            # IF NOT OVERLAPPING
            # AND newInterval end is before current start
            # append res with remainign array and break
            if newInterval[1] < intervals[index][0]:
                res.append(newInterval)
                return res + intervals[index:]
                
            # If Not overlapping
            # new Intervals start after current end
            # add current element to res
            elif intervals[index][1] < newInterval[0]:
                res.append(intervals[index])

            # overllapping hence dont add current intervals as well as newInterval
            else:
                newInterval[0] = min(newInterval[0],intervals[index][0])
                newInterval[1] = max(newInterval[1],intervals[index][1])

        # since the overlapped interval was left till last and didnt return
        res.append(newInterval)
        return res
            