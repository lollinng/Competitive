# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "val "+self.val + " "+ self.left + " "+self.right
class Solution:
    """
    Intuition:
    we have to use dfs to get to lead node
    and check if its leaf node, if its target we deleter it
    and track back and go right to delete leaf node
    in case of prent node it access the node values if they delted it will get null
    if its children both deleted it will be also deleted by returning None

    So recurion will be 
    break
    left (return None if want to delete )
    right (return None if want to delete )
    check if target and left and right none return true if you want to delete  
    """

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
   
        if root==None:
            return None

        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)
        
        if root.left==None and root.right==None and root.val == target:
            return None # making it disconnect
            
        return root  #returning the node if it doenst fit in criteria
        