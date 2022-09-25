"""
Here we have to find the path from root to laef s.t sum of values equal target sum

Intutions
1) We will use dfs in this , since we have to taverse from root to node multiple times 
2) We will dfs nodes recurse using subtracting teh value from target at each node and adding that node to temp arr
3) if the target sum becomes 0 at leaf we will append it to our answer list
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum: int) :
        res = []
        self.dfs(root,targetSum,res,[])
        return res
    
    def dfs(self,root,targetSum,res,temp):
        if root == None: # base
            return
        
        temp.append(root.val) # addtion
        
        if root.val==targetSum and root.left==None and root.right==None: # winning condition
            res.append(temp)
            return
        
        self.dfs(root.left,targetSum-root.val,res,temp.copy())       # recursion
        self.dfs(root.right,targetSum-root.val,res,temp.copy())
        return
    


input = TreeNode(5,
            TreeNode(4,
                TreeNode(11,
                    TreeNode(7),TreeNode(2))),
            TreeNode(8,
                TreeNode(13),
                TreeNode(4,
                    TreeNode(5),TreeNode(1))))
obj = Solution()
print(obj.pathSum(input,22))