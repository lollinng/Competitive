class UnionFind:
    '''
    I have to implement by size,parent,groups (at each unions groups get reduced from n nodes)

    def find wechi h recursively finds the ultimate parent

    def unions which checks ultimate parent
    if they have same then return true
    else add larger size node's parent to lower size node
    and increase the size of main root

    '''

    def __init__(self,n):
        self.parents = [x for x in range(n)]
        self.size = [1 for _ in range(n)]
        self.groups = n

    def find(self,a):
        while a!=self.parents[a]:
            self.parents[a] = self.parents[self.parents[a]] 
            a = self.parents[a]
        return a

    def union(self,a,b):
        a_root,b_root = self.find(a),self.find(b)

        if a_root == b_root:
            return True

        # if not in same group
        if self.size[a_root] > self.size[b_root]:
            self.parents[b_root] = a_root
            self.size[a_root] += self.size[b_root]
        else:
            self.parents[a_root] = b_root
            self.size[b_root] += self.size[a_root]

        self.groups-=1

        return True

class Solution:
    def findCircleNum(self, isConnected):

        rows = len(isConnected)
        cols = len(isConnected[0])

        if rows<1 :
            return 0

        union = UnionFind(rows)
        for row in range(rows):
            for col in range(cols):
                if isConnected[row][col] ==1:
                    union.union(row,col)

        return union.groups

            
