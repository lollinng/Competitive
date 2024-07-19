class Solution:
    def eraseOverlapIntervals(self, intervals):
        '''

        [[1,2],[2,3],[3,4],[1,3]]

        2->2
        3->3

        We have to remove middle intervals

        [[1,3],[2,5],[4,6],[13,14]]
        
        upon left[1]>right[start] : res+=1

        '''

        # we are sorting using ending
        # since we want to remove the meetings which ends late
        # to avoid further collisons , over meetings which ends earlier
        # meetings ending earlies avoid some extra collisons
        # hence minizing colission or removal of intervals 


        intervals = sorted(intervals,key=lambda x:x[1])
        print(intervals)

        intervals_len = len(intervals)

  
        res = 0
        index = 1
        while index<intervals_len:
            curr = intervals[index-1]
            
            while index<intervals_len and curr[1] > intervals[index][0]:
                index+=1
                res+=1

            index+=1
        return res