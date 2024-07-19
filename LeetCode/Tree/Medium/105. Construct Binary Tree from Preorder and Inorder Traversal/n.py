# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index_map = {value:index for index,value in enumerate(inorder)}
        
        def helper(pre_left,pre_right,in_left,in_right):
            if pre_left>pre_right or in_left>in_right:
                return None

                        
            root = TreeNode(preorder[pre_left])
            inorder_root_index = inorder_index_map[root.val]
            
            realative_root_index = inorder_root_index - in_left
            pre_left+=1

            # going left
            l_pre_right = pre_left+realative_root_index
            l_in_right = inorder_root_index-1
            root.left = helper(pre_left,l_pre_right,in_left,l_in_right)

            # goinf right
            l_pre_left = pre_left+realative_root_index
            l_in_left = inorder_root_index+1
            root.right = helper(l_pre_left,pre_right,l_in_left,in_right)

            return root

        return helper(0,len(preorder)-1,0,len(inorder)-1)