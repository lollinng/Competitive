class Solution:
    def averageWaitingTime(self, customers):
  
        curr_time = 0
        total_time_taken = 0
        for start_time,preparation_time in customers:
            curr_time = max(start_time,curr_time)
            curr_time += preparation_time

            total_time_taken += curr_time-start_time

        return total_time_taken/len(customers)