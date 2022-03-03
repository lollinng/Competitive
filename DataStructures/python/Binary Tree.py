class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
"""
left node - 2n+1
right node - 2n+2
                        1
                    2        3
                4      5        6
            7                      8      
"""
input = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                 TreeNode(3, TreeNode(6, TreeNode(8))))

# Input: root = [1, null, 2, 3]
input1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
