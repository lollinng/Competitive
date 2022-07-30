"""
here we have to find the center node in the graph

Intuition - 
1) the center is node is present in every edge nodes
"""


class Solution:
    def findCenter(self, edges):
        if(edges[0][0] in edges[1]):
            return edges[0][0]
        return edges[0][1]


obj = Solution()
print(obj.findCenter([[1, 2], [2, 3], [4, 2]]))
