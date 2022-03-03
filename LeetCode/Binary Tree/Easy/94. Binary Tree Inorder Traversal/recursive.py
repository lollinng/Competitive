#  Inorder (Left, Root, Right)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, node, res):
        if(node):
            self.traversal(node.left, res)
            res.append(node.val)
            self.traversal(node.right, res)


s = Solution()
# Input: root = [1, null, 2, 3]
print(s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
input = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                 TreeNode(3, TreeNode(6, TreeNode(8))))
print(s.inorderTraversal(input))
