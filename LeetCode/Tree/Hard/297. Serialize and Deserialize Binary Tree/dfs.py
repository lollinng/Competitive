# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
    
       

        def dfs(node,flat_bt):
            if not node:
                flat_bt.append('#')
                return flat_bt

            flat_bt.append(str(node.val))
            dfs(node.left,flat_bt)
            dfs(node.right,flat_bt)

            return flat_bt
        
        return ",".join(dfs(root,[]))


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        flat_bt = data.split(',')
  
        def dfs(index):
            if flat_bt[index]=="#":
                return None,index+1

            node = TreeNode(flat_bt[index])
            index+=1
            node.left,index = dfs(index)
            node.right,index = dfs(index)
            return node,index
    
        return dfs(0)[0]


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))