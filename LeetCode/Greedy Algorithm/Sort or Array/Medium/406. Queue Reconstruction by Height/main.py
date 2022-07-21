"""
Here we are trying to sort array such that each element has has only x people bigger forward to it
the x is speicfied in the array with each number

Intitution -
1) We will first sort the array in descending order acc to its value
2) we keep inserting number into secondary aray s.t it has x value before it which are greater than it
3) we keep doing that iteratively and we get the solution

Eg - [7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]] (sorted)
[[7, 0]] (new_array)
[[7, 0], [7, 1]]        
[[7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
"""


class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda p: (-p[0], p[1]))
        print(people)
        res = []
        for p in people:
            # here p is inserted at p[1] postion
            res.insert(p[1], p)
            print(res)
        return res


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
obj = Solution()
print(obj.reconstructQueue(people))
