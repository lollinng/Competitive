class Solution:
    
    def helper(self,arr,val):
        l,r = 0,len(arr)-1
        while(l<r):
            mid = l + (r-l)//2
            if arr[mid]>val:
                r = mid
            else:
                l= mid+1
        return l

    def jobScheduling(self, startTime, endTime, profit):
        # sort according to ending 
        jobs = sorted(zip(startTime, endTime, profit),key=lambda x:x[1])
        sorted_end_times = [x[1] for x in jobs]
        n = len(jobs)
    
        # dp will be maxium profit at ith time from different job
        dp = [0 for _ in range(n)]

        dp[0] = jobs[0][2]
        for i in range(1,n):
            current_start,_,current_profit = jobs[i] # getting job info

            #  finding the latest job that finishes before the current job start
            j = self.helper(sorted_end_times,current_start)-1

            # if we have atleast one job to left found by search
            # add last jobs profit to curreent profit since they dont collide
            if j>=0:
                current_profit +=dp[j]

            # current ith time job index profit is including itself or excluding itself
            dp[i] = max(current_profit,dp[i-1])
 
        return dp[-1]

        