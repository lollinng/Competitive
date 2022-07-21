"""
Here we are trying to find minimum boats needed to take all humans
institution-
1) WE sort the elements and use 2 arrays one from start and other from end
2) Maximum allowed 2 people on boat hence 2 pointers to keep them most optimally 

Solution
1) we check if their sum of pointers is within boat limits if yes we allocate them boat 
2) if not we give boat away to bigger number that is right pointer and decrement right pointer
3) we increment left pointer only if its addition with right pointer in boat limits
as shown in the image

Eg - 
people = [1, 3, 4, 7, 8], limit = 9
start end boat
  1    3    1
  1    2    2
  2    1    3

"""


class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        boat = 0
        end = len(people)-1
        start = 0
        while(start <= end):
            # it doesn't move the start index if sum of start and end are greater than limit
            # hence it gives that index its own boat and move on to next last index
            if(people[start]+people[end] <= limit):
                start += 1
            boat += 1
            end -= 1
            print(start, end, boat)
        return boat


people = [1, 3, 4, 7, 8]
limit = 9
obj = Solution()
print(obj.numRescueBoats(people, limit))
