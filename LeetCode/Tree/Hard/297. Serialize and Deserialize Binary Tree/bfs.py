# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        flat_bt = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                flat_bt.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                flat_bt.append('')

        return ','.join(flat_bt)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        flat_bt = data.split(',')
        bt_len = len(flat_bt)
        if flat_bt[0]=='':
            return None

        root = TreeNode(int(flat_bt[0]))
        queue = deque([root])
        i = 1 
        # children of node is present at i and i+1
        while queue:
            node = queue.popleft()

            if flat_bt[i]:
                node.left = TreeNode(int(flat_bt[i]))
                queue.append(node.left)
            i+=1

            if flat_bt[i]:
                node.right = TreeNode(int(flat_bt[i]))
                queue.append(node.right)
            i+=1
        
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))