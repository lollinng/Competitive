import heapq


class Solution:
    def mostBooked(self, n: int, meetings):
        meetings = sorted(meetings)

        # create two heaps
        meet_no = [x for x in range(n)]
        heapq.heapify(meet_no)
        meet_schedule = []
        heapq.heapify(meet_schedule)

        meeting_count  = [0]*n
 
        for start,end in meetings:

            while(meet_schedule and meet_schedule[0][0]<=start):
                _,room = heapq.heappop(meet_schedule)
                heapq.heappush(meet_no,room)


            # if meeting room avail
            if meet_no:
                # pop the top elemnet
                room = heapq.heappop(meet_no)
                # inser the meeting
                heapq.heappush(meet_schedule,(end,room))
            
            # if meeting room not avail
            else:
                # pop the meeting room
                curr_time,room = heapq.heappop(meet_schedule)
                # add room count
                # print(room,'below')
                
                if curr_time>start:
                    end+= curr_time-start
                heapq.heappush(meet_schedule,(end,room))

            meeting_count[room]+=1


        max_rooms = max(meeting_count )
        for i in range(n):
            if meeting_count [i] == max_rooms:
                return i
        return -1

[1,2,2,1]