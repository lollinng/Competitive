"""
BFS goes level wise . We use a queue to input the root node of the tree and iterate through its levels
using left and right leaves ans storing them in list . After we see no more nodes remaining below or in the queue
we output the sum of the leaves taken in the last level in the list
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root):
        q = []
        res = []  # last node will be stored here
        t = []          # each level will be stored here
        if root is None:
            return res
        q.append(root)        # tree object stored in queue

        while(q):
            t = []             # empty list for each level
            # len of queue = 1 one if it contains one node irrespctive of its child
            level = len(q)
            print("Level", level)
            while level != 0:
                # nodes first popped from left side in same level
                temp = q.pop(0)
                level -= 1
                t.append(temp.val)
                print(t)
                if temp.left:
                    # storing elements of the tree left level wise
                    q.append(temp.left)
                if temp.right:
                    # storing elements of the tree right level wise
                    q.append(temp.right)
            # final level list of nodes stored in res
            res.append(t)
        return sum(t)


s = Solution()
# root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
"""
left node - 2n+1
right node - 2n+2
                        1
                    2        3
                4      5        6
            7                      8 

Level 1
[1]
Level 2
[2]
[2, 3]
Level 3
[4]
[4, 5]
[4, 5, 6]
Level 2
[7]
[7, 8]
15
          
"""
input = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                 TreeNode(3, TreeNode(6, TreeNode(8))))
print(s.deepestLeavesSum(input))
