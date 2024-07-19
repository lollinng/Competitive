from collections import Counter
import heapq

"""
Here We are trying to convert string with given chars into string with no consecative chars else ""
We will be using max heap ds as it helps us to access the max element in O(1) time

Intuition - 
1) use conuter to count the number of strings.
2) create max heap from counter , since python heapq library contains min heap so we use min heap with negative value
for max heap representation
3) We keep 2 variables p_a and p_b for storing the state of popped max key,value pair got from heap and to use that
again with decremented counter for next round instead of this one coz we need to skip that character
4) now after popping all heap elements and which makes len(pq) = 0 we break the while loop
5) if the len of o/p str is same as input we return the string else not possible

complexity - O(klogn) where k is characters in array
EG - 'aba'  
c = Counter({'a': 2, 'b': 1})
pq = [(-2, 'a'), (-1, 'b')]                      res =[]
after 1 iteration
pq = [(-1, 'b')]      p_a=-1,p_b='a'            res = [a]
after 2 iteration
pq = [(-1,'a')]                                 res = [a,b]
after 3 
pq=[] and res=[a,b,a] => 'aba'

"""


class Solution:
    def reorganizeString(self, s) :
        # counter counts the occurance of of char in string
        res, c = [], Counter(s)
        # print(c)                    # Counter({'a': 2, 'b': 1})

        # We used -value so that we can use builtin min heap of python for max heap logic
        pq = [(-value, key) for key, value in c.items()]
        # print(pq)                    # [(-2, 'a'), (-1, 'b')]

        heapq.heapify(pq)
        p_a, p_b = 0, ""

        while(pq):
            a, b = heapq.heappop(pq)
            # print(a,b)                       # -2,a  coz the max => -1b=>-1a
            res.append(b)

            # less than 0 coz to add it back to heap till counter=0 and also to skip intial p_a for first iteration
            if p_a < 0:
                # here we push previous states into heap instead of a,b latest string character
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        res = "".join(res)
        # print(res)
        if len(res) != len(s):
            return ""

        return res


obj = Solution()
print(obj.reorganizeString('aab'))
