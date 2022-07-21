"""
Here are told to count an element and delete all elements consecative to it and find max value u can count

So , to simplify the problem we convert [1,1,1,2,4,5,5,5,6] -----> [0, 3, 2, 0, 4, 15, 6, 0, 0]
i,e we can convert the problem into an new array using old arrays values-> to index and 
                                                       old arrays sum_of_value to value in new array 


after converting it into the following format we can see that we can apply house robbing questions algorithm
where we add the non consecative elements to get maximum value out of an array
doing that gives us max value count not worrying about the consecative deletion of elements constraint
"""

from collections import Counter


class Solution:
    def deleteAndEarn(self, nums):

        # [1,1,1,2,4,5,5,5,6] -----> [0, 3, 2, 0, 4, 15, 6, 0, 0]
        # points = [0]*1001
        # for num in nums:
        #     points[num] += num
        c = Counter(nums)
        points = [0]           # 0 for helping with index
        for i in range(min(c), max(c)+1):
            if i in c:
                points.append(c[i] * i)
            else:
                points.append(0)
        print(points)
        return self.rob(points)

    def rob(self, points):
        for i in range(2, len(points)):
            points[i] = max(points[i-1], points[i-2]+points[i])
            print(points)
            if i > 12:
                break
        return points[-1]


s = Solution()
print(s.deleteAndEarn([4, 10, 10, 8, 1, 4, 10, 9, 7, 6]))

# [1,1,1,2,4,5,5,5,6]
# 18
# [4, 10, 10, 8, 1, 4, 10, 9, 7, 6]
# 53
